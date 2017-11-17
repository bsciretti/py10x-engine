# py10x-engine

## What is this?
This is is a programming language based on Olivetti Programma's Assembly.
This is **not** an emulator. Emulators are another thing, this language coniugates the agility of Programma's Assembly with the strongs of today's PCs.

## Language
### Overview
In this language all the basic operation are made n the A register, the "accumulator". 
Store register are: B, C, D, E, F.
Working register are: M, A, R

Every operation is made on the A register so if you read:
B-
You're making
A-B

Math operation are usable also on other register.
### Basic functions
The mathematic fundamental operations are:
* +, that make A = A + X
* -, that make A = A - X
* x, that make A = A * X
* :, that make A = A / X, also saves in R the rest of division
* v, that make sqrt X, also saves in M 2(sqer(X))

### Print
There are two instructions related to printing:
* The # prints the value of the given register
* The /# writes a blank line
### Register functions
Register are like variables. Operation are beetween the main register (A and M) and a given register. Differently from Programma 101 the M register is not implied where there is no register in the command.
* The >< exchanges the A register with the given register
* The ! puts M in the given register
  * *Attention: A! gives the abs of A*
* The ^ puts the given register in A

### Math
Math functions are ispired by Olivetti P652 and are:
* sin: Sine
* cos: Cosine
* arc: Arcosine
* tan: Tangent

### Jumps

## Functions
### Done
* Basic functions
* Print functions
* Math functions
* Jumps
### Working on it
* String management like P203
* Realistic system for string in memory
* Plotting
### Information needed
* Jumps like P101
* Possible IF in P652
* Possible WHILE in P652
