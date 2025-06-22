#Let' move to Strings
#Let start with the string declaration, indexing

str1="Hello World !" #Double quotes
str2='this is another way' #Single quotse
str3="""This is      
for the mupltile line
purpose""" # Triple quotes

print(str3)

#indexing

print(str1[0])
print(str1[3])
print(str1[-1])
print(str1[-6])

name="Avantika Junagade"
initial_first=name[0]
initial_last=name[9]
print(f"Initials of name are: {initial_first}.{initial_last}")

#String SLicing 
Str1="Kim Namjoon"

print(Str1[0:3])
print(Str1[5:7])
print(Str1[9:16])

#steping

print(Str1[::-1])
print(Str1[2:13:3])
print(Str1[-5:-1])
print(Str1[1::])
print(Str1[:4:])
print(Str1[::3])

#String Build-in function

bts="   Kim Teahyung, Taetae  "

print(f"Uppercase: {bts.upper()}")
print(f"Lowercase: {bts.lower()}")
print(bts.split(", "))
print(f"Replaced one: {bts.replace("Taetae","V")}")
print(bts.find("Taetae"))
print(bts.strip())

print(bts.strip().upper()) #Combines methods 


mail=input("Please Enter your email id:")

mail1=mail.replace("gmail","outlook")

print(f"Output: {mail1}")