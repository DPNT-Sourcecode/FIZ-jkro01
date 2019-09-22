# noinspection PyUnusedLocal
def fizz_buzz(number):
    div3 = ((number % 3) == 0)  #divisible by 3?
    div5 = ((number % 5) == 0)  #divisible by 5?

    if (div3 and div5):
        return('fizz buzz')
    if (div3):
        return('fizz')
    if (div5):
        return('buzz')
    
    return str(number)
    

