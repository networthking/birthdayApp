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
a = int(x.strftime("%j"))
y = datetime.datetime.now()
b = int(y.strftime("%j"))
c = (a - b)
d = int(c)
e = str(d)
print ("Wow " + username + " ! only " + e + " days until your birthday!")
