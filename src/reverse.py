num = 123
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
    print("reminder: ", reminder)
    print("reverse_number: ", reverse_number)
    print("num: ", num)
    print("--------------------------")
print("Revere Number ", reverse_number)