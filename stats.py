def count_words(string_to_count):
    num_words = len(string_to_count.split())
    return num_words

def count_characters(string_to_count):
    character_list = {}

    for char in string_to_count:
        char_lower = char.lower()
        if char_lower in character_list:
            character_list[char_lower] += 1
        else:
            character_list[char_lower] = 1
    
    return character_list

def get_num(input_dict):
    return input_dict["num"]

def print_report(dic):
    sorted_report_list = []
    for key, value in dic.items():
        if key.isalpha() == False:
            continue
        entry = {
            "char": key,
            "num": value
            }
        sorted_report_list.append(entry)
    sorted_report_list.sort(key = get_num, reverse=True)
    for item in sorted_report_list:
        print(f"{item["char"]}: {item["num"]}")

