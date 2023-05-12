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
        self.generateButton.clicked.connect(lambda: self.password())
        self.checkUppercase.clicked.connect(lambda: self.uppercase())
        self.checkSymbols.clicked.connect(lambda: self.symbols())

    def password(self):
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
            num_words = 0

            if (password_length >= 8) and (password_length < 16):
                length_words = math.floor(password_length / 1)
                num_words =  1
            elif (password_length >= 16) and (password_length < 30):
                length_words = math.floor(password_length / 2)
                num_words = 2
            elif (password_length >= 30) and (password_length < 41):
                length_words = math.floor(password_length / 3)
                num_words = 3
            elif (password_length >= 41) and (password_length < 55):
                length_words = math.floor(password_length / 4)
                num_words = 4
            elif (password_length >= 55) and (password_length <= 64):
                length_words = math.floor(password_length / 5)
                num_words = 5

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
                words.append(word2.strip('\n'))

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
                words.append(word3.strip('\n'))

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
                words.append(word4.strip('\n'))

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
                words.append(word5.strip('\n'))

            word_len = word1_len + word2_len + word3_len + word4_len + word5_len

            remaining = int(password_length) - int(word_len)
            numbers = []
            symbols = ['(', ')', '!', '?', '%', '$', '@', '#', '&', '*']

            num = 0
            while num <= remaining:
                rand = random.randint(0, 9)
                numbers.append(rand)
                num += 1

            display = ''
            num = 0
            if remaining >= len(words):
                while num < len(numbers):
                    if num < len(words):
                        display += f'{words[num]}'
                    display += f'{numbers[num]}'
                    num += 1

            if 'o' in display:
                display = display.replace('o', '0', num_words)
            if 'g' in display:
                display = display.replace('g', '9', num_words)
            if 'l' in display:
                display = display.replace('l', '1', num_words)
            if 'e' in display:
                display = display.replace('e', '3', num_words)

            times = 0
            if self.uppercase() == True:
                while times < 1:
                    if 'a' in display:
                        display = display.replace('a', 'A', 1)
                        times += 1
                    if 'b' in display:
                        display = display.replace('b', 'B', 1)
                        times += 1
                    if 'c' in display:
                        display = display.replace('c', 'C', 1)
                        times += 1
                    if 'd' in display:
                        display = display.replace('d', 'D', 1)
                        times += 1
                    if 'e' in display:
                        display = display.replace('e', 'E', 1)
                        times += 1
                    if 'f' in display:
                        display = display.replace('f', 'F', 1)
                        times += 1
                    if 'g' in display:
                        display = display.replace('g', 'G', 1)
                        times += 1
                    if 'h' in display:
                        display = display.replace('h', 'H', 1)
                        times += 1
                    if 'i' in display:
                        display = display.replace('i', 'I', 1)
                        times += 1
                    if 'j' in display:
                        display = display.replace('j', 'J', 1)
                        times += 1
                    if 'k' in display:
                        display = display.replace('k', 'K', 1)
                        times += 1
                    if 'l' in display:
                        display = display.replace('l', 'L', 1)
                        times += 1
                    if 'm' in display:
                        display = display.replace('m', 'M', 1)
                        times += 1
                    if 'n' in display:
                        display = display.replace('n', 'N', 1)
                        times += 1
                    if 'o' in display:
                        display = display.replace('o', 'O', 1)
                        times += 1
                    if 'p' in display:
                        display = display.replace('p', 'P', 1)
                        times += 1
                    if 'q' in display:
                        display = display.replace('q', 'Q', 1)
                        times += 1
                    if 'r' in display:
                        display = display.replace('r', 'R', 1)
                        times += 1
                    if 's' in display:
                        display = display.replace('s', 'S', 1)
                        times += 1
                    if 't' in display:
                        display = display.replace('t', 'T', 1)
                        times += 1
                    if 'u' in display:
                        display = display.replace('u', 'U', 1)
                        times += 1
                    if 'v' in display:
                        display = display.replace('v', 'V', 1)
                        times += 1
                    if 'w' in display:
                        display = display.replace('w', 'W', 1)
                        times += 1
                    if 'x' in display:
                        display = display.replace('x', 'X', 1)
                        times += 1
                    if 'y' in display:
                        display = display.replace('y', 'Y', 1)
                        times += 1
                    if 'z' in display:
                        display = display.replace('z', 'Z', 1)
                        times += 1

            if self.symbols() == True:
                if 'i' in display:
                    display = display.replace('i', '!', num_words)
                if 's' in display:
                    display = display.replace('s', '$', num_words)
                if 'S' in display:
                    display = display.replace('S', '$', num_words)
                if 'a' in display:
                    display = display.replace('a', '@', num_words)
                if 'A' in display:
                    display = display.replace('A', '@', num_words)
                if 't' in display:
                    display = display.replace('t', '+', num_words)
                if 'x' in display:
                    display = display.replace('x', '*', num_words)

            self.displayGenerator.setText(display)

        except SyntaxError:
            self.displayGenerator.setText('INVALID')

    def change_scroll(self):
        self.labelLength.setText(str(self.lengthScrollBar.value()))

    def uppercase(self):
        if self.checkUppercase.isChecked():
            return True
        else:
            return False

    def symbols(self):
        if self.checkSymbols.isChecked():
            return True
        else:
            return False
