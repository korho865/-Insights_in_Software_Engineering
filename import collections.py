import collections

def analyze_with_normalization(input_filename, output_filename="results.txt"):
    try:
        # 1. Read and Process the text
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            
            # Filter letters including ä, ö, å
            letters = [char for char in content if char.isalpha()]
            
            counts = collections.Counter(letters)
            total_letters = len(letters)
            
            # Sort keys: a...z, then others like ä, ö
            sorted_chars = sorted(counts.keys())

        # 2. Write the detailed results and normalization
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(f"--- Deeper Analysis: {input_filename} ---\n")
            out_file.write(f"Total letters (N): {total_letters}\n\n")
            
            # Header for our table
            out_file.write(f"{'Letter':<10} | {'Count':<10} | {'Weight (w)':<10}\n")
            out_file.write("-" * 35 + "\n")
            
            for char in sorted_chars:
                count = counts[char]
                # Calculate weight (Normalization step)
                weight = count / total_letters
                
                # Format to 4 decimal places for precision
                line = f"{char.upper():<10} | {count:<10} | {weight:.4f}\n"
                out_file.write(line)
            
            out_file.write("-" * 35 + "\n")
            out_file.write("Note: Sum of weights will equal 1.0\n")
        
        print(f"Analysis complete! Results saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_to_read = input("Enter the input filename: ")
    output_name = file_to_read.replace(".txt", "_normalized.txt")
    analyze_with_normalization(file_to_read, output_name)