import tkinter as tk
# import config
import os
import time
import ctypes
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox
# from config import config
# ventanas
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass


class IMS:
    def __init__(self, root):
        self.root = root
        SR_width = self.root.winfo_screenwidth()
        SR_height = self.root.winfo_screenheight()
        # self.root.geometry("%dx%d+0+0" %(SR_width, SR_height))  # ("1050x600+1+70")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), int(
                           root.winfo_screenheight()-(self.get_taskbar_height())*1.65)))
        self.root.title("| MSS - MILANES SMART SHOP || MENU ")
        self.root.focus_force()
        # ===Title===
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        self.icon_title = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "idispositivos.png")), size=(int(SR_width*0.03875), int(SR_height*0.06944)))

        title = ctk.CTkLabel(self.root, text="Milanes Smart Shop ", image=self.icon_title,
                             compound=LEFT, font=("roboto", 36, "bold"), anchor="w", padx=20)
        title.place(x=0.01, y=0.01, relwidth=0.98, relheight=0.08)

        # Btn logout
        self.icon_logout = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iclose.png")), size=(int(SR_width*0.0155), int(SR_height*0.0278)))
        btn_logout = ctk.CTkButton(self.root, text="", command=self.logout, fg_color="#222222",  hover_color="#DB3E39", border_color=(
            "#DA7E38", "#42a5f5"), image=self.icon_logout, cursor="hand2")
        btn_logout.place(relx=0.93, rely=0.02, relwidth=0.04, relheight=0.04)
        # relojito
        self.lbl_clock = ctk.CTkLabel(
            self.root, text="Bienvenido al sistema de MSS\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS", font=("roboto", 18, 'bold'), text_color="black", bg_color="#42a5f5")
        self.lbl_clock.place(relx=0, rely=0.08, relwidth=1, relheight=0.05)
        # Left MEnu
        self.Menulogo = PIL.Image.open("images/logo.png")
        self.Menulogo = self.Menulogo.resize(
            (int(SR_width*0.2249), int(SR_height*0.3334)), PIL.Image.ANTIALIAS)
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)
        #
        lbl_menulogo = ctk.CTkLabel(self.root, text="", image=self.Menulogo)
        lbl_menulogo.place(relx=0.01, rely=0.15, relwidth=0.2, relheight=0.35)
        #
        LeftMenu = ctk.CTkFrame(self.root, border_width=2)
        LeftMenu.place(relx=0.01, rely=0.47, relwidth=0.2, relheight=0.53)
        #
        lbl_menu = ctk.CTkLabel(LeftMenu, text="Menu", font=(
            "roboto", 18, 'bold')).pack(side=TOP, fill=X)
        #
        # self.icon_side = ctk.CTkImage(PIL.Image.open(
        # os.path.join(image_path, "isalir.png")), size=(55, 55))
        self.icon_side0 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iempleado.png")), size=(int(SR_width*0.03), int(SR_height*0.0410)))
        self.icon_side1 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iproveedor.png")), size=(int(SR_width*0.03), int(SR_height*0.0417)))
        self.icon_side2 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iinventario.png")), size=(int(SR_width*0.03), int(SR_height*0.0417)))
        self.icon_side3 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iproduct.png")), size=(int(SR_width*0.03), int(SR_height*0.0417)))
        self.icon_side4 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "ifacturar.png")), size=(int(SR_width*0.03), int(SR_height*0.0417)))
        self.icon_side5 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iventas.png")), size=(int(SR_width*0.03), int(SR_height*0.0417)))
        self.icon_side00 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iempleado.png")), size=(int(SR_width*0.1008), int(SR_height*0.1806)))
        self.icon_side11 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iproveedor.png")), size=(int(SR_width*0.11063), int(SR_height*0.2084)))
        self.icon_side22 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iinventario.png")), size=(int(SR_width*0.1008), int(SR_height*0.1806)))
        self.icon_side33 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iproduct.png")), size=(int(SR_width*0.0930), int(SR_height*0.166)))
        self.icon_side55 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "itventas.png")), size=(int(SR_width*0.1508), int(SR_height*0.2706)))
        # Botones menu
        btn_employee = ctk.CTkButton(LeftMenu, text="         Empleados", command=self.employee, fg_color="#222222",  hover_color="#1D2B8B", border_color=("#DA7E38", "#42a5f5"), border_width=4, corner_radius=15, image=self.icon_side0,
                                     compound=LEFT,  anchor="w", font=("roboto", 14, "bold"),  cursor="hand2").place(relx=0.01, rely=0.08, relwidth=0.98, relheight=0.145)  #
        btn_supplier = ctk.CTkButton(LeftMenu, text="         Suplidores", command=self.supplier, fg_color="#222222",  hover_color="#1D2B8B", border_color=("#DA7E38", "#42a5f5"), border_width=4, corner_radius=15, image=self.icon_side1,
                                     compound=LEFT,  anchor="w", font=("roboto", 14, "bold"),  cursor="hand2").place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.145)
        btn_category = ctk.CTkButton(LeftMenu, text="         Categorías", command=self.category, fg_color="#222222",  hover_color="#1D2B8B", border_color=("#DA7E38", "#42a5f5"), border_width=4, corner_radius=15, image=self.icon_side2,
                                     compound=LEFT,  anchor="w", font=("roboto", 14, "bold"),  cursor="hand2").place(relx=0.01, rely=0.38, relwidth=0.98, relheight=0.145)
        btn_product = ctk.CTkButton(LeftMenu, text="         Productos", command=self.product, fg_color="#222222",  hover_color="#1D2B8B", border_color=("#DA7E38", "#42a5f5"), border_width=4, corner_radius=15, image=self.icon_side3,
                                    compound=LEFT,  anchor="w", font=("roboto", 14, "bold"),  cursor="hand2").place(relx=0.01, rely=0.53, relwidth=0.98, relheight=0.145)
        btn_sales = ctk.CTkButton(LeftMenu, text="         Facturas", command=self.sales, fg_color="#222222",  hover_color="#1D2B8B", border_color=("#DA7E38", "#42a5f5"), border_width=4, corner_radius=15, image=self.icon_side4,
                                  compound=LEFT,  anchor="w", font=("roboto", 14, "bold"),  cursor="hand2").place(relx=0.01, rely=0.68, relwidth=0.98, relheight=0.145)
        btn_facturar = ctk.CTkButton(LeftMenu, text="         Ventas", command=self.billing, fg_color="#222222",  hover_color="#1D2B8B", border_color=("#DA7E38", "#42a5f5"), border_width=4, corner_radius=15, image=self.icon_side5,
                                     compound=LEFT,  anchor="w", font=("roboto", 14, "bold"),  cursor="hand2").place(relx=0.01, rely=0.83, relwidth=0.98, relheight=0.145)
        # Menu notificacion
        self.lbl_1 = ctk.CTkLabel(self.root, text="", image=self.icon_side00)
        self.lbl_1.place(relx=0.28, rely=0.22, relheight=0.18, relwidth=0.18)
        self.lbl_employee = ctk.CTkLabel(
            self.root, text="Total Empleados:\n[ 0 ]", text_color="#42a5f5", font=("roboto", 20, "bold"),)
        self.lbl_employee.place(relx=0.3, rely=0.395,)

        self.lbl_2 = ctk.CTkLabel(self.root, text="", image=self.icon_side11)
        self.lbl_2.place(relx=0.51, rely=0.22, relheight=0.18, relwidth=0.18)
        self.lbl_supplier = ctk.CTkLabel(
            self.root, text="Total Suplidores:\n[ 0 ]",  text_color="#42a5f5", font=("roboto", 20, "bold"),)
        self.lbl_supplier.place(relx=0.53, rely=0.395)

        self.lbl_3 = ctk.CTkLabel(self.root, text="", image=self.icon_side22)
        self.lbl_3.place(relx=0.75, rely=0.22, relheight=0.18, relwidth=0.18)
        self.lbl_category = ctk.CTkLabel(
            self.root, text="Total Categorías:\n[ 0 ]", text_color="#42a5f5", font=("roboto", 20, "bold"),)
        self.lbl_category.place(relx=0.76, rely=0.395)

        self.lbl_4 = ctk.CTkLabel(self.root, text="", image=self.icon_side33)
        self.lbl_4.place(relx=0.28, rely=0.57, relheight=0.18, relwidth=0.18)
        self.lbl_product = ctk.CTkLabel(
            self.root, text="Total Productos:\n[ 0 ]", text_color="#42a5f5", font=("roboto", 20, "bold"),)
        self.lbl_product.place(relx=0.3, rely=0.775)

        self.lbl_5 = ctk.CTkLabel(self.root, text="", image=self.icon_side55)
        self.lbl_5.place(relx=0.77, rely=0.52, )
        self.lbl_sales = ctk.CTkLabel(
            self.root, text="Total Ventas:\n[ 0 ]", text_color="#42a5f5", font=("roboto", 37, "bold"),)
        self.lbl_sales.place(relx=0.53, rely=0.69)
        # footer
        lbl_footer = ctk.CTkLabel(
            self.root, text=" | MSS - MILANES SMART SHOP System | ", font=("roboto", 15))
        lbl_footer.place(relx=0.23, rely=0.95, relwidth=0.75)

        self.update_content()
###############################################

    def employee(self):

        # self.new_win = Toplevel(self.root)
        self.new_win = ctk.CTkToplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
        self.new_win.grab_set()

    def supplier(self):
        self.new_win = ctk.CTkToplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
        self.new_win.grab_set()

    def category(self):
        self.new_win = ctk.CTkToplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
        self.new_win.grab_set()

    def product(self):
        self.new_win = ctk.CTkToplevel(self.root)
        self.new_obj = productClass(self.new_win)
        self.new_win.grab_set()

    def sales(self):
        self.new_win = ctk.CTkToplevel(self.root)
        self.new_obj = salesClass(self.new_win)
        self.new_win.grab_set()

    def billing(self):
        self.new_win = ctk.CTkToplevel(self.root)
        self.new_obj = BillClass(self.new_win)
        self.new_win.grab_set()

    def update_content(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select*from employee")
            employee = cur.fetchall()
            self.lbl_employee.configure(
                text=f"Total Empleados: [ {str(len(employee))} ]")
            cur.execute("select*from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.configure(
                text=f"Total Suplidores: [ {str(len(supplier))} ]")
            cur.execute("select*from category")
            Categorias = cur.fetchall()
            self.lbl_category.configure(
                text=f"Total Categorías: [ {str(len(Categorias))} ]")
            cur.execute("select*from product")
            product = cur.fetchall()
            self.lbl_product.configure(
                text=f"Total Productos: [ {str(len(product))} ]")
            cur.execute("select*from product")
            product = cur.fetchall()
            self.lbl_sales.configure(
                text=f"Total Ventas:\n[ {str(len(os.listdir('Fac')))} ]")

            time_ = time.strftime('%I:%M:%S')
            date_ = time.strftime('%d-%m-%Y')
            self.lbl_clock.configure(
                text=f"Bienvenido al sistema de MSS\t\t Fecha: {str(date_)}\t\t Hora: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system('python login.py')

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top


if __name__ == "__main__":
    root = ctk.CTk()
    odj = IMS(root)
    root.mainloop()
