def calculate():

    numdays=int(input("Number of temperatures?"))
    total=0
    for i in range(1,1+numdays):
        next_day=int(input(f"Day {i}'s high temperatures is :" ))
        total+=(next_day)
    avg=round(total/numdays,2)
    print(f"Average is {avg}")

calculate()
