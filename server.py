"""
================================================================================
 Sudo MCP Server
================================================================================

 A Model Context Protocol server that stores a sudo password (Fernet-encrypted
 with a key derived from machine-id + user) and exposes privileged command
 execution without repeated password prompts.

 Transport : stdio
 Tools     : store_password, sudo_exec, has_password, clear_password
 Storage   : ~/.config/claude-sudo-mcp/credential.enc (chmod 600)

 ⚠ Single-user workstation use only. Not a secrets manager.

--------------------------------------------------------------------------------
 Copyright © 2026 likezara™. All rights reserved.
 Developed by Kamaru (pen name).
--------------------------------------------------------------------------------
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import subprocess
from pathlib import Path

from cryptography.fernet import Fernet
from mcp.server.fastmcp import FastMCP

CONFIG_DIR = Path.home() / ".config" / "claude-sudo-mcp"
CREDENTIAL_FILE = CONFIG_DIR / "credential.enc"

mcp = FastMCP("sudo-mcp")


# ─────────────────────────────────────────────────────────────────────────────
#  Internal — Fernet key derivation + encrypt/decrypt
# ─────────────────────────────────────────────────────────────────────────────

def _derive_key() -> bytes:
    """Derive encryption key from machine-id + username."""
    machine_id = Path("/etc/machine-id").read_text().strip()
    username = os.environ.get("USER", "default")
    raw = f"{machine_id}:{username}:claude-sudo-mcp".encode()
    key = hashlib.sha256(raw).digest()
    return base64.urlsafe_b64encode(key)


def _encrypt(plaintext: str) -> str:
    return Fernet(_derive_key()).encrypt(plaintext.encode()).decode()


def _decrypt(ciphertext: str) -> str:
    return Fernet(_derive_key()).decrypt(ciphertext.encode()).decode()


def _get_password() -> str:
    if not CREDENTIAL_FILE.exists():
        raise RuntimeError("No password stored. Use store_password tool first.")
    data = json.loads(CREDENTIAL_FILE.read_text())
    return _decrypt(data["password"])


# ═════════════════════════════════════════════════════════════════════════════
#  Tools
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def store_password(password: str) -> str:
    """Store sudo password encrypted. Only needs to be done once."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    encrypted = _encrypt(password)
    CREDENTIAL_FILE.write_text(json.dumps({"password": encrypted}))
    CREDENTIAL_FILE.chmod(0o600)
    return "Password stored and encrypted successfully."


@mcp.tool()
def sudo_exec(command: str, timeout: int = 120) -> str:
    """Execute a command with sudo using the stored password.

    Args:
        command: The shell command to run with sudo.
        timeout: Timeout in seconds (default 120).
    """
    password = _get_password()
    full_command = f"echo '{password}' | sudo -S bash -c {repr(command)}"
    try:
        result = subprocess.run(
            ["bash", "-c", full_command],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = ""
        if result.stdout:
            output += result.stdout
        if result.stderr:
            stderr_lines = [
                line
                for line in result.stderr.splitlines()
                if not line.startswith("[sudo]") and "password for" not in line
            ]
            if stderr_lines:
                output += "\n".join(stderr_lines)
        if result.returncode != 0:
            output += f"\n[exit code: {result.returncode}]"
        return output.strip() or "(no output)"
    except subprocess.TimeoutExpired:
        return f"[error: command timed out after {timeout}s]"


@mcp.tool()
def has_password() -> str:
    """Check if a sudo password is already stored."""
    if CREDENTIAL_FILE.exists():
        try:
            _get_password()
            return "Yes, password is stored and valid."
        except Exception:
            return "Password file exists but cannot be decrypted."
    return "No password stored."


@mcp.tool()
def clear_password() -> str:
    """Remove the stored sudo password."""
    if CREDENTIAL_FILE.exists():
        CREDENTIAL_FILE.unlink()
        return "Password cleared."
    return "No password was stored."


if __name__ == "__main__":
    mcp.run(transport="stdio")
