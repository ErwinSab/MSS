import ctypes
import tkinter
# import config
import os
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox


class categoryClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+{2}+{3}".format(int(root.winfo_screenwidth()-root.winfo_screenwidth()*0.7), int(
                           root.winfo_screenheight()-root.winfo_screenheight()*0.27),
            int(root.winfo_screenwidth()*0.213), int(root.winfo_screenheight()*0.165)))
        self.root.title("| MSS - MILANES SMART SHOP || Categorias ")
        self.root.focus_force()
        # ==========================

        # === variables ===
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        # Iconos
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        self.icon_side0 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "isave.png")), size=(27, 27))
        # self.icon_side1 = ctk.CTkImage(PIL.Image.open(os.path.join(image_path, "iupdate.png")), size=(27, 27))
        self.icon_side2 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "idelete.png")), size=(27, 27))
        # self.icon_side3 = ctk.CTkImage(PIL.Image.open(os.path.join(image_path, "iclear.png")), size=(27, 27))

        # === Tittle ===
        self.lbl_Empleados = ctk.CTkLabel(
            self.root, text="Categorias de Productos", font=("roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)

        # ___ Buttons ___ #

        lbl_name = ctk.CTkLabel(self.root, text="Nombre de la Categoria :", font=(
            "roboto", 16, "bold"), ).place(relx=0.1, rely=0.075)
        txt_name = ctk.CTkEntry(self.root, textvariable=self.var_name, font=(
            "roboto", 18), border_color=("#DA7E38", "#42A5F5")).place(relx=0.10, rely=0.125, relwidth=0.8)
        btn_add = ctk.CTkButton(self.root, text="Añadir", image=self.icon_side0, command=self.add, font=("roboto", 15), cursor="hand2", fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5").place(relx=0.05, rely=0.195, relwidth=0.425, relheight=0.075)
        btn_delete = ctk.CTkButton(self.root, text="Borrar", image=self.icon_side2, command=self.delete, font=("roboto", 15), cursor="hand2", fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42A5F5").place(relx=0.525, rely=0.195, relwidth=0.425, relheight=0.075)

        # ===  Category Table   =====
        cat_frame = ctk.CTkFrame(self.root)
        cat_frame.place(relx=0.03, rely=0.305, relwidth=0.96, relheight=0.695)
        scrollx = ctk.CTkScrollbar(
            cat_frame, orientation=HORIZONTAL, command=XView)
        scrolly = ctk.CTkScrollbar(
            cat_frame, orientation=VERTICAL, command=YView)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.category_table = ttk.Treeview(cat_frame, columns=(
            "cid", "Name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.configure(command=self.category_table.xview)
        scrolly.configure(command=self.category_table.yview)

        self.category_table.heading(
            "cid", text="Id", command=lambda: self.sort_column("cid", False))
        self.category_table.heading(
            "Name", text="Name", command=lambda: self.sort_column("Name", False))
        self.category_table["show"] = "headings"
        self.category_table.column("cid", width=10)
        self.category_table.column("Name", width=250)
        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()
    ###################### Funtions ###########################

    def add(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror(
                    "Error", "Category name must be required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?",
                            (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "This category already exist,try different", parent=self.root)
                else:
                    cur.execute("""Insert into category(Name) values(?)""", (
                        self.var_name.get(),))
                    con.commit()
                    self.show()
                    messagebox.showinfo(
                        "Success", "Category Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.category_table.focus()
        content = (self.category_table.item(f))
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror(
                    "Error", "Please select category from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",
                            (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Error,Try again", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from category where cid=?",
                                    (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def sort_column(self, col, reverse):
        # Obtener los elementos de la columna a ordenar
        data = [(self.category_table.set(row, col), row)
                for row in self.category_table.get_children('')]
        # Ordenar los elementos según el valor de la columna
        data.sort(reverse=reverse)
        for index, (val, row) in enumerate(data):
            # Reorganizar los elementos en el treeview
            self.category_table.move(row, '', index)
        # Cambiar la dirección de ordenación para la próxima vez que se haga clic en la columna
        self.category_table.heading(
            col, command=lambda: self.sort_column(col, not reverse))

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top


if __name__ == "__main__":
    root = ctk.CTk()
    odj = categoryClass(root)
    root.mainloop()
