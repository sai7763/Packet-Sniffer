# 📡 Packet Sniffer

A Python tool that captures and analyzes live network packets using **Scapy**.  
Designed for educational purposes to understand how data flows in networks.  
⚠️ Use it responsibly on networks you own or have authorization to monitor.

---

## 🌟 Features
- Captures live packets on the network
- Displays packet source, destination, and protocol
- Easy to extend for protocol-specific analysis (HTTP, DNS, etc.)
- Real-time packet viewing

---

## 🧠 How It Works
The sniffer listens to the network interface and captures every packet.  
It uses **Scapy’s sniff()** function to read, decode, and print packet details like IPs and protocols.

---

## ⚙️ Installation & Run (Step-by-Step)

### 🪜 Step 1: Clone the repository
```bash
git clone https://github.com/sai7763/Packet-Sniffer.git
cd Packet-Sniffer
```

---

### 🪜 Step 2: Create a virtual environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🪜 Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
If you face issues, install manually:
```bash
pip install scapy
```

---

### 🪜 Step 4: Run the sniffer
**Windows (run as Administrator):**
```bash
python packet_sniffer.py
```
**Linux/macOS (requires sudo):**
```bash
sudo python3 packet_sniffer.py
```

Press `Ctrl + C` to stop capturing.

---

## 🧾 Example Output
```
Ether / IP / TCP 192.168.1.5:443 > 192.168.1.10:52134 S
Ether / IP / UDP 192.168.1.10:5678 > 8.8.8.8:53
```

---

## 💡 Notes
- Packet capturing may require **root/admin privileges**.
- Some networks block packet sniffing for security.
- Works best on Wi-Fi or LAN connections with broadcast traffic.
- Always use responsibly.

---

## 🧰 Requirements
- Python 3.8+
- Scapy (`pip install scapy`)
- Administrative or root access

---

## 🔧 Troubleshooting
- If no packets appear, disable your firewall temporarily or run as admin.
- If Scapy fails to install, ensure `pip` and `setuptools` are updated.
- Use `sudo` for permissions on Linux.

---

## 👨‍💻 Author
**Muvvala Sai (sai7763)**  
GitHub: [https://github.com/sai7763](https://github.com/sai7763)

---

## ⚖️ License
This project is licensed under the **MIT License**.  
Feel free to modify and share with proper credit.
