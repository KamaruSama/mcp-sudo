# `clear_password`

Delete the stored encrypted sudo password from disk.

## Signature

```python
clear_password() -> str
```

## Parameters

None.

## Returns

- `"Password cleared."` — if the file was deleted
- `"No password was stored."` — if there was nothing to remove

## Example

```json
{}
```

## Notes

- Fully removes `~/.config/claude-sudo-mcp/credential.enc`.
- Subsequent `sudo_exec` calls will fail until `store_password` is called again.

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
