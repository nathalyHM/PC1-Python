edad= int(input("Ingrese la edad del cliente:"))
if edad < 4:
    print("la edad del cliente es:",edad,"por lo tanto el precio de la entrada es gratis")
elif 4 <= edad <= 18:
    print("la edad del cliente es:",edad,"por lo tanto el precio de la entrada es $5")
else:
    print("la edad del cliente es:",edad,"por lo tanto el precio de la entrada es $10")      