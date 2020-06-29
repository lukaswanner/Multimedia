import numpy as np
from scipy import fftpack as sci
from PIL import Image
# This function demonstrates the jpeg encoding
#
#   input  :   original image
#   output :   matrix with quantised DCT values
def jpegEncode(input):

    # DCT matrix
    ar = np.array([range(8)])
    T = np.array(0.5 * np.cos(ar.T * (2*ar+1) * np.pi / 16))
    T[0,:] = np.sqrt(1/8)

    im = np.array(Image.open(input))
    pixellen = len(im)
    numsub = pixellen // 8

    imglist = []
    imgsplit = np.vsplit(im, numsub)
    for row, val in enumerate(imgsplit):
        for col in range(numsub):
            #print(row, col, ":")
            #print(val[:, col*8:(col+1)*8])
            imglist.append(val[:, col*8:(col+1)*8])

    dctlist = []
    for matrix in imglist:
        #dctlist.append(np.dot(T,matrix))
        dctlist.append(sci.dct(matrix))
        for row in matrix:
            x = 0
            for i in range(len(T)):
                row[i] * T[x][i]
            x += 1
        break

    # Luminance quantization matrix
    q = [   [16, 11, 10, 16, 24, 40, 51, 61],
            [12, 12, 14, 19, 26, 58, 60, 55],
            [14, 13, 16, 24, 40, 57, 69, 56],
            [14, 17, 22, 29, 51, 87, 80, 62],
            [18, 22, 37, 56, 68, 109, 103, 77],
            [24, 35, 55, 64, 81, 104, 113, 92],
            [49, 64, 78, 87, 103, 121, 120, 101],
            [72, 92, 95, 98, 112, 100, 103, 99]]



    output = 0

    return output

# This function demonstrates the jpeg decoding
#
#   input  :   matrix with quantised DCT values
#   output :   reconstructed image
def jpegDecode(input):
    # DCT matrix
    ar = np.array([range(8)])
    T = np.array(0.5 * np.cos(ar.T * (2 * ar + 1) * np.pi / 16))

    # Luminance quantization matrix
    q = [[16, 11, 10, 16, 24, 40, 51, 61],
         [12, 12, 14, 19, 26, 58, 60, 55],
         [14, 13, 16, 24, 40, 57, 69, 56],
         [14, 17, 22, 29, 51, 87, 80, 62],
         [18, 22, 37, 56, 68, 109, 103, 77],
         [24, 35, 55, 64, 81, 104, 113, 92],
         [49, 64, 78, 87, 103, 121, 120, 101],
         [72, 92, 95, 98, 112, 100, 103, 99]]


    output = 0

    return output

def main():
    input = "house.jpg"

    encoded = jpegEncode(input)
    decoded = jpegDecode(encoded)

if __name__ == "__main__":
    main()