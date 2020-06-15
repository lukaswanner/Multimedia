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
    #fig, axs = plt.subplots(2)
    #fig.suptitle('Vertically stacked subplots')
    #axs[0].plot(arr)
    sortedarr = numpy.sort(arrabs)
    for i in range(nDeleteFreq):
        index = numpy.where(arrabs == sortedarr[i])
        arr[index] = 0
    #axs[1].plot(arr)
    #plt.show()
    outputSignal = numpy.fft.ifft(arr)
    axs[1].plot(outputSignal)
    plt.show()
    return outputSignal

def main(pieces):
    # output = fft()
    output = fft(pieces[0],9000,len(pieces[0][1]))
    print(output.dtype)
    output = output.astype(int)
    print(output.dtype)
    scipy.io.wavfile.write("out.wav", 16000, output)


if __name__ == "__main__":
    wavinput = wav.read("itu_male1.wav")
    length = len(wavinput[1])
    pieces = []
    i = 0
    while i != len(wavinput[1]):
        pieces.append(wavinput[i:i + length])
        i += length
    fig, axs = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(pieces[0][1])
    main(pieces)
