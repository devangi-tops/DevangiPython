d1={
  'Name':'User',
  "E-mail":"User@gmail.com",
  'password':'User@1234'
  }

username=input("Enter username/email id:")
password=input("Enter password:")

if username==d1['E-mail'] and password==d1['password']:
    print("Login Succeess")
else:
    print("Acess denied")
