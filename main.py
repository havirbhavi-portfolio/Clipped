import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd

# Parameters
sample_rate = 48000
duration = 1  # seconds
frequency = 440  # Hz

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# -------- Part 1: sine.wav --------
amplitude_1 = 8192  # 1/4 max
sine_wave = amplitude_1 * np.sin(2 * np.pi * frequency * t)

sine_wave = sine_wave.astype(np.int16)
write("sine.wav", sample_rate, sine_wave)

# -------- Part 2: clipped.wav --------
amplitude_2 = 16384  # 1/2 max
wave = amplitude_2 * np.sin(2 * np.pi * frequency * t)

# Clipping
wave = np.clip(wave, -8192, 8192)

wave = wave.astype(np.int16)
write("clipped.wav", sample_rate, wave)

# -------- Part 3: Play clipped audio --------
sd.play(wave, samplerate=sample_rate)
sd.wait()

print("Done! Files created and audio played.")