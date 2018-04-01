import json
f = open('friends.json', 'r')
b = f.read()
f.close()
b = json.loads(b)
d = {"oe": 0, "n": 0, "z": 0,
     "oK": 1, "6": 1, "5": 1,
     "ow": 2, "-": 2, "A": 2,
     "oi": 3, "o": 3, "i": 3,
     "7e": 4, "v": 4, "P": 4,
     "7K": 5, "4": 5, "k": 5,
     "7w": 6, "C": 6, "s": 6,
     "7i": 7, "S": 7, "l": 7,
     "Ne": 8, "c": 8, "F": 8,
     "NK": 9, "E": 9, "q": 9}
# b = b["data"]["list"]  # for mine.json
b = b["data"]["confesses"]  # for friends.json

for c in b:
    print(str(c['toNick'])+' <-------- '+c['topicName'] +
          ' by '+c['fromNick'] + '  ' + 'QQ:', end='')
    ans = ''
    a = c['fromEncodeUin'][4:-1]
    l = len(a)
    i = 0
    while (i < l):
        if i+1 < l:
            x = a[i]+a[i+1]
            if x in d.keys():
                ans = ans+str(d[x])
                i = i+2
                continue
        if a[i] in d.keys():
            ans = ans+str(d[a[i]])
        i = i+1
    print(ans)
