import tkinter as tk
from interfaz.gui_app import Frame, barra_menu


def main():
    root =tk.Tk()
    root.title('Proyecto De Teoría de la Simulación')
    root.iconbitmap('..\\simulador\\img\\logo.ico')
    root.geometry("800x670")
    barra_menu(root)
    
    app= Frame(root = root)
    
    # titulo_label = tk.Label(frame, 
    #                         text='Simulador para la estimacion de  la duracion de un proyecto: SIMU-PERT',
    #                         bg="#6b68ff",
    #                         fg="white",
    #                         font=("Helvetica", 16))
    # titulo_label.pack(pady=20)
    
    # imagen = tk.PhotoImage(file='img/img-inicio.jpeg')
    # imagen_label = tk.Label(frame, image=imagen, bg="#6b68ff")
    # imagen_label.pack()
    
    
    
    
    app.mainloop() #final ejecucion

if __name__== '__main__':
    main()