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

	app.month = int(input("Well hello, " + app.name + ", please tell us your birthday, starting with the month: "))
	app.day = int(input("What day were you born?: "))
	app.year = int(input("And finally! What year did you grace us?: "))
	app.verify = input("So your birthday is, " + str(app.month) + " " + str(app.day) + " " + str(app.year) + ". Is that correct? yes / no :" )

	if(app.verify == "yes"):
		print("Great!")
		break
	else:
		print("Oh no! Lets start again! ")


import datetime
x = datetime.datetime(app.year, app.month, app.day)
y = datetime.datetime.now()
a = int(x.strftime("%j"))
b = int(y.strftime("%j"))
c = (a - b)
f = int(y.strftime("%Y"))
g = int(x.strftime("%Y"))
h = (f - g)
print ("Wow " + app.name + " you are " + str(h) + " years old, and only " + str(c) + " days until your birthday!")

exit()
