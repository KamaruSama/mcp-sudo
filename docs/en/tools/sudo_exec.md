# `sudo_exec`

Run a shell command with `sudo` using the stored, encrypted password. No interactive prompt.

## Signature

```python
sudo_exec(command: str, timeout: int = 120) -> str
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `command` | `str` | — | The shell command to execute (passed to `bash -c`) |
| `timeout` | `int` | `120` | Abort after N seconds |

## Returns

Combined stdout + stderr (sudo prompts filtered out). Appends `[exit code: N]` if non-zero.

On timeout → `"[error: command timed out after Ns]"`.

## Examples

**Install packages**
```json
{ "command": "pacman -S --noconfirm git curl" }
```

**View a protected file**
```json
{ "command": "cat /etc/shadow" }
```

**Longer-running task**
```json
{ "command": "pacman -Syu --noconfirm", "timeout": 600 }
```

## Notes

- Requires `store_password` to have been called first; otherwise raises `RuntimeError`.
- Command is run via `bash -c "$command"` — standard shell syntax works (pipes, redirects, env vars).
- Output is returned as a single string; binary output is not preserved reliably.

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
