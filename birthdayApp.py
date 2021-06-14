print("Welcome to the birthday countdown app. Lets see how many days is left until your birthday!")
username = input("Please tell us your name:")
i = 1
while i > 0: 

	month = input("Well hello, " + username + ", please tell us your birthday, starting with the month: ")
	day = input("What day were you born?: ")
	year = input("And finally! What year did you grace us?: ")
	verify = input("So your birthday is, " + month + " " + day + " " + year + ". Is that correct? yes / no :" )
	if(verify == "yes"):
		print("Great!")
		break
	else:
		print("Oh no! Lets start again! ")
date = input("whats the date?")


