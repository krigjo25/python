def main():

    """
    #   Title       :   Numb3rs
    #   Description :
        The function validates IPv4 addresses

    #   Author      :   krigjo25
    #   Date        :   13.09-22 """

    return bool(validate(input('IPv4 Address:')))


def validate(ip):

    try:

        #   Initialize a list & variables
        ipv4 = [i for i in str(ip).split('.')]

        if int(ipv4[0]) < 11 or int(ipv4[0]) > 255 or len(ipv4[0]) != 3:
            raise Exception()

    except Exception:
        return False

    return True



if __name__ == "__main__":
    main()
