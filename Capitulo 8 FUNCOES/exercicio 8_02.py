def múltiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
print(f"múltiplo(8,4) == True  -> obtido: {múltiplo(8,4)}")
print(f"múltiplo(7,3) == False -> obtido: {múltiplo(7,3)}")
print(f"múltiplo(5,5) == True  -> obtido: {múltiplo(5,5)}")