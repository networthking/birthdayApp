print("Welcome to the birthday countdown app. Lets see how many days is left until your birthday!")
username = input("Please tell us your name:")
verify = False 
while verify == False:
	month = input("Well hello, " + username + ", please tell us your birthday, starting with the month: ")
	day = input("What day were you born?: ")
	year = input("And finally! What year did you grace us?: ")
	verify = input("So your birthday is, " + month + " " + day + " " + year + ". Is that correct? yes / no :" )
	if(verify == "yes"):
		print("Great!")
	else:
		print("Oh no! Lets start again! ")
