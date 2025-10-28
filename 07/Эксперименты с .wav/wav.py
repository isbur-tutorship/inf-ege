import numpy as np
import wave
import struct

# Параметры аудио
sample_rate = 16000   # частота дискретизации (Гц)
duration = 2.0       # длительность (сек)
amplitude = 32767    # максимальная амплитуда для 16-битного звука

# === вот тут ученики могут менять функцию ===
def f(t):
    switch = np.floor(3*t) % 3
    frequencies = [
        2*np.pi*220,
        2*np.pi*int(220*2**(1/6)**2),
        2*np.pi*int(220*2**(1/6)**4)
    ]
    return np.sin(frequencies[t]*t)

# =============================================

# Генерация массива времени
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Вычисление значений функции
y = f(t)

# Нормализация, чтобы не было перегрузки
y = y / np.max(np.abs(y))

# Конвертация в 16-битные значения
samples = (amplitude * y).astype(np.int16)

# Сохранение в WAV
with wave.open("output.wav", "w") as wav_file:
    wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))
    wav_file.writeframes(struct.pack("<" + "h" * len(samples), *samples))

print("Файл output.wav успешно создан!")
