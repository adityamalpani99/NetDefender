import socket
from flask import Flask, render_template, jsonify
import scapy.all as scapy
import urllib.request
import json

app = Flask(__name__)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable, just forces the OS to figure out the default local interface
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_mac_vendor(mac_address):
    # Try to resolve MAC address to vendor using an external API for better identification
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=2)
        return response.read().decode('utf-8')
    except:
        return "Unknown Device"

def scan_network():
    local_ip = get_local_ip()
    # Assume a standard /24 subnet for home networks (e.g., 192.168.1.0/24)
    ip_parts = local_ip.split('.')
    subnet = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
    router_ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.1"

    try:
        # Create ARP request targeting the whole subnet
        arp_request = scapy.ARP(pdst=subnet)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        
        # Send packet and capture responses
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

        clients = []
        for element in answered_list:
            ip = element[1].psrc
            mac = element[1].hwsrc
            clients.append({
                "ip": ip,
                "mac": mac,
                "vendor": get_mac_vendor(mac) if ip != local_ip else "Your Device",
                "is_router": ip == router_ip
            })
        return {"subnet": subnet, "router_ip": router_ip, "devices": clients}
    except Exception as e:
        print(f"Error scanning: {e}")
        return {"error": "Failed to scan network. Did you run as Administrator/Root?"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scan')
def do_scan():
    results = scan_network()
    return jsonify(results)

if __name__ == '__main__':
    print("\n[+] Starting Local WiFi Scanner...")
    print("[!] Ensure you are running this script with Administrator/sudo privileges!")
    app.run(debug=True, port=5000, host="0.0.0.0")
