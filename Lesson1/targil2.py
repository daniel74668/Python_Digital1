print ("welcome  to soping")

tomatos = int(input(("enter how many tomatos?")))
cucambers = int(input(("enter how many cucambers?")))
cola = int(input(("enter how many colas?")))
chickens = int(input(("enter how many chickens?")))

pricetotomatos = 3
pricetocucambers = 2
pricetocola = 5
pricetochickens = 20

summary=((tomatos*pricetotomatos)+(cucambers*pricetocucambers)+(cola*pricetocola)+(chickens*pricetochickens))

print ("summary \ntomatos:  " + (str(tomatos))+ "\ncucambers: " + str(cucambers) + "\ncola: "
       + str(cola)+"\nchickens: "+ str(chickens) + "\nprice  to paymant witout Tax is  : " + str(summary)+
        "\nprice  to paymant wite Tax is  : " + str("%.1f"%(summary+1.17))
       )