## Recursive reasoning

### A magic island

> Once upon a time, there was a magic island on which a hundred smart and rational tigers lived. Even though the tigers did not like eating the local vegetation, they were not cannibals either, so that was their diet.
>
> One day a sheep appeared on the island. Every tiger wanted to eat it, and the sheep was exactly the size of a tiger's meal. As the most blood-thirsty beast approached the sheep, it said ''Be careful. Remember there is magic in the air. If one eats a sheep, they will also become a sheep immediately.''
>
>How does the story end?

We start with small cases. Denote the number of tigers as $$N$$. If $$N=1$$, then tiger will eat the sheep since no one else can threaten its life afterward. If $$N=2$$, then tiger will not eat the sheep because if one of the tigers eats the sheep, the cases reduce to the case when $$N=1$$ and then the other tiger will eat the tiger. A stalemate. If $$N=3$$, then tiger will eat the sheep since the situation reduces to the case when $$N=2$$ which is a stalemate, so the tiger who eats the sheep survives. Now you can see the pattern. If $$N$$ is an odd number, the tiger will eat the sheep while if $$N$$ is an even number, it is a stalemate. 

In order to prove it more rigorously, we need to use mathematical induction. We have already solved the base case when $$N=1,2$$. Now assume when $$N=k$$, the induction hypothesis is true. If $$k$$ is an odd number, we know $$N=k+1$$ will be a stalemate since no tiger wants to eat the sheep because it will be eaten afterward. If $$k$$ is an even number, we know when $$N=k+1$$ a tiger will eat the sheep since it can reduce the situation to a stalemate and live happily after. 

Now since $$N=100$$, the sheep and the tigers live happily after.

### Democratic pirates

> Ten democratic pirates looted 100 gold coins. Seeing that they need to divide the treasure, they agreed on the following method.
> 
> First, the most senior pirate proposes a distribution. All pirates, including the most senior one, proceed to vote. If at least half of them accept distribution, the loot is divided as proposed. If not, the most senor pirate will be thrown overboard. The process continues with the next most senior pirate, and so on.
> 
> Assume the pirates are rational: they prefer to stay alive first, and earn more gold second. Also, given two otherwise equal outcomes, they prefer to have fewer pirates on the ship.
> 
> How will the pirates divide the gold?

This problem can be solved by trying to understand what happens in case the pirates are less than 10. 

Let us start with the case where we have 2 pirates (the case of 1 pirate only is not really interesting). The most senior pirate has the majority whatever proposal he makes, because only one affirmative vote is needed. Assuming he is greedy, he will propose the distribution where he gets all 100 coins, and the second none.

Let us now analyze the case where we have 3 pirates. Using our solution for two pirates, it follows that if the proposal doesn't pass, the second pirate will propose to get all the coins. He will get them because he only needs one affirmative vote at that stage. In turn this means that the third pirate will not get paid if the first proposal doesn't pass.

Let us understand how the most senior pirate can obtain somebody else's vote. To obtain the second's vote, he would need to improve his chances - that is impossible, because he will get all coins if the proposal doesn't pass. To obtain the vote of the youngest pirate, it is needed to improve his odds, namely, that if the proposal doesn't pass he will get no coins. Then, the most senior pirate can offer the third pirate one coin, and he will get the further vote he needs, keeping for himself 99 coins.

If we have 4 pirates, the same argument shows that the oldest pirate just needs to offer the third pirate one coin, and he will get away will 99 coins. More generally, if there are $$n$$ pirates, the oldest pirate needs to offer 1 coin to the third, fifth, seventh, and ninth, because the odds of these pirates are to get zero coins if the proposal doesn't pass. It follows that the pirate leader keeps 96 coins for himself. The following table summarizes out solution.

| **Pirate** | 1  | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------------|----|---|---|---|---|---|---|---|---|----|
| **Pay**    | 96 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0  |

This solution is a very simple example of mathematical induction. We found out what happens for $$n$$ pirates, using the knowledge that we have of what happens when we have $$n-1$$.

### Kill Bill

> A thousand samurai, numbered 1 to 1000, are standing in a circle. The first one takes his sword and kills the second. Then, the next man in the circle, number 3, kills number 4. The process continues until there is only one samurai standing. What is his number?

We will present two solutions to this problem, one recursive, and one more direct. In both cases, it is useful to look at the more general setup of $$n$$ samurai. We will then denote the winner's number by $$S(n)$$.

**SOLUTION 1:**
If we go through several small cases by hand, it is easy to see that $$S(n) = 1$$ for all $$n = 2^k$$ where $$k$$ is an integer. To see this, note that if we start with $$n = 2^k$$ samurai, then going around once only the odd ones survive leaving $$2^{k-1}$$ men standing and it is number 1's turn. Reducing by a factor of two, it is easy to see that number 1 doesn't die as long as $$n$$ is a power of 2, hence $$S(2^k) = 1$$ for all $$k$$.

This is a very interesting fact, but $$n = 1000$$ is certainly not a power of 2. The key observation is that at some point after the game starts, the number of men standing will be a power of 2. For $$n = 1000$$, the largest power of two less of equal to $$n$$ is $$512 = 2^9$$. Once we reach 512, imagine that we reorder the people: 1, ..., 512. The discussion above shows that number 1 in this ordering would be the winner. We have reduced the problem to finding who is the next person to act when there are 512 men standing. If we start with 1000, it means that $$1000 - 512 = 488$$ people have been killed. Since each of these was slayed by the preceding one in sequence, we deduce that the 488 men down are $$2, 4, \dots, 976 = 2 \cdot 488$$. The next turn is in the hands of 977, so he will be the winner.

Let us try to generalize this logic to any value $$n$$. The largest power of two less of equal to $$n$$ is $$2^{\lfloor \log_2 n \rfloor}$$. It follows that
$$
n - 2^{\lfloor \log_2 n \rfloor}
$$
people are killed before we reach a power of two. The next person to act, who is also the winner, is
$$
S(n) = 2 (n - 2^{\lfloor \log_2 n \rfloor}) + 1.
$$

**SOLUTION 2:**
The second approach we present analyzes one "round" of the game, so we reduce the problem with $$n$$ samurai to one with roughly $$n/2$$.

First, consider the case in which $$n = 2m$$ is even. Going around once, only the odd men survive and there are $$m$$ of them. We can then reorder these $$1, \dots, m$$, and number $$i$$ in the new ordering translates to number $$2 i - 1$$ in the old one. The following table summarizes this observation.

| **Original ordering** | 1 | 2 | 3 | 4 | ... |          | ... | $$2m-1$$ | $$2m$$ |
|-----------------------|:-:|:-:|:-:|:-:|:---:|:--------:|:---:|:--------:|:------:|
| **Survivors**         | 1 |   | 3 |   | ... | $$2i-1$$ | ... | $$2m-1$$ |        |
| **New ordering**      | 1 |   | 2 |   | ... | $$i$$    | ... | $$m$$    |        |

In other words, if the winner in a circle of size $$m$$ is $$S(m)$$, then the winner in a circle of size $$2m$$ is
$$
S(2m) = 2 S(m) - 1.
$$

We can analyze the odd case $$n = 2m + 1$$ in a similar manner. Analyzing the first round only the odd ones survive. In the next step, $$2m + 1$$ kills number 1, and $$3$$ is the next one to act. Again, we are left with a circle of size $$m$$. If we apply the typical ordering to it, translating back sends $$i$$ to $$2 i + 1$$. The following table summarizes this information.

| **Original ordering** | 1 | 2 | 3 | 4 | 5 | ... |          | ... | $$2m$$ | $$2m+1$$ |
|-----------------------|:-:|:-:|:-:|:-:|:-:|:---:|:--------:|:---:|:------:|:--------:|
| **Survivors**         |   |   | 3 |   | 5 | ... | $$2i-1$$ | ... |        | $$2m+1$$ |
| **New ordering**      |   |   | 1 |   | 2 | ... | $$i$$    | ... |        | $$m$$    |

Then the winner is
$$
S(2m+1) = 2 S(m) + 1.
$$

These two recursive relations together with the base case $$S(1)$$ fully characterize the function $$S$$:
$$
S(n) =
\begin{cases}
2 S(m) - 1 & \textrm{if } n = 2m \textrm{ is even}, \\
2 S(m) + 1 & \textrm{if } n = 2m+1 \textrm{ is odd}, \\
1 & \textrm{if } n = 1.
\end{cases}
$$

Once we have this, it is easy to compute $$S(1000)$$. The following table summarizes the computation: we first populate the second column going down, then the third one in reverse.

| $$n$$ | Expression for $$S(n)$$    | Value of $$S(n)$$ |
|-------|----------------------------|------------------:|
| 1000  | $$S(1000) = 2 S(500) - 1$$ | 977               |
| 500   | $$S(500)  = 2 S(250) - 1$$ | 489               |
| 250   | $$S(250)  = 2 S(125) - 1$$ | 245               |
| 125   | $$S(125)  = 2 S(62)  + 1$$ | 123               |
| 62    | $$S(62)   = 2 S(31)  - 1$$ | 61                |
| 31    | $$S(31)   = 2 S(15)  + 1$$ | 31                |
| 15    | $$S(15)   = 2 S(7)   + 1$$ | 15                |
| 7     | $$S(7)    = 2 S(3)   + 1$$ | 7                 |
| 3     | $$S(3)    = 2 S(1)   + 1$$ | 3                 |
| 1     | $$S(1)    = 1           $$ | 1                 |

