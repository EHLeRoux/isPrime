def isPrime():   
    #Getting user input
    counter = 1
    divisibleCounter = 0
    #user can enter the a number 20 times
    while (counter < 20): 
        divisibleCounter = 0 #making the divisble counter equal to zero before every iteration
        userInput = (int) (input ("Please enter your number: "))
        
        #checking if the user entered 1
        if (userInput == 1): 
            print ("You have chosen number 1")
        if (userInput > 1): 
            print ("Your number is bigger than 1")
            
            #start of the for loop to check whether the number is a prime number or not
            for i in range(userInput): 
                index = 1 + i #incrementing the number which is used for division
                if (userInput % (index)) == 0: #Here we check each iteration
                    divisibleCounter = divisibleCounter + 1 #here we count the amount of numbers that can devide in the number
                    print ("Your number is divisible by {}".format(index))
                    
                else: 
                    print ("Your number is not divisible by {}".format(index))
        
        #This is the final print or check, if the number can be divided by more than 2 numbers (1 and itself) then it is not a prime, otherwise it is.
        if (divisibleCounter > 2): 
            print ("Your number is divisible by more than 2 numbers, namely 1 and the number itself. Therefore your number {} is not a prime number".format(userInput))
            
        elif(divisibleCounter == 2): 
            print ("Your number is divisible by only 2 numbers, namely 1 and the number itself. Therefore your number {} is a prime number.".format(userInput))
        

if __name__=="__main__":
    
    isPrime()