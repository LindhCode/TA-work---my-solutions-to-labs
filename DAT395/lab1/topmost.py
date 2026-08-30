import wordfreq, sys, urllib.request
from wordfreq import tokenize, countWords, printTopMost

def main():
    # Stop words from sys.argv[1]
    stopWords = []
    inp_file = open(sys.argv[1], encoding="utf-8")
    for i in inp_file:
        stopWords.append(i.strip())
    inp_file.close()

    # Text file
    if sys.argv[2].startswith("http://" or "https//"):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
    else:
        response = open(sys.argv[2], encoding="utf-8")
        lines = response
        response.close()

    # The amount to display
    count = sys.argv[3]

    # Using all predefined functions from wordfreq
    printTopMost(countWords(tokenize(lines),stopWords), int(count))


main()