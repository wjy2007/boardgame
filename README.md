# This is a boardgame that doesn't have a name(maybe will later)

## The rules are as follows:

1. Currently there are 2 players, P1 & P2, whose colors are red and blue respectively
   The players are represented by the orange arrow
   
2. Each player takes turn until it reaches round 15 (a round is complete when the 2 players have made their moves)
 
3. Specificly, in each turn (P1's turn for example):
> 1. P1 chooses the direction① (turning the arrow)
> 2. P1 clicks "the dice"② and walks③
> 3. P1 places his "carpet"④
> 4. click the "confirm" button
 
①: in the 1st round he can choose any direction of the 4, but in the later rounds he can turn to any direction except for turning back from the current direction
   e.g. currently they are facing "up", so the next player can only turn to "left", "right" or stay the same(turning "up"), he cannot turn to "down" 
   
②: the dice consists of integers from 1 to 4

③: to walk means to move the corresponding number of grids towards the current direction. If the arrow crosses the boarder, it will continue from the other side of the grid in the same row

④:the carpet is a 1×2 rectangle in red or blue. It can be seen as the players' territory. When the other player stepped on it, he will have to pay the fine. The amout of the fine is equivalent to the number of connected (only side-side contact counts) grids which are in the color of the opponent.
  The money of each player will be showed on the screen (each players' money is 30 initially)
  
## Details:

1. the dice is the small orange square in the top-right corner, and the number you rolled is shoewd on the right, **click to row it**
2. the round number is above the dice
3. everyone's score(**which is the money**) is showed below the dice, the score of the player who is ahead will be red (if the same then it's P1), the arrow on the left points the current player
4. the 
