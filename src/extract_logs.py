import sys
import os

LOG_FILE_PATH = "C:/temp/logs_2024.log"  # Adjust path to the actual log file
OUTPUT_DIR = "output"

def extract_logs(date):
    """Extract logs for a specific date and save to a file."""
    output_file = f"{OUTPUT_DIR}/output_{date}.txt"

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        with open(LOG_FILE_PATH, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if line.startswith(date):  # Fast string matching
                    outfile.write(line)
        
        print(f"Extraction complete: {output_file}")

    except FileNotFoundError:
        print(f"Error: Log file {LOG_FILE_PATH} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    input_date = sys.argv[1]
    extract_logs(input_date)
