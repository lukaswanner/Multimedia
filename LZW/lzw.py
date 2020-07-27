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
    inputlist = input.split(" ")
    decodeDict = dict.copy()

    last_code = inputlist[0]
    output = output + decodeDict.get(int(last_code))

    # j = code i = lastcode
    for code in inputlist[1:]:
        if int(code) in decodeDict.keys():
            str1 = str(decodeDict.get(int(last_code)))
            str2 = str(decodeDict.get(int(code))[0])
            decodeDict[len(decodeDict) + 1] = str1 + str2
            output = output + decodeDict.get(int(code))
        else:
            str1 = str(decodeDict.get(int(last_code)))
            str2 = str(decodeDict.get(int(last_code))[0])
            decodeDict[len(decodeDict) + 1] = str1 + str2
            output = output + str1 + str2
        last_code = code

    return output, decodeDict


def main():
    compressed, enDict, dict = lzwEncode('wabba wabba wabba wabba woo woo woo')
    print(compressed)
    print(enDict)
    decompressed, deDict = lzwDecode(compressed, dict)
    print(decompressed)



if __name__ == "__main__":
    main()