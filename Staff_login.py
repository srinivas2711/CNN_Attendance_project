'''
ADMIN MODULE 
'''
import cv2
import os
import tensorflow
import numpy as np
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tensorflow.keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img
import datetime
today = datetime.date.today()
print("If you are new user, Please insert your biometric details to train...... ")
ch=input("Are you a new user? Type y|Y or n|N to continue..........")
valid_user=0
flag=1
ins=[]
# connect with mysql database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@123",
    port="3306",
    database="project",
    )
c = connection.cursor()
if ch == "n" or ch == "N":
    print("Only admin or staff can insert student images")
    print("Please login to continue")
    root = tk.Tk()
    # create a function to close the window
    def close_window():
        root.destroy()

    # width and height
    w = 400
    h = 260

    class loginForm:
        def __init__(self, master):
            self.master = master
            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()
            x = (ws - w) / 2
            y = (hs - h) / 2
            self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))
            self.frame = tk.Frame(self.master, bg="#fff")
            self.btnsFrame = tk.Frame(self.frame, bg="#fff", padx=40, pady=15)
            self.windowTitle = tk.Label(
            self.frame,
            text="Admin login",
            bg="#fff",
            fg="green",
            font=("TimesNewRoman", 20),
            pady=30,
            )
            self.usernameLabel = tk.Label(
            self.frame, text="Username:", bg="#fff", font=("Verdana", 16)
            )
            self.usernameTextbox = tk.Entry(
            self.frame, font=("Verdana", 12), width=25, borderwidth="2", relief="ridge"
            )
            self.passwordLabel = tk.Label(
            self.frame, text="Password:", bg="#fff", font=("Verdana", 16)
            )
            self.passwordTextbox = tk.Entry(
                self.frame,
                show="*",
                font=("Verdana", 12),
                width=25,
                borderwidth="2",
                relief="ridge",
            )
            self.btnLogin = tk.Button(
            self.btnsFrame,
            text="Login",
            bg="green",
            font=("Verdana", 12),
            fg="#fff",
            padx=25,
            pady=10,
            command=self.login_func,
            )
            self.btnCancel = tk.Button(
            self.btnsFrame,
            text="Cancel",
            bg="orange",
            font=("Verdana", 12),
            fg="#fff",
            padx=25,
            pady=10,
            command=close_window,
            )
            # end create widgets
            # start place widgets
            self.frame.pack(fill="both")
            self.windowTitle.grid(row=0, column=0, columnspan=2)
            self.usernameLabel.grid(row=1, column=0)
            self.usernameTextbox.grid(row=1, column=1)
            self.passwordLabel.grid(row=2, column=0, pady=(10, 0))
            self.passwordTextbox.grid(row=2, column=1, pady=(10, 0))
            self.btnsFrame.grid(row=3, column=0, columnspan=2, pady=10)
            self.btnLogin.grid(row=0, column=0, padx=(0, 35))
            self.btnCancel.grid(row=0, column=1)
            # create a function to login
        def login_func(self):
            username = self.usernameTextbox.get()
            password = self.passwordTextbox.get()
            select_query = ("SELECT * FROM `admin` WHERE `staff_name` = %s and `password` = %s")
            vals = (
                username,
                password,
            )
            c.execute(select_query, vals)
            # print(c.fetchall())
            user = c.fetchone()
            if user is not None:
                messagebox.showinfo("Login", "VALID CREDENTIALS! PRESS OK TO CONTINUE")
                root.withdraw()
                valid_user=1
                root.destroy()
                if(valid_user):
                    print("Camera Activated For Image Capture!")
                    print('#'*5,"Enter Student class",'#'*5)
                    class OptionSelectionUI:
                        def __init__(self):
                            self.selected_option = None
                            self.window = tk.Tk()
                            self.window.title("Option Selection")
                            self.window.geometry("300x150")
                            self.option_var = tk.StringVar(value="Option 1")
                            self.option1_radio = tk.Radiobutton(self.window, text="1st_M.sc_CS", variable=self.option_var, value="1st_M.sc_CS")
                            self.option2_radio = tk.Radiobutton(self.window, text="2nd_M.sc_CS", variable=self.option_var, value="2nd_M.sc_CS")
                            self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)
                            self.option1_radio.pack(pady=10)
                            self.option2_radio.pack(pady=10)
                            self.submit_button.pack(pady=10)
                        def submit(self):
                            self.selected_option = self.option_var.get()
                            self.window.destroy()
                        def show(self):
                            self.window.mainloop()
                    option_ui = OptionSelectionUI()
                    option_ui.show()
                    stud_class=option_ui.selected_option
                    cap = cv2.VideoCapture(0)
                    folder_path = f"C:/Users/Srini/Desktop/srini/{stud_class}/"
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    print('PRESS C TO CAPTURE......')
                    print('PRESS Q TO QUIT.........')
                    while True:
                        ret, frame = cap.read()
                        cv2.imshow("Webcam", frame)
                        key = cv2.waitKey(1)
                        if key == ord('c'):
                            filename=input("Enter name of file to save {Ex:aaa.jpg}.....")
                            file_path=os.path.join(folder_path, filename)
                            cv2.imwrite(file_path, frame)
                            break
                        if key == ord('q'):
                            break
                    f_n,f_n_e=filename.split('.jpg')
                    ins.append(f_n)
                    email=input('Enter valid student email:')
                    ins.append(email)
                    ins.append(stud_class)
                    ins.append(today)
                    query = "INSERT INTO student (student_name,email,class,Attendance_date) VALUES (%s, %s, %s, %s)"
                    c.execute(query,ins)
                    connection.commit()
                    print("Data Inserted successfully!")
                    cap.release()
                    cv2.destroyAllWindows()
            else:
                messagebox.showwarning("Error", "Enter a Valid Username & Password \nOR\n Check with Admin..")
                valid_user=0
    def main():
        login_window = loginForm(root)
        root.mainloop()
        return
    print(flag)
    if flag==1:
        flag=0
        print("Entering main")
        main()
        
elif ch=='y' or ch=='Y':
    print("Sorry Only Admin has the right to create staff in Database")
    print("Please contact the Admin!!!")
else:
    print("INVALID OPTION")
    
