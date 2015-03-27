## Combinatorial probability

We all know from the simplest Venn diagram that given two sets, we can compute the size of their union as
$$
|A \cup B| =
|A| + |B| - |A \cap B|.
$$
For three sets $$A$$, $$B$$, and $$C$$, the size of their union is
$$
|A \cup B \cup C| =
|A| + |B| + |C|
- |A \cap B| - |A \cap C| - |B \cap C|
+ |A \cap B \cap C|.
$$
More generally, given $$n$$ sets $$A_1, \dots, A_n$$, we have
$$
\begin{align}
| A_1 \cup \cdots \cup A_n |
&= \sum_{I \subset \{1, \dots, n\}} (-1)^{|I| + 1} \left| \bigcap_{i \in I} A_i \right| \\
&= \sum_{k = 1}^n \left( \sum_{1 \leq i_1 < \cdots < i_k \leq n} |A_{i_1} \cap \cdots \cap A_{i_k}| \right).
\end{align}
$$
This is called the [*inclusion-exclusion principle*](http://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle. It also applicable to the probability of the union of events $$A_1, \dots, A_n \subset \Omega$$ in which case
$$
\begin{align}
\mathbb{P}( A_1 \cup \cdots \cup A_n )
&= \sum_{I \subset \{1, \dots, n\}} (-1)^{|I| + 1} \; \mathbb{P}\left( \bigcap_{i \in I} A_i \right) \\
&= \sum_{k = 1}^n \left( \sum_{1 \leq i_1 < \cdots < i_k \leq n} \mathbb{P}( A_{i_1} \cap \cdots \cap A_{i_k} ) \right).  
\end{align}
$$

Given sets $$A \subset \Omega$$, let us denote its *complement* by $$\overline{A} = A^c = \Omega \setminus A$$. Given two sets $$A, B \subset \Omega$$, we can compute the union and intersection of their complements as follows.
$$
\begin{align}
  \overline{A \cap B} &= \overline{A} \cup \overline{B} \\
  \overline{A \cup B} &= \overline{A} \cap \overline{B} \\
\end{align}
$$
More generally, given $$n$$ sets $$A_1, \dots, A_n \subset \Omega$$, we have
$$
\begin{align}
  \overline{A_1 \cap \cdots \cap A_n} &= \overline{A_1} \cup \cdots \cup \overline{A_n}, \\
  \overline{A_1 \cup \cdots \cup A_n} &= \overline{A_1} \cap \cdots \cap \overline{A_n}.
\end{align}
$$
These equalities are referred to as [*De Morgan's laws*](http://en.wikipedia.org/wiki/De_Morgan%27s_laws).


### Finding a coprime

> If you choose a number between 1 and 100, what is the probability it is not coprime to 12? What about getting a number that is not coprime to 30?


### Catching the curious counterfeiter

> The minter of a kingdom produces boxes with 100 coins in each. He replaces one coin by a false one in each box. The king received intelligence about the counterfeit operation, and draws one coin from each of 100 boxes. What is the probability that the minter's side business will remain undetected? What is the answer if both 100s are replaced by $$n$$?


### Catching the greedy counterfeiter

> Suppose the minter has expanded his operation and each box of $$n$$ he produced contains $$m$$ doctored coins. What is the probability that the king will find exactly $$r$$ false coins if he draws one from each of $$n$$ boxes?


### Identical birthdays

> How many people should be in the same room so that the probability of two having the same birthday is at least 1/2? How many people should be in the room so the probability of at least one of them having the same birthday as you is 1/2?
