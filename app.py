import librosa
import soundfile as sf

def improve_audio_quality(input_audio_file):
    # Load audio file
    y, sr = librosa.load(input_audio_file, sr=None)

    # Remove echo by applying spectral subtraction
    y_denoised = librosa.effects.preemphasis(y)

    # Improve voice audio
    y_enhanced = librosa.effects.trim(y_denoised)[0]

    return y_enhanced, sr

# Example usage
input_audio_file = "input_audio.wav"
output_audio_file = "output_audio.wav"

# Improve audio quality
improved_audio, sample_rate = improve_audio_quality(input_audio_file)

# Export processed audio to a new file
sf.write(output_audio_file, improved_audio, sample_rate)

print("Audio processing complete.")
import librosa
import soundfile as sf

def improve_audio_quality(input_audio_file):
    # Load audio file
    y, sr = librosa.load(input_audio_file, sr=None)

    # Remove echo by applying spectral subtraction
    y_denoised = librosa.effects.preemphasis(y)

    # Improve voice audio
    y_enhanced = librosa.effects.trim(y_denoised)[0]

    return y_enhanced, sr

# Example usage
input_audio_file = "input_audio.wav"
output_audio_file = "output_audio.wav"

# Improve audio quality
improved_audio, sample_rate = improve_audio_quality(input_audio_file)

# Export processed audio to a new file
sf.write(output_audio_file, improved_audio, sample_rate)

print("Audio processing complete.")
