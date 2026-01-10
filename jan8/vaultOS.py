usernames = []
platform_type = ()
user_platform = {}
account_typeSet = set()

# Take input from user
username = input("Enter username: ")
platform = input("Enter platform: ")
account_type = input("Enter account type: ")

# Store username in list
usernames.append(username)

# Store platform and account type as a tuple
platform_type = (platform, account_type)

# Store username → platform mapping in dictionary
user_platform[username] = platform

# Store unique account types in a set
account_typeSet.add(account_type)

# Display the output
print("\n--- ACCOUNT DATA SUMMARY ---")
print("Usernames       :", usernames)
print("Platform & Type :", platform_type)
print("User Mapping    :", user_platform)
print("Account Types   :", account_typeSet)
