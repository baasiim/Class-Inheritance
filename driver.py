#Import all files
import electronics
import computer
import phone

#Define main
def main():

    #Variable to store objects
    brand = (input("Enter an Electronics Brand: "))
    brand2 = (input("Enter an Electronics Brand: "))
    os = (input("Enter an Operating System: "))
    brand3 = (input("Enter an Electronics Brand: "))
    os2 = (input("Enter an Operating System: "))
    number = (input("Enter a phone number: "))

    #Instantiate the objects
    brand_object = electronics.Electronics(brand)
    os_object = computer.Computer(brand2, os)
    phone_object = phone.Phone(brand3, os2, number)

    #Print the values in each object
    print("The Electronics Object:",
          brand_object.get_brand())
    print("\n")
    print("The Computer Object:",
          os_object.get_brand(),
          os_object.get_os())
    print("\n")
    print("The Phone Object:",
          phone_object.get_brand(),
          phone_object.get_os(),
          phone_object.get_number())
    return

#Call Main
main()
