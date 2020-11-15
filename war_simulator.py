import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def standard(winner, loser):
        a = winner[0]
        b = loser[0]
        winner = winner[1:len(winner)]
        loser = loser[1:len(loser)]
        winner = np.concatenate((winner, np.random.choice([a,b], size=2, replace=False)))
        return winner, loser


def tie(A,B):
    if len(A) < 5:
        A = []
        B = [0]*52
        return A, B
    if len(B) < 5:
        B = []
        A = [0]*52
        return A, B

    every_forth_A = list(A)
    every_forth_A = every_forth_A[0::4]

    every_forth_B = list(B)
    every_forth_B = every_forth_B[0::4]

    i = 1
    while True: 
        if i ==len(every_forth_A):
            A = []
            B = [0]*52
            return A,B
        if i == len(every_forth_B):
            B = []
            A = [0]*52
            return A,B
        if every_forth_A[i] == every_forth_B[i]:
            #print('Player A:', every_forth_A[i], ' v.s. ', every_forth_B[i], ':Player B')
            if i ==len(every_forth_A):
                A = []
                return A,B
            if i == len(every_forth_B):
                B = []
                return A,B
            i +=1
        else:
            #print('Player A:', every_forth_A[i], ' v.s. ', every_forth_B[i], ':Player B')
            if every_forth_A[i] > every_forth_B[i]:
                    A_loss = A[0: 4*i+1]
                    A_keep = A[4*i+1::]

                    B_loss = B[0: 4*i+1]
                    B_keep = B[4*i+1::]
                    
                    gainz = np.concatenate((A_loss, B_loss))
                    A = np.concatenate((A_keep, np.random.choice(gainz, size=len(gainz), replace=False)))
                    B = np.array(B_keep)
                    return A, B
            else:
                    A_loss = A[0: 4*i+1]
                    A_keep = A[4*i+1::]

                    B_loss = B[0: 4*i+1]
                    B_keep = B[4*i+1::]
                    
                    gainz = np.concatenate((A_loss, B_loss))
                    B = np.concatenate((B_keep, np.random.choice(gainz, size=len(gainz), replace=False)))
                    A = np.array(A_keep)
                    return A, B


def game_simulation():
    # Build the deck
    deck = []
    for i in range(2,15):
        deck  = deck + [i]*4

    deck = np.array(deck)

    # shuffle the deck
    deck = np.random.choice(deck, size = 52, replace=False)
    A = deck[0:26]
    B = deck[26:52]

    turns = 0
    while (len(B)>0) and (len(A)>0):
        #print('Player A:', A[0], ' v.s. ', B[0], ':Player B')
        if A[0] > B[0]:
            A, B = standard(A,B)
        elif A[0] < B[0]:
            B, A = standard(B,A)
        else:
            A, B = tie(A,B)
        #print('\n Turn #: ', turns)
        #print('Player A has ', len(A), ' cards')
        #print('Player B has ', len(B), ' cards')
        turns = turns + 1

    if  len(A)>0:
        winner = 'A'
        #print('\n Player A wins!!! in ', turns, ' turns')
    else:
        winner = 'B'
        #print('\n Player B wins!!! in ', turns, ' turns')

    return winner, turns

if __name__ == '__main__':
    winner_data = []
    turns_data = []
    for i in tqdm(range(500)):
        winner, turns = game_simulation()
        winner_data.append(winner)
        turns_data.append(turns)
    A_wins = np.count_nonzero(np.array(winner_data) == 'A')
    print('Percentage of times A won :', A_wins/500)

    plt.hist(turns_data, bins=75)
    plt.show()
    

    
    

