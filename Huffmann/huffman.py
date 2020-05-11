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
    fname = 'midsummer.txt'
    probs, characters = read_text(fname)


    code, entropy, meanLength = huffman(probs)


if __name__ == '__main__':
    main()
