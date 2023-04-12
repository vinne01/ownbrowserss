n = int(input("enter the principle amount"))
rate = float(input("enter the rate"))
years = int(input("enter the number of years"))
for i in range(years):
    n = n+((n*rate)/100)
    print(n)
