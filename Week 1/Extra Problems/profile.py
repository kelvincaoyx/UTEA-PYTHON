name = input("What is your name? ")
location = input("Where are you from? ")
discipline = input("What discipline are you in? ")
club = input("What club do you want to join? ")
subject = input("What is your favourite subject? ")

fileObject = open("profile.txt", "w")

text = ("Name: " + name + \
    "\nCurrent Location: " + location + \
    "\nEngineering discipline: " + discipline + "\n" + \
    name + " wants to join: " + club + "\n" + \
    name + "'s favourite subject is: " + subject )

fileObject.write(text)