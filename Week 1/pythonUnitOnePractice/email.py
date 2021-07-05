'''
This program is used to get information from a user and
make an email from that information
'''

#asking for the user's first name and then storing it in the variable firstName
firstName = input("Enter your first name: ")

#asking for the user's last name and then storing it in the variable lastName
lastName = input("Enter your last name: ")

#asking for the user's domain name and then storing it in the variable domainName
domainName = input("Enter your domain name: ")

#creating the full email address
emailAddress = (lastName + "." + firstName + "@" + domainName)

#printing all the information to the user about their newly assigned email address
print("Hello " + firstName + ",\nYour new email address is:  " + emailAddress)


