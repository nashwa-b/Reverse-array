# x=int(input("Whats x?"))
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")

# Using function
# def main():
#     x=int(input("Whats x?"))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# main()

# Elegant way
def main():
    x=int(input("Whats x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n%2==0
main()