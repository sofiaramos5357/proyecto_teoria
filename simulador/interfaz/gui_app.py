import tkinter as tk
from PIL import Image, ImageTk 
from interfaz.grafico import generar_grafico_pert
from tkinter import ttk
import numpy as np

datoActividades = {}
actividad=0

def abrir_ventana_ayuda():
    ventana_ayuda = tk.Toplevel()
    ventana_ayuda.title("Ayuda")
    ventana_ayuda.geometry("800x600")
    ventana_ayuda.configure(bg='white') 

    titulo_ayuda = tk.Label(ventana_ayuda,
                            text="Descripción del Modelo:",
                            bg="white",
                            fg="black",
                            font=("Helvetica", 16),
                            anchor="w")
    titulo_ayuda.pack(pady=5,  padx=20, anchor="w")

    instrucciones_text = """SIMU-PERT es una herramienta diseñada para estimar la duración de proyectos mediante el método 
PERT (Program Evaluation and Review Technique). Este método considera la incertidumbre inherente
en las estimaciones de tiempo de las actividades del proyecto. A continuación, te explicamos cómo
se aplica este modelo: """
    instrucciones_label = tk.Label(ventana_ayuda,
                                    text=instrucciones_text,
                                    bg="white",
                                    fg="black",
                                    font=("Helvetica", 12),
                                    justify="left")
    instrucciones_label.pack(padx=20, pady=5, anchor="w")
    
    titulo_ayuda2 = tk.Label(ventana_ayuda,
                            text="Fórmulas y Cálculos:",
                            bg="white",
                            fg="black",
                            font=("Helvetica", 16))
    titulo_ayuda2.pack(pady=5,  padx=20, anchor="w")

    instrucciones_text2  = """• Duración Esperada (TE): Calculamos la duración esperada de cada actividad utilizando la fórmula 
 TE = (O + 4M + P) / 6, donde O es la duración optimista, M es la duración más probable y P es la duración 
 pesimista.
• Varianza (Var): Calculamos la varianza de cada actividad utilizando la fórmula Var = ((P - O) / 6)^2.
• Parámetros de Distribución Beta: Utilizamos los valores de O, M y P para calcular los parámetros alfa y
 beta de la distribución beta. """
    instrucciones_label2 = tk.Label(ventana_ayuda,
                                    text=instrucciones_text2,
                                    bg="white",
                                    fg="black",
                                    font=("Helvetica", 12),
                                    justify="left")
    instrucciones_label2.pack(padx=20, pady=5, anchor="w")
    
    titulo_ayuda3 = tk.Label(ventana_ayuda,
                            text="Intervalos de Confianza:",
                            bg="white",
                            fg="black",
                            font=("Helvetica", 16))
    titulo_ayuda3.pack(pady=5,  padx=20, anchor="w")

    instrucciones_text3  = """
• Los intervalos de confianza (68%, 95% y 99%) permiten al usuario seleccionar qué tan seguro quiere 
  estar con respecto a la duración estimada del proyecto."""
    instrucciones_label3 = tk.Label(ventana_ayuda,
                                    text=instrucciones_text3,
                                    bg="white",
                                    fg="black",
                                    font=("Helvetica", 12),
                                    justify="left")
    instrucciones_label3.pack(padx=20, pady=5, anchor="w")
    
    titulo_ayuda4 = tk.Label(ventana_ayuda,
                            text="Significado Práctico:",
                            bg="white",
                            fg="black",
                            font=("Helvetica", 16))
    titulo_ayuda4.pack(pady=5,  padx=20, anchor="w")

    instrucciones_text4  = """• Los resultados proporcionados por SIMU-PERT permiten tomar decisiones informadas en la 
    planificación y ejecución de proyectos. Los intervalos de confianza ayudan a comprender la 
    variabilidad y el riesgo asociados con las estimaciones de duración."""
    instrucciones_label4 = tk.Label(ventana_ayuda,
                                    text=instrucciones_text4,
                                    bg="white",
                                    fg="black",
                                    font=("Helvetica", 12),
                                    justify="left")
    instrucciones_label4.pack(padx=20, pady=5, anchor="w")
    
    salir_button = tk.Button(ventana_ayuda,
                             text="CERRAR", bg='#4e4bc9', fg='white', font=("Helvetica", 14),
                             command=ventana_ayuda.destroy)  # Close the window
    salir_button.pack(pady=20)
    
    

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Ayuda", menu=menu_inicio)
    menu_inicio.add_command(label="¿Cómo funciona?", command=abrir_ventana_ayuda)

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=750,  bg='#6b68ff')
        self.root = root
        self.pack()
        #self.config( bg='#6b68ff')
        
        self.titulo_label = tk.Label(self,
                                    text="Simulador para la estimación de la duración de un proyecto: \nSIMU-PERT",
                                    bg="#6b68ff",
                                    fg="white",
                                    font=("Helvetica", 20),
                                    justify="center")
        self.titulo_label.pack(pady=20, padx=20)
        
        #imagen inicio
        self.image = Image.open('..\\simulador\\img\\img-inicio.jpeg')
        self.image = self.image.resize((700, 400))
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self, image=self.image_tk, bg="#6b68ff")
        self.image_label.pack()
        
        
        #botons
        self.button_frame = tk.Frame(self, bg="#6b68ff")
        self.button_frame.pack(side='top', pady=20)

        self.boton_abrir = tk.Button(self.button_frame, text='INICIAR', bg='#4e4bc9', fg='white', font=("Helvetica", 14),
                                    command=self.iniciar_proyecto)
        self.boton_abrir.grid(row=0, column=0, padx=20, pady=20, sticky='e')

        self.boton_ayuda = tk.Button(self.button_frame, text='AYUDA', bg='#4e4bc9', fg='white', font=("Helvetica", 14), command=abrir_ventana_ayuda)
        self.boton_ayuda.grid(row=0, column=1, padx=20, pady=20, sticky='w')
        
        self.boton_ayuda = tk.Button(self.button_frame, text='VER PROYECTOS', bg='#4e4bc9', fg='white', font=("Helvetica", 14))
        self.boton_ayuda.grid(row=0, column=2, padx=20, pady=20, sticky='w')
        
    def iniciar_proyecto(self):
        self.root.configure(bg='white')
        self.root.title("Iniciar Proyecto")
        # Ocultar elementos en el marco inicial
        self.titulo_label.pack_forget()
        self.image_label.pack_forget()
        self.button_frame.pack_forget()

        inicio_frame = tk.Frame(self,  bg='white')
        inicio_frame.pack(expand=True, fill='both')
        
        inicio_label = tk.Label(inicio_frame, text='Ingrese el nombre del proyecto', bg='white', fg='black', font=("Helvetica", 20))
        inicio_label.pack(pady=20, padx=180)
        
        entry_row_frame = tk.Frame(inicio_frame, bg='white')
        entry_row_frame.pack()

        inicio_label2 = tk.Label(entry_row_frame, text='Nombre del Proyecto:', bg='white', fg='black', font=("Helvetica", 12))
        inicio_label2.grid(row=0, column=0, pady=20, padx=20)

        self.nomProyecto = tk.StringVar()
        self.entry_nombre = tk.Entry(entry_row_frame, textvariable=self.nomProyecto, font=("Helvetica", 14))
        self.entry_nombre.grid(row=0, column=1, pady=10, padx=20)

        self.boton_agregar_actividades = tk.Button(inicio_frame, text='AGREGAR ACTIVIDADES', bg='#4e4bc9', fg='white', font=("Helvetica", 14),
                                                command=lambda: agregar_actividades(self),
                                                state=tk.DISABLED)
        self.boton_agregar_actividades.pack(pady=20)
        
        self.nomProyecto.trace_add("write", self.validar_input)
        
    def validar_input(self, *args):
        if self.nomProyecto.get():
            self.boton_agregar_actividades.config(state=tk.NORMAL)
        else:
            self.boton_agregar_actividades.config(state=tk.DISABLED)

def almacenar_actividad(datoActividades, actividad, durOpt, durProb, durPes,root):
        # Llamar a la función para generar el gráfico y obtener los valores
        esperada, varianza, desvEstandar = generar_grafico_pert(durOpt, durProb, durPes)
        datoActividades[actividad] = {
        'duracion_optimista': durOpt,
        'duracion_probable': durProb,
        'duracion_pesimista': durPes,
        'pert':esperada,
        'varianza':varianza,
        'desvEstandar':desvEstandar
    }
        ventana3(root,datoActividades,actividad)

def agregar_actividades(frame):
    frame.root.destroy()

    global actividad
    actividad+=1

    root = tk.Tk()
    root.title('Registro de Actividades')
    root.geometry('800x600')
    root.configure(bg='white')

    titulo_actividades = tk.Label(root, text="Ingrese la duración esperada de cada actividad", bg='white', fg='black', font=("Helvetica", 20))
    titulo_actividades.pack(pady=20, padx=50)
        
    entry_row_frame2 = tk.Frame(root, bg='white')
    entry_row_frame2.pack()
    # duracion Optimista
    ac_label1 = tk.Label(entry_row_frame2, text='Duración Optimista:', bg='white', fg='black', font=("Helvetica", 12))
    ac_label1.grid(row=0, column=0, pady=20, padx=20)

    durOpt = tk.IntVar()
    entry_durOpt = tk.Entry(entry_row_frame2, textvariable=durOpt, font=("Helvetica", 14))
    entry_durOpt.grid(row=0, column=1, pady=10, padx=20)
        
    #duracion Pesimista
    ac_label2 = tk.Label(entry_row_frame2, text='Duración Pesimista:', bg='white', fg='black', font=("Helvetica", 12))
    ac_label2.grid(row=1, column=0, pady=20, padx=20)

    durPes = tk.IntVar()
    entry_durPes = tk.Entry(entry_row_frame2, textvariable=durPes, font=("Helvetica", 14))
    entry_durPes.grid(row=1, column=1, pady=10, padx=20)
        
    #duracion probable
    ac_label3 = tk.Label(entry_row_frame2, text='Duración más  Probable:', bg='white', fg='black', font=("Helvetica", 12))
    ac_label3.grid(row=2, column=0, pady=20, padx=20)

    durProb = tk.IntVar()
    entry_durProb = tk.Entry(entry_row_frame2, textvariable=durProb, font=("Helvetica", 14))
    entry_durProb.grid(row=2, column=1, pady=10, padx=20)
        
    #botons
    button_frame2 = tk.Frame(root, bg="white")
    button_frame2.pack(side='top', pady=20)

    boton_agregar = tk.Button(button_frame2, text='AGREGAR', bg='#4e4bc9', fg='white', font=("Helvetica", 14),
                              #command=lambda: ventana3(root)
                               command=lambda:almacenar_actividad(datoActividades, actividad, durOpt.get(), durProb.get(), durPes.get(),root))
    boton_agregar.grid(row=0, column=0, padx=20, pady=20, sticky='e')


#----------------------------------------------------------------
def ventana3(frame,datoActividades,actividad):
    if frame is not None and frame.winfo_exists():
      frame.destroy()

    root = tk.Tk()
    root.title('Duración PERT para la actividad {actividad}')
    root.geometry('800x600')
    root.configure(bg='white')

    durOpt = datoActividades[actividad]['duracion_optimista']
    durPes = datoActividades[actividad]['duracion_pesimista']
    durProb = datoActividades[actividad]['duracion_probable']
    esperada = datoActividades[actividad]['pert']
    varianza = datoActividades[actividad]['varianza']
    desvEstandar = datoActividades[actividad]['desvEstandar']

    # Agregar etiquetas
    etiquetaActividad = tk.Label(root, text="Nombre de la actividad: "+ str(actividad), bg='white', fg='black', font=("Helvetica", 16), anchor='w', width=28)
    etiquetaActividad.pack(pady=10, padx=20)

    etiqueta1 = tk.Label(root, text="Duración optimista: "+ str(durOpt)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta1.pack(pady=10, padx=20)

    etiqueta2 = tk.Label(root, text="Duración más probable: "+ str(durProb)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta2.pack(pady=10, padx=20)

    etiqueta3 = tk.Label(root, text="Duración pesimista: "+ str(durPes)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta3.pack(pady=10, padx=20)

    etiqueta4 = tk.Label(root, text="Desviacón estándar (σ): "+ str(desvEstandar), bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta4.pack(pady=10, padx=20)

    etiqueta5 = tk.Label(root, text="Duración esperada (PERT): "+ str(esperada)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta5.pack(pady=10, padx=20)

    generar_grafico_pert(int(durOpt), int(durProb), int(durPes))

    #Frame para el botón
    button_frame = tk.Frame(root, bg='white')
    button_frame.pack(side='top', pady=20)

    # Botón en el frame, centrado

    self=root
    
    # Botón en el frame
    boton_duracionFinal = tk.Button(button_frame, text='Duracion final del proyecto', bg='#4e4bc9', fg='white', font=("Helvetica", 14), command=lambda: ventana4(self,datoActividades))
    boton_duracionFinal.grid(row=0, column=0, padx=0, pady=0, sticky='w')  

    barra_menu(root)

    # Cargar la imagen exportada y mostrarla en un widget de Tkinter
    try:
        img = Image.open('..\\simulador\\img\\grafico_pert.jpeg')
        img = img.resize((700, 550))
        img_tk = ImageTk.PhotoImage(img)

        img_label = tk.Label(root, image=img_tk, bg='white')
        img_label.image = img_tk  # Guardar una referencia para evitar que se elimine
        img_label.pack(pady=20, padx=20)
    except Exception as e:
        print("Error al cargar la imagen:", e)
#--------------------------
duracionFinal = 0
suma_varianzas = 0
desv_estandar_total = 0

def ventana4(frame,datoActividades):
    #suma de resultados
    global duracionFinal
    duracionFinal = sum(actividad['pert'] for actividad in datoActividades.values())
    global suma_varianzas
    suma_varianzas = sum(actividad['desvEstandar'] ** 2 for actividad in datoActividades.values())
    global desv_estandar_total
    desv_estandar_total = np.sqrt(suma_varianzas)

    # Cerrar ventana anterior si existe y está abierta
    if frame is not None and frame.winfo_exists():
      frame.destroy()

    #funcion para eliminar actividades
    def eliminarActividad():
        item = tabla.selection()[0]
        valor_actual_actividad = int(tabla.item(item, "values")[0])
        del datoActividades[valor_actual_actividad]
        tabla.delete(item)
        #actualizar etiquetas
        global duracionFinal
        duracionFinal = sum(actividad['pert'] for actividad in datoActividades.values())
        global suma_varianzas
        suma_varianzas = sum(actividad['desvEstandar'] ** 2 for actividad in datoActividades.values())
        global desv_estandar_total
        desv_estandar_total = np.sqrt(suma_varianzas)
        etiqueta1.config(text="Duración final del proyecto: "+ str(duracionFinal)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
        etiqueta.config(text="Desviación estandar total: "+ str(desv_estandar_total)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
        mensaje_label.config(text="", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
        mensaje_label2.config(text="", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    
    #funcion para ver la grafica de una actividad
    def verGrafica():
        item = tabla.selection()[0]
        valor_actual_actividad = int(tabla.item(item, "values")[0])
        ventana3(root,datoActividades,valor_actual_actividad)
    
    def abrir_ventana_edicion():
    # Obtener el elemento seleccionado en la tabla
        item = tabla.selection()[0]
    # Crear una nueva ventana para la edición
        ventana_edicion = tk.Toplevel(root)
        ventana_edicion.title('Editar Valor')
        ventana_edicion.geometry('300x100')
    # Crear etiquetas y entradas para editar el valor de duracion
        valor_actual_actividad = int(tabla.item(item, "values")[0])
        durOpt = datoActividades[valor_actual_actividad]['duracion_optimista']
        durPes =  datoActividades[valor_actual_actividad]['duracion_pesimista']
        durProb = datoActividades[valor_actual_actividad]['duracion_probable']
    # duracion Optimista
        ac_label1 = ttk.Label(ventana_edicion, text='Duración Optimista: ')
        ac_label1.pack(pady=10)     
        entry_durOpt = ttk.Entry(ventana_edicion)
        entry_durOpt.insert(0,str(durOpt))
        entry_durOpt.pack()       
    #duracion Pesimista
        ac_label2 = ttk.Label(ventana_edicion, text='Duración Pesimista:')
        ac_label2.pack(pady=10)
        entry_durPes = ttk.Entry(ventana_edicion)
        entry_durPes.insert(0,str(durPes))
        entry_durPes.pack()       
    #duracion probable
        ac_label3 = ttk.Label(ventana_edicion, text='Duración más  Probable:')
        ac_label3.pack(pady=10)
        entry_durProb = ttk.Entry(ventana_edicion)
        entry_durProb.insert(0,str(durProb))
        entry_durProb.pack()
    # Función para guardar cambios y actualizar la tabla
        def guardar_cambios():
            esperada, varianza, desvEstandar = generar_grafico_pert(int(entry_durOpt.get()), int(entry_durProb.get()), int(entry_durPes.get()))
            datoActividades[valor_actual_actividad]['duracion_optimista']=entry_durOpt.get()
            datoActividades[valor_actual_actividad]['duracion_probable']=entry_durProb.get()
            datoActividades[valor_actual_actividad]['duracion_pesimista']=entry_durPes.get()
            datoActividades[valor_actual_actividad]['pert']=esperada
            datoActividades[valor_actual_actividad]['varianza']=varianza
            datoActividades[valor_actual_actividad]['desvEstandar']=desvEstandar
            nuevo_valor = esperada
            tabla.item(item, values=(tabla.item(item, "values")[0], nuevo_valor))
            #actualizar etiquetas
            global duracionFinal
            duracionFinal = sum(actividad['pert'] for actividad in datoActividades.values())
            global suma_varianzas
            suma_varianzas = sum(actividad['desvEstandar'] ** 2 for actividad in datoActividades.values())
            global desv_estandar_total
            desv_estandar_total = np.sqrt(suma_varianzas)
            etiqueta1.config(text="Duración final del proyecto: "+ str(duracionFinal)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
            etiqueta.config(text="Desviación estandar total: "+ str(desv_estandar_total)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
            mensaje_label.config(text="", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
            mensaje_label2.config(text="", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)

            ventana_edicion.destroy()

    # Botón para guardar cambios
        boton_guardar = ttk.Button(ventana_edicion, text="Guardar Cambios", command=guardar_cambios)
        boton_guardar.pack(pady=10)

    # Crear una nueva ventana
    root = tk.Tk()
    root.title('Duración final del proyecto')
    root.geometry('800x600')
    root.configure(bg='white')

    barra_menu(root)

    # Crear un Treeview para mostrar la tabla
    tabla = ttk.Treeview(root, columns=("Actividad", "Duración"), show="headings")
    tabla.heading("Actividad", text="Actividad")
    tabla.heading("Duración", text="Duración")

    # Insertar datos desde la lista de diccionarios
    for actividad, datos in datoActividades.items():
        pert_valor = datos['pert']
        tabla.insert("", "end", values=(actividad, pert_valor))

    # Agregar la tabla a la ventana
    tabla.pack(pady=20, padx=20)

    boton_editar = ttk.Button(root, text="Editar Valor", command=abrir_ventana_edicion)
    boton_editar.pack()

    boton_editar = ttk.Button(root, text="Eliminar Actividad", command=eliminarActividad)
    boton_editar.pack()

    boton_verGrafica = ttk.Button(root, text="Ver grafica de la actividad", command=verGrafica)
    boton_verGrafica.pack()


    # Agregar etiquetas
    etiqueta1 = tk.Label(root, text="Duración final del proyecto: "+ str(duracionFinal)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta1.pack(pady=10, padx=20)

    etiqueta = tk.Label(root, text="Desviación estandar total: "+ str(desv_estandar_total)+" días", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta.pack(pady=10, padx=20)

    etiqueta2 = tk.Label(root, text="Escoja un intervalo de confianza: ", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    etiqueta2.pack(pady=10, padx=20)

    # Crear un frame para centrar los radiobuttons
    frame_radiobuttons = ttk.Frame(root)
    frame_radiobuttons.pack(pady=10, padx=20)

    def mostrar_mensaje():
        seleccionado = var.get()
        if seleccionado=="68%":
            menorTiempo1 = duracionFinal - 1*(desv_estandar_total)
            mayorTiempo1 = duracionFinal + 1*(desv_estandar_total)
            mensaje_label.config(text=f"Menor tiempo probable: {menorTiempo1} días")
            mensaje_label2.config(text=f"Mayor tiempo probable: {mayorTiempo1} días")
        if seleccionado=="95%":
            menorTiempo2 = duracionFinal - 2*(desv_estandar_total)
            mayorTiempo2 = duracionFinal + 2*(desv_estandar_total)
            mensaje_label.config(text=f"Menor tiempo probable: {menorTiempo2} días")
            mensaje_label2.config(text=f"Mayor tiempo probable: {mayorTiempo2} días")
        if seleccionado=="99%":
            menorTiempo3 = duracionFinal - 3*(desv_estandar_total)
            mayorTiempo3 = duracionFinal + 3*(desv_estandar_total)
            mensaje_label.config(text=f"Menor tiempo probable: {menorTiempo3} días")
            mensaje_label2.config(text=f"Mayor tiempo probable: {mayorTiempo3} días")


    # Variable para almacenar la selección de los radiobuttons
    var = tk.StringVar(value=None)

    # Agregar radiobuttons al frame
    radio_68 = ttk.Radiobutton(frame_radiobuttons, text="68%", variable=var, value="68%", command=mostrar_mensaje)
    radio_68.pack(side="left", padx=10)

    radio_95 = ttk.Radiobutton(frame_radiobuttons, text="95%", variable=var, value="95%", command=mostrar_mensaje)
    radio_95.pack(side="left", padx=10)

    radio_99 = ttk.Radiobutton(frame_radiobuttons, text="99%", variable=var, value="99%", command=mostrar_mensaje)
    radio_99.pack(side="left", padx=10)

    #impresion de mensaje
    mensaje_label = tk.Label(root, text="", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    mensaje_label.pack()
    mensaje_label2 = tk.Label(root, text="", bg='white', fg='black', font=("Helvetica", 14), anchor='w', width=30)
    mensaje_label2.pack()


   #Frame para el botón
    button_frame = tk.Frame(root, bg='white')
    button_frame.pack(side='top', pady=20)

    #Botón en el frame
    boton_finalizar = tk.Button(button_frame, text='Finalizar', bg='#4e4bc9', fg='white', font=("Helvetica", 14), command=root.destroy)
    boton_finalizar.grid(row=0, column=1, padx=20, pady=40, sticky='w')

    boton_agregarActividad = tk.Button(button_frame, text='Agregar actividad', bg='#4e4bc9', fg='white', font=("Helvetica", 14), command=lambda: ventana5(root))
    boton_agregarActividad.grid(row=0, column=2, padx=10, pady=0, sticky='ew') 
#----------------------------------------------

def ventana5(frame):
    # Cerrar ventana anterior si existe y está abierta
    if frame is not None and frame.winfo_exists():
      frame.destroy()

    global actividad
    actividad+=1

    root = tk.Tk()
    root.title('Registro de Actividades')
    root.geometry('800x600')
    root.configure(bg='white')

    titulo_actividades = tk.Label(root, text="Ingrese la duración esperada de cada actividad", bg='white', fg='black', font=("Helvetica", 20))
    titulo_actividades.pack(pady=20, padx=50)
        
    entry_row_frame2 = tk.Frame(root, bg='white')
    entry_row_frame2.pack()
    # duracion Optimista
    ac_label1 = tk.Label(entry_row_frame2, text='Duración Optimista:', bg='white', fg='black', font=("Helvetica", 12))
    ac_label1.grid(row=0, column=0, pady=20, padx=20)

    durOpt = tk.IntVar()
    entry_durOpt = tk.Entry(entry_row_frame2, textvariable=durOpt, font=("Helvetica", 14))
    entry_durOpt.grid(row=0, column=1, pady=10, padx=20)
        
    #duracion Pesimista
    ac_label2 = tk.Label(entry_row_frame2, text='Duración Pesimista:', bg='white', fg='black', font=("Helvetica", 12))
    ac_label2.grid(row=1, column=0, pady=20, padx=20)

    durPes = tk.IntVar()
    entry_durPes = tk.Entry(entry_row_frame2, textvariable=durPes, font=("Helvetica", 14))
    entry_durPes.grid(row=1, column=1, pady=10, padx=20)
        
    #duracion probable
    ac_label3 = tk.Label(entry_row_frame2, text='Duración más  Probable:', bg='white', fg='black', font=("Helvetica", 12))
    ac_label3.grid(row=2, column=0, pady=20, padx=20)

    durProb = tk.IntVar()
    entry_durProb = tk.Entry(entry_row_frame2, textvariable=durProb, font=("Helvetica", 14))
    entry_durProb.grid(row=2, column=1, pady=10, padx=20)
        
    #botons
    button_frame2 = tk.Frame(root, bg="white")
    button_frame2.pack(side='top', pady=20)

    boton_agregar = tk.Button(button_frame2, text='AGREGAR', bg='#4e4bc9', fg='white', font=("Helvetica", 14),
                              #command=lambda: ventana3(root)
                               command=lambda:almacenar_actividad(datoActividades, actividad, durOpt.get(), durProb.get(), durPes.get(),root))
    boton_agregar.grid(row=0, column=0, padx=20, pady=20, sticky='e')
