## Recursive reasoning

### A magic island

> Once upon a time, there was a magic island on which a hundred smart and rational tigers lived. Even though the tigers did not like eating the local vegetation, they were not cannibals either, so that was their diet.
>
> One day a sheep appeared on the island. Every tiger wanted to eat it, and the sheep was exactly the size of a tiger's meal. As the most blood-thirsty beast approached the sheep, it said ''Be careful. Remember there is magic in the air. If one eats a sheep, they will also become a sheep immediately.''
>
>How does the story end?

Proof:
We start with small cases. Denote the number of tigers as **N**. If **N=1**, then tiger will eat the sheep since no one else can threaten its life afterward. If **N=2**, then tiger will not eat the sheep because if one of the tigers eats the sheep, the cases reduce to the case when **N=1** and then the other tiger will eat the tiger. A stalemate. If **N=3**, then tiger will eat the sheep since the situation reduces to the case when **N=2** which is a stalemate, so the tiger who eats the sheep survives. Now you can see the pattern. If **N** is an odd number, the tiger will eat the sheep while if **N** is an even number, it is a stalemate. 

In order to prove it more rigorously, we need to use mathematical induction. We have already solved the base case when **N=1,2**. Now assume when **N=k**, the induction hypothesis is true. If **k** is an odd number, we know **N=k+1** will be a stalemate since no tiger wants to eat the sheep because it will be eaten afterward. If $k$ is an even number, we know when **N=k+1** a tiger will eat the sheep since it can reduce the situation to a stalemate and live happily after. 

Now since **N=100**, the sheep and the tigers live happily after.

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

Proof:
First, denote the number of samurai who standing when there are **n** samurais as **S(n)**. First, I want to claim that if **n=2^k**, then **S(n)** is **1**. The proof is trivial by mathematical induction. When **k=1**, **1** kills **2**, so **S(2)=1**. Now if **k=m**, the induction hypothesis holds, we consider the case when **k=m+1**. After one round of killing, it reduces to the case when **k=m** and hence **S(n)=1**. 
Now the closest **2^n** to **1000** is **512**. If we can reduce the question size to **n=512**, we immediately get the answer. And it is easy by killing **1000-512** more people. So we have **S(n)=2*(1000-512)+1=977**
