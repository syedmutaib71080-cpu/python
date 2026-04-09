import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())

        else:
            print("no such file exist")

    except Exception as e :
        print(f"an exception occurred as {e}")
    
    @classmethod
    def __update(cls) :
        with open(cls.database,'w') as fs:
             fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spahar = random.choices("!@#$%^&",k=1)
        id = alpha + num + spahar
        random.shuffle(id)
        return "".join(id)
    
    
    
    
    
    def createaccount(self):
        info = {
            "name" : input("enter your name:- "),
            "age" : int(input("enter your age:- ")),
            "email" : input("enter your email:- "),
            "pin": int(input("enter your pin:- ")),
            "account" : Bank.__accountgenerate() ,
            "balance" : 0
        }
        
        if info["age"]< 18 or len(str(info["pin"])) !=4 :
            print("sorry you cannot create an account")
            
        else:
            print("account has been created successfully")
            for i in info:
                print (f"{i} :{info[i]}")
            print("please note down your account number")
            
            
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input ("enter your account number:- ")
        pin = int(input("enter your pin:- "))
        
        userdata = [i for i in Bank.data if i ['account'] == accnumber and i['pin'] == pin ]
        
        if userdata == False:
            print("no data found")
        
        else:
            amount =int(input("enter the amount you wnat to deposit :- "))
            if amount > 10000 or amount < 0 :
                print("you can only deposit below 10000")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("amount is deposited ")        


    def withdrawmoney(self):
            accnumber = input ("enter your account number:- ")
            pin = int(input("enter your pin:- "))
            
            userdata = [i for i in Bank.data if i ['account'] == accnumber and i['pin'] == pin ]
            
            if userdata == False:
                print("no data found")
            
            else:
                amount =int(input("enter the amount you wnat to withdraw :- "))
                if userdata[0]['balance'] < amount  :
                    print("you dont have that much money")
                else:
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print("amount is withdrew succesfully ")     


    def showdetail(self):
        accnumber = input ("enter your account number:- ")
        pin = int(input("enter your pin:- "))
        userdata = [i for i in Bank.data if i ['account'] == accnumber and i['pin'] == pin ]
        print("your information are \n\n\n")
        if userdata == False:
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
                
        else :
            print("no data found")
            
    def updatedetail(self):
        accnumber = input ("enter your account number:- ")
        pin = int(input("enter your pin:- "))
        userdata = [i for i in Bank.data if i ['account'] == accnumber and i['pin'] == pin ]
        
        if userdata == False:
            print("no data found")
            
        else:
            print("you cannot change age, accountno. , and balance")
            
            print("fill the detail for change or leave it empty for no change")
            
            newdata ={
                "name" : input("enter new name or press enter for skip :- "),
                "email":input("enter new email or press enter for skip :- "),
                "pin" : input("enter new pin or press enter to skip :- ")
            }
            
            if newdata["name"] == "":
                 newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                 newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                 newdata["pin"] = userdata[0]["pin"]
            
            newdata['age'] = userdata[0]['age']
            newdata['account'] = userdata[0]['account']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
                
                
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
                    
            Bank.__update()
            print("detail updated")

    def delete(self):
        accnumber = input ("enter your account number:- ")
        pin = int(input("enter your pin:- "))
        userdata = [i for i in Bank.data if i ['account'] == accnumber and i['pin'] == pin ]
        
        if userdata == False:
            print("no data founds")
            
        else:
            check = input("press y if you ACTUALLY WANT TO DELETETHE ACCOUNT OR PRESS N  :- ")
            
            if check == 'n' or check == 'N':
                print("bypass")
                
            else:
                if userdata:
                    Bank.data.remove(userdata[0])
                    print("account delated successfully")
                else:
                    print("user not found")
                
                Bank.__update()


user = Bank()
print ("press 1 for creating acount")
print ("press 2 for depositing the money in the bank")
print ("press 3 for withdrawing the money")
print ("press 4 for details")
print ("press 5 for updating the detail")
print ("press 6 for deleting account")

check = int(input ("tell your respone :-"))

if check == 1:
    user.createaccount()
    
if check == 2:
    user.depositmoney()
    
if check == 3:
    user.withdrawmoney()
    
if check == 4:
    user.showdetail()
    
if check == 5 :
    user.updatedetail()

if check == 6:
    user.delete()