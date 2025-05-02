from stats import get_num_words
from stats import count_all_chars
import sys
import os

def main():
    print(sys.argv)
    if(len(sys.argv) == 2):
        filepath = sys.argv[1]
        if os.path.exists(filepath):
            count_all_chars(filepath)
        #else:
            #print ("book does not exist in libary")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
    