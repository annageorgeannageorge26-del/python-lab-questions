try:
    units = float(input("Enter units consumed: "))
    if units < 0:
        raise ValueError("units cannot be negative")
except ValueError as e:
    print("Invalid input:", e)
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 300 + (units - 100) * 5
    else:
        bill = 800 + (units - 200) * 8
    print("Electricity bill: Rs.", bill)
finally:
    print("Program finished")