from PyQt5.QtWidgets import *
from passwordGenerator import *
import random
import linecache
import math


class Controller(QMainWindow, Ui_GeneratorWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.displayGenerator.setText('')

        self.checkUppercase.clicked.connect(lambda: self.Uppercase())
        self.checkSymbols.clikced.connect(lambda: self.Symbols())

    def words_password(self, words):
        try:
            password_length = int(input('Enter Your Password Length (8-64 characters): '))
            test_password_length = password_length

            if password_length < 8:
                raise SyntaxError
            elif password_length > 64:
                raise SyntaxError

            word1 = ''
            word1_len = 0
            word2 = ''
            word2_len = 0
            word3 = ''
            word3_len = 0
            word4 = ''
            word4_len = 0
            word5 = ''
            word5_len = 0
            length_words = 0

            if (password_length >= 8) and (password_length < 16):
                length_words = math.floor(password_length / 1)
            elif (password_length >= 16) and (password_length < 30):
                length_words = math.floor(password_length / 2)
            elif (password_length >= 30) and (password_length < 41):
                length_words = math.floor(password_length / 3)
            elif (password_length >= 41) and (password_length < 55):
                length_words = math.floor(password_length / 4)
            elif (password_length >= 55) and (password_length <= 64):
                length_words = math.floor(password_length / 5)

            file_length = 370105

            if (password_length >= 8) and (password_length <= 64):
                random_word1 = random.randint(1, file_length)
                word1 = linecache.getline('words_alpha.txt', random_word1)
                word1_len = (len(word1) - 1)
                if (word1_len >= length_words) or (word1_len < (length_words - 2)):
                    while (word1_len >= length_words) or (word1_len <= (length_words - 2)):
                        random_word1 = random.randint(1, file_length)
                        word1 = linecache.getline('words_alpha.txt', random_word1)
                        word1_len = (len(word1) - 1)
                test_password_length -= word1_len

            if (password_length >= 16) and (password_length <= 64):
                random_word2 = random.randint(1, file_length)
                word2 = linecache.getline('words_alpha.txt', random_word2)
                word2_len = (len(word2) - 1)
                if (word2_len > length_words) or (word2_len < (length_words - 2)):
                    while (word2_len >= length_words) or (word2_len <= (length_words - 2)):
                        random_word2 = random.randint(1, file_length)
                        word2 = linecache.getline('words_alpha.txt', random_word2)
                        word2_len = (len(word2) - 1)
                test_password_length -= word2_len

            if (password_length >= 30) and (password_length <= 64):
                random_word3 = random.randint(1, file_length)
                word3 = linecache.getline('words_alpha.txt', random_word3)
                word3_len = (len(word3) - 1)
                if (word3_len > length_words) or (word3_len < (length_words - 2)):
                    while (word3_len >= length_words) or (word3_len <= (length_words - 2)):
                        random_word3 = random.randint(1, file_length)
                        word3 = linecache.getline('words_alpha.txt', random_word3)
                        word3_len = (len(word3) - 1)
                test_password_length -= word3_len

            if (password_length >= 41) and (password_length <= 64):
                random_word4 = random.randint(1, file_length)
                word4 = linecache.getline('words_alpha.txt', random_word4)
                word4_len = (len(word4) - 1)
                if (word4_len > length_words) or (word4_len < (length_words - 2)):
                    while (word4_len >= length_words) or (word4_len <= (length_words - 2)):
                        random_word4 = random.randint(1, file_length)
                        word4 = linecache.getline('words_alpha.txt', random_word4)
                        word4_len = (len(word4) - 1)
                test_password_length -= word4_len

            if (password_length >= 55) and (password_length <= 64):
                random_word5 = random.randint(1, file_length)
                word5 = linecache.getline('words_alpha.txt', random_word5)
                word5_len = (len(word5) - 1)
                if (word5_len > length_words) or (word5_len < (length_words - 2)):
                    while (word5_len >= length_words) or (word5_len <= (length_words - 2)):
                        random_word5 = random.randint(1, file_length)
                        word5 = linecache.getline('words_alpha.txt', random_word5)
                        word5_len = (len(word5) - 1)
                test_password_length -= word5_len

            word_len = word1_len + word2_len + word3_len + word4_len + word5_len
            print(word_len)
            words = word1.strip() + " " + word2.strip() + " " + word3.strip() + " " + word4.strip() + " " + word5.strip()
            print(words)
            return words
        except SyntaxError:
            print("INVALID")
        except RuntimeError:
            print("ERROR")

    def display_password(self):
        pass

    def uppercase(self):
        pass

    def symbols(self):
        pass
