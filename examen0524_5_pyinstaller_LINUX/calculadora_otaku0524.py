import tkinter as tk

# la variable calc la uso para ir moviendo los numeros que introduzco
calc = 0
operandos = []


# cuadro_texto.get() me recoje lo que tengo en la entrada del cuadro de texto
# y con eval evaluo esa expresion
def entrada_teclado(pulsado):
    global calc
    if pulsado == "=":
        solucion = cuadro_texto.get()
        tmp = pulsado
        print(f"este es el valor que hemos pulsado {tmp}\n")
        operandos.append(tmp)
        cuadro_texto.insert(calc, str(pulsado))
        print(f"este es el valor de solucion {solucion}")
        res_solucion = eval(solucion)
        print(f"este es el valor de solucion {res_solucion}")
        cuadro_texto.delete(0, tk.END)
        cuadro_texto.insert(0, str(res_solucion))
    else:
        tmp = pulsado
        print(f"este es el valor que hemos pulsado {tmp}\n")
        operandos.append(tmp)
        cuadro_texto.insert(calc, str(pulsado))
        calc += 1
        print(f"este es el contendido de operandos {operandos}\n")

"""
operandos = resultado.get()
resultados_op = eval(operandos)
resultado.delete(0, tk.END)
resultado.insert(0, str(resultados_op))
"""

# resultado = eval(f"{num1} {operacion} {num2}")


def borramiento():
    cuadro_texto.delete(0, tk.END)
    calc = 0


# creo la ventana
ventana = tk.Tk()
ventana.title("CALCULEITOR")

favicon = tk.PhotoImage(file="imagenes/otaku.png")
ventana.iconphoto(True, favicon)

cuadro_texto = tk.Entry(ventana, bg="white")
cuadro_texto.grid(row=0, column=1, columnspan=4)

# NUMEROS DE LA CALCULADORA
uno = tk.Button(ventana, text="1", command=lambda: entrada_teclado("1"))
uno.grid(row=2, column=1)
dos = tk.Button(ventana, text="2", command=lambda: entrada_teclado("2"))
dos.grid(row=2, column=2)
tres = tk.Button(ventana, text="3", command=lambda: entrada_teclado("3"))
tres.grid(row=2, column=3)

cuatro = tk.Button(ventana, text="4", command=lambda: entrada_teclado("4"))
cuatro.grid(row=3, column=1)
cinco = tk.Button(ventana, text="5", command=lambda: entrada_teclado("5"))
cinco.grid(row=3, column=2)
seis = tk.Button(ventana, text="6", command=lambda: entrada_teclado("6"))
seis.grid(row=3, column=3)

siete = tk.Button(ventana, text="7", command=lambda: entrada_teclado("7"))
siete.grid(row=4, column=1)
ocho = tk.Button(ventana, text="8", command=lambda: entrada_teclado("8"))
ocho.grid(row=4, column=2)
nueve = tk.Button(ventana, text="9", command=lambda: entrada_teclado("9"))
nueve.grid(row=4, column=3)

cero = tk.Button(ventana, text="0", command=lambda: entrada_teclado("0"))
cero.grid(row=5, column=1)

# SOLO SE PUEDE USAR PACK Y GRID AL MISMO TIEMPO SI ESTAN A DISTINTO NIVEL
clear = tk.Button(ventana, text="C", command=borramiento)
clear.grid(row=1, column=1)

abrir = tk.Button(ventana, text="(", command=lambda: entrada_teclado("("))
abrir.grid(row=1, column=3)

cerrar = tk.Button(ventana, text=")", command=lambda: entrada_teclado(")"))
cerrar.grid(row=1, column=4)

sumatorio = tk.Button(ventana, text="+", command=lambda: entrada_teclado("+"))
sumatorio.grid(row=2, column=4)

punto = tk.Button(ventana, text=".", command=lambda: entrada_teclado("."))
punto.grid(row=5, column=2)

igual = tk.Button(ventana, text="=", command=lambda: entrada_teclado("="))
igual.grid(row=5, column=3)

diferencia = tk.Button(ventana, text="-", command=lambda: entrada_teclado("-"))
diferencia.grid(row=3, column=4)

producto = tk.Button(ventana, text="*", command=lambda: entrada_teclado("*"))
producto.grid(row=4, column=4)

cociente = tk.Button(ventana, text="/", command=lambda: entrada_teclado("/"))
cociente.grid(row=5, column=4)

ventana.mainloop()
