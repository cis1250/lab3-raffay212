import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False
    # Check for starting with a capital letter
    if not text[0].isupper():
        return False
    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False
    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False
    return True

# 1. Prompt the user
user_sentence = input("Enter a sentence: ")
while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# 2. Split the sentence into words
user_sentence = user_sentence.lower()
words = user_sentence.split()

# 3. Create lists
word_list = []
frequency_list = []

# 4. Iterate through words and update frequencies
for word in words:
    # Remove punctuation from word
    clean_word = ""
    for letter in word:
        if letter.isalpha():
            clean_word = clean_word + letter
    
    # Check if word already exists
    if clean_word in word_list:
        position = word_list.index(clean_word)
        frequency_list[position] = frequency_list[position] + 1
    else:
        word_list.append(clean_word)
        frequency_list.append(1)

# 5. Print results
for i in range(len(word_list)):
    print(word_list[i] + ": " + str(frequency_list[i]))

