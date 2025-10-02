import numpy as np
import sounddevice as sd


SAMPLE_RATE = 44100  # Hz
DURATION = 1.0


A4_FREQ = 440.0
NOTES = [
    "C", "C#", "D", "D#", "E", "F", "F#",
    "G", "G#", "A", "A#", "B"
]

def freq_to_note(freq):
    if freq <= 0:
        return None

    midi = round(69 + 12 * np.log2(freq / A4_FREQ))
    note = NOTES[midi % 12]
    return note

CHORDS = {
    "C MAIOR": {"C", "E", "G"},
    "C# MAIOR": {"C#", "F", "G#"},
    "D MAIOR": {"D", "F#", "A"},
    "D# MAIOR": {"D#", "G", "A#"},
    "E MAIOR": {"E", "G#", "B"},
    "F MAIOR": {"F", "A", "C"},
    "F# MAIOR": {"F#", "A#", "C#"},
    "G MAIOR": {"G", "B", "D"},
    "G# MAIOR": {"G#", "C", "D#"},
    "A MAIOR": {"A", "C#", "E"},
    "A# MAIOR": {"A#", "D", "F"},
    "B MAIOR": {"B", "D#", "F#"},

    "C MENOR": {"C", "D#", "G"},
    "C# MENOR": {"C#", "E", "G#"},
    "D MENOR": {"D", "F", "A"},
    "D# MENOR": {"D#", "F#", "A#"},
    "E MENOR": {"E", "G", "B"},
    "F MENOR": {"F", "G#", "C"},
    "F# MENOR": {"F#", "A", "C#"},
    "G MENOR": {"G", "A#", "D"},
    "G# MENOR": {"G#", "B", "D#"},
    "A MENOR": {"A", "C", "E"},
    "A# MENOR": {"A#", "C#", "F"},
    "B MENOR": {"B", "D", "F#"}
}


def recognize_chord(notes):
    note_set = set(notes)
    for chord, chord_notes in CHORDS.items():
        if chord_notes.issubset(note_set):
            return chord
    return "não entendi"

def listen_and_analyze():
    recording = sd.rec(int(SAMPLE_RATE * 1), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()

    data = recording.flatten()
    fft = np.fft.rfft(data)
    freqs = np.fft.rfftfreq(len(data), 1 / SAMPLE_RATE)
    magnitudes = np.abs(fft)

    peak_indices = magnitudes.argsort()[-10:][::-1]
    detected_notes = []
    for idx in peak_indices:
        freq = freqs[idx]
        note = freq_to_note(freq)
        if note and note not in detected_notes:
            detected_notes.append(note)

    print("Detected notes:", detected_notes)

    chord = recognize_chord(detected_notes)
    print("Recognized chord:", chord)



while True:
    listen_and_analyze()
