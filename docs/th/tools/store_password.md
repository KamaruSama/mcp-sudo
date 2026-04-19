# `store_password`

เข้ารหัสและเก็บรหัสผ่าน sudo ไว้ใช้กับ `sudo_exec` ทำครั้งเดียวต่อเครื่อง

## Signature

```python
store_password(password: str) -> str
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `password` | `str` | รหัสผ่าน sudo |

## คืนค่า

`"Password stored and encrypted successfully."` — หรือ raise error ถ้าเขียนไฟล์ไม่ได้

## ตัวอย่าง

```json
{ "password": "s3cr3t" }
```

## ความปลอดภัย

- เข้ารหัสด้วย **Fernet** (AES-128-CBC + HMAC-SHA256)
- Key สร้างจาก `/etc/machine-id` + `$USER` — **ไม่ได้เก็บลงไฟล์**
- Ciphertext เก็บที่ `~/.config/claude-sudo-mcp/credential.enc` mode **0600**
- ถอดรหัสได้เฉพาะเครื่องเดียวกัน user เดียวกัน

> ⚠ **ไม่ใช่ secrets manager** — ใครก็ตามที่อ่าน `/etc/machine-id` ได้ + รัน code ในนาม user เดียวกันได้ สามารถถอดรหัสออกได้

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
