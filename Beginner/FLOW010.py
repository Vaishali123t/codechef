#python3
t=int(input())
for i in range(t):
    ID=input()
    if ID is 'b' or 'B':
        print('BattleShip')
    elif ID is 'c' or 'C':
        print('Cruiser')
    elif ID is 'd' or 'D':
        print('Destroyer')
    else:
        print('Frigate')
