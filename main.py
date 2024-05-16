import tkinter as tk
#import pathlib
from tkinter import ttk
import webbrowser
import sqlite3
from mypackage.paper1 import tradeRobot
import pygame
from cryptography.fernet import Fernet
import os

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Aspire7\\Documents\\diplomnajaTkinter\\sound_04684.wav")  # Замените "path_to_your_sound_file.wav" на путь к вашему аудиофайлу
    pygame.mixer.music.play()

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.main()
        self.db = db
        self.key = key
        self.view_records()
        

    def main(self):
        toolbar = tk.Frame(bg='#8A2BE2', bd=2)
        toolbar.pack(side=tk.LEFT, fill=tk.Y)
        play_sound()
        btn_open_dialog = tk.Button(toolbar, width=11, height=2, text='Add paper', command=self.open_dialog, bg='white', bd=3,
                                    compound=tk.TOP)
        btn_open_dialog.pack(anchor=tk.NW)# Расположить кнопку в верхнем Левом углу
        btn_open_dialog.pack(padx=10, pady=10, ipadx=10, ipady=10)
        btn_edit_dialog = tk.Button(toolbar, width=11, height=2, text='EDIT', bg='white', bd=3,
                                    compound=tk.TOP, command=self.open_update_dialog)      
        btn_edit_dialog.pack(padx=10, pady=10, ipadx=10, ipady=10)
        btn_edit_dialog.pack(anchor=tk.NW)
        btn_delet_dialog = tk.Button(toolbar, width=11, height=2, text='DELETE', bg='white', bd=3, compound=tk.TOP, command=self.delete_records)
        btn_delet_dialog.pack(padx=10, pady=10, ipadx=10, ipady=10)
        btn_delet_dialog.pack(anchor=tk.NW)
        label5 = tk.Label(toolbar, text="Ilja_Virkunen®",bg='#8A2BE2', fg="white", font=('Courier New', 8))
        label5.pack(padx=5, pady=5, ipadx=5, ipady=5)
        label5.pack(side=tk.LEFT, anchor=tk.NW)
        btn_swedbank = tk.Button(text='Swedbank', width=10, height=3, bg='orange', font=('Bolt', 14, 'underline'), command=self.button_clickSwed)
        btn_swedbank.pack(padx=10, pady=10, ipadx=10, ipady=10)
        btn_swedbank.place(x=150, y=370)
        btn_LHV = tk.Button(text='LHV', width=10, height=3, bg='RED', font=('Bolt', 14, 'underline'), command=self.button_clickLhv)
        btn_LHV.pack(padx=10, pady=10, ipadx=10, ipady=10)
        btn_LHV.place(x=300, y=370)
        btn_SEB = tk.Button(text='SEB', width=10, height=3, bg='light green', font=('Bolt', 14, 'underline'), command=self.button_clickSeb)
        btn_SEB.place(x=450, y=370)
        stock = tradeRobot()
        frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=7, highlightbackground="#DAA520", width=10, height=10)
        frame.place(x=600, y=350, width=270, height=100)
        label = tk.Label(master=frame, text=stock, width=300, height=60, fg="white", bg="blue", font=('	Courier New', 14))
        label.pack()

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total_sum', 'quantity'),
                                 height=15, show='headings')
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("description", width=265, anchor=tk.CENTER)
        self.tree.column("costs", width=150, anchor=tk.CENTER)
        self.tree.column("total_sum", width=150, anchor=tk.CENTER)
        self.tree.column("quantity", width=150, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("description", text='name')
        self.tree.heading("costs", text='total_sum')
        self.tree.heading("total_sum", text='transactions buy/sell')
        self.tree.heading("quantity", text='quantity')
                                      


        self.tree.pack()

    def records(self, description, costs, total_sum, quantity):
        self.db.insert_data(description, costs, total_sum, quantity)
        self.view_records()

    def update_record(self, description, costs, total_sum, quantity):
        self.db.c.execute('''UPDATE paperrr SET description=?, costs=?, total_sum=?, quantity=? WHERE id=?''',
                   (description, costs, total_sum, quantity, self.tree.set(self.tree.selection()[0], '#1')))
                       
        self.db.conn.commit()
        self.view_records()
    
    def view_records(self):
        self.tree.delete(*self.tree.get_children())
        self.db.c.execute('''SELECT * FROM paperrr''')
        rows = self.db.c.fetchall()
        for row in rows:
            decrypted_row = [self.db.decrypt_data(cell) if isinstance(cell, bytes) else cell for cell in row]
            self.tree.insert('', 'end', values=decrypted_row)




    def delete_records(self):
        for selection_item in self.tree.selection():
            item_id = self.tree.set(selection_item, '#1')  # Получить id элемента
            self.db.c.execute('''DELETE FROM paperrr WHERE id=?''', (item_id,))
        self.db.conn.commit()
        self.view_records()

        self.db.conn.commit()
        self.view_records()

    def open_dialog(self):
        Child()
    def button_clickSwed(self):
        url = "https://www.swedbank.ee"  # Замените на нужный веб-сайт
        webbrowser.open(url)
    def button_clickLhv(self):
        url = "https://www.lhv.ee"
        webbrowser.open(url)
    def button_clickSeb(self):
        url = "https://www.seb.ee"
        webbrowser.open(url)
    def open_update_dialog(self):
        Update()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Add buy/sell')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        self.icon_path = 'C:\\Users\\Aspire7\\Documents\\diplomnajaTkinter\\logoico.ico'
        label_description = tk.Label(self, text='Name:')
        label_description.place(x=50, y=30)
        label_select = tk.Label(self, text='Transactions buy/sell:')
        label_select.place(x=50, y=60)
        label_total_sum = tk.Label(self, text='total_sum:')
        label_total_sum.place(x=50, y=90)
        label_quantity = tk.Label(self, text='quantity:')
        label_quantity.place(x=50, y=120)
        self.iconbitmap(self.icon_path)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=30)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=90)
        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.place(x=200, y=120)

        self.combobox = ttk.Combobox(self, values=[u"Buy", u"Sell"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=60)
        style = ttk.Style()
        style.configure('Green.TButton', foreground='black', background='Green', font=('Arial', 10))
        style.configure('Red.TButton',border=10, foreground='black', background='red')
        btn_cancel = ttk.Button(self, text='cancel', command=self.destroy, style='Red.TButton')
        btn_cancel.place(x=300, y=170)


        self.btn_ok = ttk.Button(self, text='Add', style='Green.TButton', width=10)
        self.btn_ok.place(x=210, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(), self.entry_money.get(), self.combobox.get(), self.entry_quantity.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit', style='Green.TButton' )
        btn_edit.place(x=210, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_money.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_quantity.get()))                                                                       
        self.btn_ok.destroy()
class KeyManager:
    def __init__(self, filename):
        self.filename = filename

    def generate_or_load_key(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.filename, 'wb') as f:
                f.write(key)
        return key

class DB:

    def __init__(self, key_filename):
        self.key_manager = KeyManager(key_filename)
        self.key = self.key_manager.generate_or_load_key()
        self.cipher = Fernet(self.key)
        self.conn = sqlite3.connect('paperrr.db')
        self.c = self.conn.cursor()
        self.c.execute(
                    '''CREATE TABLE IF NOT EXISTS paperrr (id INTEGER PRIMARY KEY, description BLOB, costs BLOB, total_sum BLOB, quantity BLOB)''')
        self.conn.commit()

    def encrypt_data(self, data):
        data = self.cipher.encrypt(data.encode())
        return data
    
    def decrypt_data(self, data):
        decrypted_data = self.cipher.decrypt(data).decode()
        return decrypted_data
    
    def insert_data(self, description, costs, total_sum, quantity):
        description = self.encrypt_data(description)
        costs = self.encrypt_data(costs)
        total_sum = self.encrypt_data(str(total_sum))
        quantity = self.encrypt_data(str(quantity))

        self.c.execute(
            '''INSERT INTO paperrr (description, costs, total_sum, quantity) VALUES (?, ?, ?, ?)''',
            (description, costs, total_sum, quantity)
        )
        self.conn.commit()
        print("Данные добавлены.")

if __name__ == "__main__":
    root = tk.Tk()
    db = DB('fernet_key.key')
    key = Fernet.generate_key()
    app = Main(root)
    root.configure(bg='black')
    app.pack()
    root.title("Securities Assistant")
    root.geometry("880x462+300+200")
    root.resizable(False, False)
    icon_path = icon_path = 'C:\\Users\\Aspire7\\Documents\\diplomnajaTkinter\\logoico.ico' # Замените на путь к вашей иконке
    root.iconbitmap(icon_path)
    root.mainloop()
