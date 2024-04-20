# Create my first module

def isPrime(num):
    '''
        About isPrime
        
        The function checks wheter the value is prime or not
    '''

    #   Checking if the value is prime or odd
    for x in range(2, num):
        if num % x == 0:return 'ODD', False
        
    return 'Prime', True