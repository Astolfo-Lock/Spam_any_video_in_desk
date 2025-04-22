# Spam Any Video in Desk / Spam de Videos

This program will play a video as many times as you want in floating windows, all moving randomly across your screen until the video ends.

Este programa reproduce un video muchas veces, en ventanas que se mueven aleatoriamente por la pantalla hasta que el video termina.

---

## How it works / ¿Cómo funciona?

- Opens multiple frameless windows (default: 5).
- Plays the same video simultaneously.
- The windows move randomly around the screen.
- All windows close automatically once the video ends.

- Abre varias ventanas sin marco (predeterminado: 5).
- Reproduce el mismo vídeo simultáneamente.
- Las ventanas se mueven aleatoriamente por la pantalla.
- Todas las ventanas se cierran automáticamente al finalizar el vídeo.

---
# Compilar el proyecto
```bash
pyinstaller --onefile --noconsole --icon=agarrini.ico --add-data "agarrini.mp4;." agarriniv2.py
```

# Instalar dependencias
```bash
pip install PyQt6 PyQt6-Qt6 PyQt6-sip
```
