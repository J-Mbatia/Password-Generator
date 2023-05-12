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

        self.lengthScrollBar.sliderMoved.connect(lambda: self.change_scroll())
        self.generateButton.clicked.connect(lambda: self.words_password())
        self.checkUppercase.clicked.connect(lambda: self.uppercase())
        self.checkSymbols.clicked.connect(lambda: self.symbols())

    def words_password(self):
        try:
            password_length = int(str(self.lengthScrollBar.value()))
            extra_password_length = password_length

            if password_length < 8:
                raise SyntaxError
            elif password_length > 64:
                raise SyntaxError

            words = []
            word1_len = 0
            word2_len = 0
            word3_len = 0
            word4_len = 0
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
                extra_password_length -= word1_len
                words.append(word1.strip('\n'))

            if (password_length >= 16) and (password_length <= 64):
                random_word2 = random.randint(1, file_length)
                word2 = linecache.getline('words_alpha.txt', random_word2)
                word2_len = (len(word2) - 1)
                if (word2_len > length_words) or (word2_len < (length_words - 2)):
                    while (word2_len >= length_words) or (word2_len <= (length_words - 2)):
                        random_word2 = random.randint(1, file_length)
                        word2 = linecache.getline('words_alpha.txt', random_word2)
                        word2_len = (len(word2) - 1)
                extra_password_length -= word2_len
                words.append(word1.strip('\n'))

            if (password_length >= 30) and (password_length <= 64):
                random_word3 = random.randint(1, file_length)
                word3 = linecache.getline('words_alpha.txt', random_word3)
                word3_len = (len(word3) - 1)
                if (word3_len > length_words) or (word3_len < (length_words - 2)):
                    while (word3_len >= length_words) or (word3_len <= (length_words - 2)):
                        random_word3 = random.randint(1, file_length)
                        word3 = linecache.getline('words_alpha.txt', random_word3)
                        word3_len = (len(word3) - 1)
                extra_password_length -= word3_len
                words.append(word1.strip('\n'))

            if (password_length >= 41) and (password_length <= 64):
                random_word4 = random.randint(1, file_length)
                word4 = linecache.getline('words_alpha.txt', random_word4)
                word4_len = (len(word4) - 1)
                if (word4_len > length_words) or (word4_len < (length_words - 2)):
                    while (word4_len >= length_words) or (word4_len <= (length_words - 2)):
                        random_word4 = random.randint(1, file_length)
                        word4 = linecache.getline('words_alpha.txt', random_word4)
                        word4_len = (len(word4) - 1)
                extra_password_length -= word4_len
                words.append(word1.strip('\n'))

            if (password_length >= 55) and (password_length <= 64):
                random_word5 = random.randint(1, file_length)
                word5 = linecache.getline('words_alpha.txt', random_word5)
                word5_len = (len(word5) - 1)
                if (word5_len > length_words) or (word5_len < (length_words - 2)):
                    while (word5_len >= length_words) or (word5_len <= (length_words - 2)):
                        random_word5 = random.randint(1, file_length)
                        word5 = linecache.getline('words_alpha.txt', random_word5)
                        word5_len = (len(word5) - 1)
                extra_password_length -= word5_len
                words.append(word1.strip('\n'))

            word_len = word1_len + word2_len + word3_len + word4_len + word5_len


        except SyntaxError:
            self.displayGenerator.setText('INVALID')

    def change_scroll(self):
        self.labelLength.setText(str(self.lengthScrollBar.value()))

    def display_password(self):
        pass

    def uppercase(self):
        pass

    def symbols(self):
        pass
