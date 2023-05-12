import ctypes
import tempfile
import win32print
import tkinter.filedialog
import os
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox


class salesClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+{2}+{3}".format(int(root.winfo_screenwidth()-root.winfo_screenwidth()*0.43), int(
                           root.winfo_screenheight()-root.winfo_screenheight()*0.27),
            int(root.winfo_screenwidth()*0.213), int(root.winfo_screenheight()*0.165)))
        self.root.title("| MSS - MILANES SMART SHOP || Facturas ")
        self.root.focus_force()
        # ==============================
        ctk.set_appearance_mode("Dark")
        #######################
        self.var_invoice = StringVar()
        self.chK_print = 0
        # Titulo
        self.lbl_products = ctk.CTkLabel(self.root, text="Facturas", font=(
            "roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)
        # Content
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        self.icon_side = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "ilupa.png")), size=(27, 27))
        self.icon_side3 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iclear.png")), size=(27, 27))
        self.icon_side4 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iprint.png")), size=(27, 27))

        # Frame Manejo de busqueda de facturas
        b_facturaframe = ctk.CTkFrame(self.root)
        b_facturaframe.place(relx=0.01, rely=0.08,
                             relwidth=0.35, relheight=0.90)
        lbl_empid = ctk.CTkLabel(b_facturaframe, text=" Factura:", font=(
            "roboto", 16, "bold")).place(relx=0.01, rely=0.07, relwidth=0.30)
        self.txt_search = ctk.CTkEntry(b_facturaframe, textvariable=self.var_invoice, font=(
            "roboto", 15), border_color=("#DA7E38", "#42A5F5")).place(relx=0.33, rely=0.07, relwidth=0.33, relheight=0.065)
        btn_search = ctk.CTkButton(b_facturaframe, command=self.search, image=self.icon_side, text="", cursor="hand2", font=(
            "roboto", 15), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5").place(relx=0.68, rely=0.07, relwidth=0.15, relheight=0.065)
        btn_clear = ctk.CTkButton(b_facturaframe, text="", command=self.clear, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side3).place(relx=0.84, rely=0.07, relwidth=0.15)
        btn_print = ctk.CTkButton(self.root, text="Imprimir", command=self.print_file, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side4)
        btn_print.place(relx=0.615, rely=0.9, relwidth=0.15)
        # Facturas Search

        D_factura = ctk.CTkFrame(b_facturaframe)
        D_factura.place(relx=0.05, rely=0.20, relwidth=0.90, relheight=0.78)
        self.Sales_List = ctk.CTkTextbox(D_factura, border_color=(
            "#DB3E39", "#42A5F5"), font=("roboto", 15, "bold"),)
        self.Sales_List.place(relx=0.01, rely=0.01,
                              relwidth=0.98, relheight=0.97)
        self.Sales_List.bind('<ButtonRelease-1>', self.get_data)

        # Frame Datos de facturas
        Contenidoframe = ctk.CTkFrame(self.root)
        Contenidoframe.place(relx=0.37, rely=0.08,
                             relwidth=0.62, relheight=0.8)

        self.lbl_Datos_f = ctk.CTkLabel(Contenidoframe, text="Area de datos de la factura", font=(
            "roboto", 16, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)

        self.Sales_dat = ctk.CTkTextbox(Contenidoframe, border_color=(
            "#DB3E39", "#42A5F5"),)
        self.Sales_dat.place(relx=0.02, rely=0.08,
                             relwidth=0.96, relheight=0.90)
        self.show()

####################################################################

    def show(self):
        self.Sales_List.delete("0.0", 'end')
        for i in os.listdir("Fac"):
            if i.split('.')[-1] == "txt":
                self.Sales_List.insert("0.0", i + "\n")

    def get_data(self, ev):
        # se hizo la modificacion con index y get + linestart line end debido a que txtbo no usan curseleccion
        index_ = self.Sales_List.index('insert')
        current_line = self.Sales_List.get(
            index_ + " linestart", index_ + " lineend")
        file_name = current_line
        self.Sales_dat.delete('1.0', "end")
        fp = open(f'Fac/{file_name}', 'r')
        for i in fp:
            self.Sales_dat.insert('end', i)
        fp.close()

    def search(self):
        lista_factura = self.Sales_List.get("1.0", "end")
        factura = lista_factura.split('\n')

        if self.var_invoice.get() == "":
            messagebox.showerror(
                "Error", "Se necesita que seleccione una Factura", parent=self.root)
        else:

            if (self.var_invoice.get()+".txt") in factura:
                fp = open(f'Fac/{self.var_invoice.get()}.txt', 'r')
                self.Sales_dat.delete("1.0", "end")
                for i in fp:
                    self.Sales_dat.insert('end', i)
                    fp.close
            else:
                messagebox.showerror(
                    "Error", "Factura invalida.......", parent=self.root)

    def clear(self):
        self.show()
        self.Sales_dat.delete('1.0', 'end')

    def print_file(self):
        new_file = tempfile.mktemp('.txt')
        open(new_file, 'w').write(self.Sales_dat.get('1.0', 'end'))
        os.startfile(new_file, 'print')

    """ # Obtener las impresoras instaladas
        printers = win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL, None, 1)
        printer_names = [printer[2] for printer in printers]

        # Crear una ventana de selección de impresora
        self.printer_window = tkinter.Toplevel()
        self.printer_window.title('Selecciona una impresora')

        # Crear una lista desplegable con las impresoras disponibles
        self.printer_var = tkinter.StringVar(self.printer_window)
        # Establecer la impresora predeterminada
        self.printer_var.set(printer_names[0])
        printer_dropdown = tkinter.OptionMenu(
            self.printer_window, self.printer_var, *printer_names)
        printer_dropdown.pack()

        # Crear un botón para imprimir el archivo seleccionado
        print_button = tkinter.Button(
            self.printer_window, text='Imprimir', command=self.print_selected_file)
        print_button.pack() """

    def print_selected_file(self):
        # Obtener el nombre de la impresora seleccionada
        printer_name = self.printer_var.get()

        # Hacer la impresión en la impresora seleccionada
        # Aquí debes especificar el nombre del archivo que quieres imprimir
        file_to_print = self.Sales_dat
        handle = win32print.OpenPrinter(printer_name)
        win32print.StartDocPrinter(
            handle, 1, ('Archivo de ejemplo', None, 'RAW'))
        win32print.StartPagePrinter(handle)
        with open(file_to_print, 'rb') as f:
            data = f.read()
        win32print.WritePrinter(handle, data)
        win32print.EndPagePrinter(handle)
        win32print.EndDocPrinter(handle)
        win32print.ClosePrinter(handle)

        # Cerrar la ventana de selección de impresora
        self.printer_window.destroy()

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top


if __name__ == "__main__":
    root = ctk.CTk()
    odj = salesClass(root)
    root.mainloop()
