#-----------------Send Warning Email To all students who got absent-----------------
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
for i  in rows:
    email_sender = 'srimoorthy757@gmail.com'
    email_password = 'gwyibxihdfsxtjup'
    email_receiver = i[0].strip()
    em = MIMEMultipart()
    em['From'] = 'srimoorthy757@gmail.com'
    em['To'] = i[0].strip()
    em['Subject'] = 'DGVC ATTENDANCE ALERT!!'
    t=MIMEText("Dear Student, You are marked absent today!\n"+
               "If you have any query regarding this, please contact your Staff incharge or HOD.\n"+
               "Kindly avoid taking leaves!!\n\n\n"+
               "Thank you\n,"+"Regards,\n"+"DGVC")
    em.attach(t)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
print("Email sent to each student who marked absent in database successfully!")

    

#-----------------Sending All presentees List to HOD/staff-incharge---------------
try:
    em = MIMEMultipart()
    em['From'] = 'srimoorthy757@gmail.com'
    em['To'] = 'srinivasamoorthy27@gmail.com'
    em['Subject'] = "Testing mail"
    t=MIMEText("Hi admin! Please Check Today's Attendance!!!!")
    em.attach(t)
    file_path = f'C:/Users/Srini/Desktop/Attendance/{file_n}'
    with open(file_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='xlsx')
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        em.attach(attachment)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent to Staff successfully!")
except:
    print("Email Authentication failed! Server Busy try after sometime!!!")
	
	

#Report Generation for Specific student
report_name=input("Enter student name you want to generate report")
twd=int(input("Enter total no of working days for % calculation"))
rpt_qry='select No_pre,Absent_marker from student where student_name=%s'
c.execute(rpt_qry,(report_name,))
va=c.fetchone()
print('#'*5,"REPORT DETAILS",'#'*5)
print("NAME"+"                 "+":"+report_name.upper())
print("TOTAL WORKING DAYS"+"   "+":",twd)
print("NO  OF DAYS PRESENT"+"  "+":",va[0])
print("NO  OF DAYS ABSENT"+"   "+":",va[1])
per=(va[0]/twd)*100
print("ATTENDANCE %"+"         "+":",per,"%")
print("------------THANK YOU!--------------")
    