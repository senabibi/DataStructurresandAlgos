def calculate():

    numdays=int(input("Number of temperatures?"))
    total=0
    temp=[]
    for i in range(numdays):
        next_day=int(input(f"Day {i+1}'s high temperatures is :" ))
        temp.append(next_day)
        total+=temp[i]
    avg=round(total/numdays,2)
    above=0
    for i in temp:
        if i>avg:
            above+=1
    print(f"Above of the average temperature  is {above}")
   

calculate()

