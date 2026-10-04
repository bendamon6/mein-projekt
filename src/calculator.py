def summe(a, b):
    return a + b

def durchschnitt(werte):
    if not werte:
        return 0
    return sum(werte) / len(werte)

def prozent(wert, anteil):
    return (wert * anteil) / 100

# Grundrechenarten
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division durch Null ist nicht erlaubt.")
    return x / y
