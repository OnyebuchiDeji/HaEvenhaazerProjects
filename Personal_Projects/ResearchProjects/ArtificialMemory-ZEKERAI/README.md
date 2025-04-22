#   Date: Mon-24-March-2025


#   A Simple Recurrent Neural Network: The Hopfield RNN

##   Brief about the Hopfield Neural Network

+   This small project is an implementation of Hopfield Neural Networks.
+   They are a network that works to store and retrieve stored memory when probed or cued with an input.
+   It is a simple **Recurrent Neural Network**.


##   Recurrent Neural Network
+   They are a type of Neural Netork that work with temporal or time-affected or time-dynamic processes. More clearly, they work with or on processes that exhibit dynamic temporal behaviour, or in simpler words, that uses information it obtained or generated from earlier time steps or earlier states in solving a problem.


+   Such systems are designed to solve problems that require analysis of time varying data, to the goal of predicting the behaviour of the system at some stage in the future by using information gained from analysing past behaviours.

##   Some Types of Recurrent Neural Networks
These are traditional feed-forward RNNS and are classified as McCulloch-Pitts MLP-based RNNS:
*   Elman Networks.
*   Jordan Networks.

##   RNNs: Further Elaboration
It uses a concept called a ***Moving Window***.
-   A window is a current vector or pattern of inputs.
-   Inputs are sampled or read using an input signal that is time dependent, i(t).
-   There is a fixed number of time-steps, n, which determines how much into the past one can look.
    *   e.g. i(t), i(t-1), i(t-2) ... i(t-n)
-   The input layer compasses all the input patterns represented by its own time-dependent input signal.
    *   The input layer must have n+1 nodes. Since if n=5, there will be 6 input patterns each with their own input signals:
        i(t), i(t-1), i(t-2), i(t-3), i(t-4), i(t-5).

+   The result of this functionality is a Short-term memory because of the **context units** and the **temporal extent of the moving window**.

+   The output of the RNN predicts what the signal will be a short time into the future. That is:
    *   output ~= i(t+1)

##  Hopfield Network --- a Simple RNN Memory

-   It is a simple model for understanding human memory.
-   Here are its features:
    *   It consisits of a single layer of units (inputs). That is, there are no other input layers that differe depending on time.
    *   it has no distinguished set of input units. (Unlike the normal time-differentiated input layers of normal RNNS).
    *   The network uses a single value or unit for each dimension/feature in the input patterns.
-   About the Input Units:
    *   Each unit connects to every other unit but do not connect to themselves.
    *   The connections are **weighted**, **bidirectional**, and **symmetric (Wij = Wji)**.
    *   The weights are fixed and determined in prior.
    *   The weights are calculated directly from the data that is to be stored by the network.
        +   they are not calculated piece-wise, updated via training.

##  Hopfield Networks --- How it Works

1.  When an Input Vector is parsed by the network, these happen:
    -   A single unit is randomly selected: at this stage.
        Only this unit is allowed to calculate its own activation.
    -   After this unit's recalculation of its activation, the current state of the network has effectively been revised.
    -   Now **another unit** is selected at random in order to update just its own activation.
    *   Now, though the units are randomly selected for updating, all units must be updated at the same `average rate`, that is,
        -   After 50 recurrent cycles, a unit in a Hopfield Network consisting of 5 nodes should have recalculated its activation about 10 times.

2.  The Signum activation (A) function is wdely used for calculating a unit's activation in Hopfield Networks:
    *   A = +1 if weighted sum of inputs is > 0
    *   A = -1 if weighted sum of inputs is < 0
    *   No change if weighted sum of inputs is = 0
    -   Once the selected unit has updated its activation, another unit is randomly selected and the process is repeated.

3.  **Convergence**
    -   The network has ***converged*** when all units fail to **change** their state/activation after they have been randomly selected for update.
        *   Hopfield networks are guaranteed to converge, although not necessarily to the desired stored pattern.
    -   At the point of convergence, the **current state** of activations across the units in the network constitutes a retrieved pattern.
        * one that was orginially encoded by the predetermined weights that were initially placed on the connections using the same process until that initial convergence.

##  Work Case and Elaboration on Operation:

+   A Hopfield NN could store the three pixel patterns `0, 1, and 2` of a K by G grid of pixels.
    -   In the grid, black pixels = +1, and grey pixels = -1

    -   If the grid is 7 by 9, each pattern has 7 x 9 = 63 pixels.
    -   Hence the NN will have 63 nodes.
    -   This means it will have 63 * (63 - 1) weights, since each node has weighted connections to every other node except itself.

+   Once the weights have been determined to store the patterns, the NN can be cued with a noise input, e.g. for the `1` digit.
+   Inspecting the NN's current state after a succession of activation updates gives better and better retrieval.
+   Then when no unit changes its level of activation, the NN has `converged`upon one of its **stored** patterns.


### Calculating the Weights
+   The weights in a simple Hopfield NN are determined directly from the data to be stored.
    *   **They are not learnt via a training process!**

+   The procedure for determining the weights involves calculating the *outer product* of each data vector with itself, then summing all of the resulting matrices.
        *   E.g. for the following pair of vectors:
            [ 1   1  -1]
            [-1  -1   1]
        to get the `outer product` of each vector:
    -   Multiply each vector's transpose by itself (Vt*V) to give matrices:
        For     V = [1 1 -1] 
        Vt = [
            1
            1
            -1
        ]

        Vt x V =[
             1   1  -1
             1   1  -1
            -1  -1   1
        ]

        For     V = [-1 -1  1]
        Vt = [
            -1
            -1
            1
        ]
        VtxV = [
             1  1  -1
             1  1  -1 
            -1  -1  1
        ]
    *   The above corrsponds to Hebbian and anti-HEbbian learning.

    -   Then sum the resulting matrices and zero the leading diagonal elements of the final matrix (Note: zero-ing effectively *removes* weights on self-connections, which are not used in these simple Hopfield NNs).

    W1 = [
         1   1  -1
         1   1  -1
        -1  -1   1
    ]

    W2 = [
         1   1  -1
         1   1  -1 
        -1  -1   1
    ]

    Wr = W1 + W2 = [
         2  2 -2
         2  2 -2
        -2 -2  2
    ]

    Wr (zeored) = W1 + W2 = [
         0  2 -2
         2  0 -2
        -2 -2  0
    ]

+   Wr is the resulting sum-matrix and canthen be mapped on to the NN.
    Consider 3 units, U1, U2, U3

    Wr = [
            U1  U2  U3
        U1:  0   2  -2
        U2:  2   0  -2
        U3: -2  -2   0
    ]
    *   [Here is the picture](HopfieldPic-2025-03-24_193819.png)

### Pattern Retrieval
+   If this corrupted input pattern for U1, U2, and U3:
    i = [1 -1 -1] is supplied...

    +   Now, generate a random order of node selections, e.g.
        {first node 2, then node 1, then node 3} =
        {U2, U1, U3}
    +   then apply the pattern retrieval procedure by calculating each node's activation applying the signum activation function to the weighted sum of its inputs = V x Wt

    +   So here, the activation value for U2 is recalculated (revised).

        Also, Wt is the weighted connections matrix for U2 against U1, U2, and U3 correspondingly
        Wt(u2) = [2 0 -2]
        i = [1 -1 -1]

        i * Wt(u2) => signum(2 + 0 +2) = signum(4) = 1.
            Then the activation for unit 2 in the input is set to 1
            Now, i = [ 1  *1 -1] --- note the -1 has changed to 1
            **The * represents a changed value** 
    +   Then that of U1 is recalculated:
        Wt(u1) = [0 2 -2]
        [1 *1 -1] * [0 2 -2] => signum(0 + 2 + 2) = signum(4) = 1
            Then the activation value for unit 1 in the iput is set to 1
            Now, i = [1* 1* -1]

    +   Then that of U3 is revised:
        Wt(u3) = [-2 -2 0]
        [*1 *1 -1] * [-2 -2 0] => signum(-2 - 2 + 0) = signum(-4) = -1
            So activation for unit 3 is set to -1

        Now, i = [*1 *1 -1]

+   Then the process is repeated again to see if the NN's current input activation pattern [1 1 -1] is stable.
    A new random order of selecting nodes is tried:
        {node 1, node 3, node 2} = {U1, U3, U2}

    [1 1 -1] * [0 2 02] => signum(0 + 2 + 2) = signum(4) = 1
        so activation for unit 1 in pattern i is set to 1;
        so pattern i doesn't change 
    [1 1 -1]*[-2 -2 0] => signum(-2 -2 + 0) = signum(-4) = -1
        so activation for unit 3 is set to -1, in pattern i
        so this value does not change
    [1 1 -1]*[2 0 -2] => signum(2 + 0 + 2) = signum(4) = 1
        so activation for unit 2 is set to 1
        This means pattern i does not change.

    *   Now, the "revised' pattern of activations has not changed this time around.
    pattern i is still [1 1 -1], and so is stable. Hence it must be one of the patterns originally stored by the network.

##  Downsides of the Hopfield Network:

+   One cannot guarantee to retrieve the intended pattern stored on the network from the input used to cue the network.
+   the larger the number of patterns and nodes, the more computationally intensive everything gets

##  Coolsides of the Hopfield Network:
+   Once a subsequent revised pattern results in a pattern that is not changed, the process of retrieval is stopped.

##  Finished: Thursday-27-March-2025

0
[-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]

1
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

2
[-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]


NOISE
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 
-1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1]

6 - not 6
[-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]


1 - different
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]


4
[-1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


4 - improved
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

4 - Even better
[-1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]