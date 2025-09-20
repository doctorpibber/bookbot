import sys

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents.split()

def get_num_words():
    text = get_book_text(sys.argv[1])
    count = 0
    for x in range(len(text)):
        count += 1
    
    print(f"Found {count} total words")

def sort_on(items):
    return items["num"]

def count_chars(text):
    text = get_book_text(sys.argv[1])
    string = "".join(text).lower()
    counts = {
            "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, 
            "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, 
            "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, 
            "y":0, "z":0
            }
    letter = "abcdefghijklmnopqrstuvwxyz"

    for x in string:
        if x in letter:
            counts[x] +=  1
    return counts


def to_sorted_list(counts):
    result = []
    for char, num in counts.items(): 
        result.append({"char":char, "num":num})
    result.sort(reverse=True, key=sort_on)
    return result





