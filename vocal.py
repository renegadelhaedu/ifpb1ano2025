import numpy as np
import sounddevice as sd
import time


DURATION = 2
SAMPLE_RATE = 44100

LIMIAR_GRAVE_AGUDO = 180
LIMIAR_MEDIO_AGUDO = 300


def capturar_audio(duration, sr):
    """Captura o áudio do microfone."""
    print(f"🎤 Gravando por {duration} segundos. Fale ou cante agora!")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='float64')
    sd.wait()  # Espera a gravação terminar
    print("✅ Gravação concluída.")
    return audio.flatten()


def classificar_frequencia(audio_data, sr):
    """
    Usa a Transformada Rápida de Fourier (FFT) para encontrar a
    frequência fundamental (pitch) dominante no áudio.
    """
    # 1. Aplicar a Transformada de Fourier
    # abs(np.fft.rfft) retorna a magnitude do sinal de frequência
    fft_magnitude = np.abs(np.fft.rfft(audio_data))

    # 2. Gerar as frequências correspondentes
    # Frequências de 0 Hz até Nyquist (sr/2)
    fft_freqs = np.fft.rfftfreq(len(audio_data), 1.0 / sr)

    # 3. Encontrar o pico de frequência (ignorando DC - frequência 0)
    # Procuramos o índice da maior magnitude, excluindo o primeiro índice (DC/silêncio)
    pico_indice = np.argmax(fft_magnitude[1:]) + 1

    # A frequência fundamental (f0) é o valor da frequência no pico_indice
    f0_detectada = fft_freqs[pico_indice]

    return f0_detectada


maior_feq = 0
menor_feq = 2000
lista = list()
while True:

    # 1. Captura o áudio
    audio_data = capturar_audio(DURATION, SAMPLE_RATE)

    # 2. Detecta a frequência
    frequencia = classificar_frequencia(audio_data, SAMPLE_RATE)

    print("-" * 40)
    print(f"Frequência Fundamental Detectada: {frequencia:.2f} Hz")

    lista.append(frequencia)
    # 3. Classificação (Grave, Médio ou Agudo)
    if frequencia < LIMIAR_GRAVE_AGUDO:
        classificacao = f"GRAVE ({LIMIAR_GRAVE_AGUDO} Hz)"
    elif frequencia > LIMIAR_MEDIO_AGUDO:
        classificacao = f"AGUDO ({LIMIAR_MEDIO_AGUDO} Hz)"
    else:
        classificacao = "MÉDIO"

    if frequencia < menor_feq:
        menor_feq = frequencia

    if frequencia > maior_feq:
        maior_feq = frequencia

    print(f"Resultado da Classificação: **{classificacao}**")
    print('foram lidas:', len(lista))
    print('até agora a maior foi',maior_feq, 'e a menor:', menor_feq)
    print("-" * 40)
