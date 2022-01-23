import datetime
def getdate():
  return datetime.datetime.now()

def func(n):
    if n=="karika":
        opt=int(input("\n Type 1 for entering record and 2 for fetching record:"))

        if opt==1:
            x=int(input("\nType 1 for appending exercise and 2 for meal:"))
            if x==1:
                inp=str(input("\n Enter the exercise:"))
                f=open("karika exc.txt","a")
                f.write("["+str(getdate())+"] :"+inp+"\n")
                f.close()
            elif x==2:
                 inp=str(input("\n Enter the meal taken:"))
                 f=open("karika meal.txt","a")
                 f.write("["+str(getdate())+"] :"+inp+"\n")
                 f.close()
        elif opt==2:
            x=int(input("\nType 1 for fetching exercise and 2 for meal:"))
            if x==1:
                f=open("karika exc.txt")
                for i in f:
                    print(i,end=" ")
            else:
                 f=open("karika meal.txt")
                 for i in f:
                    print(i,end=" ")      
    elif n=="damon":
        opt=int(input("\n Type 1 for entering record and 2 for fetching record:"))

        if opt==1:
            x=int(input("\nType 1 for appending exercise and 2 for meal:"))
            if x==1:
                inp=str(input("\n Enter the exercise:"))
                f=open("damon exc.txt","a")
                f.write("["+str(getdate())+"] :"+inp+"\n")
                f.close()
            elif x==2:
                 inp=str(input("\n Enter the meal taken:"))
                 f=open("damon meal.txt","a")
                 f.write("["+str(getdate())+"] :"+inp+"\n")
                 f.close()
        elif opt==2:
            x=int(input("\nType 1 for fetching exercise and 2 for meal:"))
            if x==1:
                f=open("damon exc.txt")
                for i in f:
                    print(i,end=" ")
            else:
                 f=open("damon meal.txt")
                 for i in f:
                    print(i,end=" ")      
    elif n=="klaus":
        opt=int(input("\n Type 1 for entering record and 2 for fetching record:"))

        if opt==1:
            x=int(input("\nType 1 for appending exercise and 2 for meal:"))
            if x==1:
                inp=str(input("\n Enter the exercise:"))
                f=open("klaus exc.txt","a")
                f.write("["+str(getdate())+"] :"+inp+"\n")
                f.close()
            elif x==2:
                 inp=str(input("\n Enter the meal taken:"))
                 f=open("klaus meal.txt","a")
                 f.write("["+str(getdate())+"] :"+inp+"\n")
                 f.close()
        elif opt==2:
            x=int(input("\nType 1 for fetching exercise and 2 for meal:"))
            if x==1:
                f=open("klaus exc.txt")
                for i in f:
                    print(i,end=" ")
            else:
                 f=open("klaus meal.txt")
                 for i in f:
                    print(i,end=" ")      



print("DIET MANAGEMENT\n")

name=str(input("\nEnter name whose diet plan you need to organise:"))
func(name)