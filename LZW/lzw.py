# Diese Funktion liest eine Sequenz von Zeichen und codiert diese nach dem LZW Verfahren
#
# Input:        input:          Zeichensequenz
#
# Output:       output:         codierte Zeichensequenz
#               encodeDict:     Wörterbuch
def lzwEncode(input):
    output = ""
    encodeDict = {}
    s = input[0]
    found = False
    initial_input = input

    while len(initial_input) > 0:
        encodeDict[len(encodeDict)+ 1] = min(initial_input)
        initial_input = initial_input.replace(min(initial_input),"")

    for i in range(1,len(input)):
        c = input[i]
        for keys in encodeDict.values():
            if str(keys).startswith(str(s+c)):
                s = s+c
                found = True
                break
        if not found:
            for i in range(len(encodeDict)+1):
                if s == encodeDict.get(i):
                    output = output + str(i) + " "
                    break
            encodeDict[len(encodeDict)+1] = s+c
            s = c
        found = False

    for i in range(len(encodeDict) + 1):
        if s == encodeDict.get(i):
            output = output + str(i)

    return output, encodeDict


# Diese Funktion decodiert eine LZW-codierte Zeichensequenz
#
# Input:        input:          codierte Zeichensequenz
#
# Output:       output:         decodierte Zeichensequenz
#               decodeDict:     Wörterbuch
def lzwDecode(input):
    output = ""
    decodeDict = {}
    s = input[0]
    found = False
    initial_input = input

    print("\n")

    while len(initial_input) > 0:
        decodeDict[len(decodeDict)+ 1] = min(initial_input)
        initial_input = initial_input.replace(min(initial_input),"")

    print(decodeDict)

    return output, decodeDict


def main():
    compressed, enDict = lzwEncode('wabba wabba wabba wabba woo woo woo')
    print(compressed)
    decompressed, deDict = lzwDecode(compressed)
    print(decompressed)


if __name__ == "__main__":
    main()
