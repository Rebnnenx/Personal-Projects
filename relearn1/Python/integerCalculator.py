"""_summary_
    this program prompts the user for a couple of numbers.
    it then asks which numerical operation should be conducted on the 2 numbers
    and returns the result
"""
#main function
def __main__():
    
#default value for varibles
    input_int=int(0)
    var_int1=int(0)
    var_int2=int(0)
    var_str_repeat= "y"
    
    print("Hello world! time to relearn python")
    print("would you like to play a game?")
    
    
    
#enables looping of the game
    while(var_str_repeat == "y" or var_str_repeat == "Y"): 
        
#stores first number
        input_int= input("\n\ncan you give me an integer number? ")
        var_int1= input_int 

#stores second number
        input_int=input("how about a second one? ")
        var_int2= input_int 


#obtains the operation user wishes to conduct
        print("\nWhat would you like to do?\n1. Add\n2. Subtract\n3. Multipy\n4. Divide \n5. Modulo")
        input_int= input("Please input the number of the operation: ")
        
        if(int(input_int) == 1):
            add(var_int1, var_int2)
        elif(int(input_int) == 2):
            subtract(var_int1,var_int2)
        elif(int(input_int) == 3):
            multiply(var_int1,var_int2)
        elif(int(input_int) == 4):
            divide(var_int1,var_int2)
        elif(int(input_int) == 5):
            modulo(var_int1,var_int2)
        else:
            print("improper input")
            
        var_str_repeat = input("\n\n\n\nWould you like to play again? Y/N ") #prompts to repeat the game
    
    print("\n\nThanks for playing!\nEnding Program")

#defines Addition module
def add(x, y):
    var_sum = int(x)+int(y)
    print("{} + {} = {}".format(x, y, var_sum))
    return

#defines Subtraction module
def subtract(x, y):
    var_sum = int(x)-int(y)
    print("{} - {} = {}".format(x, y, var_sum))
    return

#defines Multiplication module
def multiply(x, y):
    var_sum = int(x)*int(y)
    print("{} * {} = {}".format(x, y, var_sum))
    return

#defines Multiplication module
def divide(x, y):
    var_sum = int(x)/int(y)
    print("{} / {} = {}".format(x, y, var_sum))
    return

#defines Modulo module
def modulo(x, y):
    var_sum = int(x)%int(y)
    print("{} % {} = {}".format(x, y, var_sum))
    return

#calls main function to start program
__main__()