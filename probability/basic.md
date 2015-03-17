## Basic probability

### Successive wins

> You signed up for a tennis tournament in which you win a prize if you win (at least) two successive games in a row of three. Your two opponents are your friend and the club champion. Given the option to play friend-champion-friend or champion-friend-champion, which scenario would you pick? What is the expected number of wins in each case?

Let the probability of winning against your friend be $$p$$ and against the chamion be $$q$$. We know that $$p > q$$.

Putting the comparison of the two scenarios aside, let us try to compute the probabilities of two successive wins. To get two successive wins in a row of three games, we should either win all three, lose the first one only, or lose the last one only. If we are playing friend-champion-friend, the total probability is
$$
P_{\textrm{fcf}} =
p q p + (1 - p) q p + p q (1 - p) =
p q (2 - p).
$$
Likewise, the probability of two successive wins in a champion-friend-champion setup is
$$
P_{\textrm{cfc}} =
q p q + (1 - q) p q + q p (1 - q) =
p q (2 - q).
$$

We are now ready to compare the the scenarios. Since $$p < q$$, it follows that $$2 - p > 2 - q$$, so
$$
P_{\textrm{fcf}} < P_{\textrm{cfc}}.
$$
At first glance, this may be surprising and counter-intuitive. Why should we opt to play the more seasoned player twice, if we can do that only once? The answer lies in the middle game. If we loose it, then no matter how well we play the first and third games, we cannot obtain two successive wins. In the friend-champion-friend scenario, the middle game is the hardest one, hence the lower overall chance of two successive wins.


### Flippant juror

> As part of his jury duty, an undergraduate student was chosen to participate in a jury of three members (majority rules). To express his disinterest in the case, he decides to vote by flipping a fair coin. The other two members of the jury independently will make the right decision with probability $$p$$. How does this arrangement compare to a single member jury which decides on the correct outcome with the same probability $$p$$?

The three person jury would decide on the right outcome only if at least two of the members choose that option. There are four voting scenarios which lead to this outcome: all correct, first two correct, first and third correct, second and third correct. Adding them up, we get
$$
p \cdot p \cdot \frac{1}{2} +
p \cdot p \cdot \frac{1}{2} +
p \cdot (1 - p) \cdot \frac{1}{2} +
(1 - p) \cdot p \cdot \frac{1}{2} =
p.
$$
It turns out the three member jury is as efficient as a single member jury!


### First six

> How many times do you need to throw a die on average before you get a 6?

The is the prototypical example of a [geometric distribution](http://en.wikipedia.org/wiki/Geometric_distribution). Since the probability of throwing a $$6$$ is $$1 / 6$$, the expected number of throws is $$1 / (1 / 6) = 6$$.

Let us go over the derivation of this result. Instead of using a die, imagine we have a coin which comes up heads with probability $$p > 0$$, and we are interested in the expected number of throws $$X$$ until we get heads. The probability of getting heads for the first time in the $$k$$-th throw is
$$
\mathbb{P}(X = k) =
(1 - p)^{k-1} p.
$$
The expected value of $$X$$ is
$$
\begin{align}
\mathbb{E}(X)
&= \sum_{k \geq 1} k \mathbb{P}(X = k) \\
&= \sum_{k \geq 1} k (1 - p)^{k-1} p \\
&= p \sum_{k \geq 1} k (1 - p)^{k-1} \\
&= p \cdot \frac{1}{(1 - (1 - p))^2} \\
&= \frac{1}{p}.
\end{align}
$$
Note that we used the formula $$\sum_{k \geq 1} k x^{k-1} = 1 / (1 - x)^2$$. For more information, see the discussion of [generating functions](/number_theory/generating-functions.md).


### Perfect hand

> In a game of bridge, what is the probability that you are dealt a perfect hand (13 cards of one color)?


### Walking in Manhattan

> Imagine a city whose streets form a perfect grid. Starting at the point with coordinates $$(0,0)$$, how many ways are there to walk to the intersection $$(m, n)$$ in $$m + n$$ steps?


### A personal taste for money

> Ten white and ten black balls are placed in an urn. You are allowed to choose one of the two colors. A ball is drawn from the urn, and it the color matches you get $10. If the colors are not a match, there is no prize. If the game is to be played only once, how much are you willing to pay for it?


### St. Petersburg paradox

> A casino offers a game in which a fair coin is tossed at each stage. The initial steak is $\$2$. If the coin comes up tails, you receive the steak. If we get heads, the steak is doubled, and the process repeats. How much should they charge for this game?
> 
> What if every time we get heads, the steak is increased by one? How much should they charge?


### Even split

> What is the probability of getting exactly 50 heads if you flip 100 fair coins? Can you find a concrete figure approximating the result without using additional computational power?


### An even number of heads

> You flip $$n$$ fair coins independently. What is the probability to get an even number of heads?


### Collecting famous mathematicians

> Tasty-o-crunch, a new brand of cereal, decided to include cards featuring famous mathematicians with their product. Each box contains one of 10 possible cards all of which are equally likely to appear. How many boxes of cereal do you need to buy on average to get a complete set?


### The second best

> Eight players enter a tennis tournament with a bracket structure. Suppose that the best player will always win against the second best, who in turn wins against the next best, and so on. If the first round allocation is random, what is the probability that the second best player will play in the final? What if the tournament included $$2^n$$ players?


### The rock-paper-scissors tournament

> Two friends enter a rock-paper-scissors bracket with $6$ other players. All players are evenly matched, so the probability of winning any particular game is 1/2. If the initial arrangement is random, what is the chance that the two friends will face each other at some point during the tournament? What is the answer if the tournament has $$2^n$$ players in total?


### Comparing $$n$$ an $$n+1$$

> Amy has $$n+1$$ fair coins, while her brother Brad only has $$n$$. If both flip all of their coins, what is the probability that Amy will end up with more heads than Brad?


### Singles row

> A number of single men and women independently bought tickets for a movie, and they end up sitting in a single row. If a man and a woman occupy adjacent seats, we will call them a potential couple. Assuming that the seating arrangement is random, and there are $$a$$ men and $$b$$ women, how many potential couples are there on average?
