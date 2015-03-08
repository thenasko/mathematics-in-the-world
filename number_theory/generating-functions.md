## Generating functions

### The Fibonacci numbers and power series

> Define the function $$f(x)$$ in terms of the infinite power series
> $$
> f(x) = \sum_{n = 0}^\infty F_n x^n.
> $$
> What does the recursive relation satisfied by $$F_n$$ say about $$f(x)$$? Does this give an alternative derivation of the closed formula for $$F_n$$?

The solution of this problem is a little longer, so it is important to start with a plan and understand that well. The premise behind *generating functions*, of which $$f(x)$$ is an example, is that a recursive relation can be translated to an equation satisfied by $$f$$. We can find an expression for $$f(x)$$, and in turn that will give a closed formula for the original sequence.

Since the Fibonacci relation reads $$F_n = F_{n-1} + F_{n-2}$$, and the coefficient of $$x^n$$ in $$f(x)$$ is $$F_n$$, we need to find a way to find a way to get $$F_{n-1}$$ and $$F_{n-1}$$ as coefficients in front of $$x^n$$. Starting from $$f(x)$$ this can be easily achieved if we multiply it by $$x$$ and $$x^2$$:
$$
\begin{align}
x f(x)
&= x \sum_{n \geq 0} F_n x^n
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
&= F_0 + (F_1 - F_0) x + \sum_{n \geq 2} (F_n - F_{n-1} - F_{n-2}) x^n
= F_0 + (F_1 - F_0) x
= x.
$$


### Using generating functions

> Use generating functions to find a closed formula for each of the following sequences:
> * $$a_0 = 0,\; a_{n+1} = 2 a_n + 1$$,
> * $$b_0 = 0,\; b_{n+1} = 2 b_n + n$$.


