<div align="center">

# 🛡️ NetDefender: Private WiFi Scanner

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/yourusername/NetDefender/issues)

**Find out exactly who is on your WiFi network and securely block unauthorized devices with one click.**

[Features](#-features) • [Installation](#-installation) • [How it Works](#-how-it-works) • [Contributing](#-contributing)


</div>

---

## 🕵️‍♂️ Why NetDefender?
Ever wonder if your neighbors are using your WiFi, or if a hidden smart device is connected to your private network? 

NetDefender is a lightweight, local Python web application that performs a deep ARP scan of your network. Unlike "hacker" tools that use unreliable and disruptive deauthentication attacks, NetDefender uses **Administrative MAC Filtering**—the only 100% secure and permanent way to ban a device from your router.

## ✨ Features
- **🚀 Ultra-Fast ARP Scanning:** Discovers devices even if they are trying to hide from standard ping requests.
- **🔍 Hardware Fingerprinting:** Automatically identifies the manufacturer of the device (Apple, Samsung, Intel, etc.) using MAC vendor APIs.
- **🛡️ Secure "One-Click" Blocking Workflow:** Extracts the intruder's MAC address and routes you directly to your router's admin gateway with instructions to permanently blacklist them.
- **💻 Beautiful Local UI:** Built with Flask, TailwindCSS, and SweetAlert2 for a modern, responsive dashboard.

## ⚙️ Installation

Because NetDefender scans raw network packets, it **must be run locally** on your machine (it cannot be hosted on the internet).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adimalpani99/NetDefender.git
   cd NetDefender
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Windows users may need to install [Npcap](https://npcap.com/) for Scapy to work properly).*

3. **Run the scanner:**
   *Raw packet sniffing requires Administrator/Root privileges.*
   
   **Windows (Command Prompt as Admin):**
   ```cmd
   python app.py
   ```
   **Linux / macOS:**
   ```bash
   sudo python3 app.py
   ```

4. **View your network:** Open `http://localhost:5000` in your browser.

## 🛑 How to Block a Device
1. Click **Scan Network**.
2. Identify a device you don't recognize.
3. Click the red **Remove / Block** button.
4. NetDefender will give you the exact MAC address and open your router's login page. Simply paste the MAC address into your router's **MAC Filter / Access Control** blocklist!

## 🤝 Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
