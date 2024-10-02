#Made by Bitraven (aka Krovex, Bitravens)

import json
import string

with open('words_dictionary.json', 'r') as file:
    # Load the JSON content into a dictionary
    wordlist = json.load(file)

class ScrabbleCipher:
    def __init__(self, keyword):
        self.alpha = string.ascii_uppercase
        self.keyword = keyword.upper()
        self.initialAlpha()

    def initialAlpha(self):
        for i in self.keyword:
            self.shuffle(i)
        self.initial = self.alpha


    def shuffle(self, letter):
        try:
            tg = self.alpha.index(letter)
        except Exception as e:
            print(letter)
        self.alpha = self.alpha[tg+1:] + letter + self.alpha[:tg]


    def encrypt(self, plaintext):
        self.alpha = self.initial
        plaintext = plaintext.upper()
        ciphertext = ''
        for i in plaintext:
            pos = string.ascii_uppercase.index(i)
            ciphertext += self.alpha[pos]
            self.shuffle(i)
        return ciphertext

    def decrypt(self, ciphertext):
        self.alpha = self.initial
        plaintext = ''
        for i in ciphertext:
            pos = self.alpha.index(i)
            corLet = string.ascii_uppercase[pos]
            plaintext += corLet
            self.shuffle(corLet)
        return plaintext

cipher="TQSBAODTTABMRUHDKNVUORAKATOZLFBFDWPHQLANSZIKOSEDESXZLDYEUBJRROAVZRBSLWESCEGGOCEMLFMAHAYSRNMCXATHGNZQBCLSCEMKIVELCRXCJTBBTXGBRNDQTLJMLUOEQWTHWVBAZHAABXPZELKBNWSNCZLNSBELFFKDLVFWOWNDQWMLFXEQWAQOQRIAAVSXAADYEUUAMTHYLSCVILMNE"

def possible_words(enc):
    for key in wordlist.keys():
        class_key=ScrabbleCipher(key)
        if "FLAGHYPHEN" in class_key.decrypt(enc):
            return class_key.decrypt(enc)            

flag=possible_words(cipher)
flag = flag[flag.find("FLAG"):].replace("HYPHEN", "-") \
    .replace("ONE", "1") \
    .replace("TWO", "2") \
    .replace("THREE", "3") \
    .replace("FOUR", "4") \
    .replace("FIVE", "5") \
    .replace("SIX", "6") \
    .replace("SEVEN", "7") \
    .replace("EIGHT", "8") \
    .replace("NINE", "9") \
    .replace("ZERO", "0")


print(flag)

