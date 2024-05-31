import re
import zipfile
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from task import Task

class TextAnalyzer:
    """A class for analyzing text files."""
    def __init__(self, filename):
        """Initializes the TextAnalyzer object."""
        self.filename = filename

    def read_text_from_file(self):
        """Reads the content of the text file."""
        with open(self.filename, 'r') as file:
            self.text = file.read()

    def count_sentences(self):
        """Counts the number of sentences in the text."""
        # sentences = re.split(r'[.!?]', self.text)
        return self.text.count('.') + self.text.count('!') + self.text.count('?')

    def count_sentence_types(self):
        """Counts the number of different types of sentences."""
        narrative = len(re.findall(r'[^.!?]+[.]', self.text))
        interrogative = len(re.findall(r'[^.!?]+[?]', self.text))
        imperative = len(re.findall(r'[^.!?]+[!]', self.text))
        return narrative, interrogative, imperative

    def average_sentence_length(self):
        """Calculates the average length of sentences."""
        words_in_sentence = [len(re.findall(r'\b\w+\b', sentence)) for sentence in re.split(r'[.!?]', self.text) if sentence]
        return sum(words_in_sentence) / len(words_in_sentence)

    def average_word_length(self):
        """Calculates the average length of words."""
        words = re.findall(r'\b\w+\b', self.text)
        return sum(len(word) for word in words) / len(words)

    def count_smileys(self):
        """Counts the number of smiley faces in the text."""
        smiley_pattern = re.compile(r'[;:]-*[\(\[\]\)]+')
        smileys = re.findall(smiley_pattern, self.text)
        return len(smileys)

    def find_dates(self):
        """Finds and extracts dates mentioned in the text."""
        date_pattern = re.compile(r'(?:\b|\s)(20\d{2})(?=\b|\s)')
        dates = re.findall(date_pattern, self.text)
        return dates

    def find_words_with_consonant_vowel(self):
        """Finds words with a consonant-vowel pattern."""
        words = re.findall(r'\b\w+\b', self.text)
        consonant_vowel_words = []
        for word in words:
            if len(word) > 2 and word[-3] in 'bcdfghjklmnpqrstvwxyz' and word[-2] in 'aeiou':
                consonant_vowel_words.append(word)
        return consonant_vowel_words

    def count_words(self):
        """Counts the number of words in the text."""
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)

    def find_longest_word_and_position(self):
        """Finds the longest word in the text and its position."""
        words = re.findall(r'\b\w+\b', self.text)
        max_word = max(words, key=len)
        max_index = words.index(max_word) + 1
        return max_word, max_index

    def find_odd_words(self):
        """Finds words at odd positions in the text."""
        words = re.findall(r'\b\w+\b', self.text)
        odd_words = [word for word in words if (words.index(word) + 1) % 2 != 0]
        return odd_words

    def save_results(self, filename):
        """Saves analysis results to a text file."""
        with open(filename, 'w') as f:
            f.write(f"Number of sentences: {self.count_sentences()}\n")
            narrative, interrogative, imperative = self.count_sentence_types()
            f.write(f"Number of narrative sentences: {narrative}\n")
            f.write(f"Number of interrogative sentences: {interrogative}\n")
            f.write(f"Number of imperative sentences: {imperative}\n")
            f.write(f"Average sentence length: {self.average_sentence_length()}\n")
            f.write(f"Average word length: {self.average_word_length()}\n")
            f.write(f"Number of smileys: {self.count_smileys()}\n")
            f.write(f"List of dates: {self.find_dates()}\n")
            f.write(f"Words with consonant-vowel pattern: {self.find_words_with_consonant_vowel()}\n")
            f.write(f"Number of words: {self.count_words()}\n")
            longest_word, position = self.find_longest_word_and_position()
            f.write(f"Longest word: {longest_word}, Position: {position}\n")
            f.write(f"Odd words: {self.find_odd_words()}\n")

    def archive_results(self, filename):
        """Archives the results file into a ZIP archive."""
        with zipfile.ZipFile(filename, 'w') as z:
            z.write("task2/results.txt")

    def print_results(self):
        """Prints the analysis results to the console."""
        # \033[37m\033[1m \033[37m\033[4m \033[37m\033[0m\033[1m
        print("\033[37m\033[1m--------------------------------\033[00m")
        print("\033[37m\033[1mThe result of the text analysis:")
        print("--------------------------------\033[00m")
        print(f"Number of sentences: {self.count_sentences()}")
        narrative, interrogative, imperative = self.count_sentence_types()
        print(f"Number of narrative sentences: {narrative}")
        print(f"Number of interrogative sentences: {interrogative}")
        print(f"Number of imperative sentences: {imperative}")
        print(f"Average sentence length: {self.average_sentence_length()}")
        print(f"Average word length: {self.average_word_length()}")
        print(f"Number of smileys: {self.count_smileys()}")
        print("\033[37m\033[1m--------------------------------\033[00m")
        print("\033[37m\033[1mAdditional text analysis result:")
        print("--------------------------------\033[00m")
        print(f"List of dates: {self.find_dates()}")
        print(f"Words with consonant-vowel pattern: {self.find_words_with_consonant_vowel()}")
        print(f"Number of words: {self.count_words()}")
        longest_word, position = self.find_longest_word_and_position()
        print(f"Longest word: {longest_word}, Position: {position}")
        print(f"Odd words: {self.find_odd_words()}")
        print("\033[37m\033[1m--------------------------------\033[00m")


class Task2(Task):
    """
    A class representing Task 2.
    Inherits from Task class.
    """
    @staticmethod
    def complete_task():
        """
        Completes Task 2 by analyzing text data, printing results, saving results to a file,
        and archiving the results file.
        """
        filename = "task2/input.txt"

        analyzer = TextAnalyzer(filename)
        analyzer.read_text_from_file()
        analyzer.print_results()
        analyzer.save_results("task2/results.txt")
        analyzer.archive_results("task2/results.zip")

# Task2.complete_task()
