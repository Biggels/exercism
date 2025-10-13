class Year:
    def __init__(self, value):
        self.value = value

    def is_divisible_by(self, divisor):
        return self.value % divisor == 0

def leap_year(year):
    year = Year(year)

    return year.is_divisible_by(4) and (not year.is_divisible_by(100) or year.is_divisible_by(400))
    
