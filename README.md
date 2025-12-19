# Task 1: Basic Network Sniffer

## Project Description
This project implements a **Basic Network Sniffer** using **Python** and the **Scapy** library.  
The program captures live network packets and displays important information such as source IP address, destination IP address, protocol type, and packet payload.

The objective of this task is to understand how network traffic flows and how packets are structured at the network layer.

---

## Technologies Used
- Python 3
- Scapy
- Kali Linux (WSL)

---

## Project Structure
Network_Sniffer/  
└── sniffer.py  

---

## Requirements
- Python 3
- Scapy library
- Administrator/root privileges (required for packet capture)

Install Scapy:  
pip install scapy

---

## How to Run
Navigate to the project folder:  
cd Network_Sniffer  

Run the program with administrator privileges:  
sudo python3 sniffer.py  

Generate network traffic by browsing the internet or using:  
ping google.com  

---

## Output
The program displays the following details for captured packets:
- Source IP address
- Destination IP address
- Protocol type (TCP / UDP / ICMP)
- Packet payload

---

## Learning Outcomes
- Understanding packet capturing
- Basics of network protocols
- Practical exposure to Python in cybersecurity
- Introduction to network traffic analysis

---
