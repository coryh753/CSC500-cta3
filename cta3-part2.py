timeInput=float(input("Please enter a time: "))
alarmInput=float(input("Please enter the number of hours you would like to pass before your alarm goes off: "))

print("The time your alarm will go of is: " , (timeInput + alarmInput) % 24 )