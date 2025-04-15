import adminotp
import sendmail1
details={
        101 : ["vinod kumar","vinodkumarnaikmegavath502@gmail.com","PFS21",15000],
        102 : ["ashok","ashokmangall631@gmail.com","DA7",35000],
        103 : ["rahul","rahulkondu6@gmail.com","DS6",40000]
    }
admin_email = input("Enter Adim email id: ")
x = adminotp.otp(admin_email)
if x == True:
    print("Mails Sending in Progress")
    for data in details:
        if details[data][-1] < 40000:
            sendmail1.send_message1(details[data][1],details[data][0],details[data][-1])
    
    print("All Mails Sent Successfully")  
else:
    print("Wrong OTP Entered, Verification Failed !")
