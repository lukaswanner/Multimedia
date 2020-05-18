# Diese Funktion liest eine Textdatei im ASCII-Format
# und berechnet die relative Häufigkeit der einzelnen
# Zeichen.
#
# Input:        fname       :   Dateiname
#
# Output:       probs       :   Vektor mit den relativen Häufigkeiten
#               characters  :   Vektor mit den aufgetretenen Zeichen
#
# nützliche Tools, Collections, Befehle: open, close, read, replace, sort, Counter, numpy, matplotlib
# HINWEIS: Datenstrukturen des Skripts können abgeändert werden
#          (z.B. statt Listen Dictionarys oder Counter Objekte verwenden)


import heapq
import math
from functools import reduce


class node:

    def __init__(self, char, freq):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def __lt__(self, other):
        return self.freq < other.freq

    def __repr__(self):
        return self.char


#def read_text(fname):
#    probs = []
#    characters = []

#    return probs, characters


# Huffmann - Codierung
#
# Input:    probs           :   Auftrittswahrscheinlichkeiten
#
# Output:   code            :   Code Tabelle
#           entropy         :   Entropie
#           meanLength      :   mittlere Codewortlänge
#
# Für den Testvektor
# P = [0.05, 0.03, 0.17, 0.23, 0.01, 0.32, 0.19]
# A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# ergibt sich entrpy = 2.3378 und meanLength = 2.39.

def huffman(probs):
    #########test value########
    #P = [0.05, 0.03, 0.17, 0.23, 0.01, 0.32, 0.19]
    #A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    #probs = dict(zip(A, P))
    #########test value########

    copy_probs = probs.copy()
    code = {}
    entropy = 0
    meanLength = 0
    heap = []

    while len(probs) != 0:
        temp = min(probs.values())
        res = [key for key in probs if probs[key] == temp]

        for items in res:
            new_node = node(items, probs.pop(items))
            heapq.heappush(heap, new_node)

    for keys in heap:
        print(str(keys) + ": " + str(keys.freq))

    print("heap ist: " + str(heap))

    while len(heap) > 1:
        right = heapq.heappop(heap)
        left = heapq.heappop(heap)

        freq = left.freq + right.freq
        fused = node("None", freq)
        fused.setLeft(left)
        fused.setRight(right)

        heapq.heappush(heap, fused)

    recursive_get_code(heap[0], code, "")

    for key in code:
        meanLength += copy_probs[key] * len(code[key])

    for prob in copy_probs.values():
        entropy += prob * -math.log2(prob)

    for key in code:
        print(key + ": " + str(code[key]))

    print("entropy ist: " + str(entropy))
    print("Average wordlength ist: " + str(meanLength))

    return code, entropy, meanLength


def recursive_get_code(root, code, current_code):
    if root == None:
        return

    if (root.char != "None"):
        code[root.char] = current_code
        return

    recursive_get_code(root.left, code, current_code + "0")
    recursive_get_code(root.right, code, current_code + "1")


def main():
    file = open("midsummer.txt", "r")
    txt = file.read()
    dic = {}

    for i in range(32, 127):
        if txt.count(chr(i)) != 0:
            dic[chr(i)] = txt.count(chr(i))

    probability = {}

    for keys in dic:
        probability[keys] = dic.get(keys) / sum(dic.values())

    huffman(probability)


# code, entropy, meanLength = huffman(probs)


if __name__ == '__main__':
    main()
