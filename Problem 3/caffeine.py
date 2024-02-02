
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    caffeine_mg = caffeine_mg / 2
    sixHours = caffeine_mg
    caffeine_mg = caffeine_mg / 2
    twelveHours = caffeine_mg
    caffeine_mg = (caffeine_mg / 2) /2
    twentyfourHours = caffeine_mg
    print("After 6 hours: "f'{sixHours:.2f}' + " mg")
    print("After 12 hours: "f'{twelveHours:.2f}'  " mg")
    print("After 24 hours: "f'{twentyfourHours:.2f}' + " mg")


    
if __name__ == "__main__":
    caffeine()