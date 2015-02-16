## The Pigeonhole principle

The Pigeonhole principle states that if there are $$n+1$$ pigeons, and all of them sits in one of $$n$$ holes, then there has to be a hole that contains *at least* 2 pigeons. More generally, if there are $$mn+1$$ pigeons in $$n$$ holes, there must be a hole that contains a
t least $$m+1$$ pigeons.

Boxes are another analogy used to describe this principle. If we have $$n + 1$$ objects (socks, gloves, balls, etc.) placed in $$n$$ boxes, then at least one box contains two.

This argument was popularized by [Peter Gustav Lejeune Dirichlet](http://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet) in 1834. It is also common to refer to the idea as Dirichlet's principle or the Dirichlet principle.

(TODO: Tell the story about the inhabitants of Paris.)


### Dividing the difference

> Given $$n + 1$$ integers, there exists a pair $$a, b$$ such that $$n$$ divides $$a-b$$.

The most crucial step in applying the Dirichlet principle is identifying what plays the role of the pigeons and holes. In this problem, the pigeons are clearly the $$n+1$$ integers. To get the argument through, we need to pick $$n$$ holes. Let us choose these to be the numberts between $$0$$ and $$n-1$$ inclusive, that is, the possible *remainders* when dividing an integer by $$n$$. (Note that the remainder of $$-1$$ is $$n-1$$.) Under this scheme, each of the possible $$n+1$$ integers we started with will be associated with its remainder. Ditichlet's principle implies there are at least two integers with the samme remainder, and hence their difference must be divisible by $$n$$.

The idea of using the remainders is a very powerful tool in mathematics. Let us introduce then some notation. The remainder of a number when divided by $$n$$ will be called its *congruence class modulo* $$n$$. Whenever two numbers $$a$$ and $$b$$ have the same congruence class modulo $$n$$, we will say they are *coungruent* modulo $$n$$ and write write $$a \equiv b \pmod{n}$$.


### Summing to 10

> For every 6-element subset $$S$$ of $$\{ 1, \dots, 9 \}$$, there exists a pair of distinct integers $$a, b \in S$$ such that $$a + b = 10$$.

Let us choose categories in a way that can help us with this problem. The idea is to group together elements which sum up to 10. The first one will be $$\{1,9\}$$, the second $$\{2,8\}$$, then $$\{3,7\}$$, $$\{4,6\}$$, and at last the element 5 alone, $$\{5\}$$.

We now have 6 integers in 5 boxes, so there is at least one box that contains two of them. This box cannot be $$\{5\}$$ since it the set has only one element.  Then the box containing two has to be one of the others, which proves that there are two integers whose sum is 10.


### We have the same number of friends!

> Is it possible that at a party all guests have different numbers of friends attending?

**SOLUTION ONE:**
Let us say the number of people attending the party is $$n$$. The possibilities for the number of friends that people can have at the party vary from 0 (in case somebody does not know anybody else) to $$n-1$$ (for someone knowing everybody else). This gives us $$n$$ possibilities. On the other hand, we also have $$n$$ people, so we *cannot* conclude that there are two people with the same number of acquaintances.

We need to also analyze the possibility that there is exactly one person knowing nobody else, one person knowing exactly one other, one person knowing two, and so on until exactly one person that knows anybody else. But this is not possible. If there is a person A not knowing anybody, then there cannot be a person B that knows anybody else, because B cannot know A!

Rephrasing this, we can use a similar strategy to the previous provlem and "group" the possibilities $$0$$ and $$n-1$$ in one box. We know that at most one possibilitiy in this box will be achieved, so we are in the situation of $$n-1$$ categories with $$n$$ people associated with them. It follows that there are two people having the same number of friends.

**SOLUTION TWO:**
We will present an inductive argument which makes the use of of Dirichlet's principle a little more transparent. Suppose we know that for any group of $$n-1$$ people there are two that have the same number of friends (this is called the *inductive hypothesis*).

Consider a party of $$n$$ people. If there is a person $$A_0$$ knowing 0 people, we can consider the remaining $$n-1$$ people. You can say they are "disconnected" from $$A_0$$, so we restrict the problem to this smaller group of people. But we already know that two of them must have the same number of friends by the inductive hypothesis.

On the other hand, consider the opposite situation in which everyone has at least one friend. Then we can apply the Dirichlet principle, because we have $$n$$ people, and $$n-1$$ possibilities for the number of friends they have (the numbers from 1 to $$n-1$$).

To conclude the proof by induction, we need to do what is called "proving the base case". Suppose that we have two people (the simplest that this problem can be, because with one person the problem does not make sense), that let us prove our statement. The only two possibilities here are that they know each other, or that they don't. In both cases, they have the same number of friends, so the claim follows.


### The Friendship Theorem

> Given a group of six people, show that there always exist three such that either
> * all know each other, or
> * none of them are acquaintances.

Even though it sounds simple, this is a very tricky problem.

Start by picking one of the six people, and call her A. Let's analyze her relations with the other 5. To apply Dirichlet's principle, we will use the the two possible relation types (acquantance or not) as categories. It follows that there are at least three people (call them B, C, and D) that have the same relation with A.

First, let us say that they all know A. In this case, either two of them know each other (and hence together with A they form a triple of people that all know each other) or there is no couple of them that know each other (and in such case B, C, D form of a triple that has no acquaintances). This concludes the first case.

The case in which B, C and D do not know A is exactly the same, because the problem is symmetric. This means that if we can toggle the relations between every pair of people, the second case reduces to the first - so it must be true as well.

**REMARK-MATH-HISTORY:** Following the same argument, we can prove the same result that among 18 people there are 4 that either all know each other, or are not acquainted at all.

What would happen if we decrease 18 to 17. Would the same statement be true? More generally, what is the *minimum* number such that this situation occurs? The solutions to this problem are called [Ramsey numbers](http://en.wikipedia.org/wiki/Ramsey%27s_theorem#Ramsey_numbers). For example, this exercise showed that $$R(3,3)$$ is at most 6. Proving that $$R(4,4)=18$$ required an extensive check using a computer of all $$2.46 \times 10^{26}$$ possibilities. The only thing we know nowadays about $$R(5,5)$$ is that it lies between 43 and 49 inclusive.

The combinatorialist [Joel Spencer](http://en.wikipedia.org/wiki/Joel_Spencer) has an anecdote about [Paul Erdős](http://en.wikipedia.org/wiki/Paul_Erd%C5%91s), a Hungarian mathematician that spent many years working on this type of problems.

> Erdős asks us to imagine an alien force, vastly more powerful than us, landing on Earth and demanding the value of $$R(5, 5)$$ or they will destroy our planet. In that case, he claims, we should marshal all our computers and all our mathematicians and attempt to find the value. But suppose, instead, that they ask for $$R(6, 6)$$. In that case, he believes, we should attempt to destroy the aliens.


### The square orchard

> You own a small orchard containing 51 trees. The shape of the garden is a square with side length 70 meters. It is possible to use a circular fence of radius 10 meters to enclose at least 3 of the trees?

The statement of this problems reminds us immediately of Dirichlet theorem. We have 51 trees (pigeons), and we want 3 to be close enough so they are contained in a circle of radius 10.

To explain the solution of the problem, let us apply some reverse thinking. How many boxes do we need so that at least 3 of the 51 trees are in the same box? The answer is 25. (We solved $$mn+1=51$$ and $$m+1=3$$ to find $$n$$). This tells us that if we divide the square in 25 regions, then there is a region that contains 3 trees. For obvious reasons, we cannot split a square in 25 circles of radius 10, there's no way we can have the boundaries to adhere to one other.

On the other hand, we can try to divide the square in 25 regions each of which is *contained* in a circle of radius 10. The obvious choice is to divide it in $$25 = 5^2$$ smaller squares of radius $$70 / 5 = 14$$. The biggest square that is contained in a circle of radius 10 has side $$10 \cdot \sqrt{2} \approx 14.14$$, so a circle of radius 10 can indeed contain a square of side 14. Wrapping everything up, recall that we found that there is one of the little squares that contains at least 3 trees, hence we also have a circle of radius 10 containing the same 3 trees.


### Peaceful rooks

> What is the maximal number of rooks you can place on an chess board so that no two can attack each other?

The problems involving finding a maximum are very tricky, because they always consist in two parts.

The first step is guessing what could be the right number: in this case, after a bit of guessing, is it easy to find a configuration with 8 rooks not attacking each other.

Then it comes the second part, that people sometimes forget, but that it needed to produce a complete proof. We in f need to prove,













