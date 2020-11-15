# War_simulator
Python simulator of the card game "War". The card game War is played as follows:

1) Shuffle a standard deck and distribute the 26 cards to each player. It is a 2 player game. 
2) At each turn both players flip over their top card and compare. The player with the higher card wins both cards and puths them at the bottom of their deck. 
3) In the case of a tie, each player counts out 3 additional cards, and then they compare the 4th card. The winner collects all the cards played. If a second tie occurs you repeat step 3 again. 
4) The game ends when someone has no cards left. 
5) In the situation when one player has less than 4 cards on a tie they automatically lose as they don't have a 4th card to compare. 

The problem with the game of war is that it is rarely ever finished. It takes a very long time to finish and usually ends with one player giving up. This python script automates the process and generates the number of turns needed to finish the game. We simulate 500 games and record the number of steps it took to finish. We print the results to a histogram. 

