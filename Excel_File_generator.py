import openpyxl
import os
day_of_month=str(today.day)
month_of_year=str(today.strftime("%B"))
current_time=str(datetime.datetime.now().time())
file_n=day_of_month + month_of_year +".xlsx"
li=[]
t=()
folder_path ="C:/Users/Srini/Desktop/Attendance/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Folder Created!")
print(file_n)
file_path = os.path.join(folder_path,file_n)
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['NAME', 'LOGIN_TIME'])
t+=(val1,)
t+=(current_time,)
li.append(t)
for row in li:
    worksheet.append(row)
workbook.save(file_path)
print("Your Attendance file saved your Desktop")


#------Keep track of absentees in Database-----------------
c = connection.cursor()
print("Marking absent for absentees...")
rpq1="select email from student where pres_stat=%s and Attendance_date=%s"
rpv1=0
c.execute(rpq1,(rpv1,today))
rows = c.fetchall()
print(len(rows))
for row in rows:
    query='UPDATE student SET Absent_marker =Absent_marker+%s WHERE email=%s'
    up=(1,row[0])
    c.execute(query,up)
    print("Absent marker noted!")
connection.commit()