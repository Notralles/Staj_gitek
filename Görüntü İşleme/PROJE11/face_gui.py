# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

prototxt_path = "C:/resderp/deploy.prototxt"
model_path = "C:/resderp/res10_300x300_ssd_iter_140000.caffemodel"

class FaceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yüz Tespiti")
        self.setGeometry(200, 200, 700, 700)


        self.label = QLabel("Kamera kapalı")
        self.label.setFixedSize(640, 480)
        self.label.setStyleSheet("background-color: black; color: #D8DEE9; font-size: 20px;")


        self.btn_start = QPushButton("Başlat")
        self.btn_face = QPushButton("Yüz Tanıma: Kapalı")
        self.btn_stop = QPushButton("Bitir")


        self.btn_start.setStyleSheet("""
            QPushButton {
                background-color: #5E81AC;
                color: white;
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
        """)
        self.btn_face.setStyleSheet("""
            QPushButton {
                background-color: #A3BE8C;
                color: white;
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #B5CEA8;
            }
        """)
        self.btn_stop.setStyleSheet("""
            QPushButton {
                background-color: #BF616A;
                color: white;
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
        """)


        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_start)
        button_layout.addWidget(self.btn_face)
        button_layout.addWidget(self.btn_stop)


        self.status_label = QLabel("Durum: Kamera kapalı")
        self.status_label.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.status_label.setAlignment(Qt.AlignCenter)


        self.time_label = QLabel("Süre: 0 sn")
        self.time_label.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.time_label.setAlignment(Qt.AlignCenter)


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.time_label)
        self.setLayout(main_layout)


        self.btn_start.clicked.connect(self.start_camera)
        self.btn_face.clicked.connect(self.toggle_face_detection)
        self.btn_stop.clicked.connect(self.stop_camera)


        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
        self.face_detection_enabled = False


        self.setStyleSheet("background-color: #2E3440;")


        self.blink_timer = QTimer()
        self.blink_timer.timeout.connect(self.blink_status)
        self.blink_state = True

      
        self.start_time = None
        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.update_time)

    def start_camera(self):
        if not self.cap or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(30)
            self.status_label.setText("Durum: Kamera çalışıyor")
            self.blink_timer.start(500)
            self.start_time = time.time()
            self.time_timer.start(1000)  # her saniye güncelle

    def toggle_face_detection(self):
        self.face_detection_enabled = not self.face_detection_enabled
        if self.face_detection_enabled:
            self.btn_face.setText("Yüz Tanıma: Açık")
        else:
            self.btn_face.setText("Yüz Tanıma: Kapalı")

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        if self.face_detection_enabled:
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)),
                1.0,
                (300, 300),
                (104.0, 177.0, 123.0)
            )

            self.net.setInput(blob)
            detections = self.net.forward()

            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    text = f"{confidence*100:.1f}%"
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.putText(frame, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(qt_image))

    def update_time(self):
        elapsed = int(time.time() - self.start_time)
        self.time_label.setText(f"Süre: {elapsed} sn")

    def stop_camera(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None
        self.status_label.setText("Durum: Kamera kapalı")
        self.blink_timer.stop()
        self.status_label.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.label.setText("Kamera kapalı")
        self.label.setStyleSheet("background-color: black; color: #D8DEE9; font-size: 20px;")
        self.time_label.setText("Süre: 0 sn")
        self.time_timer.stop()

    def blink_status(self):
        if self.blink_state: 
            self.status_label.setStyleSheet("color: transparent; font-size: 16px;")
        else:
            self.status_label.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.blink_state = not self.blink_state

    def closeEvent(self, event):
        self.stop_camera()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceApp()
    window.show()
    sys.exit(app.exec_())
