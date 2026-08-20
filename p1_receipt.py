print("============================")



name = input("Enter your name:")


contact = input("Enter your Contact number:")


address = input("Enter your address:")



product1 = input("Enter product:")


price1 = float(input("Enter price:"))


quantity1 = int(input("Enter quantity:"))



sum1 = price1 * quantity1



product2 = input("Enter product:")


price2 = float(input("Enter price:"))


quantity2 = int(input("Enter quantity:"))



sum2 = price2 * quantity2



product3 = input("Enter product:")


price3 = float(input("Enter price:"))


quantity3 = int(input("Enter quantity:"))



sum3 = price3 * quantity3



discount = input("Enter discount:")

discount1 = float(discount.replace("%",""))


subtotal = sum1 + sum2 + sum3


discount_amount = subtotal * (discount1 / 100)


total = subtotal - discount_amount



print(" venedick fallorina ")

print(" STORE ")

print("location: bsit south 7 ")

print("==========================")


print("name:",name)


print("contact number:",contact)


print("address:",address)


print("product:",product1)


print("price:",price1)


print("quantity:",quantity1)


print("sum:",sum1)



print("---------------------------")



print("product:",product2)


print("price:",price2)


print("quantity:",quantity2)


print("sum:",sum2)



print("---------------------------")



print("product:",product3)


print("price:",price3)


print("quantity:",quantity3)


print("sum:",sum3)



print("----------------------------")



print("subtotal:",subtotal)



print("discount(%):",discount)


print("discount_amount):",discount_amount)


print("••••••••••••••••••••••••••••")



print("total:",total)
