def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask user for the file name
filename = input("Enter the file name (with .txt extension): ")
count_words_in_file(filename)
