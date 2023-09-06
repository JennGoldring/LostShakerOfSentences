import random

def pick_random_sentences(filename, num_sentences=3):
    with open(filename, 'r') as file:
        # Read the file content and split by line breaks
        lines = file.readlines()

        # Filter out any empty lines or lines that are just whitespace
        lines = [line.strip() for line in lines if line.strip()]

    # Randomly sample sentences
    selected_sentences = random.sample(lines, num_sentences)

    return selected_sentences


filename = "Margaritaville.txt"

# Initial prompt to start the script
input("Time to make a sentence margarita? Press Enter to continue...")

# Use a loop to continuously run the script until the user decides to stop
while True:
    sentences = pick_random_sentences(filename)
    for sentence in sentences:
        print(sentence)

    # Ask the user if they want to run again
    run_again = input("Do you want another round of sentence margarita? (yes/no): ").lower().strip()

    if run_again not in ["yes", "y"]:
        print("Cheers! Until next time.")
        break

