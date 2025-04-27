# Task 1: Pre-Analysis Task C
# my code
# def encrypt_one_char(char: str) -> str:
#     num = ord(char)
#     num2 = num + 5
#     if num2 > 126:
#         num2= num2 % 95
#         char2 = chr(num2)
#         return char2
#     else:
#         char2 = chr(num2)
#         return char2

# print(encrypt_one_char('a'))

# Teachers code
ascii_start = 32
ascii_end = 126
range_size = ascii_end - ascii_start +1
def conversion(char, key, mode):
    range_size = ascii_end - ascii_start +1

    if ascii_start <= ord(char) <= ascii_end:
        char_code = ord(char)
        if mode == 'encrypt':
            shifted_code = char_code - ascii_start + key
        elif mode == 'decrypt':
            shifted_code = char_code - ascii_start - key
        else:
            raise ValueError ('Invalid mode!!!')
        wrapped_code = shifted_code % range_size
        final_code = wrapped_code + ascii_start
        char_end = chr(final_code)
        return char_end
    else:
        return char

# print(char_end)

# sentence
def sentence_conversion(sentence, key, mode):
    shifted_sentence = ""
    for char in sentence:
        shifted_sentence += conversion(char, key, mode)

    return shifted_sentence

def caesar_shift_list(sentences: list, key: int, mode: str):
    shifted_sentences = []
    for sentence in sentences:
        new_sentence = sentence_conversion(sentence, key, mode)
        shifted_sentences.append(new_sentence)

    return shifted_sentences    

print(caesar_shift_list(['Hello', 'World'], 5, 'encrypt'))
import os
current_file = os.getcwd()
input_filename = 'caesar.txt'
fullpath = os.path.join(current_file, input_filename)
outfile = 'caesar_results.txt'
outpath = os.path.join(current_file, outfile)
def caesar_shift_file(input_filename, output_filename, key, mode):
    print(input_filename)
    with open(input_filename, 'r') as infile:
        with open(output_filename, 'w') as outfile:
            for line in infile:
                shifted_line = sentence_conversion(line, key, mode)
                outfile.write(shifted_line)

caesar_shift_file("caesar.txt", "caesar2.txt", 5, 'encrypt')
        

filrname = 'hackmeifyoucan.txt'
fullpath2 = os.path.join(os.getcwd(), filrname)
# print(fullpath)
def brute_force_decrypt(filenamewf):
    key = 1
    with open(fullpath2, 'r') as file:
        content = file.readlines()
    for key in range(range_size):
        print(f'key : {key}')
        for line in content[:3]:
            decrypted_line = sentence_conversion(line.strip(), key, 'decrypt')
            print(f'key # {key}: {decrypted_line}')
    return

brute_force_decrypt(fullpath2)

while True:
    print('\nCaesar Cipher Menu: ')
    print('1. Encrypt a Single Sentence ')
    print('2. Decrypt a Single Sentence ')
    print('3. Encrypt a list of Sentences')
    print('4. Decrypt a list of Sentences')
    print('5. Encrypt a file')
    print('6. Decrypt a file')
    print('7. Brute Force Decrypt')

    choice = int(input('What do you choose? '))
    if choice in [1, 2]:
        sentence = input('Enter a sentence: ')
        key = int(input('Enter a number: '))

        if choice == 1:
            mode = 'Encrypt'
        else:
            mode = 'Decrypt'

        result = sentence_conversion(sentence, key, mode)
        print(result)

    elif choice in [3, 4]:
        num_sentences = int(input('How many? '))
        sentences = []

        for i in range(num_sentences):
            sentence = input(f'Enter sentence {i+1} ')
            sentences.append(sentence)

        key = int(input(' Number '))
        if choice == 3:
            mode = 'Encrypt'
        else:
            mode = 'Decrypt'

        print(caesar_shift_list(sentences, key, mode))

    elif choice in [5, 6]:
        input_filename = input('What is your filename: ')
        output_filename = input('What is your outfile? ')

        key = int(input('What key '))
        if choice == 5:
            mode == 'Encrypt'
        elif choice == 6:
            mode == 'Decrypt'
        print(caesar_shift_file(input_filename, output_filename, key, mode))
    
    elif choice == 7:
        filename = input('What is your file? ')
        brute_force_decrypt(filename)