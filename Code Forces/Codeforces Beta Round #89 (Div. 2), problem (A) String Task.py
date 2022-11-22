vowles=['a','o','y','e','u','i']
s=input()
for i in range (len(s)):
    if  s[i].lower() not in vowles:
        print('.'+s[i].lower(),end='')