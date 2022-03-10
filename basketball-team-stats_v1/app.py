from pickle import TRUE
from secrets import choice
import constants as data
import copy

my_PLAYERS = copy.deepcopy(data.PLAYERS)
my_TEAMS = copy.deepcopy(data.TEAMS)


len_players = len(my_PLAYERS)
len_teams= len(my_TEAMS )

num_players_team = int(len(my_PLAYERS ) / len(my_TEAMS))

balanced_teams = []


def balance_teams():
    return  [my_PLAYERS[i:i+num_players_team] for i in range(0, len(my_PLAYERS), num_players_team)]  
    





# function to clean the Data: Height
def clean_data():
    for i in range(len_players):
        # change heigth to int
        newH = int(my_PLAYERS[i]['height'][:2:1])
        my_PLAYERS[i]['height']=newH
        
        # change experience to bool
        exp = my_PLAYERS[i]['experience']
        if exp == 'NO':
             my_PLAYERS[i]['experience'] = False
        else:
            my_PLAYERS[i]['experience'] = True

        # change guardiens to list
        my_Gardiens = my_PLAYERS[i]['guardians'].split(" and ")
        my_PLAYERS[i]['guardians'] = my_Gardiens
        #print(my_Gardiens)

def runTeam():

    balanced_teams = balance_teams()
    while True:
        opt = input("Enter an option: ")
        #print("test")
        if opt   == "B" or opt   == "C" or opt   == "A":
            pos = int(ord(opt)-65)
            this_team = balanced_teams[pos]
            total_experienced = 0
            total_inexperienced = 0
            total_height = 0
            length = len(this_team)
            Players_on_Team = []
            Guardians = []

            for x in this_team:
                if x['experience']:
                    total_experienced += 1
                else:
                    total_inexperienced += 1 
                    total_height = total_height + x['height']
                Players_on_Team.append(x['name'])
                Guardians.extend(x['guardians'])



            print()
            #print("Team:",this_team ,"Stats")
            print()
            print("--------------------")
            print("Total players:", length)
            print("Total experienced:",total_experienced )   #TODO
            print("Total inexperienced:", total_inexperienced)  #TODO
            print("Average height:", format( total_height/length,'.1f' ))   #TODO
            print()
            print('Players on Team:')
            print(', '.join(Players_on_Team) )#TODO Somthing is wrong
            print()
            print('Guardians:')
            print(', '.join(Guardians) )#TODO Somthing is wrong
            print()
            break 

    input("Press Enter to continue...")




         





def main():
    clean_data()
    '''for p in balanced_teams:
        print(p)
        print()'''
    
    print('BASKETBALL TEAM STATS TOOL')
    while True:
        print('---- MENU----')
        print()
        print()
        print('Here are your choices:')
        print('A) Display Team Stats')
        print('B) Quit')

        choice = input("Enter an option: ")


        if choice  == "B":
                print( "your choice is ", choice) # Something is wrong
                print ("Good Bye")
                break 
        elif choice == "A":
            abc = 'A'
            print()
            for x in my_TEAMS:
                print(abc,") " ,x)
                abc = chr(ord(abc) + 1)
            print()
            runTeam()
             





if __name__ == "__main__":
    main()