import note_seq
from magenta.music import NoteSequence, sequence_proto_to_midi_file
import uuid
import os

AUDIO_DIR = "static/audio"

def generar_melodia(prompt):
    os.makedirs(AUDIO_DIR, exist_ok=True)

    pitch = 60 if "triste" in prompt else 72 if "épica" in prompt else 65

    sequence = NoteSequence()
    for i in range(8):
        note = sequence.notes.add()
        note.pitch = pitch + (i % 3)
        note.start_time = i * 0.5
        note.end_time = (i + 1) * 0.5
        note.velocity = 80
    sequence.total_time = 5.0

    filename = f"{uuid.uuid4().hex}.mid"
    filepath = os.path.join(AUDIO_DIR, filename)
    sequence_proto_to_midi_file(sequence, filepath)
    return filename
