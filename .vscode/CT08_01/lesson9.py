import os
filename = 'sherlock.txt'
output_filename = 'results.txt'
filepath = os.getcwd()
fullpath = os.path.join(filepath, filename)
output_fullpath = os.path.join(filepath, output_filename)

with open(fullpath, 'r') as file:
    content = file.readlines()


def char_count(content):
    results = 0
    for line in content:
        results += len(line)
    return results



char = char_count(content)
print(char)



def count_vowels(content):
    vowels = 0
    vowel = 'aeiou'
    for line in content:
        for char in line.lower():
            if char in vowel:
                vowels += 1
    return vowels

vowels = count_vowels(content)
print(vowels)    

def freq(content: list[str]) -> dict:
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0,'u': 0 }
    vowel = count_vowels(content)
    for line in content:
        for char in line:
            if char.lower() in vowel_count:
                vowel_count[char.lower()] +=1
    return vowel_count

vowel = freq(content)
print(vowel)

def calculate_percentage(content: list[str]) -> float:
    vowels = count_vowels(content)
    char = char_count(content)
    if char > 0:
        percent = vowels/char * 100
    else:
        percent = 0
    percent = round(percent, 2)
    return percent

percent = calculate_percentage(content)
print(percent)

with open(output_fullpath, 'w') as file:
    file.write(f'Sherlock Holmes Text Analysis')
    file.write('-----------------------------')
    file.write(f'\nTotal Characters: {char}')
    file.write(f'\nTotal Vowels: {vowels}')
    file.write(f'\nVowel frequency:\n')
    for vowel, count in vowel.items():
        file.write(f'\n{vowel} = {count}')
    file.write(f'\nPercentage of vowels: {percent:.2f}%\n')