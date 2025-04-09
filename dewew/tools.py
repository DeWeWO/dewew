import os
import subprocess
import requests

def download_from_github():
    repo_url = "https://github.com/DeWeWO/uzb_kitoblar"
    destination_folder = "./uznltk"

    if not os.path.exists(destination_folder):
        print(f"Klonlanmoqda: {repo_url}")
        subprocess.run(["git", "clone", repo_url, destination_folder])
        print(f"Repozitoriya yuklandi: {destination_folder}")
    else:
        print(f"Papka mavjud: {destination_folder}")

def load_book(author, book_name):
    # Fayl URL va saqlash manzili
    base_url = "https://github.com/DeWeWO/uzb_kitoblar/tree/master"
    file_url = f"{base_url}/{author}/{book_name}.txt"
    destination_folder = os.path.join("uznltk", author)
    os.makedirs(destination_folder, exist_ok=True)
    local_path = os.path.join(destination_folder, f"{author}_{book_name}.txt")

    # Fayl mavjud bo'lmasa yuklab olamiz
    if not os.path.exists(local_path):
        print(f"⬇️ Yuklab olinmoqda: {file_url}")
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(local_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"✅ Fayl saqlandi: {local_path}")
        else:
            print(f"❌ Fayl topilmadi: {file_url}")
            return None

    # Faylni o'qib qaytaramiz
    with open(local_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
