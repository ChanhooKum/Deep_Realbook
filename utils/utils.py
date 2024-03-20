
import sys
sys.path.append('/content/drive/My Drive/Colab Notebooks/MARG/Deep Realbook/utils/')

import importlib
import config

importlib.reload(config)  # Reload the module after making changes

from config import note_to_index, index_to_note, interval_semitones, tension_intervals, tension_intervals_reduced

import json

def extract_chords_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:  # Add 'encoding=utf-8'
        data = json.load(file)
        songs_data = data.get('songs', [])
        chord_sequences = {}
        for song in songs_data:
            title = song.get('title', 'Unknown')
            measures = song.get('music', {}).get('measures', [])
            chords = []
            for measure in measures:
                for chord in measure:
                    # Replace None with "NC" (No Chord)
                    chord = chord if chord is not None else "NC"
                    chords.append(chord)
                chords.append('|')  # Add bar separator after each measure
            # Remove the last bar separator
            chord_sequence = chords[:-1]
            chord_sequences[title] = chord_sequence
        return chord_sequences


def note_to_vector(note):
    """Converts a note to its 12-dimensional vector representation."""
    vector = [0] * 12
    vector[note_to_index[note]] = 1
    return vector

def add_interval_to_vector(vector, root, interval):
    if interval in interval_semitones:
        note_index = (note_to_index[root] + interval_semitones[interval]) % 12
        vector[note_index] = 1
    return vector

def get_interval_between_notes(root_note, bass_note):
    """Calculate the interval between root note and bass note."""
    root_index = note_to_index[root_note]
    bass_index = note_to_index[bass_note]
    interval = (bass_index - root_index) % 12
    # Find the interval name
    for name, semitone in interval_semitones.items():
        if semitone == interval:
            return name
    return None

def chord_to_vector(chord):
    """Converts a chord string to its 12-dimensional vector representation."""

    # Handle special cases
    if chord == '|':
        return ['|']  # Unique representation for bar token
    elif chord == 'NC':
        return [0] * 12  # Return a vector of zeros for no chord

    parts = chord.split('/')
    main_part = parts[0]

    # Extract root and tension
    root = main_part[0]
    if len(main_part) > 1 and main_part[1] in ['#', 'b']:
        root += main_part[1]
        tension = main_part[2:]
    else:
        tension = main_part[1:]

    # Start with the root note
    vector = note_to_vector(root)

    intervals = tension_intervals.get(tension, [])

    for interval in intervals:
        vector = add_interval_to_vector(vector, root, interval)

    # Add bass note if it's a fraction chord
    if len(parts) > 1:
        bass = parts[1]
        if bass in note_to_index:  # If bass is a note
            interval = get_interval_between_notes(root, bass)
            if interval:
                vector = add_interval_to_vector(vector, root, interval)

    return vector

def create_vector_representation(chord_sequences):
    vector_dict = {}
    for key, chords in chord_sequences.items():
        vector_dict[key] = [chord_to_vector(chord) for chord in chords if chord is not None]
    return vector_dict


def get_lexicographically_smallest_rotation(queue):
    """Get the lexicographically smallest rotation of the queue."""
    n = len(queue)
    rotations = [queue[i:] + queue[:i] for i in range(n)]
    return min(rotations)

# Function to map vector to categories 'A', 'B', 'C', 'D'
def map_vectors_to_categories(vector1, vector2):
    return ['A' if v1 == 0 and v2 == 0 else
            'B' if v1 == 1 and v2 == 0 else
            'C' if v1 == 0 and v2 == 1 else
            'D' for v1, v2 in zip(vector1, vector2)]

def replace_NC_tokens(chords):
    for i in range(len(chords)):
        if chords[i] == [0,0,0,0,0,0,0,0,0,0,0,0]:  # NC token found
            if i > 0:
                # Replace with previous chord
                chords[i] = chords[i-1]
            else:
                # Look for the next non-NC chord and replace with it
                j = i + 1
                while j < len(chords) and chords[j] == [0,0,0,0,0,0,0,0,0,0,0,0]:
                    j += 1
                if j < len(chords):
                    chords[i] = chords[j]

    return chords

def create_circular_representations(songs):
    new_sequences = {}

    for song_name, chords in songs.items():
        chords = replace_NC_tokens(chords)  # Replace NC tokens
        token_sequence = []
        i = 0
        while i < len(chords) - 1:
            # Skip bar tokens
            if chords[i] == ['|']:
                i += 1
                continue

            # Find the next chord index that is not a bar token
            j = i + 1
            while j < len(chords) and chords[j] == ['|']:
                j += 1

            # Skip if no valid next chord is found
            if j >= len(chords):
                break

            # Map vectors to categories and find smallest rotation
            categories = map_vectors_to_categories(chords[i], chords[j])
            smallest_rotation = get_lexicographically_smallest_rotation(categories)
            rotation_str = ''.join(smallest_rotation)

            # Check for bar token between chords
            if j - i == 2:
                rotation_str += 'F'  # Bar token present
            else:
                rotation_str += 'E'  # No bar token

            token_sequence.append(rotation_str)
            i = j  # Move to the next chord

        new_sequences[song_name] = token_sequence

    return new_sequences


def decode_chord_representation(input_str, mapped_results):
    # Convert string back to list of categories
    categories = list(input_str)

    # Find chord pairs that match the categories in mapped_results
    for first_chord, next_chord, cat in mapped_results:
        if cat == categories:
            return first_chord, next_chord

    return None, None

def calculate_interval(note1, note2):
    index1 = note_to_index[note1]
    index2 = note_to_index[note2]
    return (index2 - index1) % 12

def transpose_chord(chord, interval):
    root = get_root(chord)
    if root is None:
        return None
    transposed_root_index = (note_to_index[root] + interval) % 12
    transposed_root = index_to_note[transposed_root_index]
    return chord.replace(root, transposed_root, 1)

def get_root(chord):
    for note in note_to_index.keys():
        if chord.startswith(note):
            return note
    return None

def process_and_transpose_sequences(generated_sequences, mapped_results):
    all_sequences_transposed_chords = []
    all_final_sequences = []

    for generated_text in generated_sequences:
        print(f"Generated Sequence: {generated_text}")

        decoded_chords = []
        bar_tokens = []
        for category_str in generated_text.split():
            # Detach the last character and decode the chord pair
            token, bar_token_indicator = category_str[:-1], category_str[-1]
            first_chord, next_chord = decode_chord_representation(token, mapped_results)

            # Add bar token information
            bar_tokens.append(bar_token_indicator)

            if first_chord and next_chord:
                decoded_chords.append((first_chord, next_chord))

        if not decoded_chords:
            print("No valid chords found in this sequence")
            continue

        transposed_chords = []
        final_sequence = []
        prev_second_chord_root = None
        for i, (first_chord, second_chord) in enumerate(decoded_chords):
            if i != 0:
                interval = calculate_interval(get_root(first_chord), prev_second_chord_root)
                first_chord = transpose_chord(first_chord, interval)
                second_chord = transpose_chord(second_chord, interval)
            transposed_chords.append((first_chord, second_chord))

            # Append to final sequence with bar tokens
            final_sequence.append(first_chord)
            if bar_tokens[i] == 'F':
                final_sequence.append('|')  # Add bar token

            prev_second_chord_root = get_root(second_chord)

        all_sequences_transposed_chords.append(transposed_chords)
        all_final_sequences.append(final_sequence)

    return all_sequences_transposed_chords, all_final_sequences
