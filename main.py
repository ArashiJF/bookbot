def main ():
    path = './books/frankestein.txt'
    text = get_file_content(path)
    char_dict = format_character_dict(get_character_dict(text))

    pretty_print(f"Text Stats for {path}", True)
    pretty_print(f"The word count for the text is {get_word_count(text)}")
    pretty_print(f"Letter occurences are as follows: ")

    for char_info in char_dict:
        if not char_info["character"].isalpha():
            continue
        pretty_print(f"The {char_info['character']} character was found {char_info['count']} times")

    pretty_print("End of Stats", True)

def pretty_print (content, use_bar = False):
    spacer = None
    if (use_bar):
        spacer = "====="
    else:
        spacer = "     "
    print(f"{spacer} {content} {spacer}")

def get_file_content (path):
    with open(path) as f:
        return f.read()

def get_word_count (text):
    words = text.split()
    return len(words)

def get_character_dict (text):
    words = text.split()
    formatted_words = []

    for word in words:
        formatted_words.append(word.lower())

    char_dict = {}
    for word in formatted_words:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def format_character_dict (data):
    pretty_list = []
    for key in data:
        pretty_list.append({ "character": key, "count": data[key] })

    pretty_list.sort(reverse=True, key=sort_on)
    return pretty_list

main()
