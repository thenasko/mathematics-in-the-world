## Prime numbers

### One less than a perfect square

> Find a prime number which is one less than a perfect square. How many can you find?

In this problems, it is very important to turn the statement into an equation. In our case, we are looking for primes
$$
p=n^2-1,
$$
where $$n$$ is an integer. Factoring the right hand side, we obtain
$$
p=(n+1)(n-1).
$$

We are now ready to use the fact that $$p$$ is a prime number. Whenever a prime number is a product of two integers, then one of the two is 1. In our case, this means that either $$n+1$$ or $$n-1$$ is 1! Hence, $$n$$ is either 0 or 2. When $$n = 0$$, the equation above implies $$p = -1$$ which is not a prime. On the other hand, when $$n=2$$, we get $$p=3$$. This is indeed a prime and the only solution to our problem.


### One more than a perfect square

> Find a prime number which is one more than a perfect square. How many can you find?

In the same way as the previous exercise, we get an equation
$$
p=n^2+1.
$$
Sadly, we cannot factorize the right hand side. To try and understand what happens, let us test some values of $$n$$ and see whether we find a prime number.

| $$n$$      | 1  | 2 | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10  |
|------------|----|---|----|----|----|----|----|----|----|-----|
| $$n^2+1$$  | 2  | 5 | 10 | 17 | 26 | 37 | 50 | 65 | 82 | 101 |
| **Prime?** | Y  | Y | N  | Y  | N  | Y  | N  | N  | N  | Y   |

As we can see, there are many solutions, and one can only guess there is an infinite number of them. This question, also known as [Landau's forth problem](http://en.wikipedia.org/wiki/Landau%27s_problems), remains open.

One fascinating feature of this type of problems is that if we *slightly* change the statement (in this case, we just altered a minus to a plus) the problem can become arbitrarily complicated, or even impossible to solve.

**REMARK-MATH-HISTORY:** Throughout history, mathematicians studied this problem quite a lot. For instance, there is a reason why the product of the numbers $$1^2+1$$ and $$2^2+1$$ is $$3^2+1$$. The [Fibonacci identity](http://en.wikipedia.org/wiki/Brahmagupta–Fibonacci_identity), probably already known to [Diophantus of Alexandria](http://en.wikipedia.org/wiki/Diophantus) in the $$3^{rd}$$ century AC, states that
$$
(a^2 + b^2)(c^2 + d^2)= (ad+bc)^2+(ac-bd)^2.
$$
This formula demonstrates that the product of two numbers that are sums of two squares is again a sum of two squares. The case we mentioned is $$a=b=d=1$$ and $$c=2$$. Try a few more cases!

Furthermore, there is also a reason why all prime factors of the numbers $$n^2+1$$ (except for 2) give remainder 1 when divided by 4. Looking more closely at the table, the odd prime factors that we get are 5, 17, 13, 37, 41, 101. All of them are congruent to 1 modulo 4 (for an explanation of congruences, see the exercise **Dividing the difference**). This observation rests on the [Quadratic reciprocity law](http://en.wikipedia.org/wiki/Quadratic_reciprocity#.E2.88.921_and_the_first_supplement), a very deep result proved by one of the greatest mathematicians of all time, [Carl Friedrich Gauss](http://en.wikipedia.org/wiki/Carl_Friedrich_Gauss), in 1798. 


### Euclid's Theorem

> How do we know that there are infinitely many primes?

In this exercise, we will use a proof by *contradiction*: we will suppose the claim is false, and deduce a contradiction from there.

Let us suppose the statement is false - that means, there are only finitely many primes. We can then consider all of them, and call them $$p_1,p_2,\ldots,p_n$$. Consider now the number
$$N=p_1\cdot p_2\cdots p_n+1.$$
We now that this number is greater than $$1$$, and hence it has to have a factorization as a product of primes. So, there has to be a prime $$p$$ that divides it. Remember that $$p$$ needs to be in the list of primes we gave before, because we are supposing they are *all* the prime numbers. So, $$p$$ divides $$N$$, but it divides also $$N-1$$, because $$N-1$$ is the product of all primes. So $$p$$ divides both $$N$$ and $$N-1$$, and hence it divides their difference $$1$$. But this is impossible, because no prime is a divisor than $$1$$, and here is the contradiction. This proves that the initial assertion is indeed true, the primes are infinitely many.
