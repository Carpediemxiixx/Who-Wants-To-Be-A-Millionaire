import random

class Millionaire:

    def __init__(self, name, prize = 0):
        # whats in this class
        self.name = name
        self.first_round
        self.second_round
        self.third_round
        
    def __repr__(self):
        #states what this class does
        print("This is Who Wants To Be A Millionaire it takes one players name and gives them 15 questions in 3 rounds of easy, medium, and hard difficulity")
        
    def first_round(self):
        #easy questions for the first round
        two = ''
        three = ''
        four = ''
        five = ''
        one = input('Who was the ancient Greek goddess of love and beauty?' + '\n' + 'A. Calliope \nB. Aphrodite \nC. Athena \nD. Calypso' + '\n').upper()
        if one == 'B':
            two = input('Which alcoholic drink is made from the leaves of the agave plant and gets its name from an area around a Mexican city?' + '\n' + 'A. Tequila \nB. Singani \nC. Chicha \nD. Kasiri' + '\n').upper()
        if two == 'A':
            three = input('What does the Q in IQ stand for?'+ '\n' + 'A. Quantity. \nB. Quorum. \nC. Quality. \nD. Quotient.' +'\n').upper()
        if three == 'D':
            four = input('What is the name of Superman’s home planet?'+ '\n' + 'A. Argon. \nB. Rann. \nC. Krypton. \nD. Qward.' +'\n').upper()
        if four == 'C':
            five = input('According to legend, kissing which stone in Ireland gives you the gift of the gab?' + '\n' + 'A. The Blarney Stone. \nB. The Baloney Stone. \nC. The Rosetta Stone. \nD. The Stone of Destiny.' + '\n').upper()
        if five == 'A':
            pass
        else:
            print('You lost before round one was over that means you leave with nothing!')
            

    def second_round(self):
        one = input('In what country did the first Starbucks open outside of North America?' + '\n' + 'A. Mexico \nB. Australia \nC. Japan \nD. China' + '\n').upper()                 
        three = ''
        four = ''
        five = ''
        if one == 'D':
            two = input('Who was the first televised President?' + '\n' + 'A. Franklin D. Roosevelt \nB. George Washington \nC. Bill Clinton  \nD. Richard Nixon' + '\n').upper()
        if two == 'A':
            three = input('Pocahontas was baptized and given what English name?'+ '\n' + 'A. Hannah \nB. Darlene \nC. Rebecca \nD. Sarah' +'\n').upper()
        if three == 'C':
            four = input('What was the original purpose of the tiny pocket in jeans?'+ '\n' + 'A. Change \nB. Pocket watches \nC. extra buttons \nD. Tobacco' +'\n').upper()
        if four == 'B':
            five = input('In what year was the internet opened to the public?' + '\n' + 'A. 1989 \nB. 1991 \nC. 1995 \nD. 1993' + '\n').upper()
        if five == 'D':
            pass
        else:
            print('You lost before round two was over that means you leave with $1000!')
                
    def third_round(self):
        one = input('What food manufacturing company headquartered in Battle Creek, Michigan, uses several animal mascots to sell its cereals, such as Newton the Owl, Tony the Tiger, and a rooster named Cornelius?' + '\n' + 'A. Kellogs \nB. General Mills \nC. Quaker Oats \nD. Post Foods' + '\n').upper()                 
        three = ''
        four = ''
        five = ''
        if one == 'A':
            two = input('Some of our favorite collective nouns for animals include a congregation of alligators, a business of ferrets, an ostentation of peacocks, and a gaggle of what other fowl?' + '\n' + 'A. Ducks \nB. Geese \nC. Owls  \nD. Eagles' + '\n').upper()
        if two == 'B':
            three = input('Who was the first woman pilot to fly solo across the Atlantic?'+ '\n' + 'A. Joan of Arc \nB. Marie Curie \nC. Florence Nightingale \nD. Amelia Earhart' +'\n').upper()
        if three == 'D':
            four = input(' Who is often credited with creating the world’s first car?'+ '\n' + 'A. Henry Ford \nB. Karl Benz \nC. Horace Dodge \nD. Billy Bob Thornton' +'\n').upper()
        if four == 'B':
            pass    
        else:
            print('You lost before round two was over that means you leave with $32000!')
    def final(self):
        final = input('The title character of this 1726 novel reaches 4 different lands as a result of a shipwreck, a storm at sea, pirates & a mutiny.' + '\n' + 'A. Lord of the Flies \nB. Treasure Island \nC. Gullivers Travels \nD. A Tale of Two Cities' + '\n').upper()
        if final == 'C':
            print('\n' + player_name + ' won $1,000,000 today!')


        

        
        
player_name = input('Please enter your name and press enter. ')
millionaire = Millionaire(player_name)
millionaire.first_round()
round_two = input('You finished round one leave with $1,000 now or keep playing? type y to continue or n to go home' + '\n').upper()
if round_two == 'Y':
    millionaire.second_round()
    round_three = input('You finished round two leave with $32,000 now or keep playing? type y to continue or n to go home' + '\n').upper()
    if round_three == 'Y':
        millionaire.third_round()
        final = input('You finished round three leave with $500,000 now or keep playing? type y to continue or n to go home' + '\n').upper()
        if final == 'Y':
            millionaire.final()
        elif final == 'N':
            print('Good-Bye')
    elif round_three == 'N':
        print('Good-bye')
        exit
    
elif round_two == 'N':
    print('Good-bye')
    exit
