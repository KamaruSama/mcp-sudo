# mcp-sudo

**MCP server สำหรับรันคำสั่ง `sudo` โดยเก็บรหัสผ่านแบบเข้ารหัส**

ให้ 4 เครื่องมือสำหรับเก็บรหัสผ่าน sudo (เข้ารหัสด้วย key ที่ผูกกับเครื่อง) และเรียกคำสั่ง privileged โดยไม่ต้องพิมพ์รหัสซ้ำ เหมาะกับ Linux workstation ที่ใช้คนเดียว

📖 **[Read in English →](README.md)**

---

## เครื่องมือ

| เครื่องมือ | หน้าที่ |
|---|---|
| [`store_password`](docs/th/tools/store_password.md) | เก็บรหัสผ่าน sudo (เข้ารหัส ครั้งเดียว) |
| [`sudo_exec`](docs/th/tools/sudo_exec.md) | รันคำสั่ง shell ด้วย sudo |
| [`has_password`](docs/th/tools/has_password.md) | เช็คว่ามีรหัสผ่านเก็บไว้หรือยัง |
| [`clear_password`](docs/th/tools/clear_password.md) | ลบรหัสผ่านออก |

---

## Security model

- รหัสผ่านเข้ารหัสด้วย **Fernet** (AES-128-CBC + HMAC-SHA256)
- Encryption key **สร้างจาก** `machine-id` + `USER` — ไม่ได้เก็บไว้ที่ไหน
- ถอดรหัสสำเร็จเฉพาะเครื่องเดียวกัน + user เดียวกัน
- Ciphertext เก็บที่ `~/.config/claude-sudo-mcp/credential.enc` (chmod 600)

**ไม่ใช่ secrets manager** — คิดว่ามันแค่ "จำรหัส sudo ไว้ให้ในเครื่องนี้" ถ้า `machine-id` ถูก copy ไปเครื่องอื่น หรือมีคนอ่าน process ของ MCP ได้ รหัสก็อาจหลุดได้

---

## ติดตั้ง

```bash
cd /path/to/mcp-sudo
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mcp cryptography

claude mcp add sudo -s user -- \
  /path/to/mcp-sudo/.venv/bin/python /path/to/mcp-sudo/server.py
```

ครั้งแรก เรียก `store_password` หนึ่งครั้งเพื่อเก็บรหัสผ่านไว้

---

## สนับสนุนผู้พัฒนา ❤

- **Ko-fi:** https://ko-fi.com/kamaru

---

## ติดต่อ

- **Portfolio / ทั่วไป:** k.kamarux@gmail.com
- **เชิงพาณิชย์ / ลิขสิทธิ์:** contact@likezara.com

---

Copyright © 2026 **likezara™**. สงวนลิขสิทธิ์
พัฒนาโดย **Kamaru** (นามปากกา)
