def caesarCipher(s, k):
    # Write your code here
    ss=''
    k=k%26
    for i in s:
        if i.isalpha():
            if i.isupper() and (ord(i)+k)>90:
                ss+=chr(ord(i)+k -26 )
            elif i.lower() and (ord(i)+k)>122:
                ss+=chr(ord(i)+k -26 )
            else:
                ss+=chr(ord(i)+k  )
                
            
        else:
            ss+=i
    return ss