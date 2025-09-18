FROM python:3.12-slim

# System deps for PyAudio (PortAudio) and runtime
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       portaudio19-dev \
       libasound2 \
       libportaudio2 \
       libportaudiocpp0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source and small Vosk model (big model is heavy — not copied by default)
COPY src ./src
COPY small_model ./small_model

# Optionally copy big model if you uncomment the next line
# COPY big_model ./big_model

# Expose TCP server port
EXPOSE 12345

# Default environment values (can be overridden at runtime)
ENV VOSK_MODEL_DIR=small_model \
    OLLAMA_MODEL=qwen3:0.6b \
    TCP_HOST=0.0.0.0 \
    TCP_PORT=12345 \
    SQLITE_PATH=/app/device.db

# Default command: run voice assistant
CMD ["python", "-m", "src.app.voice_assistant"]


