def main(): 
    print("Welcome to the tip calculator!")

    total = float(input('What was the total bill? $'))

    percentage = float(input('How much tip would you like to give? 10, 12, or 15? '))

    people = float(input('How many people to split the bill? '))

    eachBill = (total*(1 + percentage/100))/people

    rounded = round(eachBill,2)

    print(f"Each person should pay: ${rounded}")
    
main()
