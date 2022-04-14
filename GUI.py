import tkinter
#ventana
ventana = tkinter.Tk()
ventana.title("Contador")
ventana.geometry("400x300")#definimos el tamaño de la ventana
#funciones
def suma():
    valor = int(contador["text"])
    contador["text"] = f"{valor + 1}"
    valor = int(contador["text"])
    changeColor(valor)
def resta():
    valor = int(contador["text"])
    contador["text"] = f"{valor - 1}"
    valor = int(contador["text"])
    changeColor(valor)
def reiniciar():
    valor = int(contador["text"])
    contador["text"] = f"{valor * 0}"
    valor = int(contador["text"])
    changeColor(valor)
def changeColor(valor):
    if int(valor) < 0:
        contador.config(fg = "red")
    elif int(valor) == 0:
        contador.config(fg = "black")
    elif int(valor) > 0:
        contador.config(fg = "green")
#Contador
bsumar = tkinter.Button(ventana, text = "Sumar", bg="green", font= "Helvetica 10", width=10, height=2, command=suma)
bsumar.place(x=40, y=200)
brestar = tkinter.Button(ventana, text = "Restar", bg="red", font= "Helvetica 10", width=10, height=2, command=resta)
brestar.place(x=150, y=200)
breset = tkinter.Button(ventana, text = "Reiniciar", bg="gray", font= "Helvetica 10", width=10, height=2, command=reiniciar)
breset.place(x=260, y=200 )
Coun = tkinter.Label(ventana, text = "Contador", font="cambria 35")
Coun.place(x=110, y=20)
contador = tkinter.Label(ventana, text = "0", font="cambria 30")
contador.place(x=190, y=100)
ventana.mainloop() 

