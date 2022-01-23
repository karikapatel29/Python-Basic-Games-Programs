import random
human=0 
computer=0
i=0
print("LET'S PLAY SNAKE WATER GUN")
while i in range (5):
    x=random.randint(1,3)
    n=int(input("Type 1 for snake 2 for water 3 for gun 4 for exit:"))
    if n==4:
        break
    if(n==1 and x==3):
      computer+=1
    elif(n==2 and x==1):
      computer+=1
    elif(n==3 and x==2):
      computer+=1
    elif(n==2 and x==3):
      human+=1
    elif(n==1 and x==2):
      human+=1
    elif(n==3 and x==1):
      human+=1
    i+=1
if human>computer:
    print("congratulations you won")
elif computer>human:
    print("haha joke's on you...i won")
else:
    print("god knows who won!")
