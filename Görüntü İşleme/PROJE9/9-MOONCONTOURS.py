import cv2
import os
import numpy as np

image_paths = [
    "D:/ornekresim/moons/ay1.jpg",
    "D:/ornekresim/moons/ay2.jpg",
    "D:/ornekresim/moons/ay3.jpg",
    "D:/ornekresim/moons/ay4.jpg"
]

save_path = "D:/ornekresim/moonkonturlar"

lower = np.array([0, 0, 50])
upper = np.array([180, 60, 255])

for idx, path in enumerate(image_paths):
    img = cv2.imread(path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_contour = img.copy()

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        boyut = max(w, h)
        x_centered = x + w // 2 - boyut // 2
        y_centered = y + h // 2 - boyut // 2

        x_start = max(0, x_centered)
        y_start = max(0, y_centered)
        x_end = min(img.shape[1], x_start + boyut)
        y_end = min(img.shape[0], y_start + boyut)

        cv2.rectangle(img_contour, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)

    filename = os.path.join(save_path, f"ay{idx+1}_contour.jpg")
    cv2.imwrite(filename, img_contour)
    print(f"{filename} kaydedildi.")
    cv2.imshow(f"Ay {idx+1} - Konturlar", img_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
