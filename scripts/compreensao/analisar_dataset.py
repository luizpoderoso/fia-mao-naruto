import os

DATASET_PATH = os.path.join("../../dataset")

SIGNALS = ["bird", "boar", "dog", "dragon", "hare", "horse", "monkey", "ox", "ram", "rat", "snake", "tiger"]

for signal in os.listdir(DATASET_PATH):
    signal_path = os.path.join(DATASET_PATH, signal)

    if (signal not in SIGNALS): 
        continue
    
    signal_total_count = 0
    signal_png_count = 0
    signal_jpg_count = 0

    for img_name in os.listdir(signal_path):
        lower_img_name = img_name.lower()

        if lower_img_name.endswith(".png"): signal_png_count += 1
        elif lower_img_name.endswith(".jpg") or lower_img_name.endswith(".jpeg"): signal_jpg_count += 1
        signal_total_count += 1

    print(f"Selo: {signal}\nTotal de Imagens: {signal_total_count}\n---FORMATO---\nImagens PNG: {signal_png_count}\nImagens JPG: {signal_jpg_count}\nOutras imagens: {signal_total_count - signal_png_count - signal_jpg_count}\n")