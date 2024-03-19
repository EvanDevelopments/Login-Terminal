import csv
import random
import datetime
import time
usernames=[]
passwords=[]

def login():
    database=open("database.csv","r")
    dataScraper = csv.reader(database) 
    for x in dataScraper:
        usernames.append(x[0])
        passwords.append(x[1])
    database.close()
    usernamelogin=input("Enter Username:")
    passwordlogin=input("Enter Password:")
    for x in range(len(usernames)):
        if usernamelogin == usernames[x] and passwordlogin == passwords[x]:
            print("Logging in...")
            loggedin()
        else:
            login()
 
def loggedin():
    loggedinoption=input("│Calculator│Dice│Money Converter│Distance Converter│Date/Time│Area Of Circle│Gold Converter│Press The Button│Denary To Binary│Leap Year Calculator│Exit:")
    if loggedinoption.upper()=="EXIT":
        exit()
    elif loggedinoption.upper()=="LEAP YEAR CALCULATOR":
        leapyearcalculator()
    elif loggedinoption.upper()=="DENARY TO BINARY":
        denarytobinary()
    elif loggedinoption.upper()=="PRESS THE BUTTON":
        pressthebutton()
    elif loggedinoption.upper()=="GOLD CONVERTER":
        goldconverter()
    elif loggedinoption.upper()=="AREA OF CIRCLE":
        areaofcircle()
    elif loggedinoption.upper()=="DATE" or loggedinoption.upper()=="TIME":
        x=datetime.datetime.now()
        print(x)
        loggedin()
    elif loggedinoption.upper()=="CALCULATOR":
        calculator()
    elif loggedinoption.upper()=="DICE":
        dice()
    elif loggedinoption.upper()=="MONEY CONVERTER":
        moneyconverter()
    elif loggedinoption.upper()=="DISTANCE CONVERTER":
        distanceconverter()
    else:
        print("Enter an option")
        loggedin()
 
def signup():
    database=open("database.csv","r")
    dataScraper = csv.reader(database) 
    for x in dataScraper:
        usernames.append(x[0])
        passwords.append(x[1])
    database.close()
    username=input("Enter Username:")
    password=input("Enter Password:")
    password1=input("Confirm Password:")
    if password1!=password:
        print("Passwords do not match, try again:")
        signup()
    elif len(password)<=6:
        print("Password to short, try again:")
        signup()
    for x in range(len(usernames)): 
        if username == usernames[x]:        
            print("User already on system")
            signup()
    else:        
        databasewrite=open("database.csv","a")
        csvwriter = csv.writer(databasewrite,lineterminator="\n")
        csvwriter.writerow([username,password])
        databasewrite.close()
        print("Sucess...")
        home()
        
def calculator():
    firstnumber=int(input("Enter the first number:"))
    secondnumber=int(input("Enter the second number:"))
    operator=input("│+│-│/│*│:")
    if operator=="+":
        final=(firstnumber+secondnumber)
        print(firstnumber,"+",secondnumber,"=",final)
        loggedin()
    elif operator=="-":
        final=(firstnumber-secondnumber)
        print(firstnumber,"-",secondnumber,"=",final)
        loggedin()
    elif operator=="/":
        final=(firstnumber/secondnumber)
        print(firstnumber,"/",secondnumber,"=",final)
        loggedin()
    elif operator=="*":
        final=(firstnumber*secondnumber)
        print(firstnumber,"*",secondnumber,"=",final)
        loggedin()
    else:
        print("Enter an option")
        calculator()
 
def dice():
    rangedice=int(input("You roll a dice that goes from 0-"))
    value=(random.randint(3, rangedice))
    print("The dice landed on",value)
    loggedin()
 
def moneyconverter():
    convert=input("What currency do you want to convert GBP to│Dollar│Franc│Euro│Yen│leave:")
    if convert.upper()=="LEAVE":
        loggedin()
    pounds=int(input("How much do you have in GBP:"))
    if convert.upper()=="DOLLAR":
        final=(pounds*1.23)
        print("Your £",pounds,"is equal to $",final)
        loggedin()
    elif convert.upper()=="FRANC":
        final=(pounds*1.15)
        print("Your £",pounds,"is equal to ",final,"franc")
        loggedin()
    elif convert.upper()=="EURO":
        final=(pounds*1.16)
        print("Your £",pounds,"is equal to ",final,"euro")
        loggedin()
    elif convert.upper()=="YEN":
        final=(pounds*167.4)
        print("Your £",pounds,"is equal to ",final,"yen")
        loggedin()
    else:
        print("Enter an option")
        moneyconverter()

def distanceconverter():
    convert=input("Do you want to convert it to │cm│mm│miles│km│leave")
    if convert.upper()=="LEAVE":
        loggedin()
    distancemetres=int(input("Enter the distance in metres:"))
    if convert.upper()=="CM":
        final=(distancemetres*100)
        print("Your M",distancemetres,"is equal to cm",final)
        loggedin()
    elif convert.upper()=="MM":
        final=(distancemetres*1000)
        print("Your M",distancemetres,"is equal to MM ",final)
        loggedin()
    elif convert.upper()=="MILES":
        final=(distancemetres*0.000621371)
        print("Your M",distancemetres,"is equal to Miles ",final)
        loggedin()
    elif convert.upper()=="KM":
        final=(distancemetres/1000)
        print("Your M",distancemetres,"is equal to KM ",final)
        loggedin()
    else:
        print("Enter an option")
        distanceconverter()

def areaofcircle():
    π=3.14159265359
    radius=int(input("Enter the radius of your circle in cm:"))
    area=(π*radius**2)
    x = round(area, 2)
    final=print("The are of your circle is",x,"cm³")
    loggedin()

def goldconverter():
    ounce=int(input("Enter amount of gold in ounces:"))
    final=(ounce*1,463)
    print("Your",ounce,"ounces is worth £",final,)
    loggedin()

def pressthebutton():
    time_elapsed = 0
    print("You have to enter the letter after you think 10 seconds have passed. Be as close as you can.")
    time.sleep(4)
    start_time = time.time()
    button=input("Enter the letter a after 10 seconds:")
    if button.upper()=="a" or button.upper()=="A":  
        time_elapsed = time.time() - start_time
    x=round(time_elapsed,1)
    print("You entered the letter after",x,"seconds!")
    loggedin()

def denarytobinary():
    denary=int(input("Enter denary number:"))
    print(f'{denary:08b}')
    loggedin()

def leapyearcalculator():
    year=int(input("Enter the desired year:"))
    if (year % 400 == 0) and (year % 100 == 0):
        print(year,"is a leap year")
        loggedin()
    elif (year % 4 ==0) and (year % 100 != 0):
        print(year,"is a leap year")
        loggedin()
    else:
        print(year,"is not a leap year")
        loggedin()
           
def home(option=None):
    option=input("│Login│Signup│:") 
    if option.upper()=="SIGNUP":
        signup()
    elif option.upper()=="LOGIN": 
        login()
    else:
        print("Enter an option")
        home()
home()



    
