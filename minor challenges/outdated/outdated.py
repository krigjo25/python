#   Missing to remove : September 8 1994, how do i do that?
def main():

    '''
        #   Title   :
        #   Author : krigjo25
        #   Date : .09-22
        #   Description :
                A Program to convert a formated date into a american way date

                Usage : type in the terminal python outdated.py,
                wait for the date then type an date

    '''

    #   Initializing lists
    month = [   '', 'January', 'February',
                'March', 'April', 'May',
                'June', 'Juli', 'August',
                'September', 'October', 'November',
                'December']

    while True:

        #   prompting the user for a date
        date = input('date : ').strip()
        try:

            if ',' in date:
                date = date.replace(',', '').rsplit(' ')

                if date[1] in month:
                    raise TypeError()

            elif '/' in date :

                date = date.rsplit('/')

                if date[0] in month:
                    raise TypeError()

            else:
                raise TypeError()

        except Exception: continue

        if date[0] in month:
            m = month.index(date[0])
            if int(date[1]) > 31 : continue

        #   examine the list for date values is above a given value
        elif int(date[0]) > 12 or int(date[1]) > 31: continue

        else:

            m = date[0]

        d, y = date[1], date[2]

        return print(f'{y}-{str(m).zfill(2)}-{d.zfill(2)}')

main()
