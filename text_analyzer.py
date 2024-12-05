import os

path = "./text/"
files = os.listdir(path)

for file in files:
    text_file = open(path + file)
    text_string = text_file.read().lower()
    text_file.close()

    letters_list = list(text_string)
    letters_dic = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
    'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
    'y': 0, 'z': 0}

    words_list = text_string.split()

    for letter in letters_list:
        try:
            letters_dic[letter] += 1
        except:
            pass

    letters_list = []
    for letter in letters_dic:
        letters_list.append({"letter": letter, "instances": letters_dic[letter]})
        
    def dic_sort(d):
        return d["instances"]
    
    letters_list.sort(reverse=True, key=dic_sort)

    print(f'Begin report of {file}: \n')
    print(f'There are {len(words_list)} words in {file}')
    
    for letter in letters_list:
        print(f'The letter {letter["letter"]} appears {letter["instances"]} times in {file}')
    print("End report\n\n")
