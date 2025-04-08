## 🔀 1. Split Logic from CLI to Common Module

### 🎯 **Goal:** Make scan functions reusable by both CLI (`main.py`) and Web (`app.py`)

### ✅ What to do:
- Move all scan logic from `windows.py` / `linux.py` into **functions** like:
  ```python
  def ping_host(ip): ...
  def traceroute(ip): ...
  def full_nmap_scan(ip): ...
  ```
- Keep those functions in `windows.py` and `linux.py` as you already have OS-wise separation.

✅ **Every function should return output string**, not print. E.g.:
```python
return result.stdout
```

---

## 🧠 2. Create `scanner_core.py` (New File)

### 🎯 **Goal:** Create unified logic caller based on OS

```python
import platform

if platform.system() == "Windows":
    import OS_scripts.windows as scanner
else:
    import OS_scripts.linux as scanner
```

Then use:
```python
def run_ping(ip):
    return scanner.ping_host(ip)

def run_nmap(ip):
    return scanner.full_nmap_scan(ip)
```

👉 **Why?** Taki Web & CLI dono same function `run_ping()` ko call karein.

---

## 🌐 3. In `app.py`, Create Flask Routes

For each scan:
```python
@app.route('/ping', methods=['POST'])
def ping():
    ip = request.form['target_ip']
    output = run_ping(ip)  # from scanner_core.py
    return render_template('result.html', result=output)
```

👉 Ismein sirf `scanner_core.py` ke functions call honge, not directly `subprocess.run()`. Tu abstraction maintain karega.

---

## 🧑‍💻 4. In `main.py`, Call Same Functions

```python
from scanner_core import run_ping

# inside CLI menu
ip = input("Enter IP: ")
result = run_ping(ip)
print(result)
```

CLI aur Flask dono same logic call karenge = ✅ maintainable, no code repeat.

---

## 💽 5. Database Integration (Optional)

### 🎯 Goal: Store scan results (only if time permits)

- Make `database.py` → Define `ScanResult` model:
  ```python
  class ScanResult(db.Model):
      id = db.Column(...)
      scan_type = db.Column(...)
      ip = db.Column(...)
      output = db.Column(...)
      timestamp = db.Column(...)
  ```

- In each Flask route, **after scanning**, add:
  ```python
  new_result = ScanResult(scan_type="ping", ip=ip, output=output, timestamp=...)
  db.session.add(new_result)
  db.session.commit()
  ```

- Create `/history` route → Fetch & display previous results.

---

## 🧱 6. Folder Restructure (Update Imports)

Update `__init__.py` or use proper relative imports so `scanner_core.py` and Flask can use shared code.

Use:
```python
from OS_scripts.windows import ping_host
```
or:
```python
from .windows import ping_host  # if in package
```

---

## 🧠 Bonus: Make All `subprocess.run()` Return Output Properly

Right now, if you're using:
```python
subprocess.run(cmd, shell=True)
```

Update to:
```python
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
return result.stdout
```

**Important: CLI → print(result), Web → render(result)**

---

## 🔁 Summary of Changes:

| Task | What to Change |
|------|----------------|
| ✅ Scan Functions | Refactor to return output strings, no `print()` inside scan logic |
| ✅ scanner_core.py | Wrapper that picks correct OS functions |
| ✅ CLI Calls | Use `scanner_core.run_*()` functions |
| ✅ Flask Routes | Use same `scanner_core.run_*()` functions |
| ✅ DB Option | Add result storing logic in routes only |
| ✅ Folder Structure | Separate logic (OS_scripts), interface (CLI + Flask), and core (scanner_core) |

---

## ❓ You Should Ask Yourself:

- "Is my CLI doing any direct printing from subprocess?" → Replace with `return`-based flow.
- "Can this function be used in Flask?" → Yes if it returns `str`, no if it `prints` or `input()`.
