import tkinter
import time
import ctypes
# import config
import os
import tempfile
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox
# from config import config
# ventanas


class BillClass:

    def __init__(self, root):
        self.root = root
        # width = self.root.winfo_screenwidth()
        # height = self.root.winfo_screenheight()
        root.geometry(
            "{0}x{1}+0+0".format(root.winfo_screenwidth(), int(root.winfo_screenheight()-(self.get_taskbar_height())*1.65)))
        # self.root.geometry("%dx%d+0+0" % (width, height))
        self.root.title("| MSS - MILANES SMART SHOP || FACTURACION ")
        # =====================
        ctk.set_appearance_mode("Dark")
        # =====================
        # Variables
        self.cart_list = []
        self.chK_print = 0
        self.var_searchtxt = StringVar()
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
        self.icon_side4 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iall.png")), size=(27, 27))
        self.icon_side5 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iaddupdate.png")), size=(29, 29))
        self.icon_side6 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iprint.png")), size=(27, 27))
        self.icon_title = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "idispositivos.png")), size=(40, 40))
        # ===Title===
        title = ctk.CTkLabel(self.root, text="Milanes Smart Shop", image=self.icon_title,
                             compound=LEFT, font=("roboto", 32, "bold"), anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=0.95, relheight=0.05)

        # Btn logout

        self.icon_logout = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "iclose.png")), size=(34, 34))
        btn_logout = ctk.CTkButton(self.root, text="", command=self.logout, fg_color="#222222",  hover_color="#DB3E39", border_color=(
            "#DA7E38", "#42a5f5"), image=self.icon_logout, cursor="hand2")
        btn_logout.place(relx=0.93, rely=0.01, relwidth=0.04, relheight=0.04)

        # relojito
        self.lbl_clock = ctk.CTkLabel(
            self.root, text="Bienvenido al sistema de MSS\t\t Fecha:DD-MM-YYYY\t\t Hora:HH:MM:SS", font=("roboto", 20, "bold"), text_color='black', bg_color="#42A5F5")
        self.lbl_clock.place(relx=0, rely=0.06, relwidth=1, relheight=0.05)

        # Frame Lista de Products

        Productframe = ctk.CTkFrame(self.root)
        Productframe.place(relx=0.006, rely=0.115,
                           relwidth=0.3, relheight=0.88)
        self.lbl_Datos_prod = ctk.CTkLabel(Productframe, text="Todos los Productos", font=(
            "roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)
        # Product Search
        Searchlabel = ctk.CTkLabel(Productframe, text="Buscar Producto ~ Por Nombre", font=(
            "roboto", 15, "bold")).place(relx=0.01, rely=0.07, relwidth=0.66)
        btn_show_all = ctk.CTkButton(Productframe, command=self.show, image=self.icon_side4, text="Todos", cursor="hand2", font=(
            "roboto", 12), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#374BDC").place(relx=0.69, rely=0.07, relwidth=0.28)
        Searchlabel2 = ctk.CTkLabel(Productframe, text="Nombre P :", font=(
            "roboto", 15, "bold")).place(relx=0.01, rely=0.13, relwidth=0.25)
        txt_search = ctk.CTkEntry(Productframe, textvariable=self.var_searchtxt, font=(
            "roboto", 13), border_color=("#DA7E38", "#42a5f5")).place(relx=0.26, rely=0.13, relwidth=0.4)
        btn_search = ctk.CTkButton(Productframe, command=self.search, image=self.icon_side, text="Buscar", cursor="hand2", font=(
            "roboto", 13), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#42a5f5").place(relx=0.67, rely=0.13, relwidth=0.32)
        # Product Details   =====
        DProductframe = ctk.CTkFrame(Productframe)
        DProductframe.place(relx=0.01, rely=0.18,
                            relwidth=0.99, relheight=0.82)

        prod_frame = ctk.CTkFrame(DProductframe)
        prod_frame.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.95)
        scrollx = ctk.CTkScrollbar(
            prod_frame, orientation="horizontal", command=XView)
        scrolly = ctk.CTkScrollbar(
            prod_frame, orientation=VERTICAL, command=YView)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.producttable = ttk.Treeview(prod_frame, columns=(
            "pid", "name", "qty", "price", "status"),  yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.configure(command=self.producttable.xview)
        scrolly.configure(command=self.producttable.yview)

        self.producttable.heading(
            "pid", text="ID", command=lambda: self.sort_column("pid", False))
        self.producttable.heading(
            "name", text="Nombre", command=lambda: self.sort_column("pid", False))
        self.producttable.heading(
            "qty", text="Cant.", command=lambda: self.sort_column("pid", False))
        self.producttable.heading(
            "price", text="$", command=lambda: self.sort_column("pid", False))
        self.producttable.heading("status", text="Estado")
        self.producttable["show"] = "headings"
        self.producttable.column("pid", width=10)
        self.producttable.column("name", width=175)
        self.producttable.column("qty", width=45)
        self.producttable.column("price", width=75)
        self.producttable.column("status", width=50)
        self.producttable.pack(fill=BOTH, expand=1)
        self.producttable.bind('<ButtonRelease-1>', self.get_data)

        lbl_nota = ctk.CTkLabel(DProductframe, text="Nota:Cantida 0 para eliminar un producto de la Compra", font=(
            "roboto", 12, "bold"), text_color="Yellow").place(relx=0.01, rely=0.96, relwidth=0.98)

        # Frame Details Buys | Cart
        self.var_Cliname = StringVar()
        self.var_Clitelf = StringVar()
        cartframe = ctk.CTkFrame(self.root)
        cartframe.place(relx=0.307, rely=0.115, relwidth=0.442, relheight=0.88)
        self.lbl_Datos_client = ctk.CTkLabel(cartframe, text="Carrito | Cliente", font=(
            "roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)
        # Client Details
        Client_name = ctk.CTkLabel(cartframe, text="Nombre:", font=(
            "roboto", 13, "bold")).place(relx=0.01, rely=0.07, relwidth=0.13)
        txt_Client_name = ctk.CTkEntry(cartframe, textvariable=self.var_Cliname, font=(
            "roboto", 13), border_color=("#DA7E38", "#42a5f5")).place(relx=0.15, rely=0.07, relwidth=0.43)
        Client_phone = ctk.CTkLabel(cartframe, text="Telf:", font=(
            "roboto", 13, "bold"),).place(relx=0.6, rely=0.07, relwidth=0.10)
        txt_Client_phone = ctk.CTkEntry(cartframe, textvariable=self.var_Clitelf, font=(
            "roboto", 13), border_color=("#DA7E38", "#42a5f5")).place(relx=0.69, rely=0.07, relwidth=0.3)

        #### Frame Cal|Cart #####
        self.var_pid = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        # Calc
        self.var_cal_input = StringVar()

        cartframe1 = ctk.CTkFrame(cartframe, border_width=5)
        cartframe1.place(relx=0.01, rely=0.13, relwidth=0.49, relheight=0.7)

        self.txt_cal_input = ctk.CTkEntry(cartframe1, state='readonly', border_width=5, textvariable=self.var_cal_input, justify='right', font=(
            "roboto", 32, "bold")).place(relx=0.05, rely=0.03, relwidth=0.92, relheight=0.13)
        #  Buttons

        btn_7 = ctk.CTkButton(cartframe1, text="7", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            7), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.028, rely=0.19, relwidth=0.23, relheight=0.17)
        btn_8 = ctk.CTkButton(cartframe1, text="8", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            8), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.27, rely=0.19, relwidth=0.23, relheight=0.17)
        btn_9 = ctk.CTkButton(cartframe1, text="9", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            9), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.51, rely=0.19, relwidth=0.23, relheight=0.17)
        btn_div = ctk.CTkButton(cartframe1, text="/", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            '/'), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.75, rely=0.19, relwidth=0.23, relheight=0.17)
        btn_4 = ctk.CTkButton(cartframe1, text="4", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            4), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.028, rely=0.38, relwidth=0.23, relheight=0.17)
        btn_5 = ctk.CTkButton(cartframe1, text="5", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            5), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.27, rely=0.38, relwidth=0.23, relheight=0.17)
        btn_6 = ctk.CTkButton(cartframe1, text="6", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            6), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.51, rely=0.38, relwidth=0.23, relheight=0.17)
        btn_rest = ctk.CTkButton(cartframe1, text="-", cursor="hand2", font=("roboto", 30, 'bold'), command=lambda: self.get_input(
            '-'), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.75, rely=0.38, relwidth=0.23, relheight=0.17)
        btn_1 = ctk.CTkButton(cartframe1, text="1", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            1), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.028, rely=0.57, relwidth=0.23, relheight=0.17)
        btn_2 = ctk.CTkButton(cartframe1, text="2", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            2), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.27, rely=0.57, relwidth=0.23, relheight=0.17)
        btn_3 = ctk.CTkButton(cartframe1, text="3", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            3), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.51, rely=0.57, relwidth=0.23, relheight=0.17)
        btn_x = ctk.CTkButton(cartframe1, text="X", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            '*'), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.75, rely=0.57, relwidth=0.23, relheight=0.17)
        btn_C = ctk.CTkButton(cartframe1, text="C", cursor="hand2", font=("roboto", 24, 'bold'), command=self.clear_cal, fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.028, rely=0.76, relwidth=0.23, relheight=0.20)
        btn_0 = ctk.CTkButton(cartframe1, text="0", cursor="hand2", font=("roboto", 24, 'bold'), command=lambda: self.get_input(
            0), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.27, rely=0.76, relwidth=0.23, relheight=0.20)
        btn_igual = ctk.CTkButton(cartframe1, text="=", cursor="hand2", font=("roboto", 24, 'bold'), command=self.perfom_cal, fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.51, rely=0.76, relwidth=0.23, relheight=0.20)
        btn_sum = ctk.CTkButton(cartframe1, text="+", cursor="hand2", font=("roboto", 30, 'bold'), command=lambda: self.get_input(
            '+'), fg_color=(
            "#DA7E38", "#42a5f5"), text_color='black', hover_color="#374BDC").place(relx=0.75, rely=0.76, relwidth=0.23, relheight=0.20)

        # Cart

        cartframe2 = ctk.CTkFrame(cartframe)
        cartframe2.place(relx=0.5, rely=0.13, relwidth=0.49, relheight=0.7)

        self.lbl_Lproducts = ctk.CTkLabel(cartframe2, text=" Total de Productos [00]", font=(
            "roboto", 16, 'bold'), text_color='black', compound="center", bg_color="#42A5F5")
        self.lbl_Lproducts.place(
            relx=0.01, rely=0.001, relwidth=0.99, relheight=0.06)

        List_cart_frame = ctk.CTkFrame(cartframe2)
        List_cart_frame.place(relx=0.01, rely=0.061,
                              relwidth=0.99, relheight=0.94)
        scrollx = ctk.CTkScrollbar(
            List_cart_frame, orientation="horizontal", command=XView)
        scrolly = ctk.CTkScrollbar(
            List_cart_frame, orientation=VERTICAL, command=YView)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.CartTable = ttk.Treeview(List_cart_frame, columns=(
            "pid", "name", "qty", "price"),  yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.configure(command=self.CartTable.xview)
        scrolly.configure(command=self.CartTable.yview)
        self.CartTable.heading("pid", text="ID")
        self.CartTable.heading("name", text="Nombre")
        self.CartTable.heading("qty", text="Cant.")
        self.CartTable.heading("price", text="$")
        self.CartTable["show"] = "headings"
        self.CartTable.column("pid", width=20)
        self.CartTable.column("name", width=120)
        self.CartTable.column("qty", width=40)
        self.CartTable.column("price", width=100)
        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>", self.get_data_cart)
        #
        P_name = ctk.CTkLabel(cartframe, text="Nombre de Producto:", font=(
            "roboto", 15, "bold")).place(relx=0.01, rely=0.83, relwidth=0.50)
        ent_product = ctk.CTkEntry(cartframe, state='readonly', textvariable=self.var_name, font=(
            "roboto", 16, 'bold'), border_color=("#DA7E38", "#42a5f5")).place(relx=0.01, rely=0.87, relwidth=0.50)

        P_price = ctk.CTkLabel(cartframe, text="Precio por Cantidad:", font=(
            "roboto", 15, "bold")).place(relx=0.52, rely=0.83, relwidth=0.29)
        ent_precio = ctk.CTkEntry(cartframe, state='readonly', textvariable=self.var_price, font=(
            "roboto", 16, 'bold'), border_color=("#DA7E38", "#42a5f5")).place(relx=0.52, rely=0.87, relwidth=0.29)

        P_cant = ctk.CTkLabel(cartframe, text="Cantidad:", font=(
            "roboto", 15, "bold")).place(relx=0.82, rely=0.83, relwidth=0.17)
        ent_cantidad = ctk.CTkEntry(cartframe, textvariable=self.var_qty, font=(
            "roboto", 16, 'bold'), border_color=("#DA7E38", "#42a5f5")).place(relx=0.82, rely=0.87, relwidth=0.17)

        self.lbl_instock = ctk.CTkLabel(cartframe, text="En stock", font=(
            "roboto", 16, "bold"))
        self.lbl_instock.place(relx=0.01, rely=0.93, relwidth=0.28)

        btn_clear = ctk.CTkButton(cartframe, text=" Limpiar", command=self.clear_cart, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#374BDC", image=self.icon_side3).place(relx=0.3, rely=0.93, relwidth=0.28)
        btn_add = ctk.CTkButton(cartframe, text=" Add | Update ", command=self.add_update_cart, cursor="hand2", font=(
            "roboto", 15, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#374BDC", image=self.icon_side1).place(relx=0.6, rely=0.93, relwidth=0.38)

        # Frame Factura Total
        Facframe = ctk.CTkFrame(self.root)
        Facframe.place(relx=0.75, rely=0.115, relwidth=0.247, relheight=0.88)
        self.lbl_Datos_f = ctk.CTkLabel(Facframe, text="Factura del Cliente", font=(
            "roboto", 18, 'bold'), text_color='black', compound="center", bg_color="#42A5F5").place(relx=0, rely=0.01, relwidth=1, relheight=0.05)
        #

        self.txt_bill_area = ctk.CTkTextbox(Facframe, border_color=(
            "#DB3E39", "#1F7945"), font=("roboto", 12, "bold"),)
        self.txt_bill_area.place(relx=0.02, rely=0.08,
                                 relwidth=0.96, relheight=0.74)
        #
        self.lbl_amnt = ctk.CTkLabel(Facframe, text="Total Factura\n[0]", font=(
            "roboto", 16, "bold"))
        self.lbl_amnt.place(relx=0.01, rely=0.85, relwidth=0.40)
        self.lbl_discount = ctk.CTkLabel(Facframe, text="Itbis\n[18%]", font=(
            "roboto", 16, "bold"))
        self.lbl_discount.place(relx=0.41, rely=0.85, relwidth=0.24)
        self.lbl_net = ctk.CTkLabel(Facframe, text="Tolt.Itbis\n[0]", font=(
            "roboto", 16, "bold"))
        self.lbl_net.place(relx=0.64, rely=0.85, relwidth=0.29)
        btn_print = ctk.CTkButton(Facframe, text='', command=self.print_bill, cursor="hand2", font=(
            "roboto", 12, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#374BDC", image=self.icon_side6).place(relx=0.01, rely=0.93, relwidth=0.15)
        btn_clear_all = ctk.CTkButton(Facframe, text="Todo", command=self.clear_all, cursor="hand2", font=(
            "roboto", 12, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#374BDC", image=self.icon_side2).place(relx=0.17, rely=0.93, relwidth=0.27)
        btn_generate = ctk.CTkButton(Facframe, text="Generar | Imprimir", command=self.generate_bill, cursor="hand2", font=(
            "roboto", 12, 'bold'), fg_color=(
            "#DA7E38", "#374BDC"), hover_color="#374BDC", image=self.icon_side5).place(relx=0.45, rely=0.93, relwidth=0.54)

        self.show()
        self.update_date_time()
        #########################################    FUNTIONS    #########################################

    def get_input(self, num):
        xnum = self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perfom_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                "select pid, name, qty, price,status from product where status='Act'")
            rows = cur.fetchall()
            self.producttable.delete(*self.producttable.get_children())
            for row in rows:
                self.producttable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error", "Es necesario algun criterio para La Busqueda", parent=self.root)
            else:
                cur.execute(
                    "select pid, name, qty, price,status from product where Name LIKE '%" + self.var_searchtxt.get()+"%'and status='Act'")
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

    def get_data(self, ev):
        f = self.producttable.focus()
        content = (self.producttable.item(f))
        row = content['values']
        # pid,name,stock,price
        self.var_pid.set(row[0])
        self.var_name.set(row[1])
        self.var_qty.set('1')
        self.lbl_instock.configure(text=f'En stock [{str(row[2])}]')
        self.var_stock.set(row[2])
        self.var_price.set(row[3])

    def get_data_cart(self, ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        # pid,name,qty,stock
        self.var_pid.set(row[0])
        self.var_name.set(row[1])
        self.var_qty.set(row[2])
        self.var_price.set(row[3])
        self.lbl_instock.configure(text=f'En stock [{str(row[4])}]')
        self.var_stock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror(
                "Error", "Por Favor seleccione un [Producto] de la lista", parent=self.root)
        elif self.var_qty.get() == '':
            messagebox.showerror(
                "Error", "La [Cantidad] es requerida", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror(
                "Error", "[Cantidad] inválida !", parent=self.root)
        else:
            # price_cal = int(self.var_qty.get())*float(self.var_price.get())
            # price_cal = float(price_cal)
            price_cal = self.var_price.get()
            # pid,name,qty,stock
            cart_data = [self.var_pid.get(), self.var_name.get(
            ), self.var_qty.get(), price_cal, self.var_stock.get()]
            # Updating Cart
            presente = "no"
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    presente = "yes"
                    break
                index_+-1
            if presente == 'yes':
                op = messagebox.askyesno(
                    'Confirm', 'Producto ya existe\n Desea actualizar | Removerlo del Carrito de compras ', parent=self.root)
                if op == True:
                    if self.var_qty.get() == '0':
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][3] = price_cal  # pri
                        self.cart_list[index_][2] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            # pid,name,qty,stock
            self.bill_amnt = self.bill_amnt+float(row[3])*int(row[2])

        self.discount = (self.bill_amnt*18)/100
        net_pay = self.bill_amnt+self.discount
        self.lbl_amnt.configure(
            text=f'Total Factura\n RD${str(self.bill_amnt)}')
        self.lbl_net.configure(text=f'Tolt.Itbis\nRD${str(net_pay)}')
        self.lbl_Lproducts.configure(
            text=f' Total de Productos [{str(len(self.cart_list))}]')

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('', 'end', values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f'Error due to :{str(ex)}', parent=self.root)

    def generate_bill(self):
        if self.var_Cliname.get() == "" or self.var_Clitelf.get() == "":
            messagebox.showerror(
                'Error', f'Son requeridos los [ Datos del cliente ] ', parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror(
                "Error", f'Por favor ingrese un articulo en el [ carrito ] ')
        else:
            # ===BILL TOP===
            self.bill_top()
            # ===BILL MID===
            self.bill_middle()
            # ===BILL BOT===
            self.bill_bottom()
            fp = open(f'Fac/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', 'end'))
            fp.close()
            messagebox.showinfo(
                "Saved", "Factura ha sido generada !!! ", parent=self.root)
            self.chK_print = 1

    def bill_top(self):
        self.invoice = (time.strftime('%Y%m%d'))+'-'+(time.strftime("%H%M%S"))
        #
        bill_top_temp = f'''
\t      Milanes Smart Shop
\n
          Telefono | Whatsapp: 829-906-6504 
\t      @milanessmartshop1

{str('='*38)}
Nombre Cliente:{self.var_Cliname.get()}
Telf: {self.var_Clitelf.get()}\t\t\tDate: {str(time.strftime('%d/%m/%Y'))}

No. Factura: {str(self.invoice)}
{str('='*38)}
 Nombre :\t     Cant.\t Und.\tTotal
{str('='*38)}'''
        self.txt_bill_area.delete("1.0", "end")
        self.txt_bill_area.insert("1.0", bill_top_temp)

    def bill_bottom(self):
        totalt = self.bill_amnt
        bill_bottom_temp = f'''
{str('='*38)}
Sub-Total :\tRD${self.bill_amnt}
Itbis 18% : \tRD$  00.0
Total Factura :\tRD${totalt}
{str('='*38)}\n
Maria Trinidad Sanchez#37,Haina,San Cristobal
\t!!!! Gracias por su compra !!!!
'''
        self.txt_bill_area.insert("end", bill_bottom_temp)

    def bill_middle(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                # pid,name,qty,price,stock
                pid = row[0]
                name = row[1]
                qty = int(row[4])-int(row[2])
                if int(row[2]) == int(row[4]):
                    status = 'Des'
                if int(row[2]) != int(row[4]):
                    status = 'Act'
                price = float(row[3])*int(row[2])
                pund = row[3]
                pund = str(pund)
                price = str(price)
                self.txt_bill_area.insert(
                    END, '\n'+name+'\n'+'\t'+row[2]+'.0'+'\t'+'$'+pund+'\t'+'RD$'+price)
                # ===UPDATE PRODUCT TABLE====
                cur.execute(
                    'Update product set qty=?,status=? where pid=?', (qty, status, pid))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear_cart(self):
        # pid,name,qty,stock
        self.var_pid.set("")
        self.var_name.set("")
        self.var_qty.set("")
        self.var_price.set("")
        self.lbl_instock.configure(text=f'En stock')
        self.var_stock.set("")

    def clear_all(self):
        del self.cart_list[:]
        self.var_searchtxt.set('')
        self.var_Cliname.set('')
        self.var_Clitelf.set("")
        self.txt_bill_area.delete('1.0', 'end')
        self.lbl_Lproducts.configure(
            text=f' Total de Productos [0]')
        self.lbl_amnt.configure(
            text=f'Total Factura\n RD$ [0]')
        self.lbl_net.configure(text=f'Tolt.Itbis\nRD$ [0]')
        self.lbl_Lproducts.configure(
            text=f' Total de Productos [{str(len(self.cart_list))}]')
        self.chK_print = 0
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_ = time.strftime('%I:%M:%S')
        date_ = time.strftime('%d-%m-%Y')
        self.lbl_clock.configure(
            text=f"Bienvenido al sistema de MSS\t\t Fecha: {str(date_)}\t\t Hora: {str(time_)}")
        self.lbl_clock.after(200, self.update_date_time)

    def print_bill(self):
        if self.chK_print == 1:
            messagebox.showinfo(
                'Imprimir', "Porfavor espere mientras se imprime.....", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', 'end'))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror(
                'Imprimir', 'Porfavor genera una factura ,para imprimir el recibo...', parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system('python login.py')

    def get_taskbar_height(self):
        """Obtiene la altura de la barra de tareas"""
        taskbar_hwnd = ctypes.windll.user32.FindWindowW('Shell_TrayWnd', None)
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(taskbar_hwnd, ctypes.byref(rect))
        return rect.bottom - rect.top

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


if __name__ == "__main__":
    root = ctk.CTk()
    odj = BillClass(root)
    root.mainloop()
