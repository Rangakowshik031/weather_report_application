'''f=open("f1.txt","rb")
#f.write("hello\n hi \n hiiii")
print(f.read())
f.close()'''
'''
f=open("f1.txt","w")
f.write("hello")
f.close()
'''
'''f=open("f1.txt","r")
f1=open("f2.txt","w")
print(f.tell())
data=f.read()
print(data)
data1=data[::-1]
f1.write(data1)
f1.close()
f.close()
'''
'''import os 
#f=open("f1.txt","r")
os.remove("f4.txt")'''

'''import os
#os.makedirs("C:\python\hi")
os.rmdir("C:\python\hi")'''

'''l=[1,2,3,4,5]
f=open("f1.txt","w")
for i in l:
    f.write(str(i)+"\n")
f.close()'''

'''f=open("f1.txt","r")
x=open("f2.txt","w")
y=open("f3.txt","w")
#print(f.seek(1,2))
l=[]
p=f.readlines()
for i in range(len(p)):
    l.append(int(p[i]))
print(l)
for i in range(len(l)):
    if l[i]%2==0:
        x.write(str(l[i])+"\n")
    else:
        y.write(str(l[i])+"\n")
f.close()
x.close()
y.close()'''


'''f=open("f1.txt","w")
f.write("hello \n hiii")
f.close()
f=open("f2.txt","w")
f.write("hello")
f.close()


f=open("f1.txt","r")
x=open("f2.txt","r")
y=open("f3.txt","w")

p=f.read()
q=x.read()
z=p+"\n"+q
print(z)
y.write(z)
f.close()
x.close()
y.close()'''

'''from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
  
# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
  
  
# explicit function to get
# weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))
      
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, 
                 temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")
  
  
# explicit function to
# search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+"   Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))
  
  
# Driver Code
# create object
app = Tk()
# add title
app.title("Weather App")
# adjust window size
app.geometry("300x300")
  
# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Search Weather", 
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="Location", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()
'''
'''import requests
print(dir(requests))'''



'''import requests, json
 
# Enter your API key here
api_key = "c341e3a5ede9998e3438942cb2f27d12"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = input("Enter city name : ")
 
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object
# convert json format data into
# python format data
x = response.json()
 
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
 
    # store the value of "main"
    # key in variable y
    y = x['main']
 
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 
else:
    print(" City Not Found ")'''


'''import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
print(x.text)



from tkinter import *
from tkinter import messagebox
import requests, json
#api_key = "c341e3a5ede9998e3438942cb2f27d12"
# function to find weather details
# of any city using openweathermap api
def tell_weather() :

	# import required modules
	#import requests, json

	# enter your api key here
	api_key = "c341e3a5ede9998e3438942cb2f27d12"

	# base_url variable to store url
	base_url = "http://api.openweathermap.org/data/2.5/weather?"


	# take a city name from city_field entry box
	city_name = city_field.get()

	# complete_url variable to store complete url address
	complete_url = base_url + "appid =" + api_key + "&q =" + city_name

	# get method of requests module
	# return response object
	response = requests.get(complete_url)

	# json method of response object convert
	# json format data into python format data
	x = response.json()

	# now x contains list of nested dictionaries
	# we know dictionary contains key value pair
	# check the value of "cod" key is equal to "404"
	# or not if not that means city is found
	# otherwise city is not found
	if x["cod"] != "404" :

		# store the value of "main" key in variable y
		y = x["main"]

		# store the value corresponding to the "temp" key of y
		current_temperature = y["temp"]

		# store the value corresponding to the "pressure" key of y
		current_pressure = y["pressure"]

		# store the value corresponding to the "humidity" key of y
		current_humidity = y["humidity"]

		# store the value of "weather" key in variable z
		z = x["weather"]

		# store the value corresponding to the "description" key
		# at the 0th index of z
		weather_description = z[0]["description"]

		# insert method inserting the
		# value in the text entry box.
		temp_field.insert(15, str(current_temperature) + " Kelvin")
		atm_field.insert(10, str(current_pressure) + " hPa")
		humid_field.insert(15, str(current_humidiy) + " %")
		desc_field.insert(10, str(weather_description) )

	# if city is not found				
	else :

		# message dialog box appear which
		# shows given Error message
		return messagebox.showerror("Error", "City Not Found \n","Please enter valid city name")

		# clear the content of city_field entry box
		#city_field.delete(0, END)'''


# Function for clearing the
# contents of all text entry boxes
'''def clear_all() :
	city_field.delete(0, END)
	temp_field.delete(0, END)
	atm_field.delete(0, END)
	humid_field.delete(0, END)
	desc_field.delete(0, END)

	# set focus on the city_field entry box
	city_field.focus_set()'''


# Driver code

	# Create a GUI window
'''root = Tk()

	# set the name of tkinter GUI window
root.title("Gui Application")

	# Set the background colour of GUI window
root.configure(background = "light green")

	# Set the configuration of GUI window
root.geometry("425x175")

	# Create a Weather Gui Application label
headlabel = Label(root, text = "Weather Gui Application",
					fg = 'black', bg = 'red')
	
	# Create a City name : label
label1 = Label(root, text = "City name : ",fg = 'black', bg = 'dark green')
	
	# Create a City name : label
label2 = Label(root, text = "Temperature :",fg = 'black', bg = 'dark green')

	# Create a atm pressure : label
label3 = Label(root, text = "atm pressure :",fg = 'black', bg = 'dark green')

	# Create a humidity : label
label4 = Label(root, text = "humidity :",fg = 'black', bg = 'dark green')

	# Create a description :label
label5 = Label(root, text = "description :",fg = 'black', bg = 'dark green')
	

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
headlabel.grid(row = 0, column = 1)
label1.grid(row = 1, column = 0, sticky ="E")
label2.grid(row = 3, column = 0, sticky ="E")
label3.grid(row = 4, column = 0, sticky ="E")
label4.grid(row = 5, column = 0, sticky ="E")
label5.grid(row = 6, column = 0, sticky ="E")


	# Create a text entry box=
	# for filling or typing the information.
city_field = Entry(root)
temp_field = Entry(root)
atm_field = Entry(root)
humid_field = Entry(root)
desc_field = Entry(root)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	# ipadx keyword argument set width of entry space .
city_field.grid(row = 1, column = 1, ipadx ="100")
temp_field.grid(row = 3, column = 1, ipadx ="100")
atm_field.grid(row = 4, column = 1, ipadx ="100")
humid_field.grid(row = 5, column = 1, ipadx ="100")
desc_field.grid(row = 6, column = 1, ipadx ="100")

	# Create a Submit Button and attached
	# to tell_weather function
button1 = Button(root, text = "Submit", bg = "red",fg = "black", command = tell_weather)

	# Create a Clear Button and attached
	# to clear_all function
#button2 = Button(root, text = "Clear", bg = "red",fg = "black", command = clear_all)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
button1.grid(row = 2, column = 1)
#button2.grid(row = 7, column = 1)
	
	# Start the GUI
root.mainloop()'''
'''f1=open("s6.txt","w")
f1.write("regular\t expressions is\t very important\n concept in \n oop")
f1.close()

with open("s6.txt","r") as file1:
    text=file1.read()
space=tabspace=new=0
for i in text:
    if(i=='\t'):
        tabspace+=1
    elif(i==" "):
        space+=1
    elif(i=='\n'):
        new+=1
print("THE NUMBER OF TABSPACES:",tabspace)
print("THE NUMBER OF SPACES :",space)
print("THE NUMBER OF NEWLINE CHARCTERS IS :",new)'''
'''class morning():
    flag=1
    def fn(self,time):
         self.morninglogin=time
         self.hour,self.minu=hour,minu=tuple(time.split(":"))
         self.hour=int(self.hour)
         self.minu=int(self.minu)
         if((self.hour>=9 and self.minu<15 ) or (self.hour<=9)):
              print("----ATTENDENCE SHEET-----")
              print("MORNING STATUS:PRESENT")
              print("MORNING LOGIN:",self.morninglogin)
              
         else:
              print("----ATTENDENCE SHEET-----")
              print("MORNING STATUS:ABSENT")
              print("MORNING LOGIN:",self.morninglogin)
              morning.flag=0
class afternoon():
    check=1
    def an(self,time):
         self.afternoonlogin=time
         self.hour,self.minu=hour,minu=tuple(time.split(":"))
         self.hour=int(self.hour)
         self.minu=int(self.minu)
         if(self.hour==4 and (self.minu>=15 and self.minu <=30)):
             print("EVENING STATUS:PRESENT")
             print("EVENING LOGIN:",self.afternoonlogin)
         else:
             print("EVENING STATUS:ABSENT")
             print("EVENING LOGIN:",self.afternoonlogin)
             afternoon.check=0
         if(morning.flag==1 and afternoon.check==1):
            print("----FULL DAY PRESENT-----")
         elif(morning.flag==0 and afternoon.check==0):
            print("---------WHOLE DAY ABSENT-------")
         else:
            print("-----HALF DAY PRESENT-----")
class temp(morning,afternoon):
    def __init__(self):
        self.name=input("Enter your name")
        self.rollno=int(input("Enter your roll no"))
        self.section=input("Enter your section")
        self.department=input("Enter your department")
        self.m=input("morning time in the format HH:MM\n")
        self.n=input("evening time in format HH:MM\n")
    def details(self):
        print("NAME:{}\n ROLLNO:{}\n SECTION:{} \n DEPARTMENT:{}".format(self.name,self.rollno,self.section,self.department))
        morning.fn(self,self.m)
        afternoon.an(self,self.n)
        if(morning.flag==1 and afternoon.check==1):
            print("----FULL DAY PRESENT-----")
        elif(morning.flag==0 and afternoon.check==0):
            print("---------WHOLE DAY ABSENT-------")
        else:
            print("-----HALF DAY PRESENT-----")
while (True):
    x=int(input("ENTER\n 1  PEMANENT ID\n 2  TEMPORARY \n 3 EXIT \n"))
    if(x==1):
         m=input("morning time in the format HH:MM\n")
         n=input("evening time in format HH:MM\n")
         a=morning().fn(m)
         b=afternoon().an(n)
    elif(x==2):
       c=temp()
       c.details()
    elif(x==3):
        break
    else:
        print("enter proper choice")

'''




'''def solve(meal_cost, tip_percent, tax_percent):
    s=(meal_cost*tip_percent)/100
    d=(meal_cost*tax_percent)/100
    tota=meal_cost+s+d
    #print(tota)
    total=int(tota)
    print(total)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)'''




'''if __name__ == '__main__':
    N = int(input().strip())
    if N%2==0:
        if N in range(2,6):
            print("Not Weird")
        elif N in range(6,21):
            print("Weird")
        elif N>20:
            print("Not Weird")
    else:
        print("Weird")'''







































'''class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        self.s=s
        if sizeOfStack%2==0:
            mid=(sizeOfStack//2)+1
            self.s.pop(mid)
        else:
            mid=sizeOfStack//2
            self.s.pop(mid)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()'''





import re
s="20+5+66"
pat="[0-9]{1,}"
l=re.findall(pat,s)
print(l)




























