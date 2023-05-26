def ePrimo(num):
    
    if num <=1:
        return False
    
    ePrimoo = 0

    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            ePrimoo += 1
            
    if ePrimoo == 0:
        return True
    else:
        return False

def main():
    print(ePrimo(11))
    print(ePrimo(2))
main()
