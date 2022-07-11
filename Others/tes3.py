import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
	'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through the list and examine each element
#if the current element in .txt then add to database

base = sqlite3.connect('test3.db')
      
with base:
    cur = base.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS file_list( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                filename TEXT \
                )')
    base.commit()
base.close()

base = sqlite3.connect('test3.db')

with base:
    cur = base.cursor()
    for fname in fileList:
        if '.txt' in fname:
              cur.execute('INSERT INTO file_list(filename) VALUES(?)', (fname,))                          
    base.commit()
base.close()

base = sqlite3.connect('test3.db')


with base:
    cur = base.cursor()
    cur.execute('SELECT filename FROM file_list WHERE filename = ".txt"')
    for item in fileList:
        if '.txt' in item:
            print(item)
    







                



