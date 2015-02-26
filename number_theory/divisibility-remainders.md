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



### The last digit

> * What is the last digit of $$7^{2015}$$ (in base 10)?
> * What is the last digit of $$7^{7^{2015}}$$ (in base 10)?


### The last digit of Fibonacci numbers

> Consider the sequence of last digits (in base 10) obtained from the Fibonacci sequence. Is it periodic and why?

