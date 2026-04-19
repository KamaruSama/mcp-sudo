# `sudo_exec`

รันคำสั่ง shell ด้วย `sudo` โดยใช้รหัสผ่านที่เก็บไว้ (ไม่มีการถามรหัส)

## Signature

```python
sudo_exec(command: str, timeout: int = 120) -> str
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `command` | `str` | — | คำสั่ง shell ที่จะรัน (ส่งให้ `bash -c`) |
| `timeout` | `int` | `120` | timeout หน่วยวินาที |

## คืนค่า

stdout + stderr รวมกัน (กรอง sudo prompt ออกแล้ว) ถ้า exit code ไม่เป็น 0 จะมี `[exit code: N]` ต่อท้าย

ถ้า timeout → `"[error: command timed out after Ns]"`

## ตัวอย่าง

**ติดตั้ง package**
```json
{ "command": "pacman -S --noconfirm git curl" }
```

**อ่านไฟล์ที่ต้องใช้ sudo**
```json
{ "command": "cat /etc/shadow" }
```

**คำสั่งยาวๆ**
```json
{ "command": "pacman -Syu --noconfirm", "timeout": 600 }
```

## หมายเหตุ

- ต้องเรียก `store_password` มาก่อนครั้งแรก ไม่งั้นจะ raise `RuntimeError`
- รันผ่าน `bash -c "$command"` — ใช้ pipe / redirect / env var ได้ปกติ
- output เป็น string — binary output อาจเพี้ยน

---

Part of [mcp-sudo](../../../README.md) · © 2026 likezara™ · Kamaru
