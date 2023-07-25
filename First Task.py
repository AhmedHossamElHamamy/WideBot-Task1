from bintrees import FastRBTree
import re

class SpellChecker:
    def __init__(self):
        self.dictionary = FastRBTree()

    def store_dictionary(self, words):
        for word in words:
            self.dictionary.insert(word, None)

    def find_nearest_words(self, word):
        # Check if the word exists in the dictionary
        if word in self.dictionary:
            print(f"The word '{word}' is already in the dictionary.")
            return None

        # Find the nearest 2 words before and after the input word (if exist)
        prev_words = []
        next_words = []

        for item in self.dictionary.items():
            if item[0] < word:
                prev_words.append(item[0])
            elif item[0] > word:
                next_words.append(item[0])

        nearest_words = []

        # Get the two words before and after the input word
        num_prev_words = min(2, len(prev_words))
        nearest_words.extend(prev_words[-num_prev_words:])

        num_next_words = min(2, len(next_words))
        nearest_words.extend(next_words[:num_next_words])

        if nearest_words:
            print(f"Nearest words for '{word}': {nearest_words}")
        else:
            print(f"No nearest words found for '{word}'.")

        return nearest_words

    def add_word_to_dictionary(self, word):
        if word in self.dictionary:
            print(f"The word '{word}' is already in the dictionary.")
        else:
            self.dictionary.insert(word, None)
            print(f"Added word: {word}")

if __name__ == "__main__":
    spell_checker = SpellChecker()

    with open('dictionary.txt', mode='r', encoding='ANSI') as f:
        dictionary = [line.strip() for line in f]
        spell_checker.store_dictionary(dictionary)

    while True:
        print("What do you want to do?")
        print("1. Get a word")
        print("2. Add a word")
        print("3. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            word = input("Enter the word you want to check: ")
            spell_checker.find_nearest_words(word)
        elif choice == "2":
            word = input("Enter the word you want to add: ")
            spell_checker.add_word_to_dictionary(word)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
