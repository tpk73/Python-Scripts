def main ():
    print('This program converts dates.')
    date = input('Please enter a date in the form mm/dd/yyyy: ')
    date = date.split('/')

    for x in date:
        if date[0] == '01' :
            date[0] = 'January'
        if date[0] == '02' :
            date[0] = 'February'
        if date[0] == '03' :
            date[0] = 'March'
        if date[0] == '04' :
            date[0] = 'April'
        if date[0] == '05' :
            date[0] = 'May'
        if date[0] == '06' :
            date[0] = 'June'
        if date[0] == '07' :
            date[0] = 'July'
        if date[0] == '08' :
            date[0] = 'August'
        if date[0] == '09' :
            date[0] = 'September'
        if date[0] == '10' :
            date[0] = 'October'
        if date[0] == '11' :
            date[0] = 'November'
        if date[0] == '12' :
            date[0] = 'December'

    date[1] = int(date[1])
    date[1] = str(date[1])

    print('The converted date is', date[0], date[1] + ',' , date [2] + '.')
        
main()
