consumo_restaurante= int(input("ingrese el consumo en el restaurante:$"))
porcentaje_comida= int(input("Ingrese el porcentaje de propina que desea dejar:"))
propina= consumo_restaurante * (porcentaje_comida / 100)
print("La cantidad de dinero a dejar como propina es: $", propina)