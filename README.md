# 🔐 RVG Universal Password Cracker

**ZIP | RAR | 7Z | PDF | DOCX | XLSX | PPTX | APK**

A powerful, universal password cracking tool for encrypted files. Built for educational and security testing purposes.

---

## 📌 Features

- ✅ **Multi-format support** — ZIP, RAR, 7Z, PDF, MS Office (DOCX/XLSX/PPTX), APK
- ✅ **Hidden input** — File paths are hidden while typing (privacy)
- ✅ **Auto-loop** — Crack multiple files without restarting
- ✅ **Auto-search** — Automatically finds files in `/sdcard/Download/`, `/sdcard/`, and current directory
- ✅ **Progress display** — Shows attempts, speed, and percentage
- ✅ **Speed tracking** — Passwords/sec display
- ✅ **Lightweight** — No GUI, runs in terminal (Termux/Linux)

---

## 🛠️ Supported File Types

| Extension | Type |
|-----------|------|
| `.zip` | ZIP Archive |
| `.rar` | RAR Archive |
| `.7z` | 7-Zip Archive |
| `.pdf` | PDF Document |
| `.docx` | Word Document |
| `.xlsx` | Excel Document |
| `.pptx` | PowerPoint |
| `.apk` | Android APK |

---

## 📦 Requirements

- Python 3.7+
- Termux (for Android) or Linux terminal

### Python Dependencies

```bash
pip install rarfile py7zr pikepdf pycryptodome
