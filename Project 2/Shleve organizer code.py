#NOTE

print("""Welcome to the bookshelf checker! You will need this program to help you once you doubt the book order. Shelves are read from left to right, so ensure that you put book 1 on the left side of book 2. Please fill in the book codes and let the program help you with your shelf-reading task!
""")
  



#Firstbook_input
line1_1=input("Enter the first line of the book 1 code:")
line2_1=input("Enter the second line :")
line3_1=input("Enter the third line:")
line4_1=input("Enter the fourth line:")
print("")
print("Great now the second book!")
print("")
#Secondbook_input
line1_2=input("Enter the first line of the book 2 code:")
line2_2=input("Enter the second line:")
line3_2=input("Enter the third line :")
line4_2=input("Enter the fourth line:")

#2LIST  
firstbook=[line1_1,line2_1,line3_1,line4_1]
secondbook=[line1_2,line2_2,line3_2,line4_2]
#validating the fisrt line
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count=0

codebookone=[]
codebooktwo=[]
list1 = [0,1]
list2 = [0]
for i in firstbook[0]:
    codebookone.append(letters.index(i))


for g in secondbook[0]:
    codebooktwo.append(letters.index(g))

list1 = [0, 1]
list2 = [0]

i = 0
while i < len(codebookone) and i < len(codebooktwo):
    if codebookone[i] < codebooktwo[i]:
        count+=1
        break
    elif codebookone[i] > codebooktwo[i]:
        count-=1
        break
    i += 1
else:
    if len(codebookone) < len(codebooktwo):
        count+=1
    elif len(codebookone) > len(codebooktwo):
        count-=1
  
        
#second line validation

line21=[]
for i in range(len(line2_1)):
    line21.append(int(line2_1[i]))


line22=[]
for i in range(len(line2_2)):
    line22.append(int(line2_2[i]))


for i in range(min(len(line22),len(line21))):
    if line21[i]>line22[i]:
        count-=1
    elif line21[i]<line22[i]:
        count+=1
        
#3rd line validation

line31=[]
line32=[]
for i in range(len(line3_1)):

    line31.append(line3_1[i])
for i in range(1, len(line31)):
    line31[i] = int(line31[i])


for i in range(len(line3_2)):
    line32.append(line3_2[i])
for i in range(1, len(line32)):
    line32[i] = int(line32[i])


line31[0]=letters.index((line31[0]))
line32[0]=letters.index((line32[0]))

for i in range(min(len(line31),len(line32))):
    if line31[i]>line32[i]:
        count-=1
    elif line31[i]<line32[i]:
        count+=1

# fourth line validation

if line4_1>line4_2:
    count-=1
elif line4_1<line4_2:
    count+=1
    
    
if count==4:
    print("AMAZING! RIGHT ORDER")
else:
    print("OH NO! WRONG ORDER")
