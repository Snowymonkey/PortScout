# PortScout

`PortScout` is a high-speed, multi-threaded command-line network utility written in Python. It allows users to quickly perform target IP lookups, scan a single port, or concurrently scan a wide range of ports using only standard libraries.

## Features

* **Multi-Threaded Performance:** Uses Python's built in threader to scan up to 200 ports concurrently, bypassing sequential network lag.
* **Smart Filtering:** Includes a dedicated toggle to hide closed ports and only display active, open ports.

---

## Installation

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/Snowymonkey/PortScout
   cd PortScout

## Usage

| Argument | Description |
|-----------|------------|
| `-p`, `--port` | Scan a single port |
| `-pr`, `--port_range` | Scan a range of ports inclusively. Must be in format LowerPort-UpperPort |
| `-op`, `--open_ports` | Displays only open ports |
| `-l`, `--lookup` | Returns IP of given website |
| `--help` | Help information of all arguments |

### Scan a single port

```bash
python portscout.py localhost --port 80
python portscout.py localhost -p 80 
```

### Scan a range of ports

```bash
python portscout.py localhost --port_range 1-80
python portscout.py localhost -pr 1-80 
```

### Display only open ports

```bash
python portscout.py localhost --open_ports --port 80
python portscout.py localhost -op -p 80 
```

### Return the IP of a given website

```bash
python portscout.py localhost google.com --lookup
python portscout.py localhost google.com -l
```

## Notes

If you suspect that your network is dropping your packets, it may be due to the high thread count. You can easily change this in the portscout.py file, set with the `max_workers=` parameter.
