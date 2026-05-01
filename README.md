# Proxy Checker

A simple multithreaded Python proxy checker that validates proxies from a file and saves working ones.

## Features

* Thread-based proxy checking (fast execution)
* Supports HTTP/HTTPS proxies via `requests`
* Reads proxies from `proxies.txt`
* Saves valid proxies to `valid_proxies.txt`
* Live console status with color output

## Installation

```bash id="i91k2p"
git clone https://github.com/im-yellow/proxy-checker.git
cd proxy-checker
pip install -r requirements.txt
```

## Requirements

```
requests
colorama
```

## Usage

1. Add your proxies to `proxies.txt` (one per line):

```
ip:port
```

2. Run the script:

```bash id="run22"
python main.py
```

## How It Works

* Loads proxies from `proxies.txt`
* Uses `ThreadPoolExecutor` (max 100 threads)
* Sends a request through each proxy to:

  ```
  http://httpbin.org/ip
  ```
* If response is successful (status 200), proxy is marked as valid
* Valid proxies are stored in `valid_proxies.txt`

## Output Example

```
[1/500] + 185.XX.XX.1:8080
[2/500] - 103.XX.XX.2:3128

✅ Valid proxies saved to valid_proxies.txt (42)
```

## Limitations

* No SOCKS support (HTTP/HTTPS only)
* No proxy authentication support
* Performance depends on proxy quality and timeout (3s default)
* Some proxies may falsely fail due to timeout

## Disclaimer

This tool is for **educational and testing purposes only**.
The author is not responsible for any misuse.

## Contributing

Pull requests are welcome. Keep changes clean and minimal.
