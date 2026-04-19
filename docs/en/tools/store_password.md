# `store_password`

Encrypt and persist the user's sudo password for later use by `sudo_exec`. Run once per machine.

## Signature

```python
store_password(password: str) -> str
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `password` | `str` | The user's sudo password |

## Returns

`"Password stored and encrypted successfully."` — or raises on filesystem error.

## Example

```json
{ "password": "s3cr3t" }
```

## Security

- Password is encrypted with **Fernet** (AES-128-CBC + HMAC-SHA256).
- The key is derived at runtime from `/etc/machine-id` + `$USER` — never written to disk.
- The ciphertext is written to `~/.config/claude-sudo-mcp/credential.enc` with mode **0600**.
- Decryption only succeeds on the same host under the same user.

> ⚠ This is **not** a secrets manager. Anyone with read access to `/etc/machine-id` **and** the ability to run code as the same user can decrypt the password.

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
