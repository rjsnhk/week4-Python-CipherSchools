with open('file.txt','r') as f:
    f.write('hello there\nsubscribe to my channel')

with open('file.txt','a') as f:
    f.write('please do it')

with open('file.txt','r+') as f:
    f.seek(len(f.read()))
    f.write('please do it')

