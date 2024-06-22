def main():
    '''
        Title       :   EnergyMeasured
        Author      :   krigjo25
        Description :
            Defining a function to calculate the Energy.
            The formula of Energy we use the formula E = ms2.
            m = Mass (kg) * s = Speed of light which is 3*10**8
    '''
    #   Initializing variables & prompt the user.
    m = int(input("mass :"))

    # Calculating the Speed of light
    s = 3*10**8

    #   Calculates and prints out the equivalent number of Joules
    return print(m * s ** 2)

if __name__ == '__main__':
    main()
