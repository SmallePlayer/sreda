from vosk import Model, KaldiRecognizer
import pyaudio
import json

from src.core.llm import generate_prompt
from src.config.settings import VOSK_MODEL_DIR


def run_voice_assistant() -> None:
    model = Model(VOSK_MODEL_DIR)
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8192,
    )
    stream.start_stream()

    KEYWORD = "пятница"
    is_listening_for_command = False

    print(f"Слушаю... Произнесите '{KEYWORD}' для активации")

    while True:
        data = stream.read(4096, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").lower()

            if text:
                if not is_listening_for_command and KEYWORD in text:
                    print("Да, я слушаю...")
                    is_listening_for_command = True
                elif is_listening_for_command:
                    command = text.replace(KEYWORD, "").strip()
                    if command:
                        print(f"Выполняю команду: {command}")
                        generate_prompt(command)
                        is_listening_for_command = False
                        print(f"Снова слушаю ключевое слово '{KEYWORD}'...")



if __name__ == "__main__":
    run_voice_assistant()

