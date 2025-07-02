def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_characters(input_string):
    characters = list(input_string.lower())
    character_bank = {}
    for character in characters:
        if character in character_bank:
            character_bank[character] += 1
        else: 
            character_bank[character] = 1
    return character_bank

def sort_characters(character_dictionary):
    def sort_on(items):
        return items["num"]
    
    character_dictionary_list = []
    for character in character_dictionary:
        character_dictionary_list.append(
            {
                "char": character, 
                "num": character_dictionary[character]
            }
        )
    character_dictionary_list.sort(reverse=True, key=sort_on)
    return character_dictionary_list