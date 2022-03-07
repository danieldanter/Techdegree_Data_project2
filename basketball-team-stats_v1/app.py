from pickle import TRUE
import constants as data
import copy

my_PLAYERS = copy.deepcopy(data.PLAYERS)
my_TEAMS = copy.deepcopy(data.TEAMS)


length = len(my_PLAYERS)





# function to clean the Data: Height
def clean():
    for i in range(length):
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




def main():
    clean()
    print(my_PLAYERS)




if __name__ == "__main__":
    main()