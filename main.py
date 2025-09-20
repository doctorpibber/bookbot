from stats import get_book_text
from stats import get_num_words
from stats import sort_on
from stats import count_chars
from stats import to_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
text = get_book_text(path)
counts = count_chars(text)
sorted_list = to_sorted_list(counts)
for item in sorted_list:
    char = item["char"]
    num = item["num"]
    if char.isalpha():
        print(f"{char}: {num}")

count_chars(text)

to_sorted_list(counts)