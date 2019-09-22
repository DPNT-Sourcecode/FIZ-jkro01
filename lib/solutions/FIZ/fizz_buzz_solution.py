# noinspection PyUnusedLocal
def fizz_buzz(number):
    div3 = ((number % 3) == 0)  #divisible by 3?
    div5 = ((number % 5) == 0)  #divisible by 5?

    number_str = str(number)
    is_3 = '3' in number_str
    is_5 = '5' in number_str
    
    fizz = False
    buzz = False

    if (div3 or is_3):
        fizz = True
    if (div5 or is_5):
        buzz = True

    if (fizz and buzz):
        return('fizz buzz')
    if (fizz):
        return('fizz')
    if (buzz):
        return('buzz') 

    return str(number)

