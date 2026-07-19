# Task 1.2 – Core Math for Machine Learning
  
**Task:** Explain the core math concepts used in Machine Learning

---

# Introduction

Machine learning uses mathematics to understand data and make predictions. Before learning advanced algorithms, it is important to understand some basic concepts from linear algebra, calculus, and probability. This document explains these concepts in simple words with small examples.

---

# 1. Vectors and Matrices

A vector is an ordered list of numbers. It can represent values such as coordinates, features of an image, or measurements of an object.

Example:

```
v = [2, 4, 6]
```

A matrix is a table of numbers arranged in rows and columns. Matrices are used to store multiple vectors or perform transformations.

Example:

```
A = |1 2|
    |3 4|

B = |5 6|
    |7 8|
```

### 2 × 2 Matrix Multiplication

Multiply:

```
A = |1 2|
    |3 4|

B = |5 6|
    |7 8|
```

Result:

```
C = A × B

= |(1×5 + 2×7)   (1×6 + 2×8)|
  |(3×5 + 4×7)   (3×6 + 4×8)|

= |19 22|
  |43 50|
```

Matrix multiplication combines rows of the first matrix with columns of the second matrix.

---

# 2. Dot Product

The dot product multiplies corresponding elements of two vectors and adds the results.

Example:

```
[1, 2, 3] · [4, 5, 6]

= (1×4) + (2×5) + (3×6)

= 4 + 10 + 18

= 32
```

The dot product tells us how similar or aligned two vectors are. A larger positive value means the vectors point in similar directions. If the result is zero, the vectors are perpendicular.

---

# 3. Derivative and Gradient

A derivative measures how quickly a function changes. It tells us the slope of a curve at a specific point.

For example,

```
f(x) = x²
```

The derivative is

```
f'(x) = 2x
```

At x = 3,

```
f'(3) = 6
```

This means the function is increasing at a rate of 6 at that point.

A gradient is an extension of the derivative for functions with many variables. It points in the direction where the function increases the fastest.

In machine learning, gradients are used to update model parameters during training. Optimization algorithms such as Gradient Descent move in the opposite direction of the gradient to reduce prediction errors.

---

# 4. Mean, Variance, and Standard Deviation

Dataset:

```
[2, 4, 4, 4, 5, 5, 7, 9]
```

## Mean

```
Mean = (2+4+4+4+5+5+7+9) / 8

= 40 / 8

= 5
```

The mean represents the average value of the data.

## Variance

Subtract the mean from each value, square the result, and calculate the average.

```
(2−5)² = 9
(4−5)² = 1
(4−5)² = 1
(4−5)² = 1
(5−5)² = 0
(5−5)² = 0
(7−5)² = 4
(9−5)² = 16

Sum = 32

Variance = 32 / 8 = 4
```

Variance measures how spread out the data is.

## Standard Deviation

```
Standard Deviation = √Variance

= √4

= 2
```

Standard deviation tells us the average distance of values from the mean.

---

# 5. Probability and Bayes' Theorem

Conditional probability is the probability of an event happening given that another event has already happened.

Bayes' Theorem helps us update probabilities when new information becomes available.

### Disease Test Example

Suppose:

- 10,000 people
- 1% have the disease
- Test accuracy is 99%

People with disease:

```
100
```

Correct positive results:

```
99
```

Healthy people:

```
9,900
```

False positive results:

```
99
```

Total positive tests:

```
99 + 99 = 198
```

Probability that a person is actually sick after testing positive:

```
99 / 198

≈ 0.5

≈ 50%
```

Although the test is 99% accurate, a positive result means there is only about a 50% chance of actually having the disease because healthy people greatly outnumber sick people.

---

# Conclusion

These mathematical concepts form the foundation of machine learning. Vectors and matrices represent data, the dot product measures similarity, derivatives and gradients help models learn, mean and variance describe data, and probability helps us reason under uncertainty. Understanding these ideas makes it easier to learn more advanced machine learning techniques.