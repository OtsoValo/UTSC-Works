import random


# initialize the count of stay and swap
stay = 0
swap = 0
# run for specific times
for i in range(10000):
    # initialize the choice
    choice = [0, 0, 0]
    car_num = random.randrange(3)
    # put the car in random door
    choice[car_num] = 1
    # choose a door between 0 to 2
    your_choice = random.randrange(3)
    # if choose the car at the beginning, then open a random door
    if choice[your_choice] == 1:
        open_door = your_choice
        while open_door == your_choice:
            open_door = random.randrange(3)
        # open the door, and delete from the choice
        del choice[open_door]
        if your_choice > open_door:
            your_choice -= 1
    # if choose the goat at the beginning, then open a door with goat
    else:
        open_door = your_choice
        while (open_door == your_choice) or (choice[open_door]==1):
            open_door = random.randrange(3)
        # if index of your_choice is greater than deleted one, then move it
        del choice[open_door]
        if your_choice > open_door:
            your_choice -= 1
    # get the swap door random
    swap_door = 0
    while swap_door == your_choice:
        swap_door = random.randrange(len(choice))
    # determine if the door hide the car
    if choice[your_choice] == 1:
        stay += 1
    elif choice[swap_door] == 1:
        swap += 1
    # debug for the errors
    else:
        print('############ There is an error! ############')
        print('your_choice', your_choice)
        print('swap_door', swap_door)
        print('choice', choice)
        print('the car index', choice.index(1))
# print the result
print('############ The Result ############')
print('stay to win', stay)
print('swap to win', swap)
