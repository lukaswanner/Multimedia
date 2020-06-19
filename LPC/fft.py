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
    outputSignal = []
    blockcount = 10
    loop = 0
    while loop < fftLength:
        arr = numpy.fft.fft(inputSignal[1][loop:loop + fftLength//blockcount])
        arrabs = numpy.abs(arr)
    
        sortedarr = numpy.sort(arrabs)
        for i in range(nDeleteFreq//blockcount):
            index = numpy.where(arrabs == sortedarr[i])
            arr[index] = 0
    
        outputSignal.extend(numpy.fft.ifft(arr))
        loop += fftLength//blockcount
        print(loop)
    return outputSignal

def main(pieces):
    output = fft(pieces[0],120000,len(pieces[0][1]))
    output = numpy.asarray(output,dtype=numpy.int16)
    scipy.io.wavfile.write("out.wav", 16000, output)


if __name__ == "__main__":
    wavinput = wav.read("itu_female1.wav")
    length = len(wavinput[1])
    pieces = []
    i = 0
    while i != len(wavinput[1]):
        pieces.append(wavinput[i:i + length])
        i += length

    main(pieces)
