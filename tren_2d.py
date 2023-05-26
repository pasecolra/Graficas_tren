from tkinter import*

base = 480
altura = 480

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("520x520")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

c= Canvas(ventana_principal, width=base, height=altura)
c.config(bg="white")
c.place(x=20,y=20)

cuerpo=c.create_rectangle(base/2-60,base/2+210,430,altura-180, fill="grey")
cuerpo2=c.create_rectangle(base/2+30,base/2-60,410,altura-180, fill="grey")
dentro_cuerpo_2=c.create_rectangle()


ventana_principal.mainloop()