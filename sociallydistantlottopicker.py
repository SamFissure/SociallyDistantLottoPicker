import math
import random


def main():
    lottoPrint()
    choose= random.randint(1, 69)
    addToChosen(choose)
    addToDistance(choose)
    print("picked numbers ", Chosen)
    for i in range (4):
        checkSocialDistance()
        print("picked numbers ", Chosen)
    print("Powerball", random.randint(1,26))
    keyPress=input("press any key to exit ")




    #a Lottery number picker that socially distances its values.
    #Constants for ball range
    
Chosen = []
Distance = []

def lottoPrint():
    print("lottery number chooser")
def addToChosen(n):
    Chosen.append(n)

def addToDistance(n):
    Distance.append(n-7)
    Distance.append(n+6)

def checkSocialDistance():
    isNotDone=True
    #isNotDone allows for re-picking the number, isInLoop controls distance checking
    while (isNotDone==True):
        choose= random.randint(1,69)
        print("Prospective number, testing for social distance from other numbers", choose)
        #print("Number denial list size", len(Distance))
        #print("Number Denial list", Distance)
        i=0
        isInLoop=True
        while(isInLoop):
            #check if chosen number is between the lower and upper bound set by a previous ball chosen
            if ((Distance[i]<=choose) and (choose<=Distance[i+1])):
                #leave loop
                isInLoop=False
                print("Number failed to social distance")
            elif(i==(len(Distance)-2)):
                #IF we are at the end of the list AND we haven't rejected the ball
                #THEN we can add it to the list of balls, add a new bound, and exit the loop
                addToChosen(choose)
                addToDistance(choose)
                isNotDone=False
                isInLoop=False
            else:
                i+=2


    return

if __name__=="__main__":
    main()
