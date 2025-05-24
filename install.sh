#!/bin/bash
echo "[+] Installing dependencies..."
pkg update -y
pkg install -y python git

echo "[+] Cloning repository..."
git clone https://github.com/RasyidGZ/Hacking-Tools-Cloner
cd Hacking-Tools-Cloner

echo "[+] Installing Python packages..."
pip install -r requirements.txt

echo "[+] Ready! Run with:"
echo "python hacktools.py"