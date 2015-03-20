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
Note that we used the formula $$\sum_{k \geq 1} k x^{k-1} = 1 / (1 - x)^2$$. For more information, see the discussion of generating functions.


### Perfect hand

> In a game of bridge, what is the probability that you are dealt a perfect hand (13 cards of one color)?


### Walking in Manhattan

> Imagine a city whose streets form a perfect grid. Starting at the point with coordinates $$(0,0)$$, how many ways are there to walk to the intersection $$(m, n)$$ in $$m + n$$ steps?

The key to this problem is finding a suitable interpretation of the suitable paths. Given a path, we will associate to it a list of instructions *X* and *Y*: "X" stands for a step in the positive $$x$$-direction (right), and likewise for "Y". A path between $$(0,0)$$ and $$(m,n)$$ must be made up of $$m+n$$ instructions, $$m$$ of which are X and the remaining $$n$$ Y. Conversely, given such a string of Xs and Ys, we can construct a path.

We have reduced the problem to counting strings of length $$m+n$$ with $$m$$ Xs and $$n$$ Ys. The answer to this simple combinatorial problem is
$$
\binom{m+n}{m} = \binom{m+n}{n}.
$$


### A personal taste for money

> Ten white and ten black balls are placed in an urn. You are allowed to choose one of the two colors. A ball is drawn from the urn, and it the color matches you get $10. If the colors are not a match, there is no prize. If the game is to be played only once, how much are you willing to pay for it?

The probability of getting matching colors is $$1/2$$, so the expected value of the game is
$$
\frac{1}{2} \cdot 10 + \frac{1}{2} \cdot 0 = 5.
$$
Whether anyone would be willing to pay $5 for this game is an entirely different question. First, if we were allowed to play the game many times, and we paid less than $5 for it, we expect to have positive earnings. On the other hand, there is no reason to pay more than $5 from the game, that is, unless we derive additional gains by playing this game (e.g., it is enjoyable, we network, etc.).

If we are only allowed to play once, paying $5 seems like an even steeper price. In the end of the day, making a decision requires weighing the possibility of wining $5 against the possibility of loosing $5. The point of this discussion is that expected value is useful when evaluating games, but it should not be the only criterion we take into consideration. There are numerous additional factors, but one should always look at the variance and any potential stop limits.


### St. Petersburg paradox

> A casino offers a game in which a fair coin is tossed at each stage. The initial steak is $\$2$. If the coin comes up tails, you receive the steak. If we get heads, the steak is doubled, and the process repeats. How much should they charge for this game?
> 
> What if every time we get heads, the steak is increased by one? How much should they charge?


### Even split

> What is the probability of getting exactly 50 heads if you flip 100 fair coins? Can you find a concrete figure approximating the result without using additional computational power?

The probability for obtaining an even split is
$$
\frac{1}{2^{100}} \binom{100}{50} =
\frac{100!}{2^{100} \cdot 50! \cdot 50!}.
$$
To get an approximate value, we will use the [Stirling's approximation formula](http://en.wikipedia.org/wiki/Stirling%27s_approximation) which states that
$$
n! \approx \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n.
$$
Substituting, we can simplify the expression above to
$$
\frac{1}{2^{100}} \binom{100}{50}
\approx
\frac{1}{5 \sqrt{2 \pi}}
\approx
0.0798.
$$
Without approximations, the actual value is closer to $$0.0796$$.

It is worth noting that we computed there is almost 8% chance of getting an even split between heads and tails when using 100 coins. Depending on prior experience, this may intuitively appear as a fairly high value.


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
