import collections
import string

def analyze_file(filename):
    try:
        # Open with utf-8 encoding as specified in the instructions
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            
            # Filter for letters only (a-z)
            # This ignores spaces, punctuation, and digits
            letters = [char for char in content if char in string.ascii_lowercase]
            
            # Count occurrences using Counter
            counts = collections.Counter(letters)
            
            # Calculate total number of letters
            total_letters = sum(counts.values())
            
            # Output Results
            print(f"--- Statistics for: {filename} ---")
            print(f"Total letters (a-z): {total_letters}\n")
            print("Breakdown:")
            
            # Sort by letter to keep it organized A-Z
            for letter in string.ascii_lowercase:
                if counts[letter] > 0:
                    print(f"{letter.upper()}: {counts[letter]}")
                    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
analyze_file('kalevala.txt')
# analyze_file('romeo_and_juliet.txt')