import re
import zipfile
import sys
import os
# Получаем путь к текущей директории (где находится task3.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Переходим на уровень выше, чтобы получить доступ к каталогу LR4
parent_dir = os.path.dirname(current_dir)
# Добавляем путь к каталогу LR4 в PYTHONPATH
sys.path.append(parent_dir)
# Теперь мы можем импортировать модуль task
from task import Task

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def read_text_from_file(self):
        with open(self.filename, 'r') as file:
            self.text = file.read()

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.text)
        return len(sentences)
    
    # def count_sentences(self):
        # sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', self.text)
        # return len(sentences)

    def count_sentence_types(self):
        narrative = len(re.findall(r'[^.!?]+[.]+[^.!?]*', self.text))
        interrogative = len(re.findall(r'[?]', self.text))
        imperative = len(re.findall(r'[!]', self.text))
        return narrative, interrogative, imperative

    def average_sentence_length(self):
        words_per_sentence = [len(re.findall(r'\b\w+\b', sentence)) for sentence in re.split(r'[.!?]', self.text) if sentence]
        return sum(words_per_sentence) / len(words_per_sentence)

    def average_word_length(self):
        words = re.findall(r'\b\w+\b', self.text)
        return sum(len(word) for word in words) / len(words)

    def count_smileys(self):
        smiley_pattern = re.compile(r'[;:]-*[\(\[\]\)]+')
        smileys = re.findall(smiley_pattern, self.text)
        return len(smileys)

    def find_dates(self):
        date_pattern = re.compile(r'(?:\b|\s)(20\d{2})(?=\b|\s)')
        dates = re.findall(date_pattern, self.text)
        return dates

    def find_words_with_consonant_vowel(self):
        words = re.findall(r'\b\w+\b', self.text)
        consonant_vowel_words = []
        for word in words:
            if len(word) > 2 and word[-3] in 'bcdfghjklmnpqrstvwxyz' and word[-2] in 'aeiou':
                consonant_vowel_words.append(word)
        return consonant_vowel_words

    def count_words(self):
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)

    def find_longest_word_and_position(self):
        words = re.findall(r'\b\w+\b', self.text)
        max_word = max(words, key=len)
        max_index = words.index(max_word) + 1
        return max_word, max_index

    def find_odd_words(self):
        words = re.findall(r'\b\w+\b', self.text)
        odd_words = [word for word in words if (words.index(word) + 1) % 2 != 0]
        return odd_words

    def save_results(self, filename):
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
        with zipfile.ZipFile(filename, 'w') as z:
            z.write("task2/results.txt")

    def print_results(self):
        print("Results:")
        print(f"Number of sentences: {self.count_sentences()}")
        narrative, interrogative, imperative = self.count_sentence_types()
        print(f"Number of narrative sentences: {narrative}")
        print(f"Number of interrogative sentences: {interrogative}")
        print(f"Number of imperative sentences: {imperative}")
        print(f"Average sentence length: {self.average_sentence_length()}")
        print(f"Average word length: {self.average_word_length()}")
        print(f"Number of smileys: {self.count_smileys()}")
        print(f"List of dates: {self.find_dates()}")
        print(f"Words with consonant-vowel pattern: {self.find_words_with_consonant_vowel()}")
        print(f"Number of words: {self.count_words()}")
        longest_word, position = self.find_longest_word_and_position()
        print(f"Longest word: {longest_word}, Position: {position}")
        print(f"Odd words: {self.find_odd_words()}")

class Task2(Task):
    @staticmethod
    def perform():

        filename = "task2/input.txt"

        analyzer = TextAnalyzer(filename)
        analyzer.read_text_from_file()
        analyzer.print_results()
        analyzer.save_results("task2/results.txt")
        analyzer.archive_results("task2/results.zip")


