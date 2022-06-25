import re
from stopword import stop_word 

regex = re.compile('[^a-zA-Z]')
f = open("hamlet.txt","r")
s = f.read()
l = s.split()

worddict = dict()


for w in l:
    w = re.sub(regex,'',w)
    w = w.lower()
    if not stop_word(w):
        if w in worddict:
            worddict[w] += 1
        else:
            worddict[w] = 1
d = sorted(worddict.items(), key = lambda item:item[1], reverse = True)
#print(worddict.items())
for i in range(15):
    print(d[i][0],d[i][1])