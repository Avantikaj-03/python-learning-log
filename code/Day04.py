# Today we are going with loops

#For loop : used when iterationa are known 

names= ['avantika', 'sejal', 'ashish', 'saurabh']
for name in names:
    print(name)
    
for letter in "Avantika":
    print(letter)
    
for i in range(10):
    print(i)

for i in range(1, 6, 2):
    print(i)

for i in range(5):
    print(i*i)
    
# While Loop: used when iteration are unknown, run as lond as condition is true, usesd boolean conditions(T/F)
count = 1
while count <= 5:
    print(count)
    count += 1
    
user_ip= ""

while user_ip != "q":
    user_ip = input("Enter your text (for quit enter q):")
    print("Text Entered: ", user_ip)
    
#Break, Continue, Pass

for i in range(10):
    if i == 6:
        break 
    print(i)
    
for i in range(6):
    if i == 2:
        continue
    print(i)

for i in range(4):
    if i == 1:
        pass
    print(i)
    
# Let' continue in project with the knowlegde i have 