''' 
Created on Oct 1, 2018 
@author: wfox21
''' 

print("Welome")  

#personal info  

fullName = input("Please input your name: ",)  

phoneNumber = input("Please input your phone number: ")  

firstProduct = input("Please enter the name of the product you would like to purchase: ", )  

price = float(input("Please enter the price of the product: $" ))  

quantity = int(input("Please enter how many units you would like to purchase: "))  

tax = price * .06  

#subtotal price 

subtotal = quantity * price 

#final price 

total = subtotal + tax 

#print('the tax is $',tax,'the total is $', total) 

print(fullName) 
print() 
print(phoneNumber) 
print() 
print('Purchase Information:') 
print() 
print(firstProduct, "Quantity:", quantity, "Price: $", price)
print(subtotal, tax,total) 
