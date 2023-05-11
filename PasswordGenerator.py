
import random
import linecache

def main():
    try:
        password_length = int(input('Enter Your Password Length (8-64 characters)... pls?'))
        password_length = int(password_length)

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
        length_words = 0

        if (password_length >= 8) and (password_length < 16):
            length_words = password_length / 1
        elif (password_length >= 16) and (password_length < 32):
            length_words = password_length / 2
        elif (password_length >= 8) and (password_length < 16):
            length_words = password_length / 3
        elif (password_length >= 8) and (password_length < 16):
            length_words = password_length / 4

        file_length = 370105
        if (password_length >= 8) and (password_length <= 64):

            random_word1 = random.randint(1, file_length)
            word1 = linecache.getline('words_alpha.txt', random_word1)
            word1_len = (len(word1) - 1)
            if (word1_len > password_length) and (word1_len < (length_words - 2)):
                while (word1_len > password_length) and (word1_len < (length_words - 2)):
                    random_word1 = random.randint(1, file_length)
                    word1 = linecache.getline('words_alpha.txt', random_word1)
                    word1_len = (len(word1) - 1)

        if (password_length > 16) and (password_length <= 64):

            random_word2 = random.randint(1, file_length)
            word2 = linecache.getline('words_alpha.txt', random_word2)
            word2_len = (len(word2) - 1)
            if word2_len > password_length:
                while (word2_len > password_length) and (word2_len < (length_words - 2)):
                    random_word2 = random.randint(1, file_length)
                    word2 = linecache.getline('words_alpha.txt', random_word2)
                    word2_len = (len(word2) - 1)

        if (password_length > 32) and (password_length <= 64):

            random_word3 = random.randint(1, file_length)
            word3 = linecache.getline('words_alpha.txt', random_word3)
            word3_len = (len(word3) - 1)
            if word3_len > password_length:
                while (word3_len > password_length) and (word2_len < (length_words - 2)):
                    random_word3 = random.randint(1, file_length)
                    word3 = linecache.getline('words_alpha.txt', random_word3)
                    word3_len = (len(word3) - 1)

        if (password_length > 48) and (password_length <= 64):

            random_word4 = random.randint(1, file_length)
            word4 = linecache.getline('words_alpha.txt', random_word4)
            word4_len = (len(word4) - 1)
            if word4_len > password_length:
                while (word4_len > password_length) and (word1_len < (length_words - 2)):
                    random_word4 = random.randint(1, file_length)
                    word4 = linecache.getline('words_alpha.txt', random_word4)
                    word4_len = (len(word4) - 1)

        word_len = word1_len + word2_len + word3_len + word4_len
        print(word_len)
        print(word1,word2,word3,word4)

    except SyntaxError:
        print("INVALID")

if __name__ == '__main__':
    main()