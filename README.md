# 🔍 NmapLite - Professional Port Scanner

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A lightweight, educational port scanner built in Python for cybersecurity learning. This tool demonstrates fundamental networking concepts including TCP/IP, socket programming, and network reconnaissance techniques.

## 🎯 Project Purpose

Built as a learning project to understand:
- **TCP/IP Protocol Stack** - How network communication works
- **Socket Programming** - Low-level network interactions
- **Port Scanning Techniques** - Different methods of network reconnaissance
- **Multi-threading** - Concurrent programming for performance
- **Cybersecurity Fundamentals** - Ethical hacking basics

## ✨ Features

### Core Functionality
- ✅ **TCP Connect Scan** - Full three-way handshake
- ✅ **SYN Stealth Scan** - Half-open scanning (requires root)
- ✅ **Multi-threaded Scanning** - Fast concurrent port checks
- ✅ **Service Detection** - Identify services running on open ports
- ✅ **Banner Grabbing** - Extract service version information
- ✅ **Host Discovery** - Ping sweep to find live hosts
- ✅ **Port Range Scanning** - Scan specific or all 65,535 ports
- ✅ **Multiple Output Formats** - JSON, CSV, and text reports

### Advanced Features
- 🔍 **Custom Port Lists** - Scan common ports or define your own
- 📊 **Progress Indicators** - Real-time scan progress
- 🎨 **Colored Output** - Easy-to-read terminal display
- 💾 **Export Results** - Save scans for documentation
- ⚡ **Configurable Timeout** - Adjust for different networks
- 🛡️ **Error Handling** - Robust exception management

## 📁 Project Structure

```
nmaplite/
│
├── nmaplite.py              # Main scanner application
├── scanner_modules/
│   ├── __init__.py
│   ├── tcp_scanner.py       # TCP connect scan implementation
│   ├── syn_scanner.py       # SYN stealth scan (Scapy)
│   ├── service_detect.py    # Service detection & banner grab
│   └── utils.py             # Helper functions
│
├── config/
│   └── common_ports.json    # List of common ports
│
├── output/
│   └── scans/               # Saved scan results
│
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── LICENSE                 # MIT License
└── examples/
    ├── basic_scan.py       # Usage examples
    └── advanced_scan.py
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) Root/admin privileges for SYN scans

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/nmaplite.git
cd nmaplite
```

2. **Create virtual environment** (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Scanning

**Scan common ports on a target:**
```bash
python nmaplite.py -t 192.168.1.1
```

**Scan specific port range:**
```bash
python nmaplite.py -t 192.168.1.1 -p 1-1000
```

**Scan specific ports:**
```bash
python nmaplite.py -t 192.168.1.1 -p 22,80,443,8080
```

### Advanced Scanning

**Multi-threaded scan (faster):**
```bash
python nmaplite.py -t 192.168.1.1 -p 1-10000 --threads 100
```

**SYN stealth scan (requires root):**
```bash
sudo python nmaplite.py -t 192.168.1.1 -sS
```

**Service detection with banner grabbing:**
```bash
python nmaplite.py -t 192.168.1.1 -sV
```

**Save results to file:**
```bash
python nmaplite.py -t 192.168.1.1 -o results.json --format json
```

**Scan multiple targets:**
```bash
python nmaplite.py -t 192.168.1.1,192.168.1.5,192.168.1.10
```

**Verbose output:**
```bash
python nmaplite.py -t 192.168.1.1 -v
```

### Command-Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `-t, --target` | Target IP address or hostname | `-t 192.168.1.1` |
| `-p, --ports` | Port range or list | `-p 1-1000` or `-p 22,80,443` |
| `-sT` | TCP Connect Scan (default) | `-sT` |
| `-sS` | SYN Stealth Scan (requires root) | `-sS` |
| `-sV` | Service/version detection | `-sV` |
| `--threads` | Number of threads | `--threads 100` |
| `-o, --output` | Output file name | `-o scan_results.json` |
| `--format` | Output format (json/csv/txt) | `--format json` |
| `-v, --verbose` | Verbose output | `-v` |
| `--timeout` | Connection timeout (seconds) | `--timeout 2` |

## 🎓 What You'll Learn

### 1. **Network Fundamentals**
- How TCP/IP protocol works
- Three-way handshake (SYN, SYN-ACK, ACK)
- Port states (open, closed, filtered)
- Common network services and ports

### 2. **Python Programming**
- Socket programming (`socket` library)
- Multi-threading (`threading`, `concurrent.futures`)
- Command-line interfaces (`argparse`)
- Error handling and exception management
- File I/O and data serialization (JSON, CSV)

### 3. **Cybersecurity Concepts**
- Network reconnaissance techniques
- Footprinting and scanning methodologies
- Service enumeration
- Stealth vs. noisy scanning
- Ethical hacking principles

### 4. **Port Scanning Techniques**

**TCP Connect Scan (-sT)**
- Full three-way handshake completion
- Most reliable but easily detected
- Doesn't require root privileges
- Logged by most firewalls

**SYN Scan (-sS)**
- Half-open scanning technique
- Sends SYN, receives SYN-ACK, sends RST
- Stealthier than TCP connect
- Requires root/admin privileges

## 📊 Sample Output

```
╔══════════════════════════════════════════════════════════════╗
║                    NmapLite Port Scanner                     ║
║                  Cybersecurity Learning Tool                 ║
╚══════════════════════════════════════════════════════════════╝

[*] Target: 192.168.1.1
[*] Scan Type: TCP Connect Scan
[*] Port Range: 1-1000
[*] Threads: 50
[*] Started: 2025-11-05 18:43:21

[+] Scanning in progress...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% | 1000/1000 ports

╔════════════════════════════════════════════════════════════╗
║                        SCAN RESULTS                         ║
╚════════════════════════════════════════════════════════════╝

PORT      STATE    SERVICE           VERSION
────────────────────────────────────────────────────────────
22/tcp    open     ssh              OpenSSH 8.2p1 Ubuntu
80/tcp    open     http             Apache httpd 2.4.41
443/tcp   open     https            Apache httpd 2.4.41
3306/tcp  open     mysql            MySQL 8.0.23
8080/tcp  open     http-proxy       Squid http proxy 4.10

[✓] Scan completed in 12.34 seconds
[✓] Found 5 open ports
[*] Results saved to: output/scans/192.168.1.1_20251105_184333.json
```

## ⚠️ Legal & Ethical Considerations

### **IMPORTANT - READ BEFORE USING**

This tool is designed for **EDUCATIONAL PURPOSES ONLY**. Unauthorized port scanning can be illegal and unethical.

### ✅ Legal Use Cases:
- Scanning your own networks and devices
- Authorized penetration testing with written permission
- Lab environments (VMs, isolated networks)
- Capture The Flag (CTF) competitions
- Educational platforms (HackTheBox, TryHackMe)

### ❌ Illegal Use Cases:
- Scanning networks without explicit authorization
- Scanning production systems without permission
- Any form of unauthorized network reconnaissance
- Malicious intent or illegal activities

### Best Practices:
1. **Always get written permission** before scanning any network
2. **Use isolated lab environments** for learning
3. **Respect network policies** and acceptable use agreements
4. **Document everything** for transparency
5. **Understand local laws** regarding network security testing

## 🧪 Testing Environment Setup

For safe testing, create a virtual lab:

### Option 1: VirtualBox/VMware Setup
```bash
# Create isolated network with:
- Kali Linux (attacker machine)
- Metasploitable2 (vulnerable target)
- Ubuntu Server (target)
```

### Option 2: Docker Containers
```bash
docker run -d --name vulnerable-target vulnerables/web-dvwa
docker run -d --name web-server nginx
```

### Option 3: Cloud Lab
- Use AWS/Azure free tier VMs
- Ensure proper network isolation
- Scan only your own instances

## 🔧 Technical Implementation

### TCP Connect Scan Method
```python
def tcp_connect_scan(target, port, timeout=1):
    """
    Performs TCP Connect scan (full three-way handshake)
    Returns: True if port is open, False otherwise
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False
```

### Multi-threading Implementation
```python
def threaded_scan(target, ports, max_threads=50):
    """
    Uses ThreadPoolExecutor for concurrent scanning
    Significantly faster than sequential scanning
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(tcp_connect_scan, target, port): port 
                   for port in ports}
        
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result():
                print(f"[+] Port {port} is OPEN")
```

## 📈 Performance Benchmarks

| Scan Type | Ports | Threads | Time | Speed |
|-----------|-------|---------|------|-------|
| Sequential | 1000 | 1 | ~180s | 5.5 ports/s |
| Multi-threaded | 1000 | 50 | ~15s | 66 ports/s |
| Multi-threaded | 1000 | 100 | ~12s | 83 ports/s |
| SYN Scan | 1000 | - | ~8s | 125 ports/s |

*Tested on: Ubuntu 20.04, i5-10400, 16GB RAM, Local network*

## 🛠️ Dependencies

- `argparse` - Command-line interface (built-in)
- `socket` - Network communications (built-in)
- `threading` - Concurrent execution (built-in)
- `scapy` - Packet manipulation (optional, for SYN scan)
- `colorama` - Colored terminal output
- `tabulate` - Pretty table formatting
- `tqdm` - Progress bars

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions:
- UDP scanning support
- OS fingerprinting
- Firewall detection
- Network mapping visualization
- Integration with Shodan API
- Nmap XML import/export

## 📝 Roadmap

- [ ] UDP port scanning
- [ ] OS detection
- [ ] Aggressive scan mode
- [ ] Script engine (NSE-like)
- [ ] Web UI dashboard
- [ ] Network topology mapping
- [ ] Integration with vulnerability databases

## 📚 Resources & Learning Materials

### Recommended Reading:
- [Nmap Official Documentation](https://nmap.org/docs.html)
- "Black Hat Python" by Justin Seitz
- "Violent Python" by TJ O'Connor
- Python Socket Programming Guide

### Practice Platforms:
- [TryHackMe](https://tryhackme.com) - Guided cybersecurity learning
- [HackTheBox](https://hackthebox.com) - Penetration testing labs
- [OverTheWire](https://overthewire.org) - Wargames
- [PentesterLab](https://pentesterlab.com) - Web pentesting

### Related Projects:
- [Nmap](https://github.com/nmap/nmap) - Original network scanner
- [RustScan](https://github.com/RustScan/RustScan) - Modern fast port scanner
- [Masscan](https://github.com/robertdavidgraham/masscan) - Mass IP scanner

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by Nmap by Gordon Lyon (Fyodor)
- Thanks to the Python community
- Built for educational purposes
- Special thanks to cybersecurity educators

## ⚡ Quick Start Example

```python
# Simple Python usage
from nmaplite import PortScanner

scanner = PortScanner()
results = scanner.scan('192.168.1.1', ports=[22, 80, 443])

for port, status in results.items():
    print(f"Port {port}: {status}")
```

---

**⚠️ Disclaimer:** This tool is for educational and authorized testing only. The author assumes no liability and is not responsible for any misuse or damage caused by this program. Always ensure you have explicit permission before scanning any network.

**🎓 Learning Note:** Understanding how port scanners work helps you both attack and defend networks. Use this knowledge responsibly!

---

*Last Updated: November 2025*