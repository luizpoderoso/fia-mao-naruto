import cv2
import os

AUTHOR = "luiz"
VIDEO_NAME = "test.mov"
HAND_SIGNAL = "dragon"

video_path = os.path.join("videos", AUTHOR, VIDEO_NAME)
output_path = os.path.join("../dataset", HAND_SIGNAL)

os.makedirs(output_path, exist_ok=True)

SCREENSHOT_INTERVAL = 60

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print(f"Erro: não foi possível abrir o vídeo {video_path}")
    exit()

# identificar qual é o contador atual na combinação autor-sinal-contador.jpg
pre_files = [file for file in os.listdir(output_path) if file.endswith('.jpg')]
current_counter = len(pre_files)

screenshot_counter = current_counter
frame_counter = 0

print("Iniciando a extração de frames...")

while True:
    was_read, frame = video.read() # lê o frame atual do vídeo

    if not was_read: # fim do vídeo
        break

    if frame_counter % SCREENSHOT_INTERVAL == 0:
        file_name = f"{AUTHOR}-{HAND_SIGNAL}-{screenshot_counter}.jpg"
        file_path = os.path.join(output_path, file_name)

        cv2.imwrite(file_path, frame)
        screenshot_counter += 1
    
    frame_counter += 1

video.release()

print(f"\nProcesso concluído!")
print(f"Total de frames analisados no vídeo: {frame_counter}")
print(f"Total de imagens salvas em '{output_path}': {screenshot_counter - current_counter}")
