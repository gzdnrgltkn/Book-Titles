file = open("/usercode/files/books.txt", "r+")

books=file.readlines()

k=0
title_list=[]
while k<len(books):
 if k<len(books)-1:
  book_name=list(books[k])
  book_len=len(book_name)-1
  fl=book_name[0]
  title=str(fl)+str(book_len)
  title_list.append(title)
  k+=1
 else:
  book_name=list(books[k])
  book_len=len(book_name)
  fl=book_name[0]
  title=str(fl)+str(book_len)
  title_list.append(title)
  k+=1

title="\n".join(title_list) #make sure title is string

#file.close()

file = open("/usercode/files/books.txt", "w") #open it in w mode so all the other things will be deleted. it will be like e new file
file.write(title)
file.close()

file = open("/usercode/files/books.txt", "r")
print(file.read())#to read it finally
file.close()
