# importing the required modules  
import tkinter as tk                    # importing the tkinter module as tk  
from tkinter import ttk                 # importing the ttk module from the tkinter library  
from tkinter import messagebox          # importing the messagebox module from the tkinter library  
import sqlite3 as sql                   # importing the sqlite3 module as sql  

# defining the function to add tasks to the list  
def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string,))  
        list_update()  
        task_field.delete(0, 'end')  

# defining the function to update the list  
def list_update():  
    clear_list()  
    for task in tasks:  
        task_listbox.insert('end', task)  

# defining the function to delete a task from the list  
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:  
            tasks.remove(the_value)  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        

# function to delete all tasks from the list  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box:  
        while len(tasks) != 0:  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  

# function to clear the list  
def clear_list():  
    task_listbox.delete(0, 'end')  

# function to close the application  
def close():  
    print(tasks)  
    guiWindow.destroy()  

# function to retrieve data from the database  
def retrieve_database():  
    while len(tasks) != 0:  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  

# main function  
if "_name_" == "_main_":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List Manager")  
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#1A1A1A")  # Dark mode background

    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  

    tasks = []  

    # Defining frames with dark mode colors
    header_frame = tk.Frame(guiWindow, bg = "#1A1A1A")  
    functions_frame = tk.Frame(guiWindow, bg = "#1A1A1A")  
    listbox_frame = tk.Frame(guiWindow, bg = "#1A1A1A")  

    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  

    # Header label with Optima font
    header_label = ttk.Label(  
        header_frame,  
        text = "My To-Do List",  
        font = ("Optima", "28", "bold"),  
        background = "#1A1A1A",  
        foreground = "#E0E0E0"  # Light grey color for text
    )  
    header_label.pack(padx = 20, pady = 20)  

    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Optima", "12", "bold"),  
        background = "#1A1A1A",  
        foreground = "#E0E0E0"  
    )  
    task_label.place(x = 30, y = 40)  

    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Optima", "12"),  
        width = 18  
    )  
    task_field.place(x = 30, y = 80)  

    # Button styles for a professional look
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", background = "#333333", foreground = "#E0E0E0", font=("Optima", 10), padding=6)
    style.map("TButton", background=[("active", "#444444")])

    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  

    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#333333",  # Darker background for the listbox
        foreground = "#E0E0E0",  # Light grey text
        selectbackground = "#555555",  
        selectforeground = "#E0E0E0",  
        font = ("Optima", 10)  
    )  
    task_listbox.place(x = 10, y = 20)  

    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()  
# importing the required modules  
import tkinter as tk                    # importing the tkinter module as tk  
from tkinter import ttk                 # importing the ttk module from the tkinter library  
from tkinter import messagebox          # importing the messagebox module from the tkinter library  
import sqlite3 as sql                   # importing the sqlite3 module as sql  

# defining the function to add tasks to the list  
def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string,))  
        list_update()  
        task_field.delete(0, 'end')  

# defining the function to update the list  
def list_update():  
    clear_list()  
    for task in tasks:  
        task_listbox.insert('end', task)  

# defining the function to delete a task from the list  
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:  
            tasks.remove(the_value)  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        

# function to delete all tasks from the list  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box:  
        while len(tasks) != 0:  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  

# function to clear the list  
def clear_list():  
    task_listbox.delete(0, 'end')  

# function to close the application  
def close():  
    print(tasks)  
    guiWindow.destroy()  

# function to retrieve data from the database  
def retrieve_database():  
    while len(tasks) != 0:  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  

# main function  
if "_name_" == "_main_":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List Manager")  
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#1A1A1A")  # Dark mode background

    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  

    tasks = []  

    # Defining frames with dark mode colors
    header_frame = tk.Frame(guiWindow, bg = "#1A1A1A")  
    functions_frame = tk.Frame(guiWindow, bg = "#1A1A1A")  
    listbox_frame = tk.Frame(guiWindow, bg = "#1A1A1A")  

    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  

    # Header label with Optima font
    header_label = ttk.Label(  
        header_frame,  
        text = "My To-Do List",  
        font = ("Optima", "28", "bold"),  
        background = "#1A1A1A",  
        foreground = "#E0E0E0"  # Light grey color for text
    )  
    header_label.pack(padx = 20, pady = 20)  

    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Optima", "12", "bold"),  
        background = "#1A1A1A",  
        foreground = "#E0E0E0"  
    )  
    task_label.place(x = 30, y = 40)  

    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Optima", "12"),  
        width = 18  
    )  
    task_field.place(x = 30, y = 80)  

    # Button styles for a professional look
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", background = "#333333", foreground = "#E0E0E0", font=("Optima", 10), padding=6)
    style.map("TButton", background=[("active", "#444444")])

    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  

    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#333333",  # Darker background for the listbox
        foreground = "#E0E0E0",  # Light grey text
        selectbackground = "#555555",  
        selectforeground = "#E0E0E0",  
        font = ("Optima", 10)  
    )  
    task_listbox.place(x = 10, y = 20)  

    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()