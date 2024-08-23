from tkinter import * 
from tkinter.filedialog import asksaveasfile
from cgitb import reset
screen =Tk()  
screen.geometry("800x800")
screen.title("Register Form ")
screen.configure(bg="#235489", borderwidth=5, highlightthickness=7, highlightcolor="#ffffff")
formheading = Label(text="Register Form", font=( "Calibri",25,"bold"), bg="#235489", fg="#f8ea04", width="500", height= "3")   
formheading.pack()

firstname_text = Label(text="Name:", font=("Calibri", 14, "bold"), bg = "#235489", fg="#ffffff")
firstname_text.place(x=50, y= 100)
firstname = StringVar()
firstname_entry = Entry(textvariable=firstname, width="60", border="3", highlightbackground="#e674f4")
firstname_entry.place(x=170, y= 100)

lastname_text = Label(text="Family Name:", font=("Calibri", 14, "bold"), bg = "#235489", fg="#ffffff")
lastname_text.place(x=50, y= 150)
lastname = StringVar()
lastname_entry = Entry(textvariable=firstname, width="60", border="3", highlightbackground="#e674f4")
lastname_entry.place(x=170, y= 150)


education_text = Label(text="Education:", font=("Calibri", 14, "bold"), bg= "#235489" , fg="#ffffff")
education_text.place(x=50, y = 200)
education = StringVar()



education1 = Radiobutton(screen, text="Pupil", variable=education, value="Pupil", font=("Calibri", 14), bg="#235489",fg="#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x=150, y= 250)


education2 = Radiobutton(screen, text="Diploma", variable=education, value="Diploma", font=("Calibri", 14), bg="#235489",fg="#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x=250, y= 250)


education3 = Radiobutton(screen, text="Bachelor", variable=education, value="Bachelor", font=("Calibri", 14), bg="#235489",fg="#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x=350, y= 250)


education4 = Radiobutton(screen, text="Master", variable=education, value="Master", font=("Calibri", 14), bg="#235489",fg="#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x=450, y= 250)


education5 = Radiobutton(screen, text="PHD", variable=education, value="PHD", font=("Calibri", 14), bg="#235489",fg="#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x=550, y= 250)


education6 = Radiobutton(screen, text="Post doctorate", variable=education, value="Post doctorate", font=("Calibri", 14), bg="#235489",fg="#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x=650, y= 250)

gender_text = Label(text="Gender:", font=("Calibri", 14, "bold"), bg= "#235489" , fg="#ffffff")
gender_text.place(x=50, y = 300)
gender = StringVar()

gender1 = Radiobutton(screen, text="Woman", variable=gender, value="woman", font=("Calibri", 14), bg= "#235489", fg= "#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x= 150, y=350)


gender2 = Radiobutton(screen, text="Man", variable=gender, value="man", font=("Calibri", 14), bg= "#235489", fg= "#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x= 250, y=350)


gender3 = Radiobutton(screen, text="Prefer to not say", variable=gender, value="not_say", font=("Calibri", 14), bg= "#235489", fg= "#ffffff", activebackground="#1f2421", activeforeground="#ff6f59").place(x= 350, y=350)







mainloop()   