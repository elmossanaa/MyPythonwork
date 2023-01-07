secret_num =6
guess_count=0
limit =3
while guess_count <limit:
    guess = int(input("enter guess: "))
    guess_count = guess_count +1
    if guess==secret_num:
        print("you're right!")
        break
else:
    print("you lose")
    
    


