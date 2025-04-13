import os
import string
filename = 'encrypted_note.txt'
output_filename = 'results_note.txt'
filepath = os.getcwd()
fullpath = os.path.join(filepath, filename)
output_fullpath = os.path.join(filepath, output_filename)



with open(fullpath, 'r') as file:
    note = file.read()

def clean(content):
    pun = string.punctuation
    text = content.lower()
    for char in pun:
        text = text.replace(char, '')

    return text
        

no_pun = clean(note)
print(no_pun)

def decrypt(no_pun):
    words =  no_pun.split()
    decoded_message= ''
    for word in words:
        if len(word) > 0:
            decoded_message += word[0]

    return decoded_message

message = decrypt(no_pun)
print(message)



    



