from itertools import permutations

# Function to check if a word exists in a given word list
def is_word(word, word_list):
    return word in word_list

# Function to find valid words from a list of jumbled letters
def find_valid_words(letters, word_list):
    valid_words = []
    # Generate all permutations of the letters
    permutations_list = [''.join(perm) for perm in permutations(letters)]
    # Check each permutation if it is a valid word
    for word in permutations_list:
        if is_word(word, word_list):
            valid_words.append(word)
    return valid_words

# Function to solve the jumbled word problem and retrieve the secret message
def solve_secret_message(jumbled_words, word_list):
    secret_message = []
    for line in jumbled_words:
        valid_words = find_valid_words(line, word_list)
        # Assuming only one valid word per line
        if len(valid_words) == 1:
            secret_message.append(valid_words[0])
        else:
            secret_message.append('')  # Empty string if no valid word found
    return ' '.join(secret_message)

# Example usage
jumbled_words = ['haTt', 'enPros', 'asH', 'eMvito']
word_list_file = 'word_list.txt'

# Read the word list from the text file and store in a list
with open(word_list_file, 'r') as file:
    word_list = [line.strip() for line in file]

# Call the function to solve the problem and retrieve the secret message
secret_message = solve_secret_message(jumbled_words, word_list)
print("Secret Message:", secret_message)
