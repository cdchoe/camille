# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(paragraph):
    vowel_count = 0
    consonant_count = 0
    i = 0
    for character in paragraph:
        character = paragraph[i]
        if character.isalpha():
            if character in "AEIOUaeiou":
                vowel_count += 1
            else:
                consonant_count += 1
        i += 1
    return (vowel_count, consonant_count)


# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    replacement = paragraph.replace("! ",". ").replace("?",".")
    sentences = replacement.split(".")
    sentence_count = len(sentences) - 1

    vowels_per_sentence = []
    consonants_per_sentence = []
    
    for sentence in sentences:    
        vowels, consonants = counting_vowels_and_consonants(sentence)
        vowels_per_sentence.append(vowels)
        consonants_per_sentence.append(vowels)

    return (sentence_count, sum(vowels_per_sentence) / sentence_count, sum(consonants_per_sentence) / sentence_count)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)


# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

result = average_vowels_and_consonants(paragraph)
print(f"The average vowels per sentence of the paragraph is {result[1]}")
print(f"The average number of consonants per sentence of the paragraph is {result[2]}")