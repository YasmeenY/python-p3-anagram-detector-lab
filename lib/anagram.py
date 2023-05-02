class Anagram:
    def __init__(self, word):
        self.word = word
        self.letters = sorted([letter for letter in word])
    def match(self, words):
        self.words = words
        matching = list()
        for wording in words:
            if sorted([letter for letter in wording]) == self.letters:
                matching.append(wording)
        return matching
