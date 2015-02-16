## Chess

### Peaceful rooks

> What is the maximal number of rooks you can place on an chess board so that no two can attack each other?

The problems involving finding a maximum are very tricky, because they always consist in two parts.

The first step is guessing what could be the right number: in this case, after a bit of guessing, is it easy to find a configuration with 8 rooks not attacking each other. For instance, we can place them along one diagonal of the chessboard, but there is plenty of other possibilities.

Then it comes the second part, that people sometimes forget, but that it needed to produce a complete proof. What we need to do is to *prove* that 8 is indeed the maximum. In other words, that whenever we have 9 rooks or more, there are always two that attack each other.

Here, we can use the Dirichlet principle, and the argument is very simple. Suppose we have 9 or more rooks on the chessboard, there are at least two that lie in the same column, because columns are only 8. Then, these two rooks attack each other! And this concludes the proof.

### Peaceful bishops

> What is the maximal number of bishops you can place on an chess board so that no two can attack each other?

We will follow closely what we did for the previous problem. In this case, it’s slightly more complicated to guess what this maximal number is. It is indeed 14, and one possible configuration is the following.

![Chess board](Diagrams/Bishop.png)

Now we need to prove that it is not possible to place 15 or more bishops in a peaceful setting. As we did before with columns, we can now consider diagonals as the “holes” of the Dirichlet principle.

![Chess board](Diagrams/Chess_Board.png) ADD THE DIAGONALS

We have 15 diagonals, so in principle we *could* place 15 bishops in them, one in each. But exactly as it happens in the problem “We have the same number of friends” above, there are two mutually exclusive options. Looking more carefully, it is not possible to have a bishop in the “diagonal” composed by the only upper left corner *and* one in the lower right corner. They would attack each other, going through the diagonal in the other direction. So, again, we have 15 bishops, 14 boxes (collecting together the two opposite corners) so there have to be two of them in the same diagonal, that attack each other.

