class Temperature:
    def __init__(self, kelvin):
        self._kelvin = kelvin
        self.temps = {"Kelvin":self.kelvin,"Celsius":self.celsius,"Fahrenheit":self.fahrenheit}

    @property
    def kelvin(self) -> float:
        return self._kelvin

    @kelvin.setter
    def kelvin(self,kelvin:float):
        self._kelvin = kelvin

    @property
    def celsius(self) -> float:
        return self.kelvin - 273.15

    @celsius.setter
    def celsius(self,celsius:float):
        if celsius < -273.15:
            raise ValueError('This temperature is lower than absolute zero')
        self._kelvin = celsius + 273.15

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self,fahrenheit:float):
        if (fahrenheit-32)/1.8 < -273.15:
            raise ValueError('This temperature is lower than absolute zero')
        else:
            self.celsius = (fahrenheit-32)/1.8

    @property
    def newton(self):
        return (self.kelvin-273.15)/100*33

    @newton.setter
    def newton(self,newton:float):
        if (newton*100/33)+273.15 < 0:
            raise ValueError('This temperature is lower than absolute zero')
        else:
            self.kelvin = (newton*100/33)+273.15
