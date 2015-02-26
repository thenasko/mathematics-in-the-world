## Prime factorization

### Trailing zeroes

> How many zeroes does $$100!$$ end in?

The number of zeroes at the end of a number $$n$$ is given by the highest power of 10 that divides the number. Moreover, considering the highest power of 2 and the highest power of 5 dividing $$n$$, this number is going to be the smallest of the two. For example, the number $$2^4\cdot 3^2 \cdot 5^7$$ ends with 4 zeroes (in fact, this number is $$11250000$$ ).

So, we need to find how many times the primes $$2$$ and $$5$$ appear in the decomposition of $$100!$$. We are going to use the following result, that we are going to prove later.

> The highest power of a prime $$p$$ that divides a factorial $$n!$$ is given by the
$$\sum_{i=1}^\infty\left\lfloor\frac{n}{p^i}\right\rfloor.$$

Using this result, the highest power of $$2$$ and $$5$$ dividing $$100!$$ are given by
$$\left\lfloor\frac{100}{2}\right\rfloor+\left\lfloor\frac{100}{2^2}\right\rfloor+\left\lfloor\frac{100}{2^3}\right\rfloor+\left\lfloor\frac{100}{2^4}\right\rfloor+\left\lfloor\frac{100}{2^5}\right\rfloor+\left\lfloor\frac{100}{2^6}\right\rfloor=50+25+12+6+3+1=97$$
$$\left\lfloor\frac{100}{5}\right\rfloor+\left\lfloor\frac{100}{5^2}\right\rfloor=20+4=24.$$
So, the number of trailing zeroes is 24. 

Let us now prove the result, for a prime $$p$$ and a factorial $$n!$$. Let us list the multiples of $$p$$ that are less than $$n$$, the ones that bring a contribution:




### A fixed number of divisors

> What is the smallest natural number which has exactly 77 divisors?

The number of divisors of a natural number $$n=\prod p_i^{e_i}$$ is given by the product $$\prod(e_i+1)$$. This is because every divisor will be of the form $$d=\prod p_i^{f_i}$$ where every $$f_i$$ satisfies $$0\leq f_i\leq e_i$$. So, for every $$f_i$$ we have $$e_i+1$$ choices, and the choices are independent, and hence the formula follows.

Now, we want to find the smallest number $$n=\prod p_i^{e_i}$$ such that $$\prod(e_i+1)=77$$. Let us now analyze all possible decompositions of $$77$$. The only two possible options are $$7\cdot 11$$ and $$77$$ alone itself. Notice that we do not consider ones in the decomposition because we would have a factor $$e_i+1$$ equal to $$1$$, that means $$e_i=0$$. 

In the first case, we get

$$\begin{cases}e_1+1=11 \\ e_2+1=7 \end{cases}\ \ \Rightarrow \ \ \  \begin{cases}e_1=10 \\ e_2=6 \end{cases}$$

So, our number will be of the form $$n=p_1^{6}p_2^{11}$$ for $$p_1,p_2$$ prime numbers. How can we choose them so that $$n$$ is as small as possible? Of course, we need to pick $$p_1$$ and $$p_2$$ as small as possible, that means, $$2$$ and $$3$$. We are left with two possibilities now, $$n=2^{6}3^{11}$$ and $$n=2^{11}3^{6}$$, and clearly the second is smaller.

In the second case, the number is of the form $$n=p_1^{76}$$. To make it as small as possible, we need to pick $$p_1=2$$, so that $$n=2^{76}$$. This number is *way* bigger than the numbers we found before (in fact, it has more than three times the *digits*).

Concluding, having exhausted all possibilities, the smallest number with 77 divisors is $$n=2^{11}3^{6}$$.

### The locker game

> The students of a local high school enjoy the following extra-curricular activity. After the end of the day, all 100 students go in front of their closed lockers, numbered 1 to 100. The headmaster then proceeds to blow a whistle 100 times. At the first sound, all students open their lockers. At the second, the students standing by even lockers close them. The game continues in a similar manner -- at the $$n$$-th step students in front of lockers divisible by $$n$$ toggle them.
>
> Which lockers are open at the end of the game?

Instead of focusing in what happens at a specific blow, let us choose a different strategy: we pick a lock, let's say the $n$-th, and let's see how many times it is toggled throughout the 100 blows. The lock will be open in the end if is has been toggled an odd number of times. Now, the lock is toggled at the $i$-th blow whenever $i$ is a divisor or $n$, so it is toggled once for every divisor of $n$. So, the $n$-th lock will be open in the end exactly if $n$ has an odd numbers of divisors. 

We can now focus on the question: what are the numbers with an odd number of divisors? Looking at the formula from the previous exercise, the number of divisors of $$n=\prod p_i^{e_i}$$ is given by the product $$\prod(e_i+1)$$. This product can be odd only if every factor is odd too, that in turns gives us that every $$e_i$$ has to be even. But this means that the number has to be a square! Hence, the locks that are going to be open at the end are just the squares, namely

$$1,4,9,16,25,36,49,64,81,100.$$









