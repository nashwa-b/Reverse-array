#Ask user for their name
name=input("What's your Name?")
#say hello to user
print("hello, "+ name)
print("hello,",end='')
print(name)
print("hello,", name, sep="??")

#Remove white space
name = name.strip()

#capitalize
name = name.capitalize()
print(f"hello, {name}")



