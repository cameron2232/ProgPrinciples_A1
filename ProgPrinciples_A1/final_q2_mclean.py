class Phone:
    def __init__(self, model, price):
        self.model, self.price = model, price
    
    def get_price(self):
        return self.price
    
    def __str__(self):
        return f'model={self.model}, price={self.price}'

class SmartPhone(Phone):
    def __init__(self, model, price, system):
        super().__init__(model, price)
        self.system = system
        
    def __str__(self):
        return 'SmartPhone(' + super().__str__() + f', system={self.system})'
    
    def get_system(self):
        return self.system
        
def phones(phone_list, required_system):
    price = 0
    for phone in phone_list:
        if isinstance(phone, SmartPhone):
            if phone.get_system == required_system:
                if phone.get_price > price:
                    price = phone.get_price
                    expensive_phone = phone
                    return expensive_phone.__str__()
    
list_phones = [Phone('Nokia 1450', 321.54),
               SmartPhone('Google P8', 753.24, 'Android'), Phone('MS531', 234.56), SmartPhone('Samsung S21', 357.12, 'Android'),
               SmartPhone('iPhone X12', 420.78, 'iOS')]

print(phones(list_phones, 'Android'))