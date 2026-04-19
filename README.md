# mcp-sudo

<!-- mcp-name: io.github.KamaruSama/mcp-sudo -->

**MCP server for running `sudo` commands with encrypted password storage.**

Exposes 4 tools to persist a sudo password (encrypted with a machine-bound key) and invoke privileged commands without re-entering credentials. Designed for single-user Linux workstations.

📖 **[อ่านภาษาไทย →](README.th.md)**

---

## Tools

| Tool | Purpose |
|---|---|
| [`store_password`](docs/en/tools/store_password.md) | Store sudo password (encrypted, one-time) |
| [`sudo_exec`](docs/en/tools/sudo_exec.md) | Run shell command with sudo |
| [`has_password`](docs/en/tools/has_password.md) | Check if password is stored |
| [`clear_password`](docs/en/tools/clear_password.md) | Remove stored password |

---

## Security model

- Password is encrypted with **Fernet** (AES-128-CBC + HMAC-SHA256).
- Encryption key is **derived** from `machine-id` + `USER` — never stored on disk.
- Decryption only succeeds on the same machine with the same user.
- Encrypted blob lives at `~/.config/claude-sudo-mcp/credential.enc` (chmod 600).

This is **not a secrets manager**. Treat this as "remember my sudo password for this session on this box." If your machine-id is copied to another box or another user reads the MCP process, the password can be recovered.

---

## Install

```bash
cd /path/to/mcp-sudo
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mcp cryptography

claude mcp add sudo -s user -- \
  /path/to/mcp-sudo/.venv/bin/python /path/to/mcp-sudo/server.py
```

On first use, call `store_password` once to cache credentials.

---

## Support the project ❤

- **Ko-fi:** https://ko-fi.com/kamaru

---

## Contact

- **Portfolio / general:** k.kamarux@gmail.com
- **Commercial / licensing:** contact@likezara.com

---

Copyright © 2026 **likezara™**. All rights reserved.
Developed by **Kamaru** (pen name).
