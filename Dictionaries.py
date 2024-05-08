## Dictionary: String to String
## Take dictionary and create new dictionary that counts characters of key

d = {"Aaron":"William","Terry":"Brent","Timothy":"Joseph"}
d2 = {   key:len(value) for (key, value) in d.items() }

d3={}
for k, v in d.items():
    if len(k) < 6:
        d3[k]=len(v)
print(d3)
d['Aaron']