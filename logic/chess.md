## Chess

### Peaceful rooks

> What is the maximal number of rooks you can place on an chess board so that no two can attack each other?

The problems involving finding a maximum are very tricky, because they always consist of two parts.

The first step is guessing what the right number could be. In this case, it is easy to find a configuration with 8 rooks not attacking each other. For instance, we can place them along one diagonal of the chessboard, but there is plenty of other possibilities.

![Rooks](Diagrams/Rooks.png)

Once we have a guess that the maximal number of rooks is 8, we need to show it is impossible to place 9 without one attacking another. This second part is often overlooked, but it is necessary for a complete proof.

We can use the Dirichlet principle, and the argument is very simple. Suppose we have 9 or more rooks on the chessboard, there are at least two that lie in the same column, because the columns are only 8. These two rooks attack each other! And this concludes the proof.


### Peaceful bishops

> What is the maximal number of bishops you can place on an chess board so that no two can attack each other?

We will follow closely what we did for the previous problem. In this case, it is slightly more complicated to guess the maximum. Some experimentation suggests the number is 14, and one possible configuration is the following.

![Bishops](Diagrams/Bishops.png)

Now we need to demonstrate that it is not possible to place 15 or more bishops in a peaceful setting. 

**SOLUTION ONE:** As we did before with columns, we can now consider diagonals as the “holes” of the Dirichlet principle.

![Bishopdiagonals](Diagrams/Bishopdiagonals.png)

We have 15 diagonals, so in principle we *could* place 15 bishops in them, one in each. But exactly as it happens in the problem **We have the same number of friends** above, there are two mutually exclusive options. Looking more carefully, it is not possible to have a bishop in the “diagonal” composed by the only upper left corner *and* one in the lower right corner. They would attack each other, going through the diagonal in the other direction. We have 15 bishops and 14 boxes (collecting together the two opposite corners). Then there must be two of them in the same diagonal that attack each other.

**SOLUTION TWO: ROOKS ON A DIFFERENT CHESSBOARD**


