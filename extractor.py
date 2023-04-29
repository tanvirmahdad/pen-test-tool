import re


myfile = open("testsem.txt", "rt") # open lorem.txt for reading text
contents = myfile.read()
string_list = contents.split()
match=[]
match.append('pmids')
match.append('.')

match_except='n_pmids'
print(match)

matchCounter=0
found=0


match_list = []
for words in string_list:
    if any(ext in words for ext in match) and (match_except not in words):
        if (matchCounter==0 or matchCounter==1):
            matchCounter=matchCounter+1
        if(matchCounter==2):
            found=1
            matchCounter=0
    else:
        if matchCounter==1:
            matchCounter=0
        if found==1:
            match_list.append(words)
            found=0



match_list=[sub.replace('"', '') for sub in match_list]
match_list=[sub.replace(')', '') for sub in match_list]


match_list=";".join(match_list).split(";")






match_list = list(dict.fromkeys(match_list))

print(len(match_list))


print(match_list)
myfile.close()