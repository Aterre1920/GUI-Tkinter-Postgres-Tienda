import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox as MessageBox
import wikipedia
from control import *

class Supervisor():
    
    def __init__(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
     
    def actualizar_cantidad(self,producto,cantidad):
        try:
            update_cantidad(producto,cantidad)
            MessageBox.showinfo("", f"Cantidad de {producto} actualizada correctamente")
        except:
            MessageBox.showerror("", "Datos inválidos")
    
    def actualizar_precio(self,producto,precio):
        try:
            update_precio(producto,precio)
            MessageBox.showinfo("", f"Precio de {producto} actualizada correctamente")
        except:
            MessageBox.showerror("", "Datos inválidos")
        
    def agregar_vendedores(self,vendedor,contraseña,venta,comision):
        add_vendedores(vendedor,contraseña,venta,comision)
     
    def eliminar_vendedores(self,vendedor):
        try:
            delete_vendedores(vendedor)
            MessageBox.showinfo("", f"{vendedor} eliminado correctamente")
        except:
            MessageBox.showerror("", "Dato inválido")
        
class Vendedor():
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        vendedores.append([self.nombre,self.contra])
    
wikipedia.set_lang("es") #configuración de idioma en wikipedia

SUPER = Supervisor("SUPER1","jefe")
headers = ["PRODUCTOS","CANTIDAD","PRECIO UNITARIO"]

vendedores = extraer_vendedor()
try:
    Crear_tablas()
    add_vendedores('JOSE','1234',0,0)
    vendedores = extraer_vendedor()
    insert_productos('Arduino UNO',30,30.0)
    insert_productos('Capacitor',150,1.5)
    insert_productos('LDR',150,3.0)
    insert_productos('LED',500,0.2)
    insert_productos('Potenciometro',350,1.0)
    insert_productos('Resistor',200,0.5)
    insert_productos('Servomotor',50,25.0)
    insert_productos('Transistor',250,5.0)
    insert_productos('Triac',100,2.5)
except:
    print("Operaciones realizadas con anterioridad")

def Tabla(ps1):
    inventario = visualizar_productos()
    espacio = tk.Label(ps1,text="   ").grid(row=2,column=1)

    tee = tk.Label(ps1,text="INVENTARIO:",font=("Baskerville Old Face",13)).grid(row=2,column=2)
            
    for i in range(3):
        b = tk.Entry(ps1)
        b.insert(0,headers[i])
        b.config(state="disabled")
        b.grid(row=3 ,column= i+2)
    
    for i in range(9):
        b = tk.Entry(ps1)
        b.insert(0,inventario[i][0])
        b.config(state="readonly")
        b.grid(row=i+4 ,column= 2)
    
    for i in range(9):
        b = tk.Entry(ps1)
        b.insert(0,inventario[i][1])
        b.config(state="readonly")
        b.grid(row=i+4 ,column= 3)
    
    for i in range(9):
        b = tk.Entry(ps1)
        b.insert(0,inventario[i][2])
        b.config(state="readonly")
        b.grid(row=i+4 ,column= 4)
        
    return inventario

def Log_sup():
    def Super():
        if ((Us2.get() == SUPER.usuario) and (Con2.get() == SUPER.contraseña)):
            
            Login_sup.destroy()
            
            Super = tk.Toplevel()
            Super.title("Interfaz Supervisor")
            Super.geometry("400x290")
            Super.resizable(False,False)
            
            panel1 = ttk.Notebook(Super)
            panel1.pack(fill = 'both', expand = 'yes')
            
            ps1 = ttk.Frame(panel1)
            ps2 = ttk.Frame(panel1)
            ps3 = ttk.Frame(panel1)
            
            #PESTAÑA VISUALIZAR
            Tabla(ps1)
            def Table():
                Tabla(ps1)
            act = tk.Button(ps1,width=10,height=1,bg = "blue", text = "ACTUALIZAR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command = Table)
            act.grid(row=15,column=3)
            
            #PESTAÑA ACTUALIZAR PRODUCTOS
            def actu_cant():
                producto = prod_e.get()
                cantidad = cant_e.get()
                prod_e.delete(0,'end')
                cant_e.delete(0,'end')
                SUPER.actualizar_cantidad(producto,cantidad)
                
            frame1 = tk.LabelFrame(ps2,text="Actualizar cantidades de productos:")
            frame1.grid(row=1,column=1, columnspan=2, padx=100, pady=10)
            prod_l = tk.Label(frame1,text="Producto:")
            prod_l.grid(row=1,column=1)
            prod_e = tk.Entry(frame1,state='normal',width=15)
            prod_e.grid(row=1,column=2)
            cant_l = tk.Label(frame1,text="Nueva Cantidad:")
            cant_l.grid(row=3,column=1)
            cant_e = tk.Entry(frame1,state='normal',width=15)
            cant_e.grid(row=3,column=2)
            cant_b = tk.Button(frame1,width = 10, height = 1, bg = "blue", text = "ACTUALIZAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=actu_cant)
            cant_b.grid(row=4,column=2)
            
            def actu_prec():
                producto = produ_e.get()
                precio = prec_e.get()
                produ_e.delete(0,'end')
                prec_e.delete(0,'end')
                SUPER.actualizar_precio(producto,precio)
            
            frame2 = tk.LabelFrame(ps2,text="Actualizar precios de productos:")
            frame2.grid(row=2,column=1,columnspan=2, padx=100, pady=30)
            produ_l = tk.Label(frame2,text="Producto:")
            produ_l.grid(row=1,column=1)
            produ_e = tk.Entry(frame2,state='normal',width=15)
            produ_e.grid(row=1,column=2)
            prec_l = tk.Label(frame2,text="Nuevo Precio:")
            prec_l.grid(row=3,column=1)
            prec_e = tk.Entry(frame2,state='normal',width=15)
            prec_e.grid(row=3,column=2)
            prec_b = tk.Button(frame2,width = 10, height = 1, bg = "blue", text = "ACTUALIZAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=actu_prec)
            prec_b.grid(row=4,column=2)
            
            #PESTAÑA ACTUALIZAR VENDEDORES
            def agre_vend():
                try:
                    nombre = nomb_e.get()
                    contra = contr_e.get()
                    a = len(nombre)
                    b = len(contra)
                    c=(1/a)+(1/b)
                    nomb_e.delete(0,'end')
                    contr_e.delete(0,'end')
                    SUPER.agregar_vendedores(nombre,contra,0,0)
                    nombre1 = Vendedor(nombre,contra)
                    MessageBox.showinfo("", f"{nombre} agregado correctamente")
                except:
                    MessageBox.showerror("", "Datos inválidos")
                
            frame3 = tk.LabelFrame(ps3,text="Agregar vendedor:")
            frame3.grid(row=1,column=1, columnspan=2, padx=100, pady=10)
            nomb_l = tk.Label(frame3,text="Nombre:")
            nomb_l.grid(row=1,column=1)
            nomb_e = tk.Entry(frame3,state='normal',width=15)
            nomb_e.grid(row=1,column=2)
            contr_l = tk.Label(frame3,text="Contraseña:")
            contr_l.grid(row=3,column=1)
            contr_e = tk.Entry(frame3,state='normal',width=15,show='*')
            contr_e.grid(row=3,column=2)
            agre_b = tk.Button(frame3,width = 8, height = 1, bg = "blue", text = "AGREGAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=agre_vend)
            agre_b.grid(row=4,column=2)
            
            def elim_vend():
                nombre = nombre_e.get()
                nombre_e.delete(0,'end')
                SUPER.eliminar_vendedores(nombre)
            
            frame4 = tk.LabelFrame(ps3,text="Eliminar vendedor:")
            frame4.grid(row=2,column=1,columnspan=2, padx=100, pady=30)
            nombre_l = tk.Label(frame4,text="Nombre:")
            nombre_l.grid(row=1,column=1)
            nombre_e = tk.Entry(frame4,state='normal',width=15)
            nombre_e.grid(row=1,column=2)
            elim_b = tk.Button(frame4,width = 9, height = 1, bg = "#DE433A", text = "ELIMINAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=elim_vend)
            elim_b.grid(row=4,column=2)
            
            panel1.add(ps1, text = "Visualizar Inventario")
            panel1.add(ps2, text = "Actualizar Productos")
            panel1.add(ps3, text = "Agregar/Eliminar Vendedores")
            
            # Super.mainloop()
            
        else:
            MessageBox.showerror("ERROR AL LOGEAR", "Usuario y/o contraseña inválidos")
    
    #Login Supervisor

    Login_sup = tk.Toplevel()
    Login_sup.title("LOGIN")
    Login_sup.geometry("230x150")
    Login_sup.resizable(False,False)
    
    Ind = tk.Label(Login_sup,text = "Introduzca usuario y contraseña...", font = ("Times New Roman",11), fg = "black")
    Ind.place(x = 15, y = 10)
    Us1 = tk.Label(Login_sup,text = "USUARIO",font = ("Times New Roman",11), fg = "black")
    Us1.place(x = 20, y = 40)
    Us2 = tk.Entry(Login_sup, state = 'normal', width = 12)
    Us2.place(x = 140, y = 40)
    Con1 = tk.Label(Login_sup,text = "CONTRASEÑA",font = ("Times New Roman",11), fg = "black")
    Con1.place(x = 20, y = 70)
    Con2 = tk.Entry(Login_sup, show ='*', state = 'normal', width = 12)
    Con2.place(x = 140, y = 70)
    Ingresar = tk.Button(Login_sup, width = 8, height = 1, bg = "blue", text = "INGRESAR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command = Super)
    Ingresar.place(x = 75, y = 105)
    # Login_sup.mainloop()
    
    
def Log_ven():
    
    def Vende():
        for i in range(len(vendedores)):
            if ((Us22.get() == vendedores[i][0]) and (Con22.get() == vendedores[i][1])):
                
                vendedor_a = Us22.get()
                print(vendedor_a)
                
                Login_ven.destroy()
                
                Vended = tk.Toplevel()
                Vended.title("Interfaz Vendedor")
                Vended.geometry("498x340")
                Vended.resizable(False,False)
                
                indi3 = tk.Label(Vended,text='Rellene las casillas con el número de productos a comprar, \n sino comprara alguno rellenar con cero (0)')
                indi3.grid(row=1,column=1,columnspan=6)
                
                Tabla(Vended)
                
                for i in range(9):
                    a = tk.Label(Vended,text='   ')
                    a.grid(row=i+4,column=5)
                
                prod1_e = tk.Entry(Vended,state='normal',width=4)
                prod1_e.grid(row=4,column=6)
                prod2_e = tk.Entry(Vended,state='normal',width=4)
                prod2_e.grid(row=5,column=6)
                prod3_e = tk.Entry(Vended,state='normal',width=4)
                prod3_e.grid(row=6,column=6)
                prod4_e = tk.Entry(Vended,state='normal',width=4)
                prod4_e.grid(row=7,column=6)
                prod5_e = tk.Entry(Vended,state='normal',width=4)
                prod5_e.grid(row=8,column=6)
                prod6_e = tk.Entry(Vended,state='normal',width=4)
                prod6_e.grid(row=9,column=6)
                prod7_e = tk.Entry(Vended,state='normal',width=4)
                prod7_e.grid(row=10,column=6)
                prod8_e = tk.Entry(Vended,state='normal',width=4)
                prod8_e.grid(row=11,column=6)
                prod9_e = tk.Entry(Vended,state='normal',width=4)
                prod9_e.grid(row=12,column=6)
                
                def Limpiar():
                    prod1_e.delete(0,'end')
                    prod2_e.delete(0,'end')
                    prod3_e.delete(0,'end')
                    prod4_e.delete(0,'end')
                    prod5_e.delete(0,'end')
                    prod6_e.delete(0,'end')
                    prod7_e.delete(0,'end')
                    prod8_e.delete(0,'end')
                    prod9_e.delete(0,'end')
                    prod1_e.insert(0,0)
                    prod2_e.insert(0,0)
                    prod3_e.insert(0,0)
                    prod4_e.insert(0,0)
                    prod5_e.insert(0,0)
                    prod6_e.insert(0,0)
                    prod7_e.insert(0,0)
                    prod8_e.insert(0,0)
                    prod9_e.insert(0,0)
                    
                def Boleta():
                    #Extraccion de entrys
                    cant1 = int(prod1_e.get())
                    cant2 = int(prod2_e.get())
                    cant3 = int(prod3_e.get())
                    cant4 = int(prod4_e.get())
                    cant5 = int(prod5_e.get())
                    cant6 = int(prod6_e.get())
                    cant7 = int(prod7_e.get())
                    cant8 = int(prod8_e.get())
                    cant9 = int(prod9_e.get())
                    #lista de cantidades
                    cant_list=[]
                    cant_list.append(cant1)
                    cant_list.append(cant2)
                    cant_list.append(cant3)
                    cant_list.append(cant4)
                    cant_list.append(cant5)
                    cant_list.append(cant6)
                    cant_list.append(cant7)
                    cant_list.append(cant8)
                    cant_list.append(cant9)
                    #Limpieza de entrys
                    Limpiar()
                    #llamado de inventario
                    inventario = visualizar_productos()
                    #separando nombres de productos
                    prod1_n=inventario[0][0] 
                    prod2_n=inventario[1][0]
                    prod3_n=inventario[2][0]
                    prod4_n=inventario[3][0]
                    prod5_n=inventario[4][0]
                    prod6_n=inventario[5][0]
                    prod7_n=inventario[6][0]
                    prod8_n=inventario[7][0]
                    prod9_n=inventario[8][0]
                    #calculando cantidad restante de productos
                    cant_n1=(inventario[0][1])-cant1
                    cant_n2=(inventario[1][1])-cant2
                    cant_n3=(inventario[2][1])-cant3
                    cant_n4=(inventario[3][1])-cant4
                    cant_n5=(inventario[4][1])-cant5
                    cant_n6=(inventario[5][1])-cant6
                    cant_n7=(inventario[6][1])-cant7
                    cant_n8=(inventario[7][1])-cant8
                    cant_n9=(inventario[8][1])-cant9
                    #if detector de si se queda sin productos:
                    if (cant_n1 < 0) or (cant_n2 < 0) or (cant_n3 < 0) or (cant_n4 < 0) or (cant_n5 < 0) or (cant_n6 < 0) or (cant_n7 < 0) or (cant_n8 < 0) or (cant_n9 < 0):
                        MessageBox.showerror("","Cantidad no válida")
                    else:
                        #actualizando datos en postgres
                        update_cantidad(prod1_n, cant_n1)
                        update_cantidad(prod2_n, cant_n2)
                        update_cantidad(prod3_n, cant_n3)
                        update_cantidad(prod4_n, cant_n4)
                        update_cantidad(prod5_n, cant_n5)
                        update_cantidad(prod6_n, cant_n6)
                        update_cantidad(prod7_n, cant_n7)
                        update_cantidad(prod8_n, cant_n8)
                        update_cantidad(prod9_n, cant_n9)
                        #actualizando tabla
                        Tabla(Vended)
                        #precios
                        pre1 = (inventario[0][2])*cant1
                        pre2 = (inventario[1][2])*cant2
                        pre3 = (inventario[2][2])*cant3
                        pre4 = (inventario[3][2])*cant4
                        pre5 = (inventario[4][2])*cant5
                        pre6 = (inventario[5][2])*cant6
                        pre7 = (inventario[6][2])*cant7
                        pre8 = (inventario[7][2])*cant8
                        pre9 = (inventario[8][2])*cant9
                        #lista de precios
                        prec_list=[]
                        prec_list.append(pre1)
                        prec_list.append(pre2)
                        prec_list.append(pre3)
                        prec_list.append(pre4)
                        prec_list.append(pre5)
                        prec_list.append(pre6)
                        prec_list.append(pre7)
                        prec_list.append(pre8)
                        prec_list.append(pre9)
                        #subtotal
                        subtotal = float(sum(prec_list))
                        #igv
                        igv = 0.18*subtotal
                        #total
                        total = subtotal + igv
                        #lista de totales
                        totales_list=[]
                        totales_list.append(subtotal)
                        totales_list.append(igv)
                        totales_list.append(total)
                        #comision (25%)
                        comision = 0.25*total
                        #extrayendo montos guardados del vendedor
                        montos = extraer_ventaycomision(vendedor_a)
                        venta_nueva = float(montos[0]) + total
                        comision_nueva = float(montos[1]) + comision
                        #actualizando venta y comision del vendedor
                        update_ventaycomision(vendedor_a, venta_nueva,comision_nueva)
                        #ventana de boleta
                        resumen = tk.Toplevel()
                        resumen.title("RESUMEN DE COMPRA")
                        resumen.geometry("520x400")
                        resumen.resizable(False,False)
                        
                        headers1 = ['Cantidad','Producto','Precio Unit.','Importe']
                        totales = ['SUBTOTAL','IGV (18%)','TOTAL']
                        
                        espacion = tk.Label(resumen,text="  ").grid(row=2,column=1)
                        
                        titulo = tk.Label(resumen,text="ATERRE ELECTRONICS S.A.C.",font=("Castellar",15)).grid(row=2,column=2,columnspan=5)
                        res = tk.Label(resumen,text="RESUMEN:",font=("Times New Roman",12)).grid(row=3,column=2)
                        
                        for i in range(4):
                            b = tk.Entry(resumen)
                            b.insert(0,headers1[i])
                            b.config(state="disabled")
                            b.grid(row=4 ,column= i+2)
                            
                        for i in range(9):
                            b = tk.Entry(resumen)
                            b.insert(0,cant_list[i])
                            b.config(state="readonly")
                            b.grid(row=i+5 ,column= 2)
                            
                        for i in range(9):
                            b = tk.Entry(resumen)
                            b.insert(0,inventario[i][0])
                            b.config(state="readonly")
                            b.grid(row=i+5 ,column= 3)
                            
                        for i in range(9):
                            b = tk.Entry(resumen)
                            b.insert(0,inventario[i][2])
                            b.config(state="readonly")
                            b.grid(row=i+5 ,column= 4)
                            
                        for i in range(9):
                            b = tk.Entry(resumen)
                            b.insert(0,prec_list[i])
                            b.config(state="readonly")
                            b.grid(row=i+5 ,column= 5)
                            
                        espacio1 = tk.Label(resumen,text="  ").grid(row=15,column=1)
                    
                        for i in range(3):
                            b = tk.Entry(resumen)
                            b.insert(0,totales[i])
                            b.config(state='disabled')
                            b.grid(row=i+17,column=4)

                        for i in range(3):
                            b = tk.Entry(resumen)
                            b.insert(0,totales_list[i])
                            b.config(state="readonly")
                            b.grid(row=i+17 ,column= 5)

                        espacio2 = tk.Label(resumen,text="  ").grid(row=20,column=1)

                        volver = tk.Button(resumen, width = 8, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "ACEPTAR", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=resumen.destroy)
                        volver.grid(row=21,column=4,columnspan=2)
                    
                    
                
                esp=tk.Label(Vended,text=' ').grid(row=13,column=1)
                
                boleta_b = tk.Button(Vended,width = 8, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "COMPRAR", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3,command=Boleta) 
                boleta_b.grid(row=14,column=6)
                limpiar_b = tk.Button(Vended,width = 8, height = 1, bg = "#DE433A", fg = "#FFFFFF", text = "LIMPIAR", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3,command=Limpiar) 
                limpiar_b.grid(row=14,column=4)
                
                break
                # Vended.mainloop()
            
        else:
            MessageBox.showerror("ERROR AL LOGEAR", "Usuario y/o contraseña inválidos")

    #Login Vendedor

    Login_ven = tk.Toplevel()
    Login_ven.title("LOGIN")
    Login_ven.geometry("230x150") 
    Login_ven.resizable(False,False)
    
    Ind = tk.Label(Login_ven,text = "Introduzca usuario y contraseña...", font = ("Times New Roman",11), fg = "black")
    Ind.place(x = 15, y = 10)
    Us11 = tk.Label(Login_ven,text = "USUARIO",font = ("Times New Roman",11), fg = "black")
    Us11.place(x = 20, y = 40)
    Us22 = tk.Entry(Login_ven, state = 'normal', width = 12)
    Us22.place(x = 140, y = 40)
    Con11 = tk.Label(Login_ven,text = "CONTRASEÑA",font = ("Times New Roman",11), fg = "black")
    Con11.place(x = 20, y = 70)
    Con22 = tk.Entry(Login_ven, show ='*', state = 'normal', width = 12)
    Con22.place(x = 140, y = 70)
    Ingresar1 = tk.Button(Login_ven, width = 8, height = 1, bg = "blue", text = "INGRESAR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command = Vende)
    Ingresar1.place(x = 75, y = 105)
    # Login_ven.mainloop()
    
def Ven_Cli():
    
    def info1():
        busqueda = wikipedia.summary('led', sentences = 2 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - LED', busqueda)
        
    def info2():
        busqueda = wikipedia.summary('resistor', sentences = 4 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - RESISTOR', busqueda)
    
    def info3():
        busqueda = wikipedia.summary('potenciometro', sentences = 2 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - POTENCIOMETRO', busqueda)
    
    def info4():
        busqueda = wikipedia.summary('capacitor', sentences = 1 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - CAPACITOR', busqueda)
    
    def info5():
        busqueda = wikipedia.summary('triac', sentences = 3 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - TRIAC', busqueda)
        
    def info6():
        busqueda = wikipedia.summary('transistor', sentences = 3 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - TRANSISTOR', busqueda)
        
    def info7():
        busqueda = wikipedia.summary('servomotor', sentences = 1 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - SERVOMOTOR', busqueda)
    
    def info8():
        busqueda = wikipedia.summary('ldr', sentences = 2 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - LDR', busqueda)
    
    def info9():
        busqueda = wikipedia.summary('arduino uno', sentences = 2 , chars = 0 , auto_suggest = True , redirect = False) 
        MessageBox.showinfo('Información - ARDUINO UNO', busqueda)
    
    vent_cliente = tk.Toplevel()
    vent_cliente.title("Interfaz Cliente")
    vent_cliente.geometry('823x480')
    vent_cliente.resizable(False,False)
    
    titulocliente = tk.Label(vent_cliente, text = "PRODUCTOS", font = ("Castellar",45), fg = "black")
    titulocliente.place(x = 195, y = 2)
    
    led1 = PhotoImage(file="led.png",).subsample(2)
    led2 = tk.Label(vent_cliente,image=led1)
    led2.image = led1
    led2.place(x=5,y=75)
    led_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info1)
    led_boton.place(x=55,y=230)
    
    res1 = PhotoImage(file="res.png",).subsample(2)
    res2 = tk.Label(vent_cliente,image=res1)
    res2.image = res1
    res2.place(x=170,y=75)
    res_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info2)
    res_boton.place(x=220,y=230)
    
    pot1 = PhotoImage(file="pot.png",).subsample(2)
    pot2 = tk.Label(vent_cliente,image=pot1)
    pot2.image = pot1
    pot2.place(x=335,y=75)
    pot_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info3)
    pot_boton.place(x=385,y=230)
    
    cap1 = PhotoImage(file="cap.png",).subsample(2)
    cap2 = tk.Label(vent_cliente,image=cap1)
    cap2.image = cap1
    cap2.place(x=500,y=75)
    cap_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info4)
    cap_boton.place(x=550,y=230)
    
    triac1 = PhotoImage(file="triac.png",).subsample(2)
    triac2 = tk.Label(vent_cliente,image=triac1)
    triac2.image = triac1
    triac2.place(x=665,y=75)
    triac_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info5)
    triac_boton.place(x=715,y=230)
    
    tran1 = PhotoImage(file="tran.png",).subsample(2)
    tran2 = tk.Label(vent_cliente,image=tran1)
    tran2.image = tran1
    tran2.place(x=88,y=275)
    tran_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info6)
    tran_boton.place(x=138,y=430)
    
    servo1 = PhotoImage(file="servo.png",).subsample(2)
    servo2 = tk.Label(vent_cliente,image=servo1)
    servo2.image = servo1
    servo2.place(x=253,y=275)
    servo_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info7)
    servo_boton.place(x=303,y=430)
    
    ldr1 = PhotoImage(file="ldr.png",).subsample(2)
    ldr2 = tk.Label(vent_cliente,image=ldr1)
    ldr2.image = ldr1
    ldr2.place(x=418,y=275)
    ldr_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info8)
    ldr_boton.place(x=468,y=430)
    
    ard1 = PhotoImage(file="ard.png",).subsample(2)
    ard2 = tk.Label(vent_cliente,image=ard1)
    ard2.image = ldr1
    ard2.place(x=583,y=275)
    ard_boton = tk.Button(vent_cliente, width = 5, height = 1, bg = "#2DA430", fg = "#FFFFFF", text = "INFO", font = ("Berlin Sans FB Demi", 12, "bold"), borderwidth = 2.3, command=info9)
    ard_boton.place(x=633,y=430)
    
    vent_cliente.mainloop()


#Ventana Principal

ventana1 = tk.Tk()
ventana1.title("ATERRE ELECTRONICS S.A.C.")
ventana1.geometry("540x420")
ventana1.resizable(False,False)

Titulo = tk.Label(text = "BIENVENIDO A \n ATERRE ELECTRONICS S.A.C.", font = ("Broadway",25), fg = "black")
Titulo.place(x = 7, y = 20)
Ind = tk.Label(text = "Presione el botón que indique su rol/cargo:", font = ("Times New Roman",15), fg = "blue")
Ind.place(x = 15, y = 120)
Rol1 = tk.Button(ventana1, width = 11, height = 2, bg = "#05C967", text = "SUPERVISOR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command=Log_sup)
Rol1.place(x = 200, y = 160)
Rol2 = tk.Button(ventana1, width = 11, height = 2, bg = "#05C967", text = "VENDEDOR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command=Log_ven)
Rol2.place(x = 200, y = 225)
Rol3 = tk.Button(ventana1, width = 11, height = 2, bg = "#05C967", text = "CLIENTE", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command=Ven_Cli)
Rol3.place(x = 200, y = 290)
Salir = tk.Button(ventana1, width = 11, height = 2, bg = "#DE433A", text = "SALIR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command=ventana1.destroy )
Salir.place(x = 390, y = 350)
Cred = tk.Label(text = "by Anthony Terrones \n UNT - Ing. Mecatrónica", font = ("Times New Roman",10), fg = "black")
Cred.place(x = 10, y = 380)


ventana1.mainloop()