import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import ttk, simpledialog


def get_ids():
    mycursor.execute("SELECT ID FROM Marvel")
    return [item[0] for item in mycursor.fetchall()]


def get_movie_by_id(id):
    mycursor.execute("SELECT * FROM Marvel WHERE ID = %s", (id,))
    return mycursor.fetchone()


def get_all_movies():
    mycursor.execute("SELECT * FROM Marvel")
    return mycursor.fetchall()


def select_id(event):
    selected_id = combobox.get()
    movie = get_movie_by_id(selected_id)
    text_box.delete(1.0, tk.END)  # Clear the text box
    if movie is not None:
        text_box.insert(tk.END, ' '.join(str(item) for item in movie))  # Insert the movie info into the text box


def list_all():
    movies = get_all_movies()
    text_box.delete(1.0, tk.END)  # Clear the text box
    for movie in movies:
        text_box.insert(tk.END, ' '.join(str(item) for item in movie) + '\n')  # Insert the movie info into the text box


def add_movie():
    dialog = simpledialog.Dialog(root, title="Add Movie")
    label = tk.Label(dialog, text="Enter movie information (ID, MOVIE, DATE, MCU PHASE) separated by tabs:")
    label.pack()
    entry = tk.Entry(dialog)
    entry.pack()
    ok_button = tk.Button(dialog, text="Ok", command=lambda: save_movie(entry.get(), dialog))
    ok_button.pack()
    cancel_button = tk.Button(dialog, text="Cancel", command=lambda: dialog.destroy())
    cancel_button.pack()


def save_movie(movie_info, dialog):
    data = movie_info.split('\t')  # Split by tabs
    id = int(data[0])
    movie = data[1]
    date = datetime.strptime(data[2], "%B%d,%Y").date()  # Convert to date
    phase = data[3]

    # Insert data into the table
    sql = "INSERT INTO Marvel (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"
    val = (id, movie, date, phase)
    mycursor.execute(sql, val)
    mydb.commit()

    # Update the combo box values
    ids = get_ids()
    combobox['values'] = ids

    dialog.destroy()  # Close the dialog


# Connect to your database (replace 'your_database' with your actual database name)
mydb = mysql.connector.connect(
    host="localhost",
    user="egecangurcan",
    password="1234",
    database="Marvel"
)

mycursor = mydb.cursor()

# Create table
mycursor.execute("CREATE TABLE IF NOT EXISTS Marvel (ID INT, MOVIE VARCHAR(255), DATE DATE, MCU_PHASE VARCHAR(255))")

# Open the file and read it line by line
with open('Marvel.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split('\t')  # Split by tabs
        id = int(data[0])
        movie = data[1]
        date = datetime.strptime(data[2], "%B%d,%Y").date()  # Convert to date
        phase = data[3]

        # Insert data into the table
        sql = "INSERT INTO Marvel (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"
        val = (id, movie, date, phase)
        mycursor.execute(sql, val)

    mydb.commit()

# a. List all Movies.
mycursor.execute("SELECT * FROM Marvel")
for movie in mycursor.fetchall():
    print(movie)

# b. Remove TheIncredibleHulk from the table.
mycursor.execute("DELETE FROM Marvel WHERE MOVIE = 'TheIncredibleHulk'")
mydb.commit()  # Don't forget to commit changes made by DELETE, INSERT, or UPDATE queries

# c. List all Phase 2 Movies.
mycursor.execute("SELECT * FROM Marvel WHERE MCU_PHASE = 'Phase2'")
for movie in mycursor.fetchall():
    print(movie)

# d. Fix the date of Thor:Ragnarok. The date should be 2017 not 2019.
new_date = datetime.strptime("November3,2017", "%B%d,%Y").date()
mycursor.execute("UPDATE Marvel SET DATE = %s WHERE MOVIE = 'Thor:Ragnarok'", (new_date,))
mydb.commit()


root = tk.Tk()
root.title("Marvel Movies")

# (dropdown list)
ids = get_ids()
combobox = ttk.Combobox(root, values=ids)
combobox.bind("<<ComboboxSelected>>", select_id)
combobox.pack()

# Create the text box
text_box = tk.Text(root, height=1, width=30)
text_box.pack()

# Add and list buttons
add_button = tk.Button(root, text="Add", command=add_movie)
add_button.pack(side=tk.LEFT)

list_all_button = tk.Button(root, text="List All", command=list_all)
list_all_button.pack(side=tk.RIGHT)

root.mainloop()
