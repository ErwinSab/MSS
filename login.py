import os
import sys
import PIL.Image
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox
import dashboard
from dashboard import IMS

# Modes: "System" (standard), "Dark", "Light"


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class LoginClass:
    ctk.set_appearance_mode("Dark")

    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+{2}+{3}".format(int(root.winfo_screenwidth()-root.winfo_screenwidth()*0.83), int(
                           root.winfo_screenheight()-root.winfo_screenheight()*0.43),
            int(root.winfo_screenwidth()*0.40), int(root.winfo_screenheight()*0.165)))
        self.root.title("  Milanes Smart Shop")
        self.root.focus_force()

        # === variables ===
        self.employeeId = StringVar()
        self.password = StringVar()
        # ===  Iconos   ===
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        self.icon_side0 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "ilogin.png")), size=(27, 27))

        self.icon_side1 = ctk.CTkImage(PIL.Image.open(
            os.path.join(image_path, "imsshop.png")), size=(27, 27))
        # ===  Logo    ===
        self.Emplogo = PIL.Image.open(resource_path("images/imsshop.png"))
        self.Emplogo = self.Emplogo.resize((200, 200), PIL.Image.ANTIALIAS)
        self.Emplogo = ImageTk.PhotoImage(self.Emplogo)
        lbl_Emplogo = ctk.CTkLabel(self.root, text="", image=self.Emplogo)
        lbl_Emplogo.place(relx=0.1, rely=0.08, relwidth=0.8, relheight=0.5)
        # === Tittle ===
        self.lbl_InicioS = ctk.CTkLabel(
            self.root, text="Inicio de Sesión", font=("roboto", 16, 'bold'), compound="center", bg_color="#101668").place(relx=0, rely=0.01, relwidth=1, relheight=0.08)

        # ===  Datos Login   =====
        self.login_frame = ctk.CTkFrame(self.root)
        self.login_frame.place(relx=0.05, rely=0.57,
                               relwidth=0.90, relheight=0.3)

        lbl_user = ctk.CTkLabel(self.login_frame, text="ID Empleado:", font=(
            "roboto", 16, "bold"), ).place(relx=0.13, rely=0.05)
        txt_user = ctk.CTkEntry(self.login_frame, textvariable=self.employeeId, font=(
            "roboto", 16), border_color=("#DA7E38", "#1D2B8B")).place(relx=0.075, rely=0.27, relwidth=0.85, relheight=0.2)
        lbl_pass = ctk.CTkLabel(self.login_frame, text="Contraseña:", font=(
            "roboto", 16, "bold"), ).place(relx=0.13, rely=0.5)
        txt_pass = ctk.CTkEntry(self.login_frame, textvariable=self.password, show="*", font=(
            "roboto", 16), border_color=("#DA7E38", "#1D2B8B")).place(relx=0.075, rely=0.7, relwidth=0.85, relheight=0.2)
        # ___ Buttons ___ #
        btn_enter = ctk.CTkButton(self.root, text="Ingresar", image=self.icon_side0, command=self.login, font=("roboto", 15), cursor="hand2", fg_color=(
            "#DA7E38", "#1D2B8B"), hover_color="#374BDC").place(relx=0.25, rely=0.89, relwidth=0.50, relheight=0.08)

    ###################### Funtions ###########################
    def login(self):
        con = sqlite3.connect(database=r'Data/ims.db')
        cur = con.cursor()
        try:
            if self.employeeId.get() == '' or self.password.get() == '':
                messagebox.showerror(
                    "Error", "Se requieren todos los datos", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND Pass=?",
                            (self.employeeId.get(), self.password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror(
                        "Error", "Los datos son invalidos", parent=self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system('python dashboard.py')
                        
                    else:
                        os.system("python billing.py")
                        self.root.destroy()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = ctk.CTk()
    odj = LoginClass(root)
    root.mainloop()
