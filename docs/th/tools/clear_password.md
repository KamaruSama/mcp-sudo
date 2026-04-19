# `clear_password`

ลบไฟล์รหัสผ่าน sudo ที่เข้ารหัสไว้ออกจาก disk

## Signature

```python
clear_password() -> str
```

## พารามิเตอร์

ไม่มี

## คืนค่า

- `"Password cleared."` — ลบไฟล์สำเร็จ
- `"No password was stored."` — ไม่มีอะไรให้ลบ

## ตัวอย่าง

```json
{}
```

## หมายเหตุ

- ลบ `~/.config/claude-sudo-mcp/credential.enc` ออกเลย
- หลังจากนี้ `sudo_exec` จะ fail จนกว่าจะเรียก `store_password` ใหม่

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
