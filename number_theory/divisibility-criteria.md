## Divisibility criteria

A *divisibility criterion* for a number $$n$$ is a rule which quickly allows us to check if a number is divisible by $$n$$. Of course, one can always divide into $$n$$ and verify that that there is no remainder, but that is a very tedious operation.

We are looking for something much quicker, a condition one can almost check in a single glance. Usually these tricks are expressed in terms of the digits in decimal expansion. For example, a number is divisible by 10 if it ends in a 0 (in its decimal expansion).

### Searching for divisibility criteria

> Find a divisibility criterion for 2.


> Find a divisibility criterion for 5.


> Find a divisibility criterion for 4.


> Find a divisibility criterion for 8.


> Find a divisibility criterion for 3.


> Find a divisibility criterion for 9.


> Find a divisibility criterion for 11.


> Find a divisibility criterion for 7.


### All ones

> Find the smallest positive integer $$n$$ such that the decimal expansion of $$99 n$$ contains only ones.

The aim of this problem is to find the smaller number whose digits are only ones, that is multiple of $$99$$. But being multiple of 99 is the same as being contemporarily multiple of 9 and 11. So, let us apply the criteria we found in the previous exercise. For the number

$$\underbrace{11\ldots 11}_{k}$$

to be multiple of 9, we need the sum of the digits to be too. But the sum of the digits is just $$k$$, so we need $$k$$ to be divisible by 9. In order to have our number multiple of 11, we need the alternating sum of digits to be multiple of 11. But the alternating sum of digits is 0 whenever $$k$$ is even, and 1 when $$k$$ it odd, so we just need $$k$$ to be even. 

Wrapping up, we need the smallest $$k$$ that is both multiple of $$9$$ and even, so the answer is just 18. We have in fact
$$\underbrace{11\ldots 11}_{18}=99\cdot 11223344556677889$$

### Missing digits 1

> The number $$62ab427$$ is a multiple of 99. Find the digits $$a$$ and $$b$$.

As in the previous exercise, we want the sum of digits to be multiple of $$9$$, and the alternating sum to be multiple of $$11$$. 

The sum of digits is just $$21+a+b$$, and we want it to be multiple than 9. We know that $$a+b$$ is the sum of two digits, so that it can be only a number between 0 and 18. Hence, the only multiples of 9 that the sum of digits can achieve are 27 and 36, so that we have
$$21+a+b=27\ \ \text{or}\ \ 21+a+b=36$$
that becomes
$$a+b=6\ \ \text{or}\ \ a+b=15.$$

Similarly, the alternating sum is $$13+a-b$$, and we want it to be multiple of 11. The difference $$a-b$$ can only be a number from $$-9$$ to $$9$$, so that the only multiples of 11 achievable from the alternating sum of digits are $$11$$ and $$22$$. We have
$$13+a-b=11\ \ \text{or}\ \ 13+a-b=22$$
that becomes
$$a-b=-2\ \ \text{or}\ \ a-b=9.$$

So, we have possibilities for $$a+b$$ and two for $$a-b$$, that give 4 linear systems in $$a$$ and $$b$$ that we need to solve. But instead of doing this, let us be clever. If $$a-b=9$$, this automatically means $$a=9$$ and $$b=0$$ (because $$a$$ and $$b$$ are digits), but this doesn't fit with any of the two possibilities for $$a+b$$. So, the difference $$a-b$$ has to be $$-2$$. Plugging in $$a=b-2$$ in the two equations for the sum $$a+b$$, we get from the first equation $$b=4$$ (and then $$a=2$$) and from the second $$b=8.5$$ that is impossible. The number is then

$$6224427=99\cdot 62837.$$


### Missing digits 2

> Suppose $$33! = 8ab331761881188649551819440128cd00000$$. Find the digits $$a$$, $$b$$, $$c$$, and $$d$$.

Using formulas from the previous sections, the number of zeroes at the end of $$33!$$ is
$$\left\lfloor\frac{33}{5}\right\rfloor+\left\lfloor\frac{33}{25}\right\rfloor=6+1=7$$
so we immediately get that $$c$$ and $$d$$ have to be zero. 
Then, to find $$a$$ and $$b$$, we can apply the same argument as in the previous exercise, because we know that $$33!$$ is also going to be multiple of 99.
In the exact same way, we get $$a=6$$ and $$b=8$$, so that

$$33!=8683317618811886495518194401280000000.$$

### Sum the digits!

> Let $$S(n)$$ denote the sum of the decimal digits of $$n$$. Consider the following recursive sequence
> $$
a_0 = 2015!, \qquad
a_{n+1} = S(a_n).
$$
> What is the behavior of the sequence for large $$n$$? Can you find its limit? How soon is it achieved?
