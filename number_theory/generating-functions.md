## Generating functions

### The Fibonacci numbers and power series

> Define the function $$f(x)$$ in terms of the infinite power series
> $$
> f(x) = \sum_{n = 0}^\infty F_n x^n.
> $$
> What does the recursive relation satisfied by $$F_n$$ say about $$f(x)$$? Does this give an alternative derivation of the closed formula for $$F_n$$?

The solution of this problem is a little longer, so it is important to start with a plan and understand that well. The premise behind *generating functions*, of which $$f(x)$$ is an example, is that a recursive relation can be translated to an equation satisfied by $$f$$. We can find an expression for $$f(x)$$, and in turn that will give a closed formula for the original sequence.

Since the Fibonacci relation reads $$F_n = F_{n-1} + F_{n-2}$$, and the coefficient of $$x^n$$ in $$f(x)$$ is $$F_n$$, we need to find a way to place $$F_{n-1}$$ and $$F_{n-1}$$ as coefficients in front of $$x^n$$. Starting from $$f(x)$$ this can be easily achieved if we multiply it by $$x$$ and $$x^2$$:
$$
\begin{align}
x f(x)
&= x\phantom{^2} \sum_{n \geq 0} F_n x^n
= \sum_{n \geq 0} F_n x^{n+1}
= \sum_{n \geq 1} F_{n-1} x^n, \\
x^2 f(x)
&= x^2 \sum_{n \geq 0} F_n x^n
= \sum_{n \geq 0} F_n x^{n+2}
= \sum_{n \geq 2} F_{n-2} x^n.
\end{align}
$$
The sum of these two series resembles $$f(x)$$ closely.
$$
\begin{align}
f(x)
&= F_0 + F_1 x + F_2 x^2 + F_3 x^3 + F_4 x^4 + \cdots, \\
x f(x)
&= \phantom{F_0 +} F_0 x + F_1 x^2 + F_2 x^3 + F_3 x^4 + \cdots, \\
x^2 f(x)
&= \phantom{F_0 + F_1 x +} F_0 x^2 + F_1 x^3 + F_2 x^4 + \cdots.
\end{align}
$$
If we subtract the second and third line from the first, the coefficients of $$x^n$$ for $$n \geq 2$$ are zero:
$$
(1 - x - x^2) f(x)
= F_0 + (F_1 - F_0) x + \sum_{n \geq 2} (F_n - F_{n-1} - F_{n-2}) x^n
= F_0 + (F_1 - F_0) x
= x.
$$
This completes the first part of out task, that is, finding a formula for the function $$f(x)$$:
$$
f(x) = \frac{x}{1 - x - x^2}.
$$

We are now left to translate our knowledge about $$f(x)$$ to a formula for the Fibonacci sequence $$F_n$$. We see that $$f(x)$$ is a rational function (a ratio of two polynomials), but the denominator has degree 2. Such quotients are much harder to understand than ones involving a linear denominator, so out first task is present $$f(x)$$ in a more suitable form. The issue we described is a very common problem when we integrate rational functions, and it is typically resolved using the [partial fraction decomposition](http://en.wikipedia.org/wiki/Partial_fraction_decomposition).

First, we find that the roots of the denominator are $$-\psi = 1/\phi$$ and $$-\phi = 1/\psi$$, where
$$
\phi = \frac{1 + \sqrt{5}}{2}, \qquad
\psi = \frac{1 - \sqrt{5}}{2}.
$$
We can then write
$$
\begin{align}
f(x)
&= \frac{x}{1 - x - x^2} \\
&= - \frac{x}{x^2 + x - 1} \\
&= - \frac{x}{(x - 1/\phi)(x - 1/\psi)} \\
&= - \frac{\phi\psi x}{(\phi x - 1)(\psi x - 1)} \\
&= \frac{x}{(1 - \phi x)(1 - \psi x)}.
\end{align}
$$
A partial fraction decomposition for $$f(x)$$ is an expression
$$
f(x) =
\frac{A}{1 - \phi x} + \frac{B}{1 - \psi x}
$$
for some constants $$A$$ and $$B$$. Bringing this expression to a common denominator and equating the numerator to $$x$$, we find that
$$
A
= -B
= \frac{1}{\phi - \psi}
= \frac{1}{\sqrt{5}}.
$$
In conclusion, we found that
$$
f(x) =
\frac{1}{\sqrt{5}} \left( \frac{1}{1 - \phi x} - \frac{1}{1 - \psi x} \right).
$$

To find a formula for $$F_n$$, we recall the geometric series formula
$$
1 + c + c^2 + c^3 + \cdots
= \sum_{n \geq 0} c^n
= \frac{1}{1 - c},
$$
where $$|c| < 1$$. Using $$c = \phi x$$ and $$c = \psi x$$ above, we compute
$$
\begin{align}
f(x)
&= \frac{1}{\sqrt{5}} \left( \sum_{n \geq 0} \phi^n x^n - \sum_{n \geq 0} \psi^n x^n \right) \\
&= \sum_{n \geq 0} \frac{\phi^n - \psi^n}{\sqrt{5}} x^n.
\end{align}
$$
In conclusion, we showed that
$$
F_n =
\frac{\phi^n - \psi^n}{\phi - \psi} =
\frac{\phi^n - \psi^n}{\sqrt{5}}.
$$

**REMARK:**
The power series we presented for $$f(x)$$ do not converge for all values of $$x$$. Fortunately, they are valid in the intersection of $$|\phi x| < 1$$ and $$|\psi x| < 1$$ which is nonempty. Alternatively, we can explain this phenomenon by saying that all computations were performed using [formal power series](http://en.wikipedia.org/wiki/Formal_power_series) and there is no need to worry about convergence at all.


### Using generating functions

> Use generating functions to find a closed formula for each of the following sequences:
> * $$a_0 = 0,\; a_{n+1} = 2 a_n + 1$$,
> * $$b_0 = 0,\; b_{n+1} = 2 b_n + n$$.


