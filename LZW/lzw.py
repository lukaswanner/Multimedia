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
        encodeDict[len(encodeDict) + 1] = min(initial_input)
        initial_input = initial_input.replace(min(initial_input), "")

    initialDict = encodeDict.copy()

    for i in range(1, len(input)):
        c = input[i]
        for keys in encodeDict.values():
            if str(keys).startswith(str(s + c)):
                s = s + c
                found = True
                break
        if not found:
            for i in range(len(encodeDict) + 1):
                if s == encodeDict.get(i):
                    output = output + str(i) + " "
                    break
            encodeDict[len(encodeDict) + 1] = s + c
            s = c
        found = False

    for i in range(len(encodeDict) + 1):
        if s == encodeDict.get(i):
            output = output + str(i)

    return output, encodeDict, initialDict


# Diese Funktion decodiert eine LZW-codierte Zeichensequenz
#
# Input:        input:          codierte Zeichensequenz
#
# Output:       output:         decodierte Zeichensequenz
#               decodeDict:     Wörterbuch
def lzwDecode(input, dict):
    output = ""
    decodeDict = dict.copy()
    i = input[0]
    output = output + "w"
    found = False
    # todo this but clean
    codelen = 1
    while codelen < len(input):
        if input[codelen] != " ":
            if codelen + 1 < len(input) and input[codelen + 1] != " ":
                j = input[codelen] + input[codelen + 1]
                codelen = codelen + 1
            else:
                j = input[codelen]
            if int(j) in decodeDict.keys():
                str1 = str(decodeDict.get(int(i)))
                str2 = str(decodeDict.get(int(j))[0])
                decodeDict[len(decodeDict) + 1] = str1 + str2
                output = output + decodeDict.get(int(j))
            else:
                str1 = str(decodeDict.get(int(i)))
                str2 = str(decodeDict.get(int(i))[0])
                decodeDict[len(decodeDict) + 1] = str1 + str2
                output = output + str1 + str2
            i = j
        codelen = codelen + 1
    return output, decodeDict


def main():
    compressed, enDict, dict = lzwEncode('wabba wabba wabba wabba woo woo woo')
    print(compressed)
    print(dict)
    decompressed, deDict = lzwDecode(compressed, dict)
    print(decompressed)


if __name__ == "__main__":
    main()
