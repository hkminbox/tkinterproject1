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
    
#     course_val1 = coursevar1.get()
#     course_val2 = coursevar2.get()
#     course_val3 = coursevar3.get()
#     courses_list = []
#     for i in (course_val1, course_val2, course_val3):
#         if i != "":
#             courses_list.append(i)
#             
#     
#     courses_val = ','.join(courses_list)
#     
#     userName_val = entryUserName.get()
#     password_val = entryPassword.get()
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

def viewWindow():
    topView = Toplevel()
    topView.title('View Data')
    topView.geometry('550x500')
    labelHeading = Label(topView, text = "RESULTS", height = 2, width = 31, font = ("bold", 20), anchor= CENTER)
    labelHeading.place(x=0, y= 0)
    
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "database1")
    cur = myconn.cursor()
    sql_statement = "SELECT * FROM Details"
    cur.execute(sql_statement)
    data = cur.fetchall()
    
    myconn.commit()
    myconn.close()
#     Name, Age, Sex, Phone ,Blood group, and Rh



#     canvas = Canvas(topView, width=300, height=400,scrollregion=(0,0,500,500))
# #     myscrollbar=Scrollbar(topView,orient="vertical")
# #     canvas.configure(yscrollcommand=myscrollbar.set)
# #     myscrollbar.config(command=canvas.yview)
#      
#     canvas.pack(side="left")
#     scrollbar = Scrollbar(topView, orient=VERTICAL, command=canvas.yview)
#     scrollbar.pack( side = RIGHT, fill = Y )


#     canvas = Canvas(topView)
#     frame = Frame(canvas)
#     scrollbar = Scrollbar(topView, orient="vertical", command=canvas.yview)
#     canvas.configure(yscrollcommand= scrollbar.set)
#     scrollbar.pack( side = RIGHT, fill = Y )
#     canvas.pack(side="left", fill="both", expand=True)
#     canvas.create_window((4,4), window=frame, anchor="nw")
#     frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    
#     scrollbar = Scrollbar(topView)
#     scrollbar.pack( side = RIGHT, fill = Y )
#     canvas = Canvas(topView, width=550, height=500, yscrollcommand=scrollbar.set)
#     canvas.pack(side="left", fill="both", expand=0)
#     frame = Frame(canvas)
#     canvas.create_window((4,4), window=frame, anchor="nw")

    frame = ttk.Frame(topView)
    canvas = Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    
    tuple_headings = ("Id","Name","Age" ,"Gender" ,"Phone" ,"Blood group" ,"Rh")
    for index_heading, data_heading in enumerate(tuple_headings):
        Label(scrollable_frame, text= data_heading, width = 10, anchor= "w").grid(row=0, column= index_heading)
    

    offset1=0
    for index, dat in enumerate(data):
        for column_no in range(7):
            Label(scrollable_frame, text=dat[column_no], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + column_no)
            
#         Label(canvas, text=dat[0], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 0)
#         Label(canvas, text=dat[1], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 1)
#         Label(canvas, text=dat[2], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 2)
#         Label(canvas, text=dat[3], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 3)
#         Label(canvas, text=dat[4], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 4)
#         Label(canvas, text=dat[5], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 5)
#         Label(canvas, text=dat[6], width = 10, anchor= 'w').grid(row=index+1, column=offset1 + 6)
    frame.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    topView.mainloop()
    
    
    
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
    labelHeading = Label(topAdd, text = "ADD REPORT", height = 2, width = 31, font = ("bold", 20), anchor= CENTER)
    labelHeading.place(x=0, y= 0)
    
    
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

root = Tk()
root.geometry('500x500')
root.title("Admin")

addImage = PhotoImage(file = 'Add.png')
viewImage = PhotoImage(file = 'View.png')
labelHeading = Label(root, text = "BLOOD TYPING TEST", height = 2, width = 31, font = ("bold", 20), anchor= CENTER)
labelHeading.place(x=0, y= 0)

addButton = Button(root, text = "Add data", image = addImage, command = addWindow)
addButton.place(x=185, y= 215, anchor = CENTER)
viewButton = Button(root, text = "View data", image = viewImage, command = viewWindow)
viewButton.place(x=315, y= 215, anchor = CENTER)


# labelName = Label(root, text = "Name", height = 2).place(x=61, y= 80, relheight = 0.1, relwidth = 0.3)
# labelEmail = Label(root, text = "Email", height = 2).place(x=61, y= 126, relheight = 0.1, relwidth = 0.3)
# labelGender = Label(root, text = "Gender", height = 2).place(x=61, y= 172, relheight = 0.1, relwidth = 0.3)
# labelHQualification = Label(root, text = "H_Qualification", height = 2).place(x=61, y= 218, relheight = 0.1, relwidth = 0.3)
# labelCourses = Label(root, text = "Courses", height = 2).place(x=61, y= 264, relheight = 0.1, relwidth = 0.3)
# labelUser = Label(root, text = "Username", height = 2).place(x=61, y= 310, relheight = 0.1, relwidth = 0.3)
# labelPassword = Label(root, text = "Password", height = 2).place(x=61, y= 356, relheight = 0.1, relwidth = 0.3)
# 
# entryName = Entry(root)
# entryName.place(x=178, y= 100, anchor = "w")
# entryEmail = Entry(root)
# entryEmail.place(x=178, y= 147, anchor = "w")
# 
# gender_radio = IntVar()
# radiobutton_m = Radiobutton(root, text = "Male", value = 1, variable = gender_radio)
# radiobutton_m.place(x=178, y= 182)
# radiobutton_m = Radiobutton(root, text = "Female", value = 2, variable = gender_radio)
# radiobutton_m.place(x=250, y= 182)
# 
# qualification_combo = ttk.Combobox(root)
# qualification_combo['values'] = ("--SELECT--", "BTech", "MTech", "BCA", "MCA")
# qualification_combo.current(0)
# qualification_combo.place(x=178, y= 230)
# 
# coursevar1 = StringVar()
# coursevar2 = StringVar()
# coursevar3 = StringVar()
# course_check1 = Checkbutton(root, text = "Java", variable = coursevar1, offvalue = "", onvalue = "Java")
# course_check2 = Checkbutton(root, text = "Python", variable = coursevar2, offvalue = "", onvalue = "Python")
# course_check3 = Checkbutton(root, text = "PHP", variable = coursevar3, offvalue = "", onvalue = "PHP")
# course_check1.place(x=178, y= 275)
# course_check2.place(x=225, y= 275)
# course_check3.place(x=288, y= 275)
# 
# entryUserName = Entry(root)
# entryUserName.place(x=178, y= 332, anchor = "w")
# entryPassword = Entry(root, show = '*')
# entryPassword.place(x=178, y= 380, anchor = "w")



root.mainloop()
