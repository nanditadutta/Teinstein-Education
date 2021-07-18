#function for the Armstrong number
def Armstrong():
    """This function is used for identifying if the user inputs is a Armstrong number or not."""
    x = int(input("Enter a number: "))  
    sum = 0  
    temp = x 
    
    while (temp > 0):  #main logic 
        r = temp % 10  
        sum += r ** 3  
        temp=temp // 10  
    
    if (x == sum):  #if the sum and the user input is same 
        print(x,"is an Armstrong number")  
    else:  
        print(x,"is not an Armstrong number")

Armstrong() #calling of the function


