import string

def add_word(single_word, word_dict):
    if single_word not in word_dict:
        word_dict[single_word] = 1
    else:
        word_dict[single_word] += 1

def process_line(line_data, word_dict):
    word_list = line_data.split()
    for word in word_list:
        word = word.strip(string.punctuation)
        add_word(word, word_dict)

word_dict = {}
line_data = "this is a collection of words of nice words this is a fun thing it is"
process_line(line_data, word_dict)

sort_keys = sorted(word_dict)
for key in sort_keys:
    print(key + " : "+str(word_dict[key]))
