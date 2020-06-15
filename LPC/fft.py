# Input:        inputSignal:    Eingangssignal
#               nDeleteFreq:    Anzahl der zu löschenden Frequenzen
#               fftLength:      Länge der FFT
#
# Output:       outputSignal:   Ausgangssignal
#
# Nützliche Befehle/Collections/Libs: numpy, ftt, scipy.io.wavfile,...

import numpy
import scipy.io.wavfile as wav
import scipy.signal
import matplotlib.pyplot as plt


def fft(inputSignal, nDeleteFreq, fftLength):
    outputSignal = 0
    arr = numpy.fft.fft(inputSignal[1])
    arrabs = numpy.abs(arr)
    fig, axs = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(arr)
    sortedarr = numpy.sort(arrabs)
    for i in range(nDeleteFreq):
        index = numpy.where(arrabs == sortedarr[i])
        arr[index] = 0
    axs[1].plot(arr)
    plt.show()
    return outputSignal

def main(pieces):
    # output = fft()
    for i in range(len(pieces)):
        output = fft(pieces[i],80000,len(pieces[i][1]))
    print("")


if __name__ == "__main__":
    data = wav.read("itu_male1.wav")
    length = len(data[1])
    pieces = []
    i = 0
    while i != len(data[1]):
        pieces.append(data[i:i + length])
        i += length
    main(pieces)
