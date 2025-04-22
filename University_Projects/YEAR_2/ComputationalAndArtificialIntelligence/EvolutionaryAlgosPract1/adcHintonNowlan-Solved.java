
/**
 *  Date: Wednesday 12th February 2025
 * 
 *  This is the Practical 1 for Evolutionary Alrgoithms
 *  Lecture 1. 
 *  URL:
 *	file:///C:/Users/Ebenezer%20Ayo-Meti/Documents/SCHOOL/UNI_Things/Keele/Courses/Comp_Sci/YEAR_2/C&A_Intelligence-CSC20043/ea1-genetic-algorithms.pdf
 * 
 *  It is code from the Hinton and Nowlan's Experiment
 *  Hinton and Nowlan's paper, 'How Learning Can Guide Evolution',  
 *  demonstrates how learning and evolution interact.
 *  It shows the Baldwin Effect that rightfully suggests that an entity
 *  can learn during its lifetime, which drives natural selection and variation
 *  in the gene pool, leading to more diversity while making subsequent generations
 *  have better characteristics thant previous.
 * 
 *  Paper: https://content.wolfram.com/sites/13/2018/02/01-3-6.pdf
 * 
 *  Experiment's Parameters and Meanings
 * 
 *  Genome Length - 20 : this is the number of digits or character that represent a genome.
 *    A genome is, especially in this case, the complete set of genes that code for all
 *    the characteristics of the organism.
 *    In this case each character is a gene.
 * 
 *  Alleles - {0, 1, ?} : These are the different forms of a gene that can appear in a genome.
 * 
 *  Fitness Function: This is a value calculated for a specific genotype in a specific generation
 *    that determines how well that genotype performs.
 *    In this case it is calculated randomly but in a way that depends on the genotypes for every genotype for each generation.
 * 
 *    See the formula `@FitnessFunction`.
 * 
 *    In this formula, it is seen that the more genes in the genotype are of value 1, the higher the fitness function.
 *    The formula does this by ensuring that if the gene of a specific genotype is zero
 *    it takes another trial, thereby reducing the number of trials remaining.
 *    Now, the fitness value is directly proportional to the number of trials. SO the higher this number
 *    the fitter that genome. But the smaller it is, the less fit.
 *    But then in the logic, some random is added with the gene '?' such that there it allows the
 *    possibility for an added 0.5 probability on whether or not that gene should be interpreted
 *    as a 1 or 0. THis is the random characteristic that simulates learning.  
 * 
 *    Now, the set of genotypes are modified between each subsequent generation, hence the fitness value
 *    also changes.
 *     
 *      Formula:
 *        ```
 *          Fitness = (1 + 19n) / 1000
 *            n = number of trials remaining after target pattern is found.
 *            19 = genome length - 1
 *            1000 = no. of genotypes.  
 *        ```
 *        the `calculateFitnessArray()` does not yet divide by 1000
 *        I am meant to fix it to divide by this value.
 *     Now, if a genotype is perfect, that is, all its digits are 1, 
 *    the max fitness value is 20.
 * 
 *   Generational Algorithm: This usitilizes the roulette wheel selection algo.
 * 
 *    Population Size: 1000
 * 
 *  Result: Solution found rapidly.
 * 
 *  Instructions to Fix Code:
 *    A) Read through the code outline and understand what each part should do
 *    B) Write code to replace the BBBBs, to complete the code that selects parents for 
 *      reproduction
 *    C) Write code to replace the CCCCs, to produce the child genotype using crossover
 *    D) Run the completed program several times, and compare your output to figure 2 from 
 *        the paper.  (You might like to graph your results, e.g. using spreadsheet software.)
 * 
 */

import java.util.Random;

class adcHintonNowlan
{

  //  Number of genotypes to be tested for each generations
  final int numGenotypes = 1000;
  // Length of integer array, with each integer representing a gene, that make up the genetotype
  final int genotypeLength = 20;
  //  max no. of trials 
  final int numLearningTrials = 1000;
  //  number of generations to be tested..
  final int numGenerations = 50;

  Random rng = new Random();

  int random(int n) {
    return rng.nextInt(n);
  } // random integer between 0 and n-1

  final int zero = 0, one = 1, questionMark = 2;

  //  Array that stores all the genotypes for a specific generation
  int genotypes[][] = new int[numGenotypes][genotypeLength];
  //  Array that stores the fitness result for each genotype
  int fitness[] = new int[numGenotypes];

  // fitness = 1000*"1+19n/1000" where n = number of learning trials remaining
  // or rather numLearningTrials + 19 * n

  //  @FitnessFunction
  //   Now, if a genotype is perfect, that is, all its digits are 1, 
  //  *    the max fitness value is 20.
  void calculateFitnessArray() // calculate fitness[] *YOU DO NOT NEED TO UNDERSTAND THIS*
  {
    for (int i = 0; i < numGenotypes; i++) {
      int numTrialsRemaining;
      for (numTrialsRemaining = numLearningTrials; numTrialsRemaining > 0; numTrialsRemaining--) {
        int g;
        for (g = 0; g < genotypeLength; g++)
          if (genotypes[i][g] == zero || (genotypes[i][g] == questionMark && random(2) == 0))
            break;
        if (g == genotypeLength)
          break;
      }
      fitness[i] = (numLearningTrials + 19 * numTrialsRemaining) / 1000;
    }
  }

  //  Code that calculates fitness for current generation
  //  and performs Parent selection based on fitness as well
  //  as gene crossover for child, to modify the current genotype
  //  by the best performing parents
  void nextGeneration()
  { 
    //  Get fitness for prior generation
    calculateFitnessArray();

    //  Keep an accummulated fitness value for that generation of genotypes `sumFitness`
    //  it represents how well they performed
    //  IF all genotypes were perfect, sumFitness after accummulation
    //  would be 20, 000
    int sumFitness=0; for (int i=0;i<numGenotypes;i++) sumFitness += fitness[i];

    //  Modify the current genotypes based on top fitness values of prior generations
    int newGenotypes[][] = new int[numGenotypes][genotypeLength];

    for (int i=0;i<numGenotypes;i++) // for each new genotype
    { 
      int[] parentA = new int[genotypeLength];
      int[] parentB = new int[genotypeLength];

      //  Calculate new genotype
      /*
        *Select parents for reproduction.
        *The probability of a parent being selected should be proportional to its fitness.
        *Hint: calculating random(sumFitness) will help
        *BBBB
        * Find mean sum fitness
        * So if they were perfect, mSumFitness = 20'000/1000 = 20
      */
      int mSumFitness = sumFitness / numGenotypes;
      //  Parents in this case are to be selected by random though
      //  the more the fitness value, the higher the range of parents that
      //  can be selected.

      //  Populate parentA
      for (int g = 0; g < genotypeLength; g++){
        int randChoice = random(mSumFitness * random(numGenotypes));
        parentA[g] = genotypes[randChoice][g];
      }
      //  Populate parentB
      for (int g = 0; g < genotypeLength; g++){
        int randChoice = random(mSumFitness * random(numGenotypes));
        parentB[g] = genotypes[randChoice][g];
      }

      int cutPoint = 1+random(genotypeLength-1);

      // Crossover: newGenotypes[i] should copy genes before the cut point from
      // genotypes[parentA] and those from the cut point on from genotypes[parentB]

      // CCCC
      //  populate Child, new
      for (int g = 0; g < genotypeLength; g++){
        if (g < cutPoint){
          newGenotypes[i][g] = parentA[g];
        }
        if (g >= cutPoint){
          newGenotypes[i][g] = parentB[g];
        }
      }

    }

    //  update the genotypes for the next generations
    for (int i=0;i<numGenotypes;i++)
      for (int g=0;g<genotypeLength;g++) genotypes[i][g] = newGenotypes[i][g];
  }

  //  Outputs the number of each gene appeared for
  //  that generation.
  //  It divides by `d` to normalize it.
  void outputStatistics(int generation) {
    int counters[] = new int[3];
    counters[0] = counters[1] = counters[2] = 0;

    for (int i = 0; i < numGenotypes; i++)
      for (int g = 0; g < genotypeLength; g++)
        counters[(int) genotypes[i][g]]++;
        //  This counts the number of each gene that appears throughout
        //  every genotype for that generation

    double d = numGenotypes * genotypeLength;
    System.out.println("" + generation + " " + counters[0] / d + " " + counters[1] / d + " " + counters[2] / d);
  }

  void run() {
    //  Start
    //  Randomly generate gene sequences for each genotype -- first generation
    for (int i = 0; i < numGenotypes; i++)
      for (int g = 0; g < genotypeLength; g++)
        switch (random(4)) {
          case 0:
            genotypes[i][g] = zero;
            break; // 25%
          case 1:
            genotypes[i][g] = one;
            break; // 25%
          default:
            genotypes[i][g] = questionMark;
            break; // 50%
        }
    //  Output statistics for the random geneotype first generation
    outputStatistics(0);
    //  For subsequent generations
    for (int generation = 1; generation <= numGenerations; generation++) {
      nextGeneration();
      outputStatistics(generation);
    }
  }

  public static void main(String args[]) {
    new adcHintonNowlan().run();
  }

}