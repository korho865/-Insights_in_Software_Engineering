import collections

def get_weights(filename):
    """Calculates letter weights (wi or yi) for a given file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            # Keeps only letters, including Finnish ä and ö.
            letters = [char for char in content if char.isalpha()]
            if not letters:
                return None
            counts = collections.Counter(letters)
            total = len(letters)
            # w = count / N
            return {char: count / total for char, count in counts.items()}
    except FileNotFoundError:
        print(f"Warning: {filename} not found.")
        return None

def run_ml_analysis(test_files, training_files, output_filename="ml_results.txt"):
    # 1. LEARNING PHASE
    learning_data = {}
    for lang, fname in training_files.items():
        weights = get_weights(fname)
        if weights:
            learning_data[lang] = weights

    # 2. ESTIMATION PHASE & DATA EXPORT
    with open(output_filename, 'w', encoding='utf-8') as out:
        # Table Header
        header = f"{'File':<12} | {'Est. Lang':<10} | {'Estimate (%)':<15}\n"
        out.write("--- Machine Learning Language Estimation Results ---\n")
        out.write(header)
        out.write("-" * 45 + "\n")

        for test_file in test_files:
            y_weights = get_weights(test_file)
            if not y_weights:
                continue

            for lang_name, w_weights in learning_data.items():
                # Get unique characters from both training and test data
                all_chars = set(w_weights.keys()).union(set(y_weights.keys()))
                
                # Equation: P = 1 - sum |wi - yi|
                sum_diff = sum(abs(w_weights.get(c, 0) - y_weights.get(c, 0)) for c in all_chars)
                p = 1 - sum_diff
                percentage = max(0, p * 100) # Format as percentage

                # Write result row
                out.write(f"{test_file:<12} | {lang_name:<10} | {percentage:<15.6f}%\n")
            out.write("-" * 45 + "\n")

    print(f"Machine learning results have been exported to {output_filename}")

# --- EXECUTION ---
if __name__ == "__main__":
    # Define your training data (Learning Data)
    training = {
        "Finnish": "kalevala.txt",
        "English": "romeo_et_juliet.txt"
    }

    # Files to analyze (from Moodle)
    to_analyze = ["pg18857.txt", "pg27417.txt", "pg48460.txt"]

    run_ml_analysis(to_analyze, training)