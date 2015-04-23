## Dynamic programming

### Maximal contiguous sum

> Given a list of numbers
> $$
a_0, \dots, a_n,
$$
> we define a *contiguous sum* as $$a_i + \cdots + a_j$$ for some $$0 \leq i \leq j \leq n$$. Design an algorithm which computes the largest contiguous sum.

### Longest increasing subsequence

> Given a list of numbers
> $$
a_1, \dots, a_n,
$$
> design an algorithm which finds the longest sequence
> $$
i_1, \dots, i_k
$$
> such that $$i_j < i_{j+1}$$ and $$a_{i_j} \leq a_{i_{j+1}}$$ for all $$1 \leq j \leq k-1$$.


### Longest palindrome}

> A *palindrome* is a string which reads the same in both directions. For example, "abba" is a palindrome, but "abc" is not. Given a string, how would you find the longest (contiguous) palindrome it contains?


### Cheapest triangulation}

> Consider a convex polygon $$P$$ with $$n \geq 4$$ vertices $$v_1, \dots, v_n$$. A \emph{triangulation} of $$P$$ is a collection of $$n-3$$ diagonals such that no two intersect in the interior of $$P$$. Such an arrangement always breaks $$P$$ down into $$n-2$$ triangles.
> 
> Suppose the cost of a triangulation is defined as the sum of the lengths of all diagonals. How would you find the cheapest triangulation of $$P$$?


### Matrix multiplication}

> Given two matrices $$A$$ and $$B$$ of size $$a \times b$$ and $$b \times c$$ respectively, it takes $$O(a b c)$$ operations to compute the product $$A \cdot B$$. Suppose we have one more matrix $$C$$ of size $$c \times d$$. We can compute the product $$A \cdot B \cdot C$$ in one of two ways:
> $$
(A \cdot B) \cdot D, \qquad
A \cdot (B \cdot C).
$$
> Which one is better? How would you approach the problem if you had to compute the product of $$n$$ matrices?
