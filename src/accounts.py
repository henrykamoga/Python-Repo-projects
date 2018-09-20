# creating a dictionary for user name and password
# accounts = {'henry':'moga'}
accounts = {}
# get user inputs
def add_account (User_name,password):
	# store the User name and Password into a dictionary
	accounts = { User_name: password}
	print (accounts)


def log_in (User_name, Password):
	# loop throught the dictionary and get the user name and password
	for userName, password in accounts.items():
		# global dic_User_name
		# global dic_Password 
		dic_User_name = userName
		dic_Password =  password
		global dic_User_name
		global dic_Password 
		# print (dic_User_name)
		# print (dic_Password)
	# Name = dic_User_name
	# Pass =  dic_Password
		if userName == User_name and  password ==  Password:
			print ("loged in well ...")
			
		else:
			print ("invalid credentials try again !!!")

# print (dic_User_name)
# log_in()
# log_in('henry2','moga2')