import scipy.io.wavfile

from scipy import fft
from numpy import linspace, asarray
import sys



def readVoice(filepath):
    """FUNCTION THAT RETURN SIGNAl AND SAMPLING FREQUENCY OF VOICE"""
    sampling, signal = scipy.io.wavfile.read(filepath)
    if len(signal.shape) == 2:
        signal = asarray([sample[0] for sample in signal])

    return sampling, signal


def avgFrequency(w, signal):
    """FUNCTION THAT RETURN DOMINANT FREQUENCY"""
    n = min(4 * w, len(signal))
    spec = abs(fft.fft(signal[0:n]))
    freq = linspace(0, w, n)
    amplitudes = []
    frequencies = []

    for ind, f in enumerate(freq):
        if f > 85 and f < 250:  # czestotliwosc ludzkiego glosu
            amplitudes.append(spec[ind])
            frequencies.append(f)

    i = max(amplitudes)
    indexMaxAmp = amplitudes.index(i)
    avgFreq = frequencies[indexMaxAmp]

    return avgFreq


def checkSex(freq):
    """FUNCTION DECIDES SEX USING FREQUENCY"""
    if freq < 172.5:  # maks. czestotliwosc u mezczyzn
        print("M")
    else:
        print("K")


def main(argv):
    filepath = str(argv[0])
    w, s = readVoice(filepath)
    freq = avgFrequency(w, s)
    checkSex(freq)


if __name__ == "__main__":
    main(sys.argv[1:])
