# x=1
# y=2
# z=x+y
# print(z)   

#read as string
# x=input("whats x")
# y=input("whats y")
# z=x+y
# print(z)

#using int
# x=input("whats x")
# y=input("whats y")
# z=int(x)+int(y)
# print(z)

#avoid z
# x=int(input("whats x"))
# y=int(input("whats y"))
# print(x+y)

#float
# x=float(input("whats x"))
# y=float(input("whats y"))
# print(x+y)

#rounding to integer
# x=float(input("Whats x? "))
# y=float(input("Whats y? "))
# z=round(x+y)
# print(z)

#Getting commas in nos
# x=float(input("Whats x? "))
# y=float(input("Whats y? "))
# z=round(x+y)
# print(f"{z:,}")

#rounding
# x=float(input("Whats x? "))
# y=float(input("Whats y? "))
# z=round(x/y,2)  #has to roung upto 2 digit 
# print(z)

#same as before
# x=float(input("Whats x? "))
# y=float(input("Whats y? "))
# z=x/y  #has to roung upto 2 digit 
# print(f"{z:.2f}")

#square using def
def main():
    x=int(input("Whats x? "))
    print("x squared is", square(x))

def square(n):
    return n*n  #or n**2 or pow(n,2)
main()




