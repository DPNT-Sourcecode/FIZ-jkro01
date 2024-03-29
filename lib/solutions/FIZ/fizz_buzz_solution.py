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

    deluxe_number = False       #new deluxe rule
    if (div3 and is_3):
        deluxe_number = True
    if (div5 and is_5):
        deluxe_number = True
        
    output = ''

    if (fizz):
        output = 'fizz'
    if (buzz):
        output = 'buzz'
    if (fizz and buzz):
        output = 'fizz buzz'
 
    if (number %2 == 0):    #check whether odd or even
        deluxe_str = 'deluxe'   #even
    else:
        deluxe_str = 'fake deluxe'  #odd

    if (deluxe_number):  #changed deluxe rule
        if (output == ''):
            output = deluxe_str
        else:
            output = output + ' ' + deluxe_str

    if (output == ''):
        return str(number)
    else:
        return output



