from decorator import funcInfoDec

@funcInfoDec
def count_words_in_quotes(text):
    """Function to count the number of words enclosed in quotation marks ("") in a given text"""
    count = 0
    inside_quotes = False
    for char in text:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == ' ' and inside_quotes:
            count += 1
    return count

def count_letter_occurrences(text):
    """Function to count the occurrences of each letter in a given text"""
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def extract_phrases_separated_by_commas(text):
    """Function to extract phrases separated by commas from a given text and sort them alphabetically"""
    phrases = [phrase.strip() for phrase in text.split(',') if phrase.strip()]
    phrases.sort()
    return phrases

def task4():
    input_text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

    # a) Determine the number of words enclosed in quotation marks ("")
    quote_count = count_words_in_quotes(input_text)
    print("The number of words enclosed in quotation marks:", quote_count)

    # b) Determine how many times each letter is repeated
    letter_occurrences = count_letter_occurrences(input_text)
    print("Repetition of each letter:")
    for letter, count in sorted(letter_occurrences.items()):
        print(f"{letter}: {count}")

    # c) Display all phrases separated by commas in alphabetical order
    phrases = extract_phrases_separated_by_commas(input_text)
    print("Phrases separated by commas (in alphabetical order):")
    for phrase in phrases:
        print(phrase)

