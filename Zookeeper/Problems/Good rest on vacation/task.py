# put your python code here
print()
vacation_days = int(input())
print()
cost_per_day = int(input())
print()
one_flight = int(input())
print()
hotel_days = int(input())

print(vacation_days * cost_per_day + one_flight * 2 + (hotel_days * (vacation_days - 1)))
