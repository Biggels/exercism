class Year:
    def __init__(self, value):
        self.value = value

    def is_divisible_by(self, divisor):
        return self.value % divisor == 0



def leap_year(year):
    year = Year(year)
    if not year.is_divisible_by(4):
        return False
    if not year.is_divisible_by(100):
        return True
    if not year.is_divisible_by(400):
        return False
    return True
    
