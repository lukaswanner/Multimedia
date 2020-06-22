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
import scipy as sci


def fft(inputSignal, nDeleteFreq, fftLength):
    outputSignal = []
    inputlen = len(inputSignal[1])
    loop = 0
    while loop < inputlen:
        arr = numpy.fft.fft(inputSignal[1][loop:loop + fftLength])
        arrabs = numpy.abs(arr)
    
        sortedarr = numpy.sort(arrabs)
        for i in range(nDeleteFreq):
            index = numpy.where(arrabs == sortedarr[i])
            """arr = numpy.delete(arr,index)"""
            arr[index] = 0

        outputSignal.extend(numpy.fft.ifft(arr))
        loop += fftLength

    return outputSignal

def main(pieces):
    output = fft(pieces[0],500,512)
    output = numpy.real(output)
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
