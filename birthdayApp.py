class App():
	name = None
	day = None
	month = None
	year = None
	verify = None
	
	
app = App()

print("Welcome to the birthday countdown app. Lets see how many days is left until your birthday!")
app.name = input("Please tell us your name:")

i = 1
while i > 0: 

	app.month = int(input("Well hello, " + username + ", please tell us your birthday, starting with the month: "))
	app.day = int(input("What day were you born?: "))
	app.year = int(input("And finally! What year did you grace us?: "))
	app.verify = input("So your birthday is, " + month + " " + day + " " + year + ". Is that correct? yes / no :" )
	
	if(app.verify == "yes"):
		print("Great!")
		break
	else:
		print("Oh no! Lets start again! ")
		
		
		
		
		
		
		
		
class comingOfageClass():
	test = 'hello'
	pass
app = comingOfageClass()
print(app.test)
exit()



print("Welcome to the birthday countdown app. Lets see how many days is left until your birthday!")
username = input("Please tell us your name:")
i = 1
while i > 0: 

	month = input("Well hello, " + username + ", please tell us your birthday, starting with the month: ")
	m = int(month)
	day = input("What day were you born?: ")
	d = int(day)
	year = input("And finally! What year did you grace us?: ")
	y = int(year)
	verify = input("So your birthday is, " + month + " " + day + " " + year + ". Is that correct? yes / no :" )
	if(verify == "yes"):
		print("Great!")
		break
	else:
		print("Oh no! Lets start again! ")
import datetime
x = datetime.datetime(y, m, d)
y = datetime.datetime.now()
a = int(x.strftime("%j"))
b = int(y.strftime("%j"))
c = (a - b)
d = int(c)
e = str(d)
f = int(y.strftime("%Y"))
g = int(x.strftime("%Y"))
h = (f - g)
i = str(h)
print ("Wow " + username + " you are " + i + "years old, and only " + e + " days until your birthday!")
