# Yet another random comment
from num2words import num2words
import string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def count_vowels(text: str) -> int:
    text = text.lower()
    return text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

def clean_text(text: str) -> str:
    text = text.lower()
    return   ''.join((''.join(char for char in text if char not in string.punctuation)).split())

def fraction_to_words(num: int, den: int) -> str:
    plural_s = 's' if (num > 1) else ''
    num = num2words(num)
    den = num2words(den, to = 'ordinal')

    text = f'{num} {den}{plural_s}'

    return text

def words_to_fraction(text: str) -> str:
    text = clean_text(text)
    vowels = count_vowels(text)
    fraction = f'{str(vowels)}/{str(len(text))}' 
    
    return fraction

def fraction_to_word_fraction(fraction: str) -> str:
    nums = int(fraction.split('/'))
    words = fraction_to_words(nums[0], nums[1])
    new_fract = words_to_fraction(words)
    return new_fract


if __name__ == '__main__':
    v = count_vowels('I have two lots of a')
    # print(v)
    t = words_to_fraction('Fred wz ; here')
    w = fraction_to_words(3, 10)
    # print(w)
    w = fraction_to_words(1, 10)
    # print(w)

    f = fraction_to_word_fraction('1/10')
    print(f)
    f = fraction_to_word_fraction('3/10')
    print(f)
    

