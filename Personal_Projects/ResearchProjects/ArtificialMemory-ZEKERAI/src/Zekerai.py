"""
    This is where the different Hopfield Systems and any supporting structure will be defined.

"""

import random as rnd
import time
# import math
# import typing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from App import Grid

class HopfieldN1:
    def __init__(self):
        self.weight_matrix = []
        self.called = False 
        self.prev_revised_pattern_v2 = []
        # self.lag = 1000

    def oninit(self, inputs):
        """
            Is called once to initialize the Hopfield Network
            by calculating weights based on inputs patterns from the grid
            
            only when `called` is reset can it be called again.
        """
        if self.called:
            return

        self.weight_matrix = self.calculate_weights(list(inputs)) 
    
    def reset(self):
        self.weight_matrix.clear()
        self.called = False


    def calculate_outer_product(self, vect: list[int]) -> list[list[int]]:
        """
            *   Returns a 2D array (matrix) of the outer product of a vector.
            *   The outer array is the multiplication of that
                vector's transpose with its normal self.
                OP(V) = Vt x V
                OP(V) = outer product of V
                Vt = transpose of V
        """
        output_arr: list[list[int]] = []
        for r in range(len(vect)):
            row = []
            for c in range(len(vect)):
                row.append(vect[r] * vect[c])
            output_arr.append(row)
        
        return output_arr


    def sum_matrices(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        """Sums two matrices of the same dimensions"""
        l = len(mat1)
        output_arr = []
        for r in range(l):
            row = []
            for c in range(l):
                row.append(mat1[r][c] + mat2[r][c])
            output_arr.append(row)

        return output_arr

                
    def zero_leading_diagonal(self, mat: list[list[int]]):
        l = len(mat)
        for r in range(l):
            for c in range(l):
                if r == c:
                    mat[r][c] = 0
        return mat


    def calculate_weights(self, inputs: list[list[int]]):
        """
            Calculates the Hopfield System's weights
            based on inputs.
        """
        final_mat = self.calculate_outer_product(inputs[0])
        
        for i in range(1, len(inputs)):
            this_input = self.calculate_outer_product(inputs[i])
            final_mat = self.sum_matrices(final_mat, this_input)
            
        final_mat = self.zero_leading_diagonal(final_mat)
        return final_mat

    def multiply_matrices(self, v1, v2):
        """
            Performs matrix multiplication on vectors
            of same dimensions.
            It's basically vector multiplication
        """
        l = len(v1)
        output_arr = []
        for c in range(l):
            output_arr.append(v1[c] *v2[c])

        return output_arr

    def signum_add(self, v):
        """
            Adds up the values in the matrix
            and if they are greater than 0, set to 1
            If less than 0, set to -1
        """
        sum = 0
        for c in v:
            sum += c 

        if sum == 0:
            return sum

        #   Else clamp to ensure either -1 or 1, and return
        return max(-1, min(sum, 1))

        

    def retrieve_pattern(self, noisyInput):
        """
            The heaviest part.
            Performs the bulk of the algorithm to calculate.

            Using run_count and recalc_frequency
            I have verified that the way I have performed the algorithm,
            each unit/node is called/updated at the same average rate.

            Uncomment the code that has to do with `run_count` and `recalc_frequency`
            to confirm this.
        """
        is_stable = False
        length = len(noisyInput)
        list_of_indices = [i for i in range(length)]

        #   These two are used to ensure that the each unit is updated at the same average rate.
        #   SO if run_count is 50 and there are 5 nodes (indices), then
        #   the frequency for each should be 50 / 5 = 10
        # run_count = 0
        # recalc_frequency: dict[int, int]= dict(*list_of_indices)  ##  CAP
        # recalc_frequency: dict[int, int] = {val:0 for val in list_of_indices}

        #   Ensure to make a copy
        pattern = list(noisyInput)
        prev_revised_pattern = list(noisyInput)
        

        while not is_stable:
            """
                First, select create a random order of indexes
                which acts as the random order of selecting nodes
                `rnd.shuffle(ls)` shuffles list ls in place
                `rnd.sample(ls, k)` samples k values from ls
                    randomly without repeating any.
                    To ensure it samples from all, make k= len(ls)   
            """
            random_order_node_list = rnd.sample(list_of_indices, length)

            for node_index_val in random_order_node_list:
                #   recalculate activation
                #   multiply the noisy input and the current node's matrix vector
                mult_res = self.multiply_matrices(pattern, self.weight_matrix[node_index_val])
                res = self.signum_add(mult_res)
                if res != 0:
                    pattern[node_index_val] = res
                # recalc_frequency[node_index_val] += 1
            
                # run_count += 1

  
            #   Comment this to use the run_count test below
            if prev_revised_pattern == pattern:
                is_stable = True
                break

            # shouldExit = False
            # if prev_revised_pattern == pattern:
            #     for key in recalc_frequency:
            #         if recalc_frequency[key] == int(run_count // length):
            #             shouldExit = True
                
            #     if shouldExit:
            #         is_stable = True
            #         print("Final Run Count:", run_count)
            #         for key, val in recalc_frequency.items():
            #             print("Revise Update Count for node {0}: {1}".format(key, val))
            #         break

            prev_revised_pattern = pattern

        
        return pattern
    

    def retrieve_pattern_v2(self, noisyInput):
        """
            This follows the previous albeit it returns the input pattern
            after every revision so the process of revising can be seen
            Hence, it is called continually in the main loop
        """
        is_stable = False
        length = len(noisyInput)
        list_of_indices = [i for i in range(length)]

        #   Ensure to make a copy
        pattern = list(noisyInput)

        

        while not is_stable:
            random_order_node_list = rnd.sample(list_of_indices, length)

            for node_index_val in random_order_node_list:
                #   recalculate activation
                #   multiply the noisy input and the current node's matrix vector
                mult_res = self.multiply_matrices(pattern, self.weight_matrix[node_index_val])
                res = self.signum_add(mult_res)
                if res != 0:
                    pattern[node_index_val] = res
                    yield pattern


            time.sleep(3)
            
            #   Comment this to use the run_count test below
            if self.prev_revised_pattern_v2 == pattern:
                is_stable = True
                break
                
            self.prev_revised_pattern_v2 = list(pattern)


        return pattern


def test1():
    hp = HopfieldN1()
    m1 = hp.calculate_outer_product([1, 1, -1])
    m2 = hp.calculate_outer_product([-1, -1, 1])
    sum = hp.sum_matrices(m1, m2)
    print("M1:", m1)
    print("M2:", m2)
    print("M1 + M2:", sum)
    print("M1 + M2 -- zeroed out:", hp.zero_leading_diagonal(sum))

def test2():
    hp = HopfieldN1()
    print("Final Mat:", hp.calculate_weights([[1, 1, -1], [-1, -1, 1]]))

def test3():
    hp = HopfieldN1()
    p1 = [1, 1, -1]
    p2 = [-1, -1, 1]
    noise = [1, -1, -1]
    hp.weight_matrix = hp.calculate_weights([p1, p2])
    res = hp.retrieve_pattern(noise)
    print("Noise:",noise)
    print("Retrieved Pattern:", res)

    

def main():
    test3()

if __name__=="__main__":
    main()