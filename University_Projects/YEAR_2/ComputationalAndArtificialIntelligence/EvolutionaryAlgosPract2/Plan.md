#   Date: Thurs-27-Feb-2025

#   About The Travelling Salesman Problem
https://www.lancaster.ac.uk/stor-i-student-sites/libby-daniells/2020/04/21/the-travelling-salesman-problem/


#   Plan

+   The Travelling Salesman Problem (TSP):
    -   There are a bunch of coordinates in a 2d space.
    -   The goal of the Salesman is to visit every coordinate and return back to his starting position.
    -   Each coordinate can only be visited once.
    -   Indeed, the order the salesman takes affects the maximum distance he travels.
    -   This order is what is manipulated, mutated and hence evolved to obtain the minimum distance traveled.

    -   Hence the order of towns to visit is important, and the fitness is evaluated using the negative of the maximum distance that it takes using a certain route.
    -   The order of towns is what is formed by the `genomes` or `genes` of an `individual`. An individual is represented by a unique `genotype`
        *   A `genotype` is a collection of genomes.
    -   **Crossover** randomly selects two `Parents` with the probability of picking those that could have performed well. Half of each of their genomes are taken to modify a child genome in the population.
    -   **Mutation** randomly swithces two genes of an individual.


##  My Sols:
+   Ensure that after crossovers, no genes are repeated in the child genome. this is because the original is never repeated.
+   Ensure

##  Objectives
+   After calculating the distance, find the maximum distance from summing all the distances.
+   Make it that for each generation, you can debug to display the distance of its route.
+   


#   Notes: TSP

+   It is an **NP-hard (Nondeterministic polynomial time) problem**. A problem is NP-hard if an algorithm for solving it can be translated into one for solving a (nondeterministic polymnomial time) problem.
        *   This means there is no polynomial-time algorithm that is known to efficiently solve every travelleing salesman problem.
        *   This means heuristics or approximate methods are used to solbe the TSP optimally for improved speed in finding the solution and closeness to the optimal solution.

+   The TSP can be divided into two types:
    -   **The Asymmetric Travelling Salesman Problem (ASTSP)**, where distance from A to B is different to that from B to A.
    -   **THe Symmetric Travelling Salesman Problem (STSP)**, where distance from A to B is equal to distance from B to A.