'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''

es_vegetariana = input("¿Quieres una pizza vegetariana?(S/N):")
ingredientes_fijos = "la mozzarella y el tomate"

if es_vegetariana == "S":
    print("Ingredientes vegetarianos: Pimiento y tofu.")
    ingrediente_seleccionado = input("Inserta el ingrediente seleccionado de los anteriores:")
    ingrediente_seleccionado = str.lower(ingrediente_seleccionado)
    if ingrediente_seleccionado == "pimiento" or ingrediente_seleccionado == "tofu":
        print("Se ha añadido", ingrediente_seleccionado,"a la pizza vegetariana, además de", ingredientes_fijos,".")
    else:
        print("Ingrediente incorrecto.")

elif es_vegetariana == "N":
    print("Ingredientes NO vegetarianos: Peperoni, Jamón y Salmón.")
    ingrediente_seleccionado = input("Inserta el ingrediente seleccionado de los anteriores:")
    ingrediente_seleccionado = str.lower(ingrediente_seleccionado)
    if ingrediente_seleccionado == "peperoni" or ingrediente_seleccionado == "jamon" or ingrediente_seleccionado == "salmon":
        print("Se ha añadido", ingrediente_seleccionado,"a la pizza NO vegetariana, además de", ingredientes_fijos,".")
    else:
        print("Ingrediente incorrecto.")
else:
    print("Respuesta no válida.")