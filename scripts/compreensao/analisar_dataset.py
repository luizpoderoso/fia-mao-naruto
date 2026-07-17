import os
import hashlib
from PIL import Image

DATASET_PATH = os.path.join("../../dataset")
SIGNALS = ["bird", "boar", "dog", "dragon", "hare", "horse", "monkey", "ox", "ram", "rat", "snake", "tiger"]

def get_img_hash(caminho_arquivo): # calcula o identificado único da imagem
    hash_md5 = hashlib.md5()
    with open(caminho_arquivo, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

for signal in os.listdir(DATASET_PATH):
    signal_path = os.path.join(DATASET_PATH, signal)

    if (signal not in SIGNALS): 
        continue
    
    signal_total_count = 0
    signal_png_count = 0
    signal_jpg_count = 0
    singnal_duplicates_count = 0

    resolutions = dict()
    seen_hashes = set()

    for img_filename in os.listdir(signal_path):
        lower_img_name = img_filename.lower()

        # formato
        if lower_img_name.endswith(".png"): signal_png_count += 1
        elif lower_img_name.endswith(".jpg") or lower_img_name.endswith(".jpeg"): signal_jpg_count += 1
        signal_total_count += 1

        # resoluções
        img_path = os.path.join(signal_path, img_filename)
        try:
            with Image.open(img_path) as img:
                key = f"{img.size[0]}x{img.size[1]}"

                if key not in resolutions: resolutions[key] = 0
                resolutions[key] += 1
        except Exception:
            pass

        # duplicatas
        try:
            img_hash = get_img_hash(img_path)
            if img_hash in seen_hashes: # verifica se o hash já foi visto, ou seja, a imagem é idêntica a outra
                signal_duplicates_count += 1
            else:
                seen_hashes.add(img_hash)
        except Exception:
            pass

    print(f"{'-' * 25}\nSelo: {signal}\nTotal de Imagens: {signal_total_count}")

    print("\n---RESOLUÇÕES---")
    for key in resolutions:
        length = resolutions[key]
        print(f"{key}: {length}")

    print(f"\n---FORMATO---\nImagens PNG: {signal_png_count}\nImagens JPG: {signal_jpg_count}\nOutras imagens: {signal_total_count - signal_png_count - signal_jpg_count}")

    print(f"\n---GERAL---\nDuplicatas: {singnal_duplicates_count}\n{'-' * 25}\n")