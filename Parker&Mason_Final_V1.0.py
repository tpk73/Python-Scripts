import datetime
from math import *

def main ():

    new = []
    p = []
    e = []
    i = []
    c = []
    d = []
    pi = 3.141592653589793
    
    
    print('This program reads your horoscope and prints out your biorhythm.')
    print()


    name = input('Please enter your first name: ')
        
    bday = input('Enter Birthdate (mm/dd/yyyy): ')

    of = open(name + '.txt', 'w')
        
    new.append(name)

    of.write('Name: ' + name + '\n')
    of.write('Birthdate: ' + bday + '\n')
    of.write('~'*50 + '\n')

    bday = bday.split('/')

    day = int(bday[1])
        
        #Horoscope
        
    if name != '':
        
        #print('Here is', name + "'s Horoscope and Biorhythm.")

        if bday != '':
                
            if bday[0] =='12' and day > 21 and day < 32 or bday[0] == '01' and day > 0 and day < 21 :
                scope = 'Capricorn'
                of.write(name + ' you are a Capricorn.''\n')
                of.write('\n' + "Capricorn traits include:" + '\n' + '\n' + "Practical" + '\n' + "Intelligent"
                         + '\n' + "Ambitious" + '\n' + "Disciplined" + '\n' + "Patient" + '\n' + "Humorous"
                         + '\n' + "Reserved" + '\n' + "Pessamistic" + '\n')

            if bday[0] == '01' and day > 20 and day < 32 or bday[0] == '02' and day > 0 and day < 19 :
                scope = 'Aquarius'
                of.write(name + ' you are an Aquarius.''\n')
                of.write('\n' + "Aquarius traits include:" + '\n' + '\n' + "Friendly" + '\n' + "Honest"
                         + '\n' + "Loyal" + '\n' + "Inventive" + '\n' + "Independent" + '\n' + "Intellectual"
                         + '\n' + "Unpredictable" + '\n' + "Detatched" + '\n')

            if bday[0] == '02' and day > 18 and day < 29 or bday[0] == '03' and day > 0 and day < 21:
                scope = 'Pisces'
                of.write(name + ' you are a Pisces.''\n')
                of.write('\n' + "Pisces traits include:" + '\n'+ '\n' + "Imaginative" + '\n' + "Sensitive"
                         + '\n' + "Compassionate" + '\n' + "Selfless" + '\n' + "Intuitive" + '\n' + "Kind"
                         + '\n' + "Idealistic" + '\n' + "Secretive" + '\n' + "Weak-willed" + '\n' )

            if bday[0] == '03' and day > 20 and day < 32 or bday[0] == '04' and day > 0 and day < 21:
                scope = 'Aries'
                of.write(name + ' you are an Aries.''\n')
                of.write('\n' + "Aries traits include:" + '\n'+ '\n' + "Adventurous" + '\n' + "Courageous"
                         + '\n' + "Confident" + '\n' + "Enthusiastic" + '\n' + "Witty" + '\n' + "Energetic"
                         + '\n' + "Selfish" + '\n' + "Impulsive" + '\n' + "Quick-tempered" + '\n')

            if bday[0] == '04' and day > 20 and day < 31 or bday[0] == '05' and day > 0 and day < 22:
                scope = 'Taurus'
                of.write(name + ' you are a Taurus.''\n')
                of.write('\n' + "Taurus traits include:" + '\n'+ '\n' + "Patient" + '\n' + "Warmhearted"
                         + '\n' + "Determined" + '\n' + "Placid" + '\n' + "Reliable" + '\n' + "Loving"
                         + '\n' + "Jealous" + '\n' + "Inflexible" + '\n' + "Greedy" + "\n" )

            if bday[0] == '05' and day > 21 and day < 32 or bday[0] == '06' and day > 0 and day < 22:
                scope = 'Gemini'
                of.write(name + ' you are a Gemini.''\n')
                of.write('\n' + "Gemini traits include:" + '\n'+ '\n' + "Adaptable" + '\n' + "Communicative"
                         + '\n' + "Intellectual" + '\n' + "Youthful" + '\n' + "Eloquent" + '\n' + "Witty"
                         + '\n' + "Nervous" + '\n' + "Superficial" + '\n' + "Cunning" + "\n")

            if bday[0] == '06' and day > 21 and day < 31 or bday[0] == '07' and day > 0 and day < 23:
                scope = 'Cancer'
                of.write(name + ' you are a Cancer.''\n')
                of.write('\n' + "Cancer traits include:" + '\n'+ '\n' + "Emotional" + '\n' + "Imaginative"
                         + '\n' + "Cautious" + '\n' + "Protective" + '\n' + "Loving" + '\n' + "Sympathetic"
                         + '\n' + "Moody" + '\n' + "Clingy" + '\n' + "Overemotional" + "\n")

            if bday[0] == '07' and day > 22 and day < 32 or bday[0] == '08' and day > 0 and day < 24:
                scope = 'Leo'
                of.write(name + ' you are a Leo.''\n')
                of.write('\n' + "Leo traits include:" + '\n'+ '\n' + "Generous" + '\n' + "Creative"
                         + '\n' + "Open-minded" + '\n' + "Faithful" + '\n' + "Loving" + '\n' + "Enthusiastic"
                         + '\n' + "Patronizing" + '\n' + "Bossy" + '\n' + "Intolerant" + "\n")

            if bday[0] == '08' and day > 23 and day < 32 or bday[0] == '09' and day > 0 and day < 23:
                scope = 'Virgo'
                of.write(name + ' you are a Virgo.''\n')
                of.write('\n' + "Virgo traits include:" + '\n'+ '\n' + "Modest" + '\n' + "Reliable"
                         + '\n' + "Practical" + '\n' + "Analytical" + '\n' + "Shy" + '\n' + "Diligent"
                         + '\n' + "Worrier" + '\n' + "Overcritical" + '\n' + "Perfectionist" + "\n")

            if bday[0] == '09' and day > 22 and day < 31 or bday[0] == '10' and day > 0 and day < 24:
                scope = 'Libra'
                of.write(name + ' you are a Libra.''\n')
                of.write('\n' + "Libra traits include:" + '\n'+ '\n' + "Diplomatic" + '\n' + "Romantic"
                         + '\n' + "Easygoing" + '\n' + "Sociable" + '\n' + "Idealistic" + '\n' + "Charming"
                         + '\n' + "Indecisive" + '\n' + "Gullible" + '\n' + "Flirtatious" + "\n")

            if bday[0] == '10' and day > 23 and day < 32 or bday[0] == '11' and day > 0 and day < 23:
                scope = 'Scorpio'
                of.write(name + ' you are a Scorpio.''\n')
                of.write('\n' + "Scorpio traits include:" + '\n'+ '\n' + "Determined" + '\n' + "Emotional"
                         + '\n' + "Passionate" + '\n' + "Magnetic" + '\n' + "Forceful" + '\n' + "Powerful"
                         + '\n' + "Resentful" + '\n' + "Obsessive" + '\n' + "Secretive" + "\n")

            if bday[0] == '11' and day > 22 and day < 31 or bday[0] == '12' and day > 0 and day < 22:
                scope = 'Sagittarius'
                of.write(name + ' you are a Sagittarius.''\n')
                of.write('\n' + "Sagittarius traits include:" + '\n'+ '\n' + "Optimistic" + '\n' + "Good-humored"
                         + '\n' + "Honest" + '\n' + "Philosophical" + '\n' + "Freedom-loving" + '\n' + "Straightforward"
                         + '\n' + "Careless" + '\n' + "Superficial" + '\n' + "Restless" + "\n")
                    
    #Biorhythm
                    
        if bday != '':

            #print(bday)
                
            #dtc = int(input('Number of days to chart: '))+4
            dtc = (30)+4
            birthday = datetime.date(int(bday[2]), int(bday[0]), int(bday[1]))
            #print(birthday)
            today = datetime.date.today()
            dfb = (today - birthday).days
            #print(dfb)
            #print(dtc)
            date = datetime.datetime.now() - datetime.timedelta(days = 4)
            for fb in range(dfb - 4, dfb + dtc):
                phys = int(15 * sin(2 * pi * fb/23))
                emot = int(15 * sin(2 * pi * fb/28))
                intl = int(15 * sin(2 * pi * fb/33))
                p.append(phys)
                e.append(emot)
                i.append(intl)
                c.append((phys + emot + intl)/3)
                d.append(date)

                date += datetime.timedelta(days=1)
                #print(date)
                #print(p,e,i,c,d)
                #print(fb)
            #print('~'*50)
            #print('Biorhythm for   : ', name)
            #print('Birthdate Input : ', birthday.strftime('%d %b %Y'))
            #print("Today's Date    : ", today.strftime('%d %b %Y'))
            #print('Days From Birth : ', dfb)
            #print('~'*50)

            of.write('~'*50 + '\n')
            of.write('Biorhythm for   : ' + str(name) + '\n')
            tmp =   ('Birthday Input  : ', birthday.strftime('%d %b %Y'))
            tmp =   (''.join(map(str, tmp)))
            of.write("Today's Date    : "+ today.strftime('%d %b %Y') + '\n')
            tmp = (''.join(map(str, tmp)))
            of.write(str(tmp) + '\n')
            tmp =   ('Days From Birth : ', dfb)
            tmp = (''.join(map(str, tmp)))
            of.write(str(tmp) + '\n')
            of.write('~'*50 + '\n')
        for t in range(0,dtc):
            pei_str = [' '] * 45
            pei_str.insert(0, d[t].strftime('%d %b %y'))
            pei_str.insert((20+int(p[t])), 'p')
            pei_str.insert((20+int(e[t])), 'e')
            pei_str.insert((20+int(i[t])), 'i')
            pei_str.insert((20+int(c[t])), 'c')

            otput = (''.join(map(str, pei_str)))
            #print(otput)
            of.write(otput+ '\n')
            
                                       
    print()
    print('Thank You! Your data is waiting for you here:', name +'.txt')

    of.close()

main()
