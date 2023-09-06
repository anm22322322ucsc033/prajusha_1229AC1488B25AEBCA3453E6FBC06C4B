#to find the leap year or not using if...esle statement.

year = int(input('Enter year : '))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")