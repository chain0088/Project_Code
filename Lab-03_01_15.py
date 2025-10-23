#Chatri Taruyanon
#6809610063
#15

Coke = float(input("Enter amount of Coke: "))
price_of_each_can = float(input("Enter price of each can: "))
Total_of_can = price_of_each_can * Coke
Nori_Lay = float(input("Enter amount of Nori Lay: "))
price_of_each_bag = float(input("Enter price of each bag: "))
Total_of_bag = price_of_each_bag * Nori_Lay
Tissue_Paper = float(input("Enter amount of Tissue Paper: "))
price_of_each_roll = float(input("Enter price of each roll: "))
Total_of_roll = price_of_each_roll * Tissue_Paper
Total_of_all = Total_of_can+Total_of_bag+Total_of_roll
print("Product         Unit       Price      Total")
print("Coke             %d         %d         %d" %(Coke,price_of_each_can,Total_of_can))
print("Nori Lay         %d         %d         %d" %(Nori_Lay,price_of_each_bag,Total_of_bag))
print("Tissue Paper     %d         %d         %d" %(Tissue_Paper,price_of_each_roll,Total_of_roll))
print("Total                                 %d" %(Total_of_all))