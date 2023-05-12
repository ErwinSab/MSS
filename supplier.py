import ctypes
import tkinter as tk
# mport config
import os
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import CTk

# Modes: "System" (standard), "Dark", "Light"


class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+{2}+{3}".format(int(root.winfo_screenwidth()-root.winfo_screenwidth()*0.43), int(
                           root.winfo_screenheight()-root.winfo_screenheight()*0.27),
            int(root.winfo_screenwidth()*0.213), int(root.winfo_screenheight()*0.165)))
        self.root.title("| MSS - MILANES SMART SHOP || Suplidores ")
        self.root.focus_force()
        # ===============================
        ctk.set_appearance_mode("Dark")

        # ALL Variables =======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # Iconos

        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        self.icon_side = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "ilupa.png")), size=(20, 20))
        self.icon_side0 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "isave.png")), size=(27, 27))
        self.icon_side1 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iupdate.png")), size=(27, 27))
        self.icon_side2 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "idelete.png")), size=(27, 27))
        self.icon_side3 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iclear.png")), size=(27, 27))

        # Titulo

        self.lbl_Supplier = ctk.CTkLabel(self.root, text="Suplidor", font=(
            "roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)

        # Frame Manejo de poroductos

        Datosframe = ctk.CTkFrame(self.root)
        Datosframe.place(relx=0.01, rely=0.08, relwidth=0.36, relheight=0.90)

        # === Tittle ===
        Dsuplabel = ctk.CTkLabel(
            Datosframe, text=" Suplidores :", font=("roboto", 14, "bold"))
        Dsuplabel.place(relx=0.01, rely=0.01)

        # ===  Supplier Tabla   ===
        tree_frame = ctk.CTkFrame(Datosframe)
        tree_frame.place(relx=0.02, rely=0.08, relwidth=0.98, relheight=0.92)

        scrollx = ctk.CTkScrollbar(
            tree_frame, orientation=HORIZONTAL, command=XView)
        scrolly = ctk.CTkScrollbar(
            tree_frame, orientation=VERTICAL, command=YView)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.supplierTable = ttk.Treeview(tree_frame, columns=(
            "invoice", "Name", "Contact", "Desc"),  yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.configure(command=self.supplierTable.xview)
        scrolly.configure(command=self.supplierTable.yview)

        self.supplierTable.heading(
            "invoice", text="Invoice No.", command=lambda: self.sort_column("invoice", False))
        self.supplierTable.heading(
            "Name", text="Name", command=lambda: self.sort_column("Name", False))
        self.supplierTable.heading(
            "Contact", text="Contact", command=lambda: self.sort_column("Contact", False))
        self.supplierTable.heading(
            "Desc", text="Description", command=lambda: self.sort_column("Desc", False))

        self.supplierTable["show"] = "headings"

        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("Name", width=100)
        self.supplierTable.column("Contact", width=100)
        self.supplierTable.column("Desc", width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # Frame Search

        Searchframe = ctk.CTkFrame(self.root)
        Searchframe.place(relx=0.38, rely=0.08, relwidth=0.609, relheight=0.90)

        #
        titulolabel = ctk.CTkLabel(Searchframe, text="Buscar Suplidor :", font=(
            "roboto", 15, "bold")).place(relx=0.02, rely=0.01, relwidth=0.3)
        lbl_search = ctk.CTkLabel(Searchframe, text="Invoice No.", font=(
            "roboto", 15)).place(relx=0.01, rely=0.1, relwidth=0.31)
        txt_search = ctk.CTkEntry(Searchframe, textvariable=self.var_searchtxt, font=(
            "roboto", 15), border_color=("#DA7E38", "#42A5F5")).place(relx=0.33, rely=0.1, relwidth=0.33)
        btn_search = ctk.CTkButton(Searchframe, command=self.search, image=self.icon_side, text="Buscar", cursor="hand2", font=(
            "roboto", 15), fg_color=("#DA7E38", "#374BDC"), hover_color="#374BDC").place(relx=0.67, rely=0.1, relwidth=0.32)

        # Content
        datoslabel = ctk.CTkLabel(Searchframe, text="Datos Suplidor :", font=(
            "roboto", 15, "bold")).place(relx=0.02, rely=0.17, relwidth=0.3)
        lbl_supplier_invoice = ctk.CTkLabel(Searchframe, text="Invoice No :", font=(
            "roboto", 14, "bold"), ).place(relx=0.05, rely=0.27, relwidth=0.25)
        txt_supplier_invoice = ctk.CTkEntry(Searchframe, textvariable=self.var_sup_invoice, border_color=(
            "#DA7E38", "#42A5F5"), font=("roboto", 14, "bold"))
        txt_supplier_invoice.place(relx=0.35, rely=0.27, relwidth=0.60)
        lbl_name = ctk.CTkLabel(Searchframe, text="Nombre    :", font=(
            "roboto", 14, "bold"), ).place(relx=0.05, rely=0.37, relwidth=0.25)
        txt_name = ctk.CTkEntry(
            Searchframe, textvariable=self.var_name, font=("roboto", 14, "bold"), border_color=("#DA7E38", "#42A5F5"))
        txt_name.place(relx=0.35, rely=0.37, relwidth=0.60)
        lbl_contact = ctk.CTkLabel(Searchframe, text="Contacto  :", font=(
            "roboto", 14, "bold"), ).place(relx=0.05, rely=0.47, relwidth=0.25)
        txt_contact = ctk.CTkEntry(Searchframe, textvariable=self.var_contact, border_color=(
            "#DA7E38", "#42A5F5"), font=("roboto", 14, "bold"))
        txt_contact.place(relx=0.35, rely=0.47, relwidth=0.60)
        lbl_desc = ctk.CTkLabel(Searchframe, text="Descripcion", font=(
            "roboto", 14, "bold"), ).place(relx=0.37, rely=0.55, relwidth=0.25)
        self.txt_desc = ctk.CTkTextbox(
            Searchframe, font=("roboto", 14, "bold"))
        self.txt_desc.place(relx=0.1, rely=0.61, relwidth=0.80, relheight=0.15)

        # ===Buttons====

        btn_add = ctk.CTkButton(Searchframe, text=" Save", command=self.add, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side0).place(relx=0.02, rely=0.78, relwidth=0.46)
        btn_update = ctk.CTkButton(Searchframe, text="Update", command=self.update, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side1).place(relx=0.02, rely=0.89, relwidth=0.46)
        btn_delete = ctk.CTkButton(Searchframe, text="Delete", command=self.delete, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side2).place(relx=0.5, rely=0.78, relwidth=0.46)
        btn_clear = ctk.CTkButton(Searchframe, text=" Clear", command=self.clear, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side3).place(relx=0.5, rely=0.89, relwidth=0.46)

        # =========================================================================

    def add(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "Error", "Es necesario un RNC o Cedula ,Invoice.no", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Este numero de Invoice No. ya fue asignado,Intente uno diferente !", parent=self.root)
                else:
                    cur.execute("""Insert into supplier(invoice,Name,Contact,Desc) values(?,?,?,?)""", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get("1.0", END)))
                    con.commit()
                    self.show()
                    messagebox.showinfo(
                        "Success", " Suplidor añadido !!! ", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete("1.0", END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "Error", "Es necesario Invoice.no !! o Seleccione uno Existente !!", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                con.commit()
            row = cur.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Invoice No. Invalido !", parent=self.root)
            else:
                cur.execute("""Update supplier set Name=?,Contact=?,Desc=? where invoice=? """, (
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get("1.0", END),
                            self.var_sup_invoice.get()))
                con.commit()
                self.show()
                messagebox.showinfo(
                    "Success", "Suplidor Actualizado !", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror(
                    "Error", "Es necesario un Invoice no.", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",
                            (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invoice No. Invalido !", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Realmente quieres borrarlo ?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from supplier where invoice=?",
                                    (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Suplidor Borrado !", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_searchtxt.set("")
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete("1.0", END)
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error", "Se requiere Invocie No.", parent=self.root)
            else:
                cur.execute(
                    "select * from supplier where invoice like '%"+self.var_searchtxt.get()+"%'")
                row = cur.fetchone()
                if row != None:
                    self.supplierTable.delete(
                        *self.supplierTable.get_children())
                    self.supplierTable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No se encuentra records que coincidan!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def sort_column(self, col, reverse):
        # Obtener los elementos de la columna a ordenar
        data = [(self.supplierTable.set(row, col), row)
                for row in self.supplierTable.get_children('')]
        # Ordenar los elementos según el valor de la columna
        data.sort(reverse=reverse)
        for index, (val, row) in enumerate(data):
            # Reorganizar los elementos en el treeview
            self.supplierTable.move(row, '', index)
        # Cambiar la dirección de ordenación para la próxima vez que se haga clic en la columna
        self.supplierTable.heading(
            col, command=lambda: self.sort_column(col, not reverse))

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top


if __name__ == "__main__":
    root = ctk.CTk()
    odj = supplierClass(root)
    root.mainloop()
