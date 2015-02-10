## Symmetry

### Calendar dice

> You are planning to order two custom-made dice so they can show the current day of the month (01 to 31). Each face can be engraved with a single digit. You want to use both dice every day, but the order in which you arrange them doesn't matter. Is this possible? If so, provide a sample arrangement of the faces.

Since the two dice (say, A and B) must be able to represent 11 and 22, 1 and 2 must appear on both dice. We claim that 0 must also appear on both dice. Assume the contrary that 0 only appear on one die, say die A, then this only 0 must be used to represent 01,02,...,09 So die B must have all of 1,2,...9 - which is impossible. So 0,1,2 appear on both die. There are only 6 faces left (because 3 faces of each die are taken up by 0,1,2) but the 7 numbers 3,4,...,9 must appear somewhere, contradiction.


### A simple card game

> Someone stops you on the street asking to play the following game. You start with a standard shuffled deck of 52 cards, and take two cards at a time. If both cards are red, they go to your pile. If both cards are black, they go to the opponent's pile. If the cards have different colors, they are discarded. Once the deck is exhausted, the game ends. If you have more cards in your pile, you win $100, and otherwise you don't get anything.
> 
> How much are you willing to pay for the game?

I am willing to pay nothing. Note that in each step of the game, the sum of red cards in my pile and red cards in the center pile is equal to the sum of black cards in my opponent's pile and the blue cards in the center pile. (When I or my opponent take two cards of the same color, it does not change anything; when two cards of different colors are disgarded, both sums are decreased by 1.) So at the end of the game, my pile and my opponent's pile always have equal numbers of cards, so I don't win.

How do you come up with this result? Intuition. This is not as tongue-in-cheek as it might sound. Whenever we have a repeated process, it is a good idea to look for some quantity that is invariant (does not change) or monovariant (only goes up or only goes down) when each iteration of the process occurs, then compare the beginning and the end. Alternatively, you can try with small cards, say 4, and see what happens.

### Apples and oranges

> A stall at the farmer's market sells three products: boxes of apples, boxes of oranges, and a mix of the two. All boxes are fully opaque and mislabeled. The seller offers his customers a discount if they can guess the the contents of all boxes by opening a minimal number of them. What is this number, and how can one get the discount?
> 
> Imagine that the seller becomes more strict with his discount policy. He has redefined ``opening'' a box to mean reaching in and picking a single piece of fruit. How does the problem change?


### Separating coins

> There is a room with 100 coins on the floor, 10 of them are heads up, and the remaining are tails up. If you enter blindfolded, can you produce two piles such that the number of heads up coins in each is equal.
> 
> Assume you cannot distinguish the two sides of a coin by touching it, but you are allowed to turn coins.

You divide the 100 coins into pile A with 10 coins and pile B with 90 coins. Flip all coins in pile A. Then pile A and pile B have equal numbers of heads.

How do you come up with this algorithm? When you are told you cannot do something (say, in this example, blindfolded, or in many other examples, like picking things from a black box etc.) You try to figure out the operations you can legitimately do, especially those that are helpful to your cause. Most of the time it involves some sort of global properties. (In this case, the total head in each pile) Here, we are not told how many coins are in each pile, and since a blindfolded person can count, we can chooose a convenient size. We can also flip all coins in each pile once we know how many coins there are in each pile. Note that flipping random coins won't help you.
