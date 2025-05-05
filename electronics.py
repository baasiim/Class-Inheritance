#Start with class
class Electronics:

    #Class Variable
    brand_name = str()

    #Constructor
    def __init__(self, get_brand):
        self.set_brand(get_brand)

    #Set method
    def set_brand(self, brand_name):
        self.brand_name = brand_name

    #Get method
    def get_brand(self):
        return self.brand_name
