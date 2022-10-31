# with open('message.txt','a') as fileWrite:
#     fileWrite.write('whatsup polapain')

with open('message.txt','r') as fileRead:
    text=  fileRead.read()
    print(text)


