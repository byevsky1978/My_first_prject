# if prices in ILS add 18% TAX
#     if prices in $ add 20% tax
#     the results in 2 lists  NIS and $
prices = ["25$", "50$", "48ILS", "34$", "25$", "100ILS", "papa"]
prices_NIS=[]
prices_USD=[]
for price in prices:
    if "$" in price:
        price=price.replace("$","")
        price_as_int = int(price)
        price_as_int =  price_as_int * 1.2
        prices_USD.append(price_as_int)
    elif "ILS" in price:
       price = price.replace("ILS", "")
       price_as_int = int(price)
       price_as_int = price_as_int * 1.18
       prices_NIS.append(price_as_int)
    else:
        print('price incude vaue that cannt be cacuated')
print(prices_USD)
print(prices_NIS)


# if prices in ILS add 18% TAX
#     if prices in $ add 20% tax
#     the results in 2 lists
# prices = ["25$","50$","222EURO","48ILS","34$","25$","100ILS"]
# prices_ILS =[]
# prices_dolars = []
#
# for price in prices:
#     if "ILS" in price:
#         price=price.replace("ILS","")
#         price_as_int = int(price)
#         price_with_tax= price_as_int*1.18
#         prices_ILS.append(price_with_tax)
#         print (f"{price_with_tax} ILS added to ILS list")
#
#     elif "$" in price:
#         price=price.replace("$","")
#         price_as_int = int(price)
#         price_with_tax= price_as_int*1.2
#         prices_dolars.append(price_with_tax)
#         print (f"{price_with_tax}  Dolars added to dollars list")
#
#
#     else:
#         print("Price include value that can not be calulated")
#
# print ("Test End")
#
#
