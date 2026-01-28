s=input("enter the sentence")
c=s.title()
words=c.split()
print(words)
for i in words:
  print(i[0],end="")