# `has_password`

เช็คว่ามีรหัสผ่าน sudo เก็บไว้ และถอดรหัสได้หรือไม่ในเครื่องนี้

## Signature

```python
has_password() -> str
```

## พารามิเตอร์

ไม่มี

## คืนค่า

เป็น 1 ใน:

- `"Yes, password is stored and valid."` — มีไฟล์ credential และถอดรหัสได้
- `"Password file exists but cannot be decrypted."` — มีไฟล์แต่ key ไม่ตรง (เช่น ย้ายเครื่อง)
- `"No password stored."` — ไม่มีไฟล์

## ตัวอย่าง

```json
{}
```

## หมายเหตุ

- เช็ค read-only เรียกได้เร็ว ก่อนเรียก `store_password` ใหม่

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
