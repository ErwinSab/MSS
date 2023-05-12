import ctypes
import tkinter
import os
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox


class productClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+{2}+{3}".format(int(root.winfo_screenwidth()-root.winfo_screenwidth()*0.22), int(
                           root.winfo_screenheight()-root.winfo_screenheight()*0.27),
            int(root.winfo_screenwidth()*0.213), int(root.winfo_screenheight()*0.165)))
        self.root.title("| MSS - MILANES SMART SHOP || Productos ")
        self.root.focus_force()
        # ===========================
        ctk.set_appearance_mode("Dark")
        # ===========================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        # ============================
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

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

        self.lbl_products = ctk.CTkLabel(self.root, text="Productos", font=(
            "roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)

        # Frame Manejo de poroductos

        Manejoframe = ctk.CTkFrame(self.root)
        Manejoframe.place(relx=0.01, rely=0.08, relwidth=0.35, relheight=0.90)

        # Content

        Manejolabel = ctk.CTkLabel(
            Manejoframe, text="Manejo del Producto :", font=("roboto", 14, "bold"))
        Manejolabel.place(relx=0.01, rely=0.01, relwidth=0.6)

        lbl_Category = ctk.CTkLabel(Manejoframe, text="Categoria  :", font=(
            "roboto", 14, "bold")).place(relx=0.05, rely=0.1, relwidth=0.30)
        cmb_Category = ctk.CTkComboBox(Manejoframe, variable=self.var_cat, values=self.cat_list, border_color=("#DA7E38", "#42A5F5"), button_color=("#DA7E38", "#42A5F5"), state='readonly',
                                       justify=CENTER, font=("roboto", 15))
        cmb_Category._entry.configure(
            readonlybackground=cmb_Category._apply_appearance_mode(cmb_Category._fg_color))
        cmb_Category.place(relx=0.35, rely=0.1, relwidth=0.60)
        cmb_Category.set("Seleccionar")

        lbl_Suplidor = ctk.CTkLabel(Manejoframe, text="Suplidor     :", font=(
            "roboto", 14, "bold")).place(relx=0.05, rely=0.2, relwidth=0.30)
        cmb_Suplidor = ctk.CTkComboBox(Manejoframe, variable=self.var_sup, values=self.sup_list, border_color=("#DA7E38", "#42A5F5"), button_color=("#DA7E38", "#42A5F5"), state='readonly',
                                       justify=CENTER, font=("roboto", 15))
        cmb_Suplidor._entry.configure(
            readonlybackground=cmb_Suplidor._apply_appearance_mode(cmb_Suplidor._fg_color))
        cmb_Suplidor.place(relx=0.35, rely=0.2, relwidth=0.60)
        cmb_Suplidor.set("Seleccionar")
        lbl_name = ctk.CTkLabel(Manejoframe, text="Nombre      :", justify="right", font=(
            "roboto", 14)).place(relx=0.05, rely=0.3, relwidth=0.25)
        txt_name = ctk.CTkEntry(Manejoframe, textvariable=self.var_name, border_color=(
            "#DA7E38", "#42A5F5"), font=("roboto", 14, "bold")).place(relx=0.35, rely=0.3, relwidth=0.60)
        lbl_price = ctk.CTkLabel(Manejoframe, text="Precio          :", justify="right", font=(
            "roboto", 14)).place(relx=0.05, rely=0.4, relwidth=0.25)
        txt_price = ctk.CTkEntry(Manejoframe, textvariable=self.var_price, border_color=(
            "#DA7E38", "#42A5F5"), font=("roboto", 14, "bold")).place(relx=0.35, rely=0.4, relwidth=0.60)
        lbl_quantity = ctk.CTkLabel(Manejoframe, text="Cantidad   :", font=(
            "roboto", 14)).place(relx=0.05, rely=0.5, relwidth=0.25)
        txt_quantity = ctk.CTkEntry(Manejoframe, textvariable=self.var_qty, border_color=(
            "#DA7E38", "#42A5F5"), font=("roboto", 14, "bold")).place(relx=0.35, rely=0.5, relwidth=0.60)
        lbl_status = ctk.CTkLabel(Manejoframe, text="Estatus      :", font=(
            "roboto", 14, "bold")).place(relx=0.05, rely=0.6, relwidth=0.30)
        cmb_Status = ctk.CTkComboBox(Manejoframe, variable=self.var_status, values=("Act", "Des",), border_color=("#DA7E38", "#42A5F5"), button_color=("#DA7E38", "#42A5F5"), state='readonly',
                                     justify=CENTER, font=("roboto", 15))
        cmb_Status._entry.configure(
            readonlybackground=cmb_Status._apply_appearance_mode(cmb_Status._fg_color))
        cmb_Status.place(relx=0.35, rely=0.6, relwidth=0.60)
        cmb_Status.set("Act")

        # Buttons

        btn_add = ctk.CTkButton(Manejoframe, text=" Save", command=self.add, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side0).place(relx=0.02, rely=0.78, relwidth=0.46)
        btn_update = ctk.CTkButton(Manejoframe, text="Update", command=self.update, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side1).place(relx=0.02, rely=0.89, relwidth=0.46)
        btn_delete = ctk.CTkButton(Manejoframe, text="Delete", command=self.delete, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side2).place(relx=0.5, rely=0.78, relwidth=0.46)
        btn_clear = ctk.CTkButton(Manejoframe, text=" Clear", command=self.clear, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side3).place(relx=0.5, rely=0.89, relwidth=0.46)

        # Frame Search

        Searchframe = ctk.CTkFrame(self.root)
        Searchframe.place(relx=0.37, rely=0.08, relwidth=0.62, relheight=0.90)

        # Content

        Searchlabel = ctk.CTkLabel(Searchframe, text="Buscar Producto", font=(
            "roboto", 15, "bold")).place(relx=0.01, rely=0.01, relwidth=0.3)

        cmb_search = ctk.CTkComboBox(Searchframe, variable=self.var_searchby, values=(
            "Nombre", "Categoria", "Estatus"), border_color=("#DA7E38", "#42A5F5"), button_color=("#DA7E38", "#42A5F5"), state='readonly',
            justify=CENTER, font=("roboto", 15))
        cmb_search._entry.configure(
            readonlybackground=cmb_search._apply_appearance_mode(cmb_search._fg_color))
        cmb_search.place(relx=0.01, rely=0.1, relwidth=0.31)
        cmb_search.set("Select")

        txt_search = ctk.CTkEntry(Searchframe, textvariable=self.var_searchtxt, font=(
            "roboto", 15), border_color=("#DA7E38", "#42A5F5")).place(relx=0.33, rely=0.1, relwidth=0.33)
        btn_search = ctk.CTkButton(Searchframe, command=self.search, image=self.icon_side, text="Buscar", cursor="hand2", font=(
            "roboto", 15), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5").place(relx=0.67, rely=0.1, relwidth=0.32)
        #
        Productlabel = ctk.CTkLabel(Searchframe, text="Productos :", font=(
            "roboto", 15, "bold")).place(relx=0.01, rely=0.2, relwidth=0.20)
        # ===  Product Details   =====
        prod_frame = ctk.CTkFrame(Searchframe)
        prod_frame.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.75)
        scrollx = ctk.CTkScrollbar(
            prod_frame, orientation="horizontal", command=XView)
        scrolly = ctk.CTkScrollbar(
            prod_frame, orientation=VERTICAL, command=YView)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.producttable = ttk.Treeview(prod_frame, columns=(
            "pid", "Category",  "name", "qty", "price", "status", "Supplier"),  yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.configure(command=self.producttable.xview)
        scrolly.configure(command=self.producttable.yview)

        self.producttable.heading(
            "pid", text="P-ID", command=lambda: self.sort_column("pid", False))
        self.producttable.heading(
            "Category", text="Categoria", command=lambda: self.sort_column("Category", False))
        self.producttable.heading(
            "name", text="Nombre", command=lambda: self.sort_column("name", False))
        self.producttable.heading(
            "qty", text="Cantidad", command=lambda: self.sort_column("qty", False))
        self.producttable.heading(
            "price", text="Precio", command=lambda: self.sort_column("price", False))
        self.producttable.heading(
            "status", text="Estado", command=lambda: self.sort_column("status", False))
        self.producttable.heading(
            "Supplier", text="Suplidor", command=lambda: self.sort_column("Supplier", False))

        self.producttable["show"] = "headings"

        self.producttable.column("pid", width=50)
        self.producttable.column("Category", width=90)
        self.producttable.column("name", width=120)
        self.producttable.column("qty", width=50)
        self.producttable.column("price", width=80)
        self.producttable.column("status", width=80)
        self.producttable.column("Supplier", width=150)
        self.producttable.pack(fill=BOTH, expand=1)
        self.producttable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    ##################

    def fetch_cat_sup(self):
        self.cat_list.append("Vacio")
        self.sup_list.append("Vacio")
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Seleccionar")
                for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Seleccionar")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Seleccionar" or self.var_cat.get() == "Vacio" or self.var_sup.get() == "Seleccionar" or self.var_name.get() == "":
                messagebox.showerror(
                    "Error", "Se requiere todos los datos del producto", parent=self.root)
            else:
                cur.execute("Select * from product where name=?",
                            (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Este Producto ya existe ! ,Intente uno diferente", parent=self.root)
                else:
                    cur.execute("""Insert into product(Category,name,qty,price,status,Supplier) values(?,?,?,?,?,?)""", (
                        self.var_cat.get(), self.var_name.get(), self.var_qty.get(), self.var_price.get(), self.var_status.get(), self.var_sup.get(),))
                    con.commit()
                    self.show()
                    messagebox.showinfo(
                        "Success", "Producto creado con Exito !!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.producttable.delete(*self.producttable.get_children())
            for row in rows:
                self.producttable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.producttable.focus()
        content = (self.producttable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_name.set(row[2])
        self.var_qty.set(row[3])
        self.var_price.set(row[4])
        self.var_status.set(row[5])
        self.var_sup.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "Error", "Porfavor seleccione un pruducvto de la lista", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",
                            (self.var_pid.get(),))
                con.commit()
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Este ID de producto es invalido", parent=self.root)
            else:
                cur.execute("""Update product set Category=?,name=?,qty=?,price=? ,status=?,Supplier=? where pid=? """, (
                            self.var_cat.get(),
                            self.var_name.get(),
                            self.var_qty.get(),
                            self.var_price.get(),
                            self.var_status.get(),
                            self.var_sup.get(),
                            self.var_pid.get()))
                con.commit()
                self.show()
                messagebox.showinfo(
                    "Success", "Producto Actualizado satisfactoriamente !!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "Error", "Se requiere que seleccione un Producto del listado existente ", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Id del producto invalido", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Realmente quiere eliminar este Producto?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from producto where pid=?",
                                    (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Producto eliminado satisfactoriamente !!!", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_cat.set("seleccionar")
        self.var_name.set("")
        self.var_qty.set("")
        self.var_price.set("")
        self.var_status.set("Act")
        self.var_sup.set("Seleccionar")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror(
                    "Error", "Seleccione una opcion para Buscar", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error", "Es necesario algun criterio para La Busqueda", parent=self.root)
            elif self.var_searchby.get() == "Nombre":
                cur.execute("select * from product where Name LIKE '%" +
                            self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.producttable.delete(*self.producttable.get_children())
                    for row in rows:
                        self.producttable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No existen registros con esta condicion !!!", parent=self.root)
            elif self.var_searchby.get() == "Categoria":
                cur.execute(
                    "select * from product where Category LIKE '%" + self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.producttable.delete(*self.producttable.get_children())
                    for row in rows:
                        self.producttable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No existen registros con esta condicion !!!", parent=self.root)
            elif self.var_searchby.get() == "Estatus":
                cur.execute(
                    "select * from product where status LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.producttable.delete(*self.producttable.get_children())
                    for row in rows:
                        self.producttable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No existen registros con esta condicion !!!", parent=self.root)
            else:
                cur.execute("select * from product where " +
                            self.var_searchby.get() + " LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.producttable.delete(*self.producttable.get_children())
                    for row in rows:
                        self.producttable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No existen registros con esta condicion !!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def sort_column(self, col, reverse):
        # Obtener los elementos de la columna a ordenar
        data = [(self.producttable.set(row, col), row)
                for row in self.producttable.get_children('')]
        # Ordenar los elementos según el valor de la columna
        data.sort(reverse=reverse)
        for index, (val, row) in enumerate(data):
            # Reorganizar los elementos en el treeview
            self.producttable.move(row, '', index)
        # Cambiar la dirección de ordenación para la próxima vez que se haga clic en la columna
        self.producttable.heading(
            col, command=lambda: self.sort_column(col, not reverse))

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top


if __name__ == "__main__":
    root = ctk.CTk()
    odj = productClass(root)
    root.mainloop()
