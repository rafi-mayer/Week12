import string
import random


alphabet = string.ascii_lowercase
AlphabetList = list(alphabet)
random.shuffle(AlphabetList)
print(''.join(AlphabetList[1:13]))