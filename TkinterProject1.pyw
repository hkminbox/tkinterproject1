'''
CREATE TABLE Details(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name CHAR(40),
    Age INT,
    Sex ENUM("Male","Female"),
    Phone BIGINT,
    `Blood group` ENUM("A","B","AB","O"),
    Rh ENUM ("Positive", "Negative")
);
'''

from tkinter import *
from tkinter import ttk, Toplevel
from tkinter import messagebox
import mysql.connector
topSearch = None
def saveData():
    global entryName
    global entryAge
    global gender_radio
    global entryPhone
    global group_combo
    global type_radio
    
    name_val = entryName.get()
    age_val = entryAge.get()
    
    gender_val = None
    gender_num = gender_radio.get()
    if gender_num == 1:
        gender_val = "Male"
    elif gender_num == 2:
        gender_val = "Female"
    
    phone_val = entryPhone.get()
    
    group_val = group_combo.get()
    
    type_val = None
    type_num = type_radio.get()
    if type_num == 1:
        type_val = "Positive"
    elif type_num == 2:
        type_val = "Negative"

    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "database1")
    cur = myconn.cursor()
    sql_statement = "INSERT INTO Details (Name, Age, Sex, Phone, `Blood group`, Rh) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name_val, age_val, gender_val, phone_val, group_val, type_val)
    cur.execute(sql_statement, val)
    myconn.commit()
    myconn.close()
    messagebox.showinfo("Data Added", "Report Added succesfully")

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def viewAllWindow():
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "database1")
    cur = myconn.cursor()
    sql_statement = "SELECT * FROM Details"
    cur.execute(sql_statement)
    data = cur.fetchall()
    myconn.close()
    
    if data != []:
        viewSearch(data)
    else:
        messagebox.showinfo("No Data", "Database is Empty")

def viewSearch(data):
    global topSearch
    if(topSearch is not None):
        topSearch.destroy()
    topSearch = Toplevel()
    topSearch.title('Search')
    topSearch.geometry('575x500')
    topSearch.minsize(width=575, height=500)
    topSearch.maxsize(width=575, height=500)
    labelHeading = Label(topSearch, text = "SEARCH RESULTS ", height = 1, width = 21, font = ("bold", 18), anchor= CENTER)
    labelHeading.pack()
    
    
    heading_frame = ttk.Frame(topSearch)
    tuple_headings = ("Id","Name","Age" ,"Gender" ,"Phone" ,"Blood group" ,"Rh")
    for index_heading, data_heading in enumerate(tuple_headings):
        if index_heading == 0:
            Label(heading_frame, text= data_heading, width = 5, anchor= 'w', relief="groove", bg = 'PeachPuff2').grid(row=0, column= index_heading)
        else:
            Label(heading_frame, text= data_heading, width = 10, anchor= 'w', relief="groove", bg = 'PeachPuff2').grid(row=0, column= index_heading)
    heading_frame.pack()

    frame = ttk.Frame(topSearch)
    canvas = Canvas(frame, width=550, height=500)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    

    for index, dat in enumerate(data):
        for column_no in range(7):
            color =  lambda index: 'light cyan' if index%2 else None
            if column_no == 0:
                Label(scrollable_frame, text=dat[column_no], width = 10, anchor= CENTER, bg = color(index)).grid(row=index+1, column=column_no)
            else:
                Label(scrollable_frame, text=dat[column_no], width = 10, anchor= 'w', bg = color(index)).grid(row=index+1, column=column_no)

    frame.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    topSearch.mainloop()
    
    
    
def addWindow():
    global entryName
    global entryAge
    global gender_radio
    global entryPhone
    global group_combo
    global type_radio
    
    
    topAdd = Toplevel()
    topAdd.title('Add Data')
    topAdd.geometry('500x500')
    labelHeading_add = Label(topAdd, text = "ADD REPORT", height = 2, width = 31, font = ("bold", 20), anchor= CENTER)
    labelHeading_add.place(x=0, y= 0)
    
    
    labelName = Label(topAdd, text = "Name", height = 2).place(x=91, y= 80, relheight = 0.1, relwidth = 0.3)
    labelAge = Label(topAdd, text = "Age", height = 2).place(x=91, y= 126, relheight = 0.1, relwidth = 0.3)
    labelGender = Label(topAdd, text = "Gender", height = 2).place(x=91, y= 172, relheight = 0.1, relwidth = 0.3)
    labelPhone = Label(topAdd, text = "Phone", height = 2).place(x=91, y= 218, relheight = 0.1, relwidth = 0.3)
    labelGroup = Label(topAdd, text = "Blood group", height = 2).place(x=91, y= 264, relheight = 0.1, relwidth = 0.3)
    labelRh = Label(topAdd, text = "Rh", height = 2).place(x=91, y= 310, relheight = 0.1, relwidth = 0.3)
    
    entryName = Entry(topAdd)
    entryName.place(x=228, y= 100, anchor = "w")
    entryAge = Entry(topAdd)
    entryAge.place(x=228, y= 147, anchor = "w")
    
    gender_radio = IntVar()
    radiobutton_m = Radiobutton(topAdd, text = "Male", value = 1, variable = gender_radio)
    radiobutton_m.place(x=228, y= 185)
    radiobutton_f = Radiobutton(topAdd, text = "Female", value = 2, variable = gender_radio)
    radiobutton_f.place(x=300, y= 185)
    
    entryPhone = Entry(topAdd)
    entryPhone.place(x=228, y= 240, anchor = "w")
    
    group_combo = ttk.Combobox(topAdd)
    group_combo['values'] = ("--SELECT--", "A","B","AB","O")
    group_combo.current(0)
    group_combo.place(x=228, y= 277)
    
    type_radio = IntVar()
    radiobutton_p = Radiobutton(topAdd, text = "Positive", value = 1, variable = type_radio)
    radiobutton_p.place(x=228, y= 325)
    radiobutton_n = Radiobutton(topAdd, text = "Negative", value = 2, variable = type_radio)
    radiobutton_n.place(x=300, y= 325)
    
    submitButton = Button(topAdd, text = "SUBMIT", width = 20, bg = 'brown', fg = 'white', command = saveData)
    submitButton.place(x=245, y= 430, anchor = CENTER)

    topAdd.mainloop()
    
def sql_generate(entryFindPhone, find_group_combo):
    find_phone_entry = entryFindPhone.get()
    find_group = find_group_combo.get()
    sql_find = None
    if find_phone_entry == "" and find_group != "--SELECT--":
        sql_find = "SELECT * FROM Details WHERE `Blood group` = " + "'"  + find_group + "'"
    elif find_phone_entry != "" and find_group == "--SELECT--":
        sql_find = "SELECT * FROM Details WHERE Phone = " + "'" + find_phone_entry + "'"
    elif find_phone_entry != "" and find_group != "--SELECT--":
        sql_find = "SELECT * FROM Details WHERE Phone = " + find_phone_entry + " AND `Blood group` = " + "'" + find_group + "'"
    return sql_find
    
def findDisplay(entryFindPhone, find_group_combo):
    global topFind
    sql_statement = sql_generate(entryFindPhone, find_group_combo)
    if(sql_statement != None):
        myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "database1")
        cur = myconn.cursor()
        cur.execute(sql_statement)
        data = cur.fetchall()
        myconn.close()
        
        if data != []:
            viewSearch(data)
        else:
            messagebox.showinfo("No Data", "No report matches search")
            topFind.focus()
    else:
        messagebox.showinfo("No Data", "No report matches search")
        topFind.focus()
        


def findWindow():
    global topFind
    topFind = Toplevel()
    topFind.title('Add Data')
    topFind.geometry('500x500')
    
    labelHeading_find = Label(topFind, text = "FIND REPORT", height = 2, width = 31, font = ("bold", 20), anchor= CENTER)
    labelHeading_find.place(x=0, y= 0)
    
    labelFindPhone = Label(topFind, text = "Phone Number", height = 2).place(x=91, y= 80, relheight = 0.1, relwidth = 0.3)
    labelFindGroup = Label(topFind, text = "Blood Group", height = 2).place(x=91, y= 126, relheight = 0.1, relwidth = 0.3)
    
    entryFindPhone = Entry(topFind, width = 30)
    entryFindPhone.place(x=228, y= 105, anchor = "w")
    
    find_group_combo = ttk.Combobox(topFind, width = 27)
    find_group_combo['values'] = ("--SELECT--", "A","B","AB","O")
    find_group_combo.current(0)
    find_group_combo.place(x=228, y= 140)
    

    findConditionButton = Button(topFind, text = "FIND", width = 30, bg = 'black', fg = 'white', command = lambda: findDisplay(entryFindPhone, find_group_combo))
    findConditionButton.place(x=275, y= 250, anchor = CENTER)
    
    topFind.mainloop()

root = Tk()
root.geometry('500x500')
root.title("Admin")

addImage = PhotoImage(file = 'Add.png')
viewAllImage = PhotoImage(file = 'ViewAll.png')
findImage = PhotoImage(file = 'Find.png')

labelHeading = Label(root, text = "BLOOD TYPING TEST", height = 2, width = 31, font = ("bold", 20), anchor= CENTER)
labelHeading.place(x=0, y= 0)

addButton = Button(root, text = "Add data", image = addImage, command = addWindow)
addButton.place(x=185, y= 215, anchor = CENTER)
viewButton = Button(root, text = "View all data", image = viewAllImage, command = viewAllWindow)
viewButton.place(x=315, y= 215, anchor = CENTER)
findButton = Button(root, text = "Find", image = findImage, command = findWindow)
findButton.place(x=250, y= 300, anchor = CENTER)

root.mainloop()
