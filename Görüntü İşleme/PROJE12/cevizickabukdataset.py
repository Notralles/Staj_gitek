import cv2
import os

input_folders = {
    "cevizic": "C:/cevizic",
    "cevizkabuk": "C:/cevizkabuk"
}

output_dataset = r"C:/datasetcrop"

for folder_name, input_path in input_folders.items():
    output_path = os.path.join(output_dataset, folder_name)
    os.makedirs(output_path, exist_ok=True)

    for img_name in os.listdir(input_path):
        if not img_name.lower().endswith((".bmp")):
            continue

        img_path = os.path.join(input_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Okunamadı: {img_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

       
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            print(f"Kontur bulunamadı: {img_path}")
            continue

        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cropped = img[y:y+h, x:x+w]

        save_path = os.path.join(output_path, img_name)
        success = cv2.imwrite(save_path, cropped)

        if success and os.path.exists(save_path):
            print(f"Kaydedildi: {save_path}")
        else:
            print(f" Kayıt başarısız: {save_path}")

print("Croplanmış görüntüler kaydedildi")
