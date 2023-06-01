from tkinter import *


BASE = 460
ALTURA = 460


ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")



frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="orange", width=480, height=480)
frame_graficacion.place(x=10, y=10)
 

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)


parachoques_1=c.create_oval(BASE/2-35,ALTURA/2+10,BASE/2-115,ALTURA/2+90,fill="blue", outline="")
parachoques_2=c.create_rectangle(BASE/2-95,ALTURA/2-5,BASE/2-85,ALTURA/2+105,fill="orange2", outline="")
parachoques_3=c.create_rectangle(BASE/2-85,ALTURA/2+5,BASE/2-75,ALTURA/2+95,fill="blue", outline="")
cuerpo_del_tren = c.create_rectangle(BASE/2-75,ALTURA/2+100,BASE/2+150,ALTURA/2,fill="orange3",outline="")
ventana = c.create_rectangle(BASE/2+20,ALTURA/2+0,BASE/2+140,ALTURA/2-80,fill="yellow2",outline="")
ventana_pequeña= c.create_rectangle(BASE/2+30,ALTURA/2-10,BASE/2+130,ALTURA/2-70,fill="green", outline="")
sobre_ventana= c.create_rectangle(BASE/2,ALTURA/2-80,BASE/2+160,ALTURA/2-95,fill="pink", outline="")
sobre_sobre_ventana= c.create_rectangle(BASE/2+20,ALTURA/2-95,BASE/2+140,ALTURA/2-105,fill="orange", outline="")
base_chimenea=c.create_rectangle(BASE/2-50,ALTURA/2,BASE/2-20,ALTURA/2-40,fill="orange2", outline="")
base_base_chimenea=c.create_rectangle(BASE/2-60,ALTURA/2-40,BASE/2-10,ALTURA/2-60,fill="blue", outline="")
rueda_1=c.create_oval( BASE/2-75,ALTURA/2+70,BASE/2-10,ALTURA/2+130,fill="green2", outline="")
rueda_2=c.create_oval( BASE/2,ALTURA/2+70,BASE/2+65,ALTURA/2+130,fill="white", outline="")
rueda_3=c.create_oval( BASE/2+75,ALTURA/2+70,BASE/2+140,ALTURA/2+130,fill="white", outline="")
unidor_1=c.create_rectangle(BASE/2-45,ALTURA/2+90,BASE/2+15,ALTURA/2+110,fill="blue2", outline="")
unidor_2=c.create_rectangle(BASE/2+45,ALTURA/2+90,BASE/2+105,ALTURA/2+110,fill="gray", outline="")
nombre_ñero = c.create_text(BASE/2+30,ALTURA/2+40, text="paul sebastian colmenares", font=10)
circulo_ventana=c.create_oval(BASE/2+40,ALTURA/2-10,BASE/2+120,ALTURA/2-70,fill="yellow2", outline="")
hojo_izquierdo=c.create_oval(BASE/2+50,ALTURA/2-60,BASE/2+80,ALTURA/2-40,fill="green", outline="")
hojo_izquierdo_pupila=c.create_oval(BASE/2+60,ALTURA/2-55,BASE/2+70,ALTURA/2-45,fill="red2", outline="")
hojo_derecho=c.create_oval(BASE/2+80,ALTURA/2-60,BASE/2+110,ALTURA/2-40,fill="yellow2", outline="")
hojo_derecho_pupila=c.create_oval(BASE/2+90,ALTURA/2-55,BASE/2+100,ALTURA/2-45,fill="blue", outline="")
boca=c.create_oval(BASE/2+65,ALTURA/2-30,BASE/2+95,ALTURA/2-15,fill="red", outline="")


frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=10, height=10)
frame_controles.place(x=10, y=10)


ventana_principal.mainloop()