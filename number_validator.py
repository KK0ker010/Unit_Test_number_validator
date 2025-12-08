class NumberValidator:
    """Számvalidáló osztály különböző matematikai műveletekhez"""
    
    def __init__(self):
        self.validated_numbers = []
    
    def is_even(self, number):
        """Páros szám ellenőrzés"""
        if number is None:
            return False
        return number % 2 == 0
    
    def is_positive(self, number):
        """Pozitív szám ellenőrzés"""
        if number is None:
            return False
        return number > 0
    
    def is_in_range(self, number, min_val, max_val):
        """Ellenőrzi, hogy a szám a megadott tartományban van-e"""
        if number is None:
            return False
        return min_val <= number <= max_val
    
    def get_absolute_value(self, number):
        """Abszolút érték visszaadása"""
        if number is None:
            return 0
        return abs(number)
    
    def is_divisible_by(self, number, divisor):
        """Ellenőrzi, hogy a szám osztható-e a megadott osztóval"""
        if number is None or divisor is None or divisor == 0:
            return False
        return number % divisor == 0
    
    def square(self, number):
        """Szám négyzete"""
        if number is None:
            return 0
        return number ** 2
    
    def is_prime(self, number):
        """Prímszám ellenőrzés"""
        if number is None or number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


