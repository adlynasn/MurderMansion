
# Method 1 ✅
# need to test time complexity

# File1 = open("file1.txt","r")
# File2 = open("file2.txt","r")

# Dic1 = File1.read().split()
# Dic2 = File2.read().split()

# print(Dic1)
# print(Dic2)

# DF = [ x for x in Dic1 if x not in Dic2 ]
# DF2 = [ x for x in Dic2 if x not in Dic1 ]

# print("Different words:")
# print(DF)
# print(DF2)

#Method 2

from difflib import SequenceMatcher

text1 = "This is the first text."
text2 = "This is the second text."

matcher = SequenceMatcher(None, text1, text2)
differences = matcher.get_opcodes()

unique_words_in_text1 = [text1[i:j] for opcode, i, j, _, _ in differences if opcode == 'delete']
unique_words_in_text2 = [text2[i:j] for opcode, _, _, i, j in differences if opcode == 'insert']

print("Unique words in text 1:", unique_words_in_text1)
print("Unique words in text 2:", unique_words_in_text2)

