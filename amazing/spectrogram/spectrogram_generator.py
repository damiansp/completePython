import librosa
import matplotlib.pyplot as plt


def main(args):
    audio = args[1]
    x, sr = librosa.load(audio)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plot(Xdb, sr, audio)


def plot(x, sr, title):
    plt.figure(figsize=(10, 5))
    librosa.display.specshow(x, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.title(title)
    plt.show()
