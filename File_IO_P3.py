def count_words_in_file(filename: str) -> int:
    with open(filename, 'r') as file: # Open the file in read mode
        word_count = 0  # Initialize word count to zero
        in_word = False  # Flag to track 
        for line in file:
            for c in line: # Iterate through each character in the line
                if c.isspace():  
                    in_word = False  
                else:
                    if not in_word:  # Check if not already in a word
                        word_count += 1  
                        in_word = True

        return word_count  # Return the total number of words found in the file


filename = "sample.txt" 
num_words = count_words_in_file(filename)    
if num_words >= 0:
    print(f"Number of words in file '{filename}': {num_words}")
else:
    print(f"Error counting'{filename}'")
