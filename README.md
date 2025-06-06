# Cybersecurity Utilities

This repository contains a proof-of-concept GUI tool for performing basic port
scanning using [`nmap`](https://nmap.org/).

## Requirements

- Python 3
- `nmap` must be installed and available in your system `PATH`.

## Port Scanner GUI

The `port_scanner_gui.py` script opens a small window where you can enter an
IP address or domain name. When you click **Scan**, it runs:

```
nmap -Pn -sV <target>
```

The output from `nmap` is displayed in the window in the standard format showing
open ports and service information.

### Running the tool

```bash
python3 port_scanner_gui.py
```

Enter the desired IP address or domain name and press **Scan**.

## Hello World Example

The `hello_world.py` script is a minimal example that simply prints `Hello, world!`.

Run it with:

```bash
python3 hello_world.py
```

