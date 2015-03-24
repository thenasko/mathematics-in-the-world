## Conditional probability

Given two events $$A, B \subset \Omega$$, the *conditional probability of $$A$$ given $$B$$* is defined as
$$
\mathbb{P}(A \,|\, B) =
\frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}.
$$
Given a random variable $$X$$, it is also possible to define its *conditional expectation* as
$$
\mathbb{E}(X \,|\, B) = \sum_k k \cdot \mathbb{P}(X = k \,|\, B).
$$

(a) **Law of total probability.**

Suppose $$E_1, \dots, E_n \subset \Omega$$ are mutually exclusive events such that $$\bigcup_{i = 1}^n E_i = \Omega$$. Given any event $$A \subset \Omega$$, we can compute its probability by
$$
\mathbb{P}(A) = \sum_{i = 1}^n \mathbb{P}(A \,|\, E_i) \cdot \mathbb{P}(E_i).
$$
Similarly, given a random variable $$X$$, we can express its expectation in terms of its conditional expectations:
$$
\mathbb{E}(X) = \sum_{i = 1}^n \mathbb{E}(X \,|\, E_i) \cdot \mathbb{P}(E_i).
$$
  
(b) **Multiplication rule of conditional probability.**

Given events $$E_1, \dots, E_n \subset \Omega$$, the probability of their intersection can be computed using conditional probability as
$$
\mathbb{P}(E_1 \cap \cdots \cap E_n) =
\mathbb{P}(E_1) \; \mathbb{P}(E_2 \,|\, E_1) \; \mathbb{P}(E_3 \,|\, E_1 \cap E_2) \;\cdots\; \mathbb{P}(E_n \,|\, E_1 \cap \cdots \cap E_{n-1}).
$$
  
(c) **Bayes formula.**

Given two events $$A, B \subset \Omega$$, the ratio of the conditional probabilities both ways can be expressed as
$$
\frac{\mathbb{P}(A \,|\, B)}{\mathbb{P}(B \,|\, A)} =
\frac{\mathbb{P}(A)}{\mathbb{P}(B)}.
$$


### Two sons

> You go to dinner with your guy friend. During the conversation, he mentioned he is one of two children. What is the probability that they are both boys? Later on, he clarified that he is the older sibling. What is the probability now?


### Doctored coin

> You are given 100 coins: one has heads on both of its sides, and the other 99 are normal. All coins are fair in the sense that both sides come up with equal probability. If you choose a random coin from the pile, toss is 10 times and each time it comes up heads, what is the probability you found the doctored coin?


### Increasing order

> You throw a fair dice three times. What is the chance the results will come up in strictly increasing order?


### Two heads

> You toss a fair coin until two consecutive throws come up heads. What is the average number of tosses before the game terminates?

