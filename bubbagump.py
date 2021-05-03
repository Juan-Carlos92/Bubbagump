menu = """
1-Camarones a la diabla.
2-Caldo de camarones.
3-Hamburguesa de camarón.
4-Ensalada de camarón.
5-Ceviche de camarón.

Elige una opción para darte los ingredientes y preparación:  """
opcion = input(menu)

if opcion == "1":
    print("""
8 chiles guajillos, desvenado
3 chiles de árbol
2 dientes de ajo
1/4 cebollas
2 chiles chipotles adobados
2 cucharadas de Aceite De Oliva Extra Especial®
2 cucharadas de mantequilla
1/4 cebollas, finamente picada
2 jitomates, finamente picado
1 pizca de sal Great Value®
1 pizca de pimienta
2 cucharadas de Aceite De Oliva Extra Especial®
4 tazas de camarón mediano, limpio
1/2 cucharaditas de sal Great Value®
1/4 cucharaditas de pimienta
2 cucharadas de cilantro fresco, finamente picado

Preparación:
1-Hierve agua en una ollita a fuego medio. Retira del fuego y remoja los chiles guajillos y los de árbol durante 5 minutos o hasta que se ablanden.
2-Licúa los chiles con el ajo, la cebolla, el chile chipotle y un poco del líquido de remojo de los chiles.
3-En una ollita a fuego medio, calienta la mantequilla y el aceite. Fríe la cebolla hasta que esté transparente y agrega el jitomate. Añade la salsa y cocina alrededor de 10 minutos hasta que espese. Sazona con sal y pimienta.
4-En una sartén profunda a fuego medio, fríe los camarones con el aceite de oliva y sazona con sal y pimienta. Agrega la salsa y mezcla muy bien. Cocina 5 minutos más y termina con cilantro picado.
""")

elif opcion == "2":
    print("""
500 gramos de camarón seco
2 papas blancas, cortada en cubos pequeños
2 zanahorias
4 jitomates
5 chiles guajillos
1/4 cebollas
1 1/2 litros de agua
4 ramas de perejil
3 ramas de epazote
1 diente de ajo
15 gramos de sal
5 gramos de pimienta molida

Preparación:

1-Coloca agua en una olla y lleva a punto de hervor.
2-Licúa los chiles junto con el jitomate, ajo y cebolla. Incorpora un poco del agua.
3-Cuela la salsa y viértela sobre el agua. Cocina por 10 minutos.
4-Agrega camarones secos.
5-Pela las papas. Córtalas en cubos.
6-Pela las zanahorias y córtalas en cubos pequeños.
7-Agrega las papas y zanahorias al caldo.
8-Agrega perejil y epazote. Sazona.
9-Deja que hierva por 5 minutos. Sirve.
    """)
elif opcion == "3":
    print("""
16 Camarones grandes, sin cabeza y limpios.
2 cucharadas de Ajos finamente picado.
300 gr de Queso Chihuahua rallado.
1 Pimiento Verde en juliana.
1 Pimiento Rojo en juliana.
2 tazas de Lechugas variadas.
2 cucharadas de Margarina.
4 piezas de Bollos o Pan para hamburguesa.
1/2 taza de Mayonesa.
1/4 taza de Chile Chipotle molido.
Sal al gusto. 
Pimienta al gusto. 
Papel Aluminio.

Preparación:

1-Funde la margarina, acitrona el ajo ylos camarones. Salpimienta y cocina por 2 minutos. Retira y reserva.
2-Sofríe en la misma sartén los pimientos y regresa al fuego los camarones.
3-Cocina por 5 minutos más y rectifica sazón.
4-Espolvorea el queso y tapa con papel aluminio para que se funda.
5-Dora el pan y unta mayonesa en la base, acomoda las lechugas y coloca encima los camarones.
6-Unta la tapa del pan con chipotle, tapa la hamburguesa y sirve.

Así nomas
    """)
elif opcion =="4":
    print("""
1/2 kg camarón mediano, sin cabeza.
1 cucharada Paprika.
2 cucharadas mantequilla.
4 cucharadas cebollla, finamente picadas.
2 cucharadas ajos, finamente picados.
1 lechuga Francesa.
2 limones en supremas.
1/2 cebolla morada en juliana.
50 grs cacahuates troceados.
Sal y pimienta al gusto.

Preparación:

1-Salpimienta los camarones y mezcla con la paprika. Reserva.
2-Funde la mantequilla, acitrona la cebolla y el ajo.
3-Agrega los camarones y dora. Cocina hasta que se cuezan. Reserva.
4-Mezcla la lechuga, la cebolla morada y las supremas de limón.
5-Coloca en un plato extendido y agrega los camarones.
6-Vierte el aderezo, espolvorea los cacahuates y sirve.
    """)
elif opcion == "5":
    print("""
1/2 kg de Camarón pacotilla, limpio.
2 cucharadas de Aceite de Oliva.
1/2 taza de Jugo de limón.
3 jitomates sin semillas y en cubos.
1/2 Pepino sin semillas y en cubos.
1/2 Cebolla morada picada.
2 Chiles serranos sin semillas y en cubos.
2 cucharadas de Cilantro.
Tostadas chicas.
Sal y pimienta al gusto.

Preparación:

1-Coloca en un tazón los camarones. Vierte el aceite de oliva y el jugo de limón.
2-Añade el jitomate, el pepino, la cebolla morada, el chile serrano, el cilantro.
3-Salpimienta y mezcla. Sirve y acompaña con tostadas.
    """)
else:
    print("Prueba con una opción de la lista" + (menu))