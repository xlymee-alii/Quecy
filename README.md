# Quecy

Quecy is a local desktop AI assistant built with Python. Its current Phase 3C version provides a simple desktop chat window that sends prompts to Qwen3 0.6B through Ollama and reads replies aloud with pyttsx3.

## Status

**Current phase: Phase 3C.** The checked-in application is the working Phase 3C implementation in `app.py`. Phase 3D is the next planned phase; it has not been implemented in this repository.

### Implemented in Phase 3C

- PySide6 desktop window
- Chat interface with a read-only conversation area
- Text input and Send button
- Enter-to-send
- Ollama connection
- Qwen3 0.6B responses through Ollama
- pyttsx3 voice output

### Not implemented

- Background worker/thread architecture
- Responsive, non-blocking Ollama generation
- A proper Stop button
- Advanced speech interruption
- Modern futuristic UI
- System tray support
- Global hotkey
- Computer or system controls
- `.exe` packaging

## Architecture

```text
User
  ↓
PySide6 GUI
  ↓
Python
  ↓
Ollama
  ↓
Qwen3 0.6B
  ↓
Response
  ↓
pyttsx3
  ↓
Speaker
```

The current application calls Ollama synchronously from the GUI event handler, then speaks the resulting answer. Ollama must be installed and running separately; the Qwen model is not bundled with Quecy.

## Tech stack

- Python
- PySide6
- Ollama Python package
- Qwen3 0.6B, served locally through Ollama
- pyttsx3

## Installation

### 1. Install Ollama

Install Ollama from [ollama.com](https://ollama.com/), then ensure its local service is available.

### 2. Download the model

In a terminal, run:

```powershell
ollama pull qwen3:0.6b
```

### 3. Install Python dependencies

Use Python 3 and install the dependencies in this repository:

```powershell
python -m pip install -r requirements.txt
```

### 4. Run Quecy

```powershell
python app.py
```

Enter a prompt and press Enter or select **SEND**. Quecy displays and voices the model's reply.

## Current limitations

Generation and speech run on the GUI thread, so the window can become unresponsive while Ollama is generating a response or pyttsx3 is speaking. There is no functional in-app stop control, and errors from unavailable Ollama or a missing model are not yet presented with dedicated UI feedback.

## Roadmap

### Next: Phase 3D (planned)

Phase 3D is planned to address the Phase 3C interaction limitations, beginning with background worker/thread architecture, non-blocking generation, a proper Stop control, and improved speech interruption. These items are planned only and are not part of the current code.

### Future plans

- Modern futuristic UI
- System tray and global hotkey support
- Computer and system controls
- Windows `.exe` packaging

For packaging, a future release may use a Python packaging tool to produce a Windows executable after the application architecture is ready. No executable is currently included or supported.

## Failure data and previous attempts

A prior command-line prototype explored threaded text-to-speech and keyboard-based speech interruption. It depended on an extra keyboard-control package and used a manual terminal loop; it was not suitable as the Phase 3C desktop application. That experiment is intentionally excluded from this repository rather than retained as active code. The documented outcome is the current minimal PySide6 Phase 3C application, whose remaining blocking behavior is listed above.

## Project structure

```text
Quecy/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Development notes

This repository deliberately preserves the current Phase 3C scope. It does not implement Phase 3D or future roadmap work.
