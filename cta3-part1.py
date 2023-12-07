def salesTax(billAmount):
    return (billAmount * .07)

def tipAmount(billAmount):
    return (billAmount * .18)

def totalBill(billAmount):
    billTax = float(salesTax(billAmount))
    billTip = float(tipAmount(billAmount))

    return billTax + billTip + billAmount

try:
    billAmount = float(input("Please enter the amount of your bill: "))
    print(f'Total bill with tip and sales tax: {totalBill(billAmount)}')
except ValueError:
    print("Please enter only numbers")