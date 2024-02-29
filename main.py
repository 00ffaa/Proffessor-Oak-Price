import pandas as pd

pokemon=pd.read_csv('C:/Users/kino/PycharmProjects/HowManyGamesForAllThePokemon/pokemon_availability.csv')

allowed_symbols=['C', 'S', 'D', 'R', 'E', 'B', 'CD', 'DA', 'CC', 'FS', 'EV', 'ED']

#defaults here are the games featured in the video, remove and add as you like
necessary_games=[38,37,36,33,32,29,28,25,24,21,22,20,19]

number_remaining=0

#loop through every pokemon
for i in range(1,1086):
    temp=[]
    count=0
    #loop through every game
    for j in range(1,38):
        temp.append(pokemon.at[i,str(j)])
        #loop through allowed catch types
        for k in allowed_symbols:
            if temp[j-1]==k:
                count+=1

    already_in_necessary=False

    #loops through games we have in our necessary list
    for j in necessary_games:
        for k in allowed_symbols:
            #if this has been in one of the necessary games
            if pokemon.at[i,str(j)] == k:
                already_in_necessary=True

    if already_in_necessary==False:
        number_remaining+=1
        print(pokemon.at[i,'Name'])

print(f"{number_remaining} left")


