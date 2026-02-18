import collections

def analyze_to_file(input_filename, output_filename="results.txt"):
    try:
        # 1. Read the input file (UTF-8 for Finnish characters)
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            
            # Filter: only keep letters (a-z, ä, ö, etc.)
            letters = [char for char in content if char.isalpha()]
            
            counts = collections.Counter(letters)
            total_letters = len(letters)
            
            # Sort keys alphabetically: a, b, c... z, ä, ö
            sorted_chars = sorted(counts.keys())

        # 2. Write the data out to a new text file
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(f"--- Statistics for: {input_filename} ---\n")
            out_file.write(f"Total letters found: {total_letters}\n")
            out_file.write("-" * 30 + "\n")
            
            for char in sorted_chars:
                line = f"{char.upper()}: {counts[char]}\n"
                out_file.write(line)
        
        print(f"Success! Analysis of '{input_filename}' saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Execution ---
if __name__ == "__main__":
    file_to_read = input("Enter the input filename (e.g., kalevala.txt): ")
    # This will create 'kalevala_results.txt'
    output_name = file_to_read.replace(".txt", "_results.txt")
    
    analyze_to_file(file_to_read, output_name)