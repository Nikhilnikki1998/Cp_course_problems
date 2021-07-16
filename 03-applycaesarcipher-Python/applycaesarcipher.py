# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")



def fun_applycaesarcipher(msg, shift):
    st=""
    for i in msg:
        # print(i)
        if(i==" "):
            # print(i)
            st+=i

            continue
        ascii=ord(i)
        if(97<=ascii and ascii<=122):
            
            b=ascii+shift
            if(b>122):
                b=b-122
                b=96+b
            elif(b<97):
                b=97-b
                b=123-b
        elif(65<=ascii and ascii<=90):
            b=ascii+shift
            if(b>90):
                b=b-90
                b=64+b
            elif(b<65):
                b=65-b
                b=91-b
        a=chr(b)
        st+=a
        # print(st)
    return st
 




