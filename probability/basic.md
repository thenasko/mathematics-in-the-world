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

We can iterate over all even integers between $$0$$ and $$n$$ and add up the probabilities for obtaining that particular number of heads. The resulting expression is
$$
\frac{1}{2^n} \sum_{\substack{0 \leq k \leq n \\ k \textrm{ even}}} \binom{n}{k}.
$$
Trying out some small values for $$n$$, it is easy to see that the answer is 1/2 independently from $$n$$.

There is a simple trick which helps us evaluate the expression above. Recall the formula
$$
(x + y)^n = \sum_{k = 0}^n \binom{n}{k} x^{n-k} y^k.
$$
Replacing $$y$$ with $$-y$$, we get
$$
(x - y)^n = \sum_{k = 0}^n (-1)^k \binom{n}{k} x^{n-k} y^k.
$$
Adding and subtracting the two allows us to filter only even or odd values for $$k$$:
$$
\begin{align}
\frac{ (x+y)^n + (x-y)^n }{2}
&= \sum_{\substack{0 \leq k \leq n \\ k \textrm{ even}}} \binom{n}{k} x^{n-k} y^k, \\
\frac{ (x+y)^n - (x-y)^n }{2}
&= \sum_{\substack{0 \leq k \leq n \\ k \textrm{ odd}}} \binom{n}{k} x^{n-k} y^k.
\end{align}
$$
Plugging in $$x = y = 1/2$$, we find that
$$
\begin{align}
\frac{1}{2^n} \sum_{\substack{0 \leq k \leq n \\ k \textrm{ even}}} \binom{n}{k}
&= \frac{ (1/2 + 1/2)^n + (1/2 - 1/2)^n }{2} \\
&= \frac{ 1^n + 0^n }{2} \\
&= \frac{1}{2}.
\end{align}
$$

In fact, this line of reasoning generalizes substantially. We can use it to show that given arbitrary coins (not necessarily fair), the probability of obtaining an even number of heads is $$1/2$$ if and only if at least one of the coins is fair.

It is worth mentioning that the problem has a very simpler but less enlightening solution. Imagine we have a configuration of $$n$$ coins, and we take the first one and flip it. If we started with an even configuration, we end up with an odd one, and vice versa. This line of reasoning shows that there are equal number of even and odd arrangements. Since all configurations of $$n$$ coins are equally likely, it follows that the probability of getting an even (or odd) one is exactly $$1/2$$.

Alternatively, it is also possible to solve this problem by induction. Consider a sequence of coin tosses and associated random variables $$H_i$$ such that $$H_i = 1$$ if the $i$-th toss came up heads, and $$H_i = 0$$ otherwise. Since all coins are fair, we know that
$$
\mathbb{P}(H_i = 0) =
\mathbb{P}(H_i = 1) =
\frac{1}{2}.
$$
Then set $$X_n = \sum_{i = 1}^n H_i$$. As a base case, we note
$$
\mathbb{P}(X_1 \textrm{ is even}) =
\mathbb{P}(H_1 = 0) =
\frac{1}{2}.
$$
Next, assume that $$\mathbb{P}(X_n \textrm{ is even}) = 1/2$$. We can use conditional probability to compute
$$
\begin{align}
\mathbb{P}(X_{n+1} \textrm{ is even})
&= 
\mathbb{P}(X_{n+1} \textrm{ is even} | H_{n+1} = 0) \mathbb{P}(H_{n+1} = 0) +
\mathbb{P}(X_{n+1} \textrm{ is even} | H_{n+1} = 1) \mathbb{P}(H_{n+1} = 1) \\
&=
\mathbb{P}(X_n \textrm{ is even}) \mathbb{P}(H_{n+1} = 0) +
\mathbb{P}(X_n \textrm{ is odd}) \mathbb{P}(H_{n+1} = 1) \\
&=
\frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} \\
&=
\frac{1}{2}.
\end{align}
$$


### Collecting famous mathematicians

> Tasty-o-crunch, a new brand of cereal, decided to include cards featuring famous mathematicians with their product. Each box contains one of 10 possible cards all of which are equally likely to appear. How many boxes of cereal do you need to buy on average to get a complete set?

This problem may appear somewhat difficult at first, but there is a simple observation which leads to a solution. It is worth spending a bit of time grappling with the problem in order to get a better sense where the difficulty lies.

Let $$X_i$$ denote the number of boxes it takes us to collect $$i$$ distinct mathematicians. Clearly, $$X_1 = 1$$. Once we have our first card, the probability of drawing the same one is $$1/10$$. If we think of this as a coin which comes up tails with probability $$1 - 1/10 = 5/10$$, the expected number of boxes we need to buy before obtaining our second card is $$1 / (9/10) = 10/9$$. This shows that $$\mathbb{E}(X_2 - X_1) = 10/9$$. Continuing this line of reasoning, we compute
$$
\begin{align}
\mathbb{E}(X_1) &= \frac{10}{10} = 1, \\
\mathbb{E}(X_2 - X_1) &= \frac{10}{9}, \\
\mathbb{E}(X_3 - X_2) &= \frac{10}{8}, \\
\mathbb{E}(X_4 - X_3) &= \frac{10}{7}, \\
\mathbb{E}(X_5 - X_4) &= \frac{10}{6}, \\
\mathbb{E}(X_6 - X_5) &= \frac{10}{5}, \\
\mathbb{E}(X_7 - X_6) &= \frac{10}{4}, \\
\mathbb{E}(X_8 - X_7) &= \frac{10}{3}, \\
\mathbb{E}(X_9 - X_8) &= \frac{10}{2}, \\
\mathbb{E}(X_10 - X_9) &= \frac{10}{1}.
\end{align}
$$
Adding all of these, we find the desired answer
$$
\mathbb{E}(X_10) =
10 \left( \frac{1}{1} + \frac{1}{2} + \cdots + \frac{1}{10} \right) \approx
29.290.
$$

What if there were 100 distinct cards instead of 10? The sum $$\sum_{k = 1}^{100} 1/k$$ is much more tiresome to compute. Fortunately, there is an [approximation](http://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant#Asymptotic_expansions) we can use:
$$
\sum_{k = 1}^n \frac{1}{k} =
\ln n + \gamma + \frac{1}{2n} - \frac{1}{12 n^2} + \frac{1}{120 n^3} + O(n^{-4}).
$$
Here $$\gamma \approx 0.577$$ denotes the [Euler-Mascheroni constant](http://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant). Using the approximation, we find that $$\mathbb{E}(X_10) \approx 29.288$$.

The advantages of using the Euler-Mascheroni approximation are twofold. First, we can compute $$\mathbb{E}(X_n)$$ in constant time, whereas the original formula would require linear time in $$n$$. Second, for large values of $$n$$ floating point errors can accumulate quickly, so using the original formula may actually lead to a worse approximation of the actual value than the Euler-Mascheroni approximation.


### The second best

> Eight players enter a tennis tournament with a bracket structure. Suppose that the best player will always win against the second best, who in turn wins against the next best, and so on. If the first round allocation is random, what is the probability that the second best player will play in the final? What if the tournament included $$2^n$$ players?


### The rock-paper-scissors tournament

> Two friends enter a rock-paper-scissors bracket with $6$ other players. All players are evenly matched, so the probability of winning any particular game is 1/2. If the initial arrangement is random, what is the chance that the two friends will face each other at some point during the tournament? What is the answer if the tournament has $$2^n$$ players in total?


### Comparing $$n$$ an $$n+1$$

> Amy has $$n+1$$ fair coins, while her brother Brad only has $$n$$. If both flip all of their coins, what is the probability that Amy will end up with more heads than Brad?



### Singles row

> A number of single men and women independently bought tickets for a movie, and they end up sitting in a single row. If a man and a woman occupy adjacent seats, we will call them a potential couple. Assuming that the seating arrangement is random, and there are $$a$$ men and $$b$$ women, how many potential couples are there on average?


### Two loans

> An aspiring loan shark, Tony, has made two month-long loans. He becomes worried that some of them will default. After a sleepless night of computations, he figures out that the chance of default for the first loan is 10%, and for the second is 20%. What are the possible values for the probability that at least one of the loans will default? What are the possible correlations between the two events?
