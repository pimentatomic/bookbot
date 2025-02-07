def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = word_count(text.split())
    char_count = get_chars_dict(text)
    report = get_report(char_count, book_path, words_num)
    print(report)
    # print(f"{words_num} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    return len(text)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_report(dict, path, words_num):
    list_of_dic = []
    for char, count in dict.items():
        char_dict = {
            "char": char,
            "num": count
        }
        list_of_dic.append(char_dict)

    def sort_on(dict):
        return dict["num"]
    
    list_of_dic.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{words_num} words found in the document \n")
    for dic in list_of_dic:
        if dic["char"].isalpha():
            print(f"The '{dic["char"]}' character was found {dic["num"]} times")
    print("--- End report ---")

main()