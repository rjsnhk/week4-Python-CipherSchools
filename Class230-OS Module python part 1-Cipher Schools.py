import os 
print(os.getcwd())
os.mkdir('movies')

if os.path.exists('movies'):
    print('already exists')
else:
    os.mkdir('movies')

open('file.txt','a').close()
os.mkdir(r'F:\codes\movies')

print(os.listdir())