# Filen er ikke i bruk
from asyncio.windows_events import NULL
import mysql.connector
import tkinter as tk
import numpy as np
from tkinter import messagebox

print("Connecting to database...")
database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Hallo123",
    database="utleie"
)
print("Connected to database.")

print("Loading all data...")
cursor = database.cursor()
cursor.execute("SELECT * FROM komponenter")
cursor = cursor.fetchall()
components = np.array(cursor)
component_names = []
for component in components:
    component_names.append(component[1])
cursor = cursor.clear()
print("Loaded all data.")

def focus1(event):
    name_field.focus_set()

def focus2(event):
    phone_field.focus_set()
 
def focus3(event):
    email_field.focus_set()
 
def focus4(event):
    component_field.focus_set()
 
def clear():
     
    name_field.delete(0, tk.END)
    phone_field.delete(0, tk.END)
    email_field.delete(0, tk.END)

def insert():
    clear()


if __name__ == "__main__":
     
    root = tk.Tk()
    root.configure(background='dark green')
    root.title("Utlånsoversikt")
    root.geometry("500x250")
 
    heading = tk.Label(root, text="Filtrer og søk etter utlån", bg="dark green")
    name_label = tk.Label(root, text="Navn", bg="dark green")
    phone_label = tk.Label(root, text="Telefonnummer", bg="dark green")
    email_label = tk.Label(root, text="E-postadresse", bg="dark green")
    component_label = tk.Label(root, text="Komponent", bg="dark green")
    
    heading.grid(row=0, column=1)
    name_label.grid(row=1, column=0)
    phone_label.grid(row=2, column=0)
    email_label.grid(row=3, column=0)
    component_label.grid(row=4, column=0)
    
    name_field = tk.Entry(root)
    phone_field = tk.Entry(root)
    email_field = tk.Entry(root)
    component_name = tk.StringVar(root)
    component_field = tk.OptionMenu(root, component_name, *component_names)

    name_field.bind("<Return>", focus1)
    phone_field.bind("<Return>", focus2)
    email_field.bind("<Return>", focus3)
    component_field.bind("<Return>", focus4)

    name_field.grid(row=1, column=1, ipadx="100")
    phone_field.grid(row=2, column=1, ipadx="100")
    email_field.grid(row=3, column=1, ipadx="100")
    component_field.grid(row=4, column=1, ipadx="100")

    submit = tk.Button(root, text="Søk etter utlån", fg="Black",
                            bg="Grey", command=insert)
    submit.grid(row=5, column=1)
    root.mainloop()