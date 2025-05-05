#Import the parent class
import electronics

#Class variable
class Computer(electronics.Electronics):
    operating_system = str()

    #Constructor
    def __init__(self, brand_name, operating_system):
        super().__init__(brand_name)
        self.set_os(operating_system)

    #Set method
    def set_os(self, operating_system):
        self.operating_system = operating_system

    #Get Method
    def get_os(self):
        return self.operating_system
