import re

myfile = open("file.txt", "rt") # open lorem.txt for reading text
contents = myfile.read()
string_list = contents.split()
match = 'PMID'

match_list = []
for words in string_list:
    if match in words:
        match_list.append(words)

match_list = [sub.replace('\\', '') for sub in match_list]
match_list = [sub.replace('"', '') for sub in match_list]
match_list = [sub.replace('(', '') for sub in match_list]
match_list = [sub.replace(')', '') for sub in match_list]
match_list = [sub.replace('PMID:', '') for sub in match_list]
match_list = list(dict.fromkeys(match_list))



print(match_list)
print(len(match_list))
myfile.close()
