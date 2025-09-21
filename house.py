# name=input("Whats your name?")

# if name=="Harry":
#     print("Gryffindor")
# elif name=="Hermione":
#     print("Gryffindor")
# elif name=="Ron":
#     print("Gryffindor")
# elif name=="Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Simpler
# name=input("Whats your name?")

# if name=="Harry" or name=="Hermione" or name=="Ron":
#     print("Gryffindor")
# elif name=="Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Using Match
# name=input("Whats your name?")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherine")
#     case _:
#         print("Who?")



name=input("Whats your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")
    
    