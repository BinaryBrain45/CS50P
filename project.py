import time
import random
from faker import Faker
import re

fake = Faker()

def generate_random_sentence():

    return fake.sentence()

def calculate_words_per_minute(start_time, end_time, typed_text):

    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60.0
    word_count = len(typed_text.split())
    wpm = word_count / minutes
    return wpm

def calculate_accuracy(original_sentence, typed_text):

    original_words = re.findall(r'\w+', original_sentence)
    typed_words = re.findall(r'\w+', typed_text)
    correct_count = sum(1 for w1, w2 in zip(original_words, typed_words) if w1.lower() == w2.lower())
    accuracy = (correct_count / len(original_words)) * 100
    return accuracy

def run_speed_typing_test():
    """Runs the speed typing test."""
    print("Welcome to the Speed Typing Test!")
    print("You will be given random sentences to type. Ready to start?")
    input("Press Enter to begin...")
    print("")

    # Generate random sentences for the test
    sentences = [generate_random_sentence() for _ in range(5)]

    total_wpm = 0
    total_accuracy = 0

    for sentence in sentences:
        print("Type the following sentence:")
        print(sentence)
        print("")

        start_time = time.time()
        typed_text = input("> ")
        end_time = time.time()

        wpm = calculate_words_per_minute(start_time, end_time, typed_text)
        total_wpm += wpm

        accuracy = calculate_accuracy(sentence, typed_text)
        total_accuracy += accuracy

        print("")
        print(f"Your typing speed for this sentence: {wpm:.2f} words per minute")
        print(f"Accuracy: {accuracy:.2f}%")
        print("")

    average_wpm = total_wpm / len(sentences)
    average_accuracy = total_accuracy / len(sentences)

    print(f"Average typing speed: {average_wpm:.2f} words per minute")
    print(f"Average accuracy: {average_accuracy:.2f}%")

def main():
    run_speed_typing_test()

if __name__ == "__main__":
    main()