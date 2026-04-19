# `has_password`

Check whether a sudo password is already stored and decryptable on this machine.

## Signature

```python
has_password() -> str
```

## Parameters

None.

## Returns

One of:

- `"Yes, password is stored and valid."` — credential file exists and decrypts OK
- `"Password file exists but cannot be decrypted."` — file present but key mismatch (e.g. moved from another host)
- `"No password stored."` — no credential file found

## Example

```json
{}
```

## Notes

- Cheap, read-only check. Call this before prompting the user to re-run `store_password`.

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
