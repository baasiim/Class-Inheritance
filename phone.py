#Import the parent class
import computer

#Class Variable
class Phone(computer.Computer):
    phone_number = str()

    #Constructor
    def __init__(self, brand_name, operating_system, phone_number):
        super().__init__(brand_name, operating_system)
        self.set_number(phone_number)

    #Set method
    def set_number(self, phone_number):
        self.phone_number = phone_number

    #Get method
    def get_number(self):
        return self.phone_number