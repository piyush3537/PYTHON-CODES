# password validation
password = "jeenu12@"
import time
attempt=3
while 1:
     user_pass=input("enter the password")
     if user_pass == password:
        print("login successfull")
        break
     else:
        print("wrong password,try again")
     attempt-=1
     if attempt<=0:
       print("failed to login")
       print("waiting time start")
       count=10
       while count:
        time.sleep(1)
        print(count,end="  ")
        count-=1
        attempt=3