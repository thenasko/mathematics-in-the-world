## Divisibility and remainders
### Square plus one

> Can you find a positive integer $$d$$ which divides both $$n^2 + 1$$ and $$(n+1)^2 + 1$$ for some $$n \in \mathbb{Z}$$? How many such $$d$$ are there?

Trying small values of $$n$$, we immediately find that $$d=5$$ works; for instance, choosing $$n=2$$ or $$n=7$$. Then, of course $$d=1$$ works too, because $$1$$ divides all integers.

Let us now prove that $$1$$ and $$5$$ are the only possibilities. Suppose we have a $$d$$ that divides both $$n^2 + 1$$ and $$(n+1)^2 + 1$$; then it divides their difference, in symbols
$$d\mid 2n+1.$$
Now, let's try to combine the relation $$d\mid 2n+1$$ with the ones we had before, in particular we can do
$$d\mid n(2n+1)$$
$$d\mid 2(n^2+1)$$
and taking the difference again we get
$$d\mid n-2.$$
With the same procedure, we have
$$d\mid 2n+1$$
$$d\mid 2(n-2)$$
and taking the difference we get $$d\mid 5$$. Wrapping everything up, we showed that if there exist a $$d$$ that divides both $$n^2 + 1$$ and $$(n+1)^2 + 1$$ for some integer $$n$$, then it *has* to divide $$5$$. But this means that $$d$$ can only be either $$5$$ or $$1$$.



### Integers?

> Why are the fractions
> $$\frac{n(n+1)}{2}
> \qquad\textrm{and}\qquad
> \frac{n(n+1)(2n+1)}{6}$$
> integers (for $$n \in \mathbb{Z}$$)? Try to find an argument which doesn't appeal to the summation identities.

For the first, let us show that $$n(n+1)$$ is always divisible by $$2$$. Let us consider all possibilities for the remainders of $$n$$ and $$n+1$$ modulo 2.

| $$n$$ | $$n+1$$  | $$n(n+1)$$ | modulo 2 |
|-------|:--------:| ------:|
| 0     | 1| 0 |
| 1 | 0 | 0 |

This shows that whatever is the remainder of $$n$$ modulo 2, the remainder of $$n(n+1)$$ is always 0, so the fraction $$\frac{n(n+1)}{2}$$ is an integer. In other words, among two consecutive integers one has to be even, so their product will be even too.

For the second fraction, we can just do the table mod 6 as we did before. Notice that the third column can just be obtained by summing the first two, and that when we are modulo 6 the product $$2\cdot 3$$ is $$0$$.

| $$n$$ | $$n+1$$  | $$2n+1$$ | $$n(n+1)(2n+1)$$ |  modulo 6 |
|-------|:--------:| :------:|------:|
| 0     | 1| 1 | 0|
| 1 | 2 | 3 | 0|
| 2 | 3 | 5 | 0|
| 3 | 4 | 1 | 0|
| 4 | 5 | 3 | 0|
| 5 | 0 | 5 | 0|




### The last digit

> * What is the last digit of $$7^{2015}$$ (in base 10)?
> * What is the last digit of $$7^{7^{2015}}$$ (in base 10)?

Let us look at the last digit powers of 7 have. Notice that to obtain the last digit of $$7^n$$, we don't need to know the entire number $$7^{n-1}$$, but only its last digit!

| Power of 7 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------------|:--------:|
| Last digit | 1 | 7 | 9 | 3 | 1 | 7 | 9 | 3 | 1 | 7 |

It is clear that we have a period of order 4. In particular, we have the following table (that can be proved by induction, for example).

$$7^n\equiv\begin{cases}
1\ (\textrm{mod}\ 10)\ \text{if }n\equiv 0\ (\textrm{mod}\ 4) \\
7\ (\textrm{mod}\ 10)\ \text{if }n\equiv 1\ (\textrm{mod}\ 4) \\
9\ (\textrm{mod}\ 10)\ \text{if }n\equiv 2\ (\textrm{mod}\ 4) \\
3\ (\textrm{mod}\ 10)\ \text{if }n\equiv 3\ (\textrm{mod}\ 4) \\
\end{cases}$$

So, to go back to to the first question in our problem, notice that the remainder of $$2015$$ when divided by $$4$$ is $$3$$. Then, the last digit of $$7^{2015}$$ is $$3$$. Notice that once we notice that $$7^4\equiv 1\ (\textrm{mod}\ 10)$$, we can just say

$$7^{2015}\equiv (7^4)^{503}\cdot 7^3\equiv 7^3\equiv 3\ (\textrm{mod}\ 10). $$

To solve the second question, we need to find the remainder of the exponent of $$7^{7^{2015}}$$ - namely, $$7^{2015}$$ - when divided by 4. But we have

$$7^{2015}\equiv (-1)^{2015}\equiv -1\ (\textrm{mod}\ 4) $$

so that the last digit of $$7^{7^{2015}}$$ is again $$3$$.

### The last digit of Fibonacci numbers

> Consider the sequence of last digits (in base 10) obtained from the Fibonacci sequence. Is it periodic and why?

Consider the last digit of the first Fibonacci numbers.
