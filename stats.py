def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(content):
    content = content.lower()
    dict = {}
    for char in content:
        dict[char] = dict.get(char, 0) + 1
    return dict

def get_dict_array(dict):
    dict_array = []
    for key, value in dict.items():
        dict_array.append({
            "char": key,
            "num": value
        })
    dict_array.sort(key=lambda x: x["num"], reverse=True)
    return dict_array

def report(path, count, dict_array):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count ------- ")
    for item in dict_array:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END =============== ")

