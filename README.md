<div align="center">

# 🔐 Password Generator

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #4 — Pick a length. Get a random unbreakable password. 🖤**

</div>

---

## 💡 What It Does

```
You pick how long the password should be.
It generates a random mix of:
→ Letters (a-z, A-Z)
→ Numbers (0-9)
→ Symbols (!@#$%...)

Then tells you if it's Weak, Moderate, or Strong 💪
```

---

## 🎮 Demo

```bash
WELCOME TO PASSWORD GENERATOR! 😊
> Enter length: 12
  Your password is: aB3$kL!9mN@2
  Password is strong 💪

> Enter length: 4
  Your password is: aB3$
  Password too weak 😅
```

---

## ▶️ Run It

```bash
python Password_genrator.py
```

---

## 🔒 Strength Checker

| Length | Strength | Verdict |
|--------|----------|---------|
| < 6 | 🔴 Weak | Too short! |
| 6 – 10 | 🟡 Moderate | Could be stronger |
| > 10 | 🟢 Strong | Now we're talking 💪 |

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `string.ascii_letters` | All A-Z, a-z letters |
| `string.digits` | All 0-9 numbers |
| `string.punctuation` | All symbols !@#$... |
| `random.choice()` | Pick one random character |
| `for` loop + `range()` | Run exactly `length` times |
| `+=` | Add character to password each loop |
| `len()` | Measure password for strength check |

---

## 💻 Source Code

```python
import random
import string

print("WELCOME TO PASSWORD GENERATOR! 😊")

all_characters = string.ascii_letters + string.digits + string.punctuation
Length = int(input("Enter the length of password you want to generate: "))

password = ""
for i in range(Length):
    password += random.choice(all_characters)

print("Your password is:", password)

if len(password) < 6:
    print("Password too weak 😅")
elif len(password) > 10:
    print("Password is strong 💪")
else:
    print("Password is moderate, try bigger than 10 for stronger! 😏")
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
