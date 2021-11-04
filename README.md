Mc Dowell’s  

Una hamburguesería, busca automatizar sus pedidos con una aplicación.  

Los contratan para que puedan hacer un pequeño sistema, un programa de consola como los que venimos haciendo en el curso. 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Les cuentan las opciones que tienen. 

Solo 3 combos y un postre: 

Combo Simple (Hamburguesa simple + Bebida + Fritas) costo 650 pesos Combo Doble (Hamburguesa doble + Bebida + Fritas) costo 700 pesos Combo Triple (Hamburguesa Triple + Bebida + Fritas) costo 800 pesos 

Postre : 

Mc Flurby de dulce de leche costo 250 pesos \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

Se busca que se pueda automatizar los pedidos y los cobros, para también dar bien el vuelto.  Luego si se confirma la compra, lograr volcar los datos del cliente / fecha / compra / total, para guardarlas en una planilla Excel. Sin borrar los anteriores registros. 



|Cliente |Fecha |Combo S |Combo D |Combo T |Flurby |Total |
| - | - | - | - | - | - | - |
|Juan |Sat Oct 23 10:18:18 2021 |1 |1 |0 |2 |1850 |
|Tomas |Sat Oct 23 11:18:18 2022 |0 |1 |0 |1 |950 |
|Romina |Sat Oct 23 11:30:18 2023 |0 |0 |0 |2 |500 |
También en el mismo directorio acompañando el Excel , debería de quedar registro de entrada y salida del sistema del operario de caja, acompañando el monto total al cerrar el sistema(se cierra la caja) en un archivo txt . Sin borrar los anteriores accesos.  

Registro.txt : 

IN Sat Oct 23 10:18:18 2021 Encargad@ Gerardo  

OUT Sat Oct 23 11:39:15 2021 Encargad@ Gerardo $3300 ############################################### 

IN Sat Oct 23 11:41:20 2021 Encargad@ Horacio OUT………………………………………………… 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

Ni bien se ingresa al programa nos debería de aparecer el mensaje: (En rojo los ingresos) 

Bienvenido a McDowell´s  

Ingrese su nombre encargad@ : Gerardo                                                        

Luego una vez que se ingresa correctamente el nombre, pasar al menú : 

McDowell´s 

Recuerda que siempre hay que recibir al cliente con una sonrisa :) 

1 – Ingreso de nuevo pedido 2 – Cambio de turno 

3 – Apagar sistema 

Si el encargado elige la opción 1, pasamos a empezar a pedir los ítems: 

Ingrese cantidad Combo S : 1 Ingrese cantidad Combo D: 1 Ingrese cantidad Combo T: 0 Ingrese cantidad Flurby: 2 

Total $1850 

Abona con $ 2000   Vuelto $ 150 

Si el encargado elige la opción 2, ponemos la pantalla siguiente: 

Bienvenido a McDowell´s  

Ingrese su nombre encargad@ : Horacio        

Y luego el menú nuevamente. Por supuesto registrar los cambios en los archivos como ya mencionamos.                                                                                 

Si el encargado elige la opción 3, cerramos el programa. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

El programa no debe de detenerse a causa de errores, Uds. los tienen que contemplar. Usar las herramientas vistas en el curso para limpiar la pantalla y hacer un menú bastante intuitivo, fácil de usar.  