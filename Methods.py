import mysql.connector
import Gui as g
import tkinter.messagebox as mb

# edit to connect database
mydb = mysql.connector.connect(host="localhost", user="----", passwd="-----", database="--------")
cursor = mydb.cursor()

var = 0
sex = "none"


def main():
    refresh_info()
    g.window.mainloop()


def refresh_info():
    cursor.execute("select * from student")
    g.listbox_right.delete(0,100)
    for i in cursor:
       g.listbox_right.insert("end", i)


def search_info():
    id = g.Entry_Student_ID.get()
    name = g.Entry_Student_Name.get()

    g.listbox_left.delete(0, 100)
    cursor.execute("select * from student where name = '" + name + "' OR id = '"+id+"' ")
    for i in cursor:
        g.listbox_left.insert("end", i)


def female_selected():
    global sex
    sex = "Female"
    return sex


def male_selected():
    global sex
    sex = "Male"
    return sex


def add_info():
    global sex
    name = g.Entry_Student_Name.get()
    grade = g.Entry_Grade.get()
    sex = sex
    id = g.Entry_Student_ID.get()
    date = g.Entry_Date.get()
    month = g.Entry_Month.get()
    year = g.Entry_Year.get()

    m = mb.askyesno("Student Adding", "Are You Sure add Student \nName = {}\nId = {}\nGrade = {}\nSex = {}\ndate = {}/{}/{}".format(name, id, grade, sex, date, month, year))

    if m == 1:
        cursor.execute("insert into student values ('"+name+"', '"+id+"', '"+grade+"', '"+sex+"', '"+date+"', '"+month+"', '"+year+"')")
        mb.showinfo("Student Adding", "Successfully added Student \nName = {}\nId = {}\nGrade = {}\nSex = {}\ndate = {}/{}/{}".format(name, id, grade, sex, date, month, year))
    else:
        mb.showinfo("Unsuccessfull", "Canceled")


def delete_student():
    id = g.Entry_Student_ID.get()
    n = mb.askyesno("Student Information", "Are You Sure Delete Student \n Id = {}".format(id))

    if n == 1:
        cursor.execute(" delete from student where id = '"+id+"' ")
        mb.showinfo("Student deleting", "Successfully deleted Student \n Id = {}".format(id))
    else:
        mb.showinfo("Unsuccessfully", "Canceled")


def reset_info():
    g.Entry_Student_Name.delete(0,40)
    g.Entry_Grade.delete(0, 40)
    g.Entry_Student_ID.delete(0, 40)
    g.Entry_Date.delete(0, 40)
    g.Entry_Month.delete(0, 40)
    g.Entry_Year.delete(0, 40)


if __name__ == "__main__":
    main()
