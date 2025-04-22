import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl, QTimer, Qt, QSize
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(BASE_DIR, "C:/Users/Astolfo-Lock/Pictures/Agarrini/Agarrini/agarrini.mp4") # video
INSTANCES = 5 # ventanas

class VideoWindow(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setSource(QUrl.fromLocalFile(video_path))

        self.media_player.mediaStatusChanged.connect(self.check_status)
        self.media_player.mediaStatusChanged.connect(self.adjust_to_video_size)
        self.media_player.play()

        self.timer = QTimer()
        self.timer.timeout.connect(self.move_randomly)
        self.timer.start(300)  #movimiento

    def adjust_to_video_size(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            size = self.media_player.videoSink().videoSize()
            if size.isValid():
                self.resize(size.width(), size.height())

    def move_randomly(self):
        screen = QApplication.primaryScreen().availableGeometry()
        max_x = screen.width() - self.width()
        max_y = screen.height() - self.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.move(new_x, new_y)

    def check_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.close()
            QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    windows = []
    for i in range(INSTANCES):
        win = VideoWindow(VIDEO_PATH)
        win.move(random.randint(0, 800), random.randint(0, 600))
        win.show()
        windows.append(win)

    sys.exit(app.exec())
