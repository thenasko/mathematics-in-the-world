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
| **Prime?**    | Y | Y | N | Y | N | Y | N | N | N | Y  |

As we can see, there are many solutions. In fact, there is an infinite number of them.
This is indeed a way more complicated problem than the previous one, and no explicit solution is known. One funny feature of this kind of problems, is that if we *slightly* change one problem (in this case, we just changed a negative sign to a positive!) the problem can become arbitrarily complicated, or even impossible to solve. 

Throughout history, mathematicians studied this problem quite a lot. For instance, there is a reason behind the fact that the product of the two numbers $$1^2+1$$ and $$2^2+1$$ is the third one, $$3^2+1$$. This reason is called [Fibonacci identity](http://en.wikipedia.org/wiki/Brahmagupta–Fibonacci_identity), that is

$$(a^2 + b^2)(c^2 + d^2)= (ad+bc)^2+(ac-bd)^2 $$

This formula allows the product of two numbers that are sum of two squares to be expressed again as the sum of two squares. In our case, we just applied with $$a=b=d=1$$ and $$c=2$$.

Furthermore, there is also a reason why all prime factors of the numbers $$n^2+1$$ (except for 2) give remainder 1 when divided by 4. Looking more closely at the table, in fact, the odd prime factors that we get are $5,17,13,37,41,101$, all of them (using the notation introduced in the exercise **Dividing the difference**)having remainder 1 when divided by 4. 





