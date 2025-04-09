import os
import subprocess
import requests
from colorama import init, Fore, Back, Style

init()
def download_all():
    repo_url = "https://github.com/DeWeWO/uzb_kitoblar"
    destination_folder = "./uznltk"

    if not os.path.exists(destination_folder):
        print(f"{Fore.YELLOW + Style.BRIGHT}Klonlanmoqda: {repo_url}")
        subprocess.run(["git", "clone", repo_url, destination_folder])
        print(f"{Fore.GREEN + Style.BRIGHT}Repozitoriya yuklandi: {destination_folder}")
    else:
        print(f"{Fore.RED + Style.BRIGHT}Papka mavjud: {destination_folder}")

def download_book(author, book_name):
    base_url = "https://github.com/DeWeWO/uzb_kitoblar/tree/master"
    file_url = f"{base_url}/{author}/{book_name}.txt"
    destination_folder = os.path.join("uznltk", author)
    os.makedirs(destination_folder, exist_ok=True)
    local_path = os.path.join(destination_folder, f"{author}_{book_name}.txt")

    if not os.path.exists(local_path):
        print(f"{Fore.YELLOW + Style.BRIGHT}Yuklab olinmoqda: {file_url}")
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(local_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"{Fore.GREEN + Style.BRIGHT}Fayl saqlandi: {local_path}")
        else:
            print(f"{Fore.RED + Style.BRIGHT}Fayl topilmadi: {file_url}")
            return None

    with open(local_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
