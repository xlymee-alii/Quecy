import sys
import pyttsx3

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QTextEdit, QLineEdit, QPushButton
)

from ollama import chat


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


# Voice
voice = pyttsx3.init()
voice.setProperty("rate", 140)
voice.setProperty("volume", 1.0)


def send_message():
    message = input_box.text().strip()

    if not message:
        return

    chat_box.append("You: " + message)
    input_box.clear()

    response = chat(
        model="qwen3:0.6b",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    answer = response.message.content

    chat_box.append("Quecy: " + answer)

    voice.say(answer)
    voice.runAndWait()


# Button = Send
send_button.clicked.connect(send_message)

# Enter = Send
input_box.returnPressed.connect(send_message)


layout.addWidget(chat_box)
layout.addWidget(input_box)
layout.addWidget(send_button)

window.setLayout(layout)

window.show()

sys.exit(app.exec())