'''Price of House is $1 million. If buyer has a credit, they need
to put down 10%. Otherwise, they need to put down 20%. Print the
down payment'''
price= 1_000_000
buyer= input("good credit/bad credit: ")
if(buyer=='good credit'):
    
    down_payment= .10*price
    
else:
    
    down_payment= .20*price
    
print(f"downpayment is: ${down_payment}")
print("have a nice day")

