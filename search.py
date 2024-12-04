import sys
import re

def search(pattern, file, ignore_case=False, show_count=False, whole_words=False):
    try:
        count = 0
        with open(file, 'r') as f:
            for line in f:
                if whole_words:
                    word_boundary_pattern = r'\b' + re.escape(pattern) + r'\b'
                    if (re.search(word_boundary_pattern, line, re.IGNORECASE) if ignore_case else re.search(word_boundary_pattern, line)):
                        print(line.strip())
                        count += 1
                else:        
                    if (re.search(pattern, line, re.IGNORECASE) if ignore_case else re.search(pattern, line)):
                        print(line.strip())
                        count += 1
            if show_count:
                print(count)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    args = sys.argv[1:]
    ignore_case = '-i' in args
    show_count = '-c' in args
    whole_words = '-w' in args

    # remove flags from args
    args = [arg for arg in args if not arg.startswith('-')]
    
    
    
    if len(args) != 2:
        print("Wrong number of arguments.")
        print("Example command: python search.py [-i] [-c] [-w] <pattern> <file>")
        return

    pattern, file = args
    search(pattern, file, ignore_case, show_count, whole_words)

if __name__ == '__main__':
    main()
