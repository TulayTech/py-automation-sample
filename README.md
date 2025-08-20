# Day 1 — Test Steps Logger

A tiny Python script that starts building your automation muscles.

It:
- Asks **who** is running the test (your name),
- Asks **what** step you completed (e.g., “checked login screen”),
- Appends that entry to **`day1_log.txt`**,
- Prints a **success message** with a **timestamp** so you have proof of completion.

---

## 🧠 Why each piece exists

- `from pathlib import Path`
  We use `Path` to build file paths cleanly (no messy string paths).
  `Path(__file__).parent / "day1_log.txt"` means “save the log next to this script.”

- `from datetime import datetime`
  Used to stamp each success message with the **current date/time**, so you know *when* a step was logged.

- `input(...).strip()`
  `input()` pauses and waits for user text.
  `.strip()` removes accidental spaces so the saved text is clean.

- `with open(log_file, "a", encoding="utf-8") as f:`
  Opens/creates the file in **append** mode:
  - If the file doesn’t exist → create it.
  - If it does exist → **add** to the end (don’t erase old entries).
  The `with` block ensures the file **always** closes safely.

- `if __name__ == "__main__": main()`
  Only runs `main()` when you execute the file directly.
  (If someone imports this file later, it won’t auto‑run.)

---

### 🧪 Run it
```bash
python3 hello_automation.py