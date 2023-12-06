### Cryptographie symetrique
text=input("Entre un text :")
tabcode ={"a":"0!","b":"5!","c":"11?","d":"6B","e":"a8","f":"C45","g":"8A:","h":"u:","i":"2G","j":"m0ù","k":"ty0","l":"(!","m":"!7-","n":"p|",
          "o":"B2#","p":"J5#","q":"${","r":"#!3","s":"E12!","t":"w0#","u":"ù1#","v":"0S#","w":"A15","x":"O2","y":"2H","z":"V2"," ":"&!"}
codetext=""
for s in tabcode:
    codetext+=tabcode[s]
print("Cryptage :"+codetext)
code = codetext
for k in tabcode:
         if(tabcode[k] in code):
                  code=code.replace(tabcode[k],k)
print("Decryptage :"+code)
