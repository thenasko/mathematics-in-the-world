## Recursive reasoning

### A magic island

> Once upon a time, there was a magic island on which a hundred smart and rational tigers lived. Even though the tigers did not like eating the local vegetation, they were not cannibals either, so that was their diet.
>
> One day a sheep appeared on the island. Every tiger wanted to eat it, and the sheep was exactly the size of a tiger's meal. As the most blood-thirsty beast approached the sheep, it said ''Be careful. Remember there is magic in the air. If one eats a sheep, they will also become a sheep immediately.''
>
>How does the story end?


### Democratic pirates

> Ten democratic pirates looted 100 gold coins. Seeing that they need to divide the treasure, they agreed on the following method.
> 
> First, the most senior pirate proposes a distribution. All pirates, including the most senior one, proceed to vote. If at least half of them accept distribution, the loot is divided as proposed. If not, the most senor pirate will be thrown overboard. The process continues with the next most senior pirate, and so on.
> 
> Assume the pirates are rational: they prefer to stay alive first, and earn more gold second. Also, given two otherwise equal outcomes, they prefer to have fewer pirates on the ship.
> 
> How will the pirates divide the gold?

This problem can be solved trying to understand what happens in case the pirates are less than 10. 

Let us start with the case where we have 2 pirates (the case of 1 pirate only is not really interesting); the oldest pirate has the majority whatever proposal he makes, because only one affirmative vote is needed; he can then just propose the distribution where he gets all 100 coins, and the second none.

Let us now analyze the case where we have 3 pirates; at first, using what we just found out, if the proposal doesn't pass, the second oldest pirate will propose to get all the coins, and he will get them because he only needs one affirmative vote at that stage. So, let us understand how the oldest pirate can obtain somebody else's vote; to obtain the second's vote, he would need to improve his chances - that is impossible, because he will get all coins if the proposal doesn't pass; to obtain the vote of the younger pirate, it is needed to improve his odds, that if the proposal doesn't pass are to get no coins. The senior pirate can then offer the third pirate one coin, and he will get the further vote he needs, keeping for himself 99 coins.

If we have 4 pirates, the same argument shows that the oldest pirate just needs to offer the third pirate one coin, and he will get away will 99 coins. More in general, if there are $$n$$ pirates, the oldest pirate needs to offer 1 coin to the third, the fifth, and so on, because the odds of these pirates are to get zero coins if the proposal doesn't pass. In our case, then, the oldest pirate will keep for him 96 coins, and give one each to the pirates in positions 3,5,7,9.

This solution is a very simple example of mathematical induction; we found out what happens for $$n$$ pirates, using the knowledge that we have of what happens when we have $$n-1$$.

### Kill Bill

> A thousand samurai, numbered 1 to 1000, are standing in a circle. The first one takes his sword and kills the second. Then, the next man in the circle, number 3, kills number 4. The process continues until there is only one samurai standing. What is his number?


