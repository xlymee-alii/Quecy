import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton
)

from PySide6.QtCore import QThread, QObject, Signal, Slot

from ollama import chat
import pyttsx3


# -------------------------
# Ollama Worker
# -------------------------

class OllamaWorker(QObject):
    finished = Signal(str)
    error = Signal(str)

    @Slot(str)
    def generate(self, message):
        try:
            response = chat(
    model="qwen3:0.6b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are Quecy, a local desktop assistant. "
                "Be concise, direct, and helpful."
            )
        },
        {"role": "user", "content": message}
    ],
    options={
        "num_predict": 150,
        "temperature": 0.6
    }
)

            answer = response.message.content
            self.finished.emit(answer)

        except Exception as e:
            self.error.emit(str(e))


# -------------------------
# Quecy App
# -------------------------

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Quecy")
window.resize(600, 700)

layout = QVBoxLayout()

chat_box = QTextEdit()
chat_box.setReadOnly(True)

input_box = QLineEdit()
input_box.setPlaceholderText("Ask Quecy...")

send_button = QPushButton("SEND")

layout.addWidget(chat_box)
layout.addWidget(input_box)
layout.addWidget(send_button)

window.setLayout(layout)


# -------------------------
# Voice
# -------------------------

voice = pyttsx3.init()
voice.setProperty("rate", 140)
voice.setProperty("volume", 1.0)


# -------------------------
# Worker Setup
# -------------------------

thread = QThread()
worker = OllamaWorker()

worker.moveToThread(thread)

thread.start()


# -------------------------
# Send Message
# -------------------------

def send_message():

    message = input_box.text().strip()

    if not message:
        return

    chat_box.append("You: " + message)

    input_box.clear()

    send_button.setEnabled(False)
    input_box.setEnabled(False)

    worker.generate(message)


# -------------------------
# Response Received
# -------------------------

def receive_response(answer):

    chat_box.append("Quecy: " + answer)

    send_button.setEnabled(True)
    input_box.setEnabled(True)

    voice.say(answer)
    voice.runAndWait()


# -------------------------
# Error
# -------------------------

def show_error(error):

    chat_box.append("Quecy Error: " + error)

    send_button.setEnabled(True)
    input_box.setEnabled(True)


# -------------------------
# Connections
# -------------------------

send_button.clicked.connect(send_message)

input_box.returnPressed.connect(send_message)

worker.finished.connect(receive_response)

worker.error.connect(show_error)


# -------------------------
# Start App
# -------------------------

window.show()

sys.exit(app.exec())