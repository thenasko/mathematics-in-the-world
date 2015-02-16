## Prime numbers

### One less than a perfect square

> Find a prime number which is one less than a perfect square. How many can you find?

In this problems, it is very important to make the statement into an equation. In our case, it becomes

$$p=n^2-1,$$

where $$n$$ is an integer and $$p$$ is a prime number. Next step, is an algebraic manipulation of the equation, and we get

$$p=(n+1)(n-1).$$

We can now use the information that we have, that $$p$$ is a prime number. The property that we are going to use is that whenever a prime number is a product of two integers, then one of the two is 1. In our case, this means that either $$n+1$$ or $$n-1$$ is 1! Hence, that $$n$$ is either 0 or 2. In case $$n$$ is 0, looking again at the equation, then $$p$$ would be -1, that is not a prime number. In the other case, when $$n=2$$, we get $$p=3$$, that is indeed a prime number, and is the only solution to our problem.

### One more than a perfect square

> Find a prime number which is one more than a perfect square. How many can you find?

In the same way as the previous exercise, we get the equation

$$p=n^2-1$$

where sadly we cannot perform any algebraic manipulation. To try to understand that happens, let us just try some values of $$n$$ and see whether we find a prime number.  

| $$n$$ | 1  | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------------|----|---|---|---|---|---|---|---|---|----|
| $$n^2+1$$    | 2 | 5 | 10 | 17 | 26 | 37 | 50 | 65 | 82 | 101  |
|------------|----|---|---|---|---|---|---|---|---|----|
| **Prime?**    | Y | Y | N | Y | N | Y | N | N | N | Y  |

This is indeed a way more complicated problem than the previous one, and no solution is known. One funny feature of this kind of problems, is that if we *slightly* change one problem (in this case, we just changed a negative sign to a positive!) the problem can become arbitrarily complicated. In this 





