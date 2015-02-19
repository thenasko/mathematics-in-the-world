## Prime factorization

### Trailing zeroes

> How many zeroes does $$100!$$ end in?

The number of zeroes at the end of a number $$n$$ is given by the highest power of 10 that divides the number. Moreover, considering the highest power of 2 and the highest power of 5 dividing $$n$$, this number is going to be the smallest of the two. For example, the number $$2^4\cdot 3^2 \cdot 5^7$$ ends with 4 zeroes (in fact, this number is $$11250000$$).

### A fixed number of divisors

> What is the smallest natural number which has exactly 77 divisors?

The number of divisors of a natural number $$n=\prod p_i^{e_i}$$ is given by the product $$\prod(e_i+1)$$. This is because every divisor will be of the form $$d=\prod p_i^{f_i}$$ where every $$f_i$$ satisfies $$0\leq f_i\leq e_i$$. So, for every $$f_i$$ we have $$e_i+1$$ choices, and the choices are independent, and hence the formula follows.

Now, we want to find the smallest number $$n=\prod p_i^{e_i}$$ such that $$\prod(e_i+1)=77$$. Let us now analyze all possible decompositions of $$77$$. The only two possible options are $$7\cdot 11$$ and $$77$$ alone itself. Notice that we do not consider ones in the decomposition because we would have a factor $$e_i+1$$ equal to $$1$$, that means $$e_i=0$$. 

In the first case, we get

$$\begin{cases}e_1+1=11 \\ e_2+1=7 \end{cases}\ \ \Rightarrow \ \ \  \begin{cases}e_1=10 \\ e_2=6 \end{cases}$$

So, our number will be of the form $$n=p_1^{6}p_2^{11}$$ for $$p_1,p_2$$ prime numbers. How can we choose them so that $$n$$ is as small as possible? Of course, we need to pick $$p_1$$ and $$p_2$$ as small as possible, that means, $$2$$ and $$3$$. We are left with two possibilities now, $$n=2^{6}3^{11}$$ and $$n=2^{11}3^{6}$$, and clearly the second is smaller.

In the second case, the number is of the form $$n=p_1^{76}$$. To make it as small as possible, we need to pick $$p_1=2$$, so that $$n=2^{76}$$.

### The locker game

> The students of a local high school enjoy the following extra-curricular activity. After the end of the day, all 100 students go in front of their closed lockers, numbered 1 to 100. The headmaster then proceeds to blow a whistle 100 times. At the first sound, all students open their lockers. At the second, the students standing by even lockers close them. The game continues in a similar manner -- at the $$n$$-th step students in front of lockers divisible by $$n$$ toggle them.
>
> Which lockers are open at the end of the game?

