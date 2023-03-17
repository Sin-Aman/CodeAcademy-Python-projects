#Create a username and password generator

def username_generator( first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    return first_name + last_name
  else:
    return first_name[:3] + last_name[:4]

def password_generator(user_name):
  password =''
  for i in range(len(user_name)):
    password += user_name[i-1]
  return password

print(password_generator("AmanSinha"))