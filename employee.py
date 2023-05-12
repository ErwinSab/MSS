import ctypes
import tkinter
import os
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox


class employeeClass:

    def __init__(self, root):
        self.root = root
        SR_width = self.root.winfo_screenwidth()
        SR_height = self.root.winfo_screenheight()
        self.root.geometry("{0}x{1}+{2}+{3}".format(int(root.winfo_screenwidth()-root.winfo_screenwidth()*0.22), int(
                           root.winfo_screenheight()-root.winfo_screenheight()*0.27),
            int(root.winfo_screenwidth()*0.21), int(root.winfo_screenheight()*0.165)))

        self.root.title("| MSS - MILANES SMART SHOP || Empleados ")
        self.root.focus_force()
        # ===============================
        self.Pframe = ctk.CTkFrame(self.root)
        self.Pframe.place(relx=1, rely=1, relwidth=1, relheight=1)
        # ALL Variables =======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        #
        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        # ===Iconos====
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
        self.lbl_Empleados = ctk.CTkLabel(
            self.root, text="Empleados", font=("roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5")
        self.lbl_Empleados.place(relx=0, rely=0.01, relwidth=1, relheight=0.05)

        # marco Buscar empleado
        SearchFrame = ctk.CTkFrame(self.root)
        SearchFrame.place(relx=0.01, rely=0.07, relwidth=0.35, relheight=0.11)
        Searchlabel = ctk.CTkLabel(SearchFrame, text="Busqueda de Empleados", font=(
            "roboto", 14, "bold"))
        Searchlabel.place(relx=0.01, rely=0.01, relwidth=0.98)

        self.cmb_search = ctk.CTkComboBox(SearchFrame, variable=self.var_searchby, values=(
            "Select", "Nombre", "Telefono", "Email"), border_color=("#DA7E38", "#42A5F5"), button_color=("#DA7E38", "#42A5F5"), state='readonly',
            justify=CENTER, font=("roboto", 15))
        self.cmb_search._entry.configure(
            readonlybackground=self.cmb_search._apply_appearance_mode(self.cmb_search._fg_color))
        self.cmb_search.place(relx=0.01, rely=0.42, relwidth=0.31)

        self.cmb_search.set("Select")

        txt_search = ctk.CTkEntry(SearchFrame, textvariable=self.var_searchtxt, border_color=("#DA7E38", "#42A5F5"), font=(
            "roboto", 15)).place(relx=0.33, rely=0.42, relwidth=0.33)
        btn_search = ctk.CTkButton(SearchFrame, command=self.search, image=self.icon_side, text="Buscar", cursor="hand2", font=(
            "roboto", 15), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5").place(relx=0.67, rely=0.42, relwidth=0.32)
        # === Tittle ===
        Datosframe = ctk.CTkFrame(self.root)
        Datosframe.place(relx=0.37, rely=0.07, relwidth=0.62, relheight=0.50)
        Datoslabel = ctk.CTkLabel(Datosframe, text="Datos del Empleado :", font=(
            "roboto", 15, "bold"))
        Datoslabel.place(relx=0.01, rely=0.01, relwidth=0.3)
        # Content
        lbl_empid = ctk.CTkLabel(Datosframe, text="Emp ID:", font=(
            "roboto", 12, "bold")).place(relx=0.44, rely=0.05, relwidth=0.09)
        txt_empid = ctk.CTkEntry(Datosframe, textvariable=self.var_emp_id, border_color=(
            "#DA7E38", "#42A5F5"), font=("roboto", 12, "bold")).place(relx=0.54, rely=0.05, relwidth=0.07)
        lbl_utype = ctk.CTkLabel(Datosframe, text="Tipo :", font=(
            "roboto", 12, "bold")).place(relx=0.68, rely=0.05, relwidth=0.07)
        cmb_utype = ctk.CTkComboBox(Datosframe, variable=self.var_utype, border_color=(
            "#DA7E38", "#42A5F5"), values=("Select", "Admin", "Normal"), button_color=("#DA7E38", "#42A5F5"), state="readonly", justify=CENTER, font=("roboto", 12))
        cmb_utype._entry.configure(
            readonlybackground=cmb_utype._apply_appearance_mode(cmb_utype._fg_color))
        cmb_utype.place(relx=0.76, rely=0.05, relwidth=0.23)
        cmb_utype.set("Select")
        lbl_name = ctk.CTkLabel(Datosframe, text="Nombre :", font=(
            "roboto", 12, "bold")).place(relx=0.01, rely=0.2, relwidth=0.11)
        txt_name = ctk.CTkEntry(Datosframe, textvariable=self.var_name, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.13, rely=0.2, relwidth=0.48)
        lbl_contact = ctk.CTkLabel(Datosframe, text="Telefono :", font=(
            "roboto", 12, "bold")).place(relx=0.62, rely=0.2, relwidth=0.14)
        txt_contact = ctk.CTkEntry(Datosframe, textvariable=self.var_contact, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.76, rely=0.2, relwidth=0.23)
        lbl_email = ctk.CTkLabel(Datosframe, text="   Email :", font=(
            "roboto", 12, "bold")).place(relx=0.01, rely=0.35, relwidth=0.11)
        txt_email = ctk.CTkEntry(Datosframe, textvariable=self.var_email, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.13, rely=0.35, relwidth=0.48)
        lbl_gender = ctk.CTkLabel(Datosframe, text="  Genero :", font=(
            "roboto", 12, "bold")).place(relx=0.62, rely=0.35, relwidth=0.14)
        cmb_gender = ctk.CTkComboBox(Datosframe, variable=self.var_gender, border_color=(
            "#DA7E38", "#42A5F5"), button_color=("#DA7E38", "#42A5F5"), values=("Select", "Masculino", "Femenino"), state='readonly', justify=CENTER, font=("roboto", 12))
        cmb_gender._entry.configure(
            readonlybackground=cmb_gender._apply_appearance_mode(cmb_gender._fg_color))
        cmb_gender.place(relx=0.76, rely=0.35, relwidth=0.23)
        cmb_gender.set("Select")
        lbl_dob = ctk.CTkLabel(Datosframe, text="D.O.B :", font=(
            "roboto", 12, "bold")).place(relx=0.25, rely=0.50, relwidth=0.14)
        txt_dob = ctk.CTkEntry(Datosframe, textvariable=self.var_dob, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.38, rely=0.50, relwidth=0.23)
        lbl_salary = ctk.CTkLabel(Datosframe, text="  Salario :", font=(
            "roboto", 12, "bold")).place(relx=0.62, rely=0.50, relwidth=0.14)
        txt_salary = ctk.CTkEntry(Datosframe, textvariable=self.var_salary, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.76, rely=0.50, relwidth=0.23)
        lbl_doj = ctk.CTkLabel(Datosframe, text="D.O.J :", font=(
            "roboto", 12, "bold")).place(relx=0.25, rely=0.65, relwidth=0.14)
        txt_doj = ctk.CTkEntry(Datosframe, textvariable=self.var_doj, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.38, rely=0.65, relwidth=0.23)
        lbl_password = ctk.CTkLabel(Datosframe, text="Password :", font=(
            "roboto", 12, "bold")).place(relx=0.62, rely=0.65, relwidth=0.14)
        txt_password = ctk.CTkEntry(Datosframe, textvariable=self.var_pass, show="*", border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold")).place(relx=0.76, rely=0.65, relwidth=0.23)

        lbl_address = ctk.CTkLabel(Datosframe, text="Dirección:", font=(
            "roboto", 12, "bold")).place(relx=0.05, rely=0.65)
        self.direcciontxt = ctk.CTkTextbox(Datosframe, border_color=(
            "#DA7E38", "#42A5F5"), font=(
            "roboto", 12, "bold"))
        self.direcciontxt.place(relx=0.02, rely=0.78,
                                relwidth=0.96, relheight=0.18)

        # LOgo
        self.Emplogo = PIL.Image.open("images/ipersonas.jpeg")
        self.Emplogo = self.Emplogo.resize((300, 125), PIL.Image.ANTIALIAS)
        self.Emplogo = ImageTk.PhotoImage(self.Emplogo)
        lbl_Emplogo = ctk.CTkLabel(self.root, text="", image=self.Emplogo)
        lbl_Emplogo.place(relx=0.028, rely=0.19, relwidth=0.318)
        # ===Buttons====
        btn_add = ctk.CTkButton(self.root, text="   Save", command=self.add, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side0).place(relx=0.025, rely=0.42, relwidth=0.15)
        btn_update = ctk.CTkButton(self.root, text="Update", command=self.update, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side1).place(relx=0.025, rely=0.50, relwidth=0.15)
        btn_delete = ctk.CTkButton(self.root, text="Delete", command=self.delete, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side2).place(relx=0.20, rely=0.42, relwidth=0.15)
        btn_clear = ctk.CTkButton(self.root, text="  Clear", command=self.clear, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=("#DA7E38", "#374BDC"), hover_color="#42A5F5", image=self.icon_side3).place(relx=0.20, rely=0.50, relwidth=0.15)
        # ===  Employee Details   =====
        emp_frame = ctk.CTkFrame(self.root)
        emp_frame.place(relx=0.01, rely=0.6, relwidth=0.98, relheight=0.39)
        scrollx = ctk.CTkScrollbar(
            emp_frame, orientation="horizontal", command=XView)
        scrolly = ctk.CTkScrollbar(
            emp_frame, orientation=VERTICAL, command=YView)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
            "eid", "Name", "Contact", "Email", "utype", "DoB", "DoJ", "Gender", "Salary", "Address"),  yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.configure(command=self.EmployeeTable.xview)
        scrolly.configure(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading(
            "eid", text="ID", command=lambda: self.sort_column("eid", False))
        self.EmployeeTable.heading(
            "Name", text="Nombre", command=lambda: self.sort_column("Name", False))
        self.EmployeeTable.heading(
            "Contact", text="Telf.", command=lambda: self.sort_column("Contact", False))
        self.EmployeeTable.heading(
            "Email", text="Email", command=lambda: self.sort_column("Email", False))
        self.EmployeeTable.heading(
            "utype", text="type", command=lambda: self.sort_column("utype", False))
        self.EmployeeTable.heading("DoB", text="DoB")
        self.EmployeeTable.heading("DoJ", text="DoJ")
        # self.EmployeeTable.heading("Pass", text="Pass")
        self.EmployeeTable.heading("Salary", text="Salario")
        self.EmployeeTable.heading("Gender", text="Genero")
        self.EmployeeTable.heading("Address", text="Dirreccion")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=50)
        self.EmployeeTable.column("Name", width=150)
        self.EmployeeTable.column("Contact", width=100)
        self.EmployeeTable.column("Email", width=200)
        self.EmployeeTable.column("utype", width=80)
        self.EmployeeTable.column("DoB", width=80)
        self.EmployeeTable.column("DoJ", width=80)
        # self.EmployeeTable.column("Pass", width=80)
        self.EmployeeTable.column("Salary", width=80)
        self.EmployeeTable.column("Gender", width=80)
        self.EmployeeTable.column("Address", width=500)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        ##

        self.show()
        # =========================================================================

    def add(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Se requiere almenos un ID de Empleado ", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Este ID de Empleado ya esta en uso,Intente uno diferente", parent=self.root)
                else:
                    cur.execute("""Insert into employee(eid, Name, Contact, Email, utype, DoB, DoJ, Pass, Gender, Salary, Address) values(?,?,?,?,?,?,?,?,?,?,?)""", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_utype.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_gender.get(),
                        self.var_salary.get(),
                        self.direcciontxt.get("0.0", "end")))
                    con.commit()
                    self.show()
                    messagebox.showinfo(
                        "Success", "Empleado creado satisfactoriamente!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                "select eid, Name, Contact, Email, utype, DoB, DoJ, Gender, Salary, Address from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_email.set(row[3])
        self.var_utype.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_gender.set(row[7])
        self.var_salary.set(row[8])
        self.direcciontxt.delete("0.0", 'end')
        self.direcciontxt.insert("0.0", row[9])
        # pass

        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        cur.execute("Select pass from employee where eid=?",
                    (self.var_emp_id.get(),))
        con.commit()
        rowpass = cur.fetchone()
        self.var_pass.set(rowpass[0])

    def update(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Se requiere un ID de empleado existente", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                con.commit()
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Este ID de empleado no existe", parent=self.root)
            else:
                cur.execute("""Update employee set Name=?,Email=?,Gender=?,Contact=?,DoB=?,DoJ=?,Pass=?,utype=?,Salary=?,Address=? where eid=? """, (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.var_salary.get(),
                            self.direcciontxt.get("0.0", "end"),
                            self.var_emp_id.get()))
                con.commit()
                self.show()
                messagebox.showinfo(
                    "Success", "Employee Updated Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",
                            (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from employee where eid=?",
                                    (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Normal")
        self.var_salary.set("")
        self.direcciontxt.delete("0.0", 'end')
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
                cur.execute("select * from employee where Name LIKE '%" +
                            self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(
                        *self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found !!!", parent=self.root)
            elif self.var_searchby.get() == "Telefono":
                cur.execute(
                    "select * from employee where Contact LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(
                        *self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found !!!", parent=self.root)
            else:
                cur.execute("select * from employee where " +
                            self.var_searchby.get() + " LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(
                        *self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found !!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def sort_column(self, col, reverse):
        # Obtener los elementos de la columna a ordenar
        data = [(self.EmployeeTable.set(row, col), row)
                for row in self.EmployeeTable.get_children('')]
        # Ordenar los elementos según el valor de la columna
        data.sort(reverse=reverse)
        for index, (val, row) in enumerate(data):
            # Reorganizar los elementos en el treeview
            self.EmployeeTable.move(row, '', index)
        # Cambiar la dirección de ordenación para la próxima vez que se haga clic en la columna
        self.EmployeeTable.heading(
            col, command=lambda: self.sort_column(col, not reverse))

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top


if __name__ == "__main__":
    root = ctk.CTk()
    odj = employeeClass(root)
    root.mainloop()
