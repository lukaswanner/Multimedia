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


class node:

    def __init__(self, char, prob):
        self.prob = prob
        self.char = char
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def __lt__(self, other):
        return self.prob < other.prob

    def __repr__(self):
        return self.char


def read_text(fname):
    probs = []
    characters = []

    return probs, characters


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
    code = {}
    entropy = 0
    meanLength = 0

    return code, entropy, meanLength


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


    heap = []
    temp = min(dic.values())
    res = [key for key in dic if dic[key] == temp]
    print(res)
    while len(dic) != 0:
        temp = min(dic.values())
        res = [key for key in dic if dic[key] == temp]

        for items in res:
            new_node = node(items, dic.pop(items))
            heapq.heappush(heap, new_node)

    for keys in heap:
        print(str(keys) + ": " + str(keys.prob))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        prob = left.prob+ right.prob
        fused = node("None",prob)
        fused.setLeft(left)
        fused.setRight(right)

        heapq.heappush(heap,fused)




# code, entropy, meanLength = huffman(probs)


if __name__ == '__main__':
    main()
