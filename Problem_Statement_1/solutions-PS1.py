import math
# Uppercase alphabets (A-Z): The ASCII values range from 65 (for 'A') to 90 (for 'Z').
# Lowercase alphabets (a-z): The ASCII values range from 97 (for 'a') to 122 (for 'z').


accepted=input("enter message to be encoded")
accepted_asci=[ord(c) for c in accepted]
s=int(input("enter 1 to encode and anything to decode message"))
def coder():
    coded=" "
    shift=int(input("enter amount by which it is to be shifted(between 1 to 26)"))
    if s==1:
        for i in accepted_asci:
            if (i>64 and i+shift<91) or (i>96 and i+shift<123) :
                coded=coded+chr(i+shift)
            elif (i>64 and i+shift>91) or (i>96 and i+shift>123):
                coded=coded+chr(i+shift-26)
            else :
                coded=coded+chr(i)
    else :
        for i in accepted_asci:
            if (i-shift>64 and i<91) or (i-shift>96 and i<123) :
                coded=coded+chr(i-shift)
            elif (i-shift>64 and i>91) or (i-shift>96 and i>123):
                coded=coded+chr(i-shift+26)
            else :
                coded=coded+chr(i)
    print("operation succesfully done, the resultant message is ",coded)
coder()