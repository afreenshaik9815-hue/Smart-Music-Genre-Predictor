import librosa
import numpy as np

def extract_features(file):
    y, sr = librosa.load(file, duration=5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr), axis=1)
    return mfcc
