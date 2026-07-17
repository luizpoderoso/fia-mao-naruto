import os
from PIL import Image
import imagehash

DATASET_PATH = os.path.join("../../dataset")
SIGNALS = ["bird", "boar", "dog", "dragon", "hare", "horse", "monkey", "ox", "ram", "rat", "snake", "tiger"]
IMG_DIFFERENCE_LIMIT = 5

total_count = 0
png_count = 0
jpg_count = 0
duplicates_count = 0
simmilar_count = 0

resolutions_count = dict()

for signal in os.listdir(DATASET_PATH):
    signal_path = os.path.join(DATASET_PATH, signal)

    if (signal not in SIGNALS): 
        continue
    
    signal_total_count = 0
    signal_png_count = 0
    signal_jpg_count = 0
    signal_duplicates_count = 0
    signal_simmilar_count = 0

    signal_resolutions_count = dict()
    seen_hashes = set()

    for img_filename in os.listdir(signal_path):
        lower_img_name = img_filename.lower()

        # formato
        if lower_img_name.endswith(".png"): signal_png_count += 1
        elif lower_img_name.endswith(".jpg") or lower_img_name.endswith(".jpeg"): signal_jpg_count += 1
        signal_total_count += 1

        img_path = os.path.join(signal_path, img_filename)
        try:
            with Image.open(img_path) as img:
                # resoluções
                key = f"{img.size[0]}x{img.size[1]}"
                
                if key not in signal_resolutions_count: signal_resolutions_count[key] = 0
                if key not in resolutions_count: resolutions_count[key] = 0
                
                signal_resolutions_count[key] += 1
                resolutions_count[key] += 1
                
                # duplicatas / semelhantes
                img_hash = imagehash.phash(img)
                
                is_duplicate = False
                is_similar = False

                for seen_hash in seen_hashes:
                    difference = img_hash - seen_hash
                    
                    if difference == 0:
                        is_duplicate = True
                        break
                    elif difference <= IMG_DIFFERENCE_LIMIT:
                        is_similar = True
                
                if is_duplicate:
                    signal_duplicates_count += 1
                elif is_similar:
                    signal_simmilar_count += 1
                else:
                    seen_hashes.add(img_hash)
        except Exception:
            pass

    print(f"{'-' * 25}\nSelo: {signal}\nTotal de Imagens: {signal_total_count}")

    print("\n---RESOLUÇÕES---")
    for key in signal_resolutions_count:
        length = signal_resolutions_count[key]
        print(f"{key}: {length}")

    print(f"\n---FORMATO---\nImagens PNG: {signal_png_count}\nImagens JPG: {signal_jpg_count}\nOutras imagens: {signal_total_count - signal_png_count - signal_jpg_count}")

    print(f"\n---GERAL---\nDuplicatas: {signal_duplicates_count}\nSemelhantes: {signal_simmilar_count}\n{'-' * 25}\n")
    
    total_count += signal_total_count
    png_count += signal_png_count
    jpg_count += signal_jpg_count
    duplicates_count += signal_duplicates_count
    simmilar_count += signal_simmilar_count
    
print(f"{'-' * 25}\nTotal\nTotal de Imagens: {total_count}")

print("\n---RESOLUÇÕES---")
for key in resolutions_count:
    length = resolutions_count[key]
    print(f"{key}: {length}")
    
print(f"\n---FORMATO---\nImagens PNG: {png_count}\nImagens JPG: {jpg_count}\nOutras imagens: {total_count - png_count - jpg_count}")

print(f"\n---GERAL---\nDuplicatas: {duplicates_count}\nSemelhantes: {simmilar_count}\n{'-' * 25}\n")