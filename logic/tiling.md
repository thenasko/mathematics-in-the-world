## Tiling and packing

### Tiling with dominoes

> We are given a $$8 \times 8$$ board with two diagonal corners missing. Is it possible to cover it completely with dominoes without any pieces overlapping.
> 
> Assume the board and domino squares are of the same size.

At firth sight, it is tempting to think that the answer to this question is positive. On the other hand, experimentation shows that a tiling is hard to get. As a general principle, trying to obtain a tiling (of a possibly smaller board) is a good place to start building intuition about a problem.

Let us imagine we have tried to tile the board by hand a few times unsuccessfully, and we are now convinced that no tiling exists. How can we go about proving such a result? One way would be to start adding dominoes one by one, enumerate all possible scenarios and find that none of them lead to a solution. While this may work for some smaller cases, it is clear it is not the correct strategy here.

The idea is to look for a property satisfied by any tileable board. If we show that our board does not satisfy this condition, then naturally no tiling exists. It is no coincidence that the question is stated for an $$8 \times 8$$ board, the same size as chess board. One distinguishing feature of chess boards is they are colored in black and white in an alternating pattern.

![Chess board](Diagrams/Chess_Board.png)

Direct inspection shows that no matter how we place a domino on the board, it always covers one white and one black square. It follows that if a board (of any shape) has a tiling by $$n$$ domino pieces, then after coloring it with the chess pattern, there must be $$n$$ white and $$n$$ black blocks.

This is just what we need. Starting from the standard board above, we need to remove two diagonally opposite corners. Without loss of generality, we can always rotate the board so these are the upper left and lower right corners. Constructing a coloring as the one shown above, both of these places are white. While the original board had an equal number of black and white pieces, each 32, the modified one has 30 white and 32 black pieces. These numbers are not equal, so we conclude that the modified board cannot be tiled with dominoes.

Note that the statement of the problem made no mention of a coloring. That was the crucial step in our solution, but at the same time, it is an auxiliary construction we have control over. Two colors worked well here, but there is no reason why we shouldn't use three or more colors in a different problem.


### Tiling with length 3 pieces

> Can you tile an $$8 \times 8$$ board with $$1 \times 3$$ pieces?
> 
> What if one corner of the board is missing?

No we can't. $$8*8=64$$ is not divisible by $$3$$.

No, we still can't. Color the $$8x8$$ board with 0,1,2 three colors in following way. For $$T_{ij}$$, color it with $$i+j(mod 3)$$. If we count the number of each color, we have number of $$0$$-tile is $$22$$, $$1$$-tile is $$20$$, $$2$$-tile is $$21$$. But each $$1 x 3$$ will cover each color once. So it is impossible.


### Tiling with T-pieces

> Can you tile a $$10 \times 10$$ board with pieces of the following shape.
> 
> ![T-shaped piece](Diagrams/Tetris_T.png)

The shape of the pieces makes this problem appear a little harder, but in fact it is quite simple. Let us imagine a tiling exists, and we color the board in the standard alternating black and white pattern. The pieces which constitute the tiling can be split into two categories: type A which has 3 black and 1 white squares, and type B with 1 black and 3 white squares.

![T-shaped pieces types](Diagrams/Tetris_T_two.png)

Suppose there are $$a$$ pieces of type A, and $$b$$ pieces of type B. The entire board has $$10^2 = 100$ squares of which 50 are black and 50 are white. Equating the squares in each color, we obtain the following.
$$
\begin{align}
3 a + b &= 50 \\
a + 3 b &= 50 \\
\end{align}
$$
Adding and subtracting these equations, it is easy to arrive at $$a + b = 25$$ and $$a = b$$. But then $$2a = 25$$ which has no integer solutions, and we reached a contradiction. We conclude that it is impossible to tile a $$10 \times 10$$ board with T-shaped pieces.

Note that the same argument works for any board of size $$n \times n$$ where $$n$$ is odd but not divisible by 4.


### Packing bricks

> Is it possible to fit 53 bricks of size $$1 \times 1 \times 4$$ into a $$6 \times 6 \times 6$$ box?

Impossible.
The idea is similar to Problem 4, but with different coloring. This time instead of coloring alternatively with 1 x 1 x 1 block, we color alternatively with 2 x 2 x 2 block. WLOG, assume black is at the corner. And hence we have $$B=2* 2* 2*(5+4+5)=112$$ while $$W=2* 2* 2*(4+5+4)=101$$. But now each bricks of 1 x 1 x 4 much cover two white and two black and hence it is impossible to fit in.

