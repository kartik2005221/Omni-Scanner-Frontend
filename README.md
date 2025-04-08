# Omni-Scanner
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue) ![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-brightgreen) [![Platform](https://img.shields.io/badge/Platform-Linux%20|%20Windows-informational)](#)

**Discover. Analyze. Secure.**

Omni Scanner is a powerful, versatile, and open-source network scanning suite built with Python. This tool offers both an interactive CLI mode and a user-friendly web interface powered by Flask. Use it to perform quick network discovery, detailed port scans, traceroutes, and more.

---

## 🚀 Features

### CLI Mode
- **Network Discovery:** ARP scanning to detect local devices.
- **Ping Customization:** Supports simple ping, flood ping, and adaptive latency checks.
- **Traceroute:** Visualize network paths to targets.
- **Advanced Scans:** Nmap integration for OS detection, service fingerprinting, and stealth scans.
- **User-Friendly Output:** Clean terminal tables, colored output, and progress tracking.
- **Graceful Interrupt Handling:** Clean exit messages on Ctrl+C.

### Web Interface
- **Interactive Dashboard:** Access scans via a modern, Bootstrap-based web UI.
- **Simple Forms:** Input IP/domain and select scan types (Ping, Nmap, Traceroute, etc.).
- **Real-Time Results:** View live output from your scans formatted neatly.
- **Scan History:** Save scan results to a database and view past scans.
- **Seamless Integration:** Both CLI and Web interfaces reuse the same core scanning functions.

---

## ⚙️ Installation
### Prerequisites
- **Python 3.8+**
- **Nmap:** [Download here](https://nmap.org/download.html)
- **Linux/macOS:** `arp-scan` (install via your package manager)
- **Windows:** **Npcap** for raw packet support

### Clone the Repository
```bash
git clone https://github.com/kartik2005221/Omni-Scanner.git
cd Omni-Scanner
````

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

### CLI Mode
Run the command-line interface with:
```bash
sudo python3 main.py
```
_Follow on-screen menu prompts for different scan options._

### Web Interface Mode
Start the Flask server by running:
```bash
python app.py
```

or

```bash
flask run
```

Then, open any web browser and go to:
```
http://localhost:8668
```

_Use the interactive forms to select a scan type and view results._

---

## ⚠️ Legal & Ethical Disclaimer

**BEFORE USING THIS TOOL:**
- **Obtain written permission** before scanning networks you do not own.
- **Do NOT scan public or critical infrastructure** without authorization.
- Use Omni Scanner **only for educational and ethical purposes**.
- Comply with all local/global laws.
- You assume full responsibility for your actions.
---

## 🤝 Contributing

We welcome contributions to improve Omni-Scanner!  
**How to Contribute:**
- **Report Bugs:** Open an issue labeled "Bug".
- **Suggest Features:** Use the "Enhancement" label.
- **Code Contributions:**
   1. Fork the repository.
   2. Create a feature branch (`git checkout -b feature/amazing-feature`).
   3. Commit the changes and open a Pull Request.

---

## 📜 License
This project is distributed under the **GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007**. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.

---

## 📬 Contact
- **Email:** [kartik2005221@proton.me](mailto:kartik2005221@proton.me)
- **GitHub:** [@kartik2005221](https://github.com/kartik2005221)
- **Twitter:** [@kartik2005221](https://twitter.com/kartik2005221)
- **LinkedIn:** [in/kartik2005221](https://linkedin.com/in/kartik2005221)

---

_Made with ❤️ and sudo privileges._  
_Ethical hacking starts with responsibility._