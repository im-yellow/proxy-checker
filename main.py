import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

init(autoreset=True)

def check_proxy(index, total, proxy, timeout=3):
    proxy = proxy.strip()
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}',
    }
    try:
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[{index}/{total}] + {proxy}{Style.RESET_ALL}")
            return proxy
    except requests.exceptions.RequestException:
        pass

    print(f"{Fore.RED}[{index}/{total}] - {proxy}{Style.RESET_ALL}")
    return None

if __name__ == '__main__':
    with open("proxies.txt", "r") as file:
        proxies_list = [line.strip() for line in file if line.strip()]

    total_proxies = len(proxies_list)
    valid_proxies = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_proxy = {
            executor.submit(check_proxy, idx, total_proxies, proxy): proxy
            for idx, proxy in enumerate(proxies_list, start=1)
        }

        for future in as_completed(future_to_proxy):
            result = future.result()
            if result:
                valid_proxies.append(result)

    if valid_proxies:
        with open("valid_proxies.txt", "w") as f:
            f.writelines(f"{proxy}\n" for proxy in valid_proxies)
        print(f"\n✅ Valid proxies saved to valid_proxies.txt ({len(valid_proxies)})")
    else:
        print("\n❌ No valid proxies found.")
