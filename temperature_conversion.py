# class fo temerature conversion
farenheit=float(input("Enter the temperature in Farenheit: "))
celcius=float(input("Enter the temperature in Celcius: "))
class Temperature:
    def __init__(self, farenheit, celcius):
        self.farenheit=farenheit
        self.celcius=celcius

    def convert_farenheit(self):
        return (self.farenheit - 32) * 5/9
    def convert_celcius(self):
        return (self.celcius * 5/9) + 32
    
T = Temperature(farenheit, celcius)
print(T.convert_celcius())
print(T.convert_farenheit())
    