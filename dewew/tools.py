import os
import subprocess

def download_from_github(repo_url, destination_folder):
    if not os.path.exists(destination_folder):
        print(f"Klonlanmoqda: {repo_url}")
        subprocess.run(["git", "clone", repo_url, destination_folder])
        print(f"Repozitoriya yuklandi: {destination_folder}")
    else:
        print(f"Papka mavjud: {destination_folder}")

# Misol uchun:
repo_url = "https://github.com/DeWeWO/uzb_kitoblar"
destination_folder = "./my_project/vendor/my_tool"

download_from_github(repo_url, destination_folder)
