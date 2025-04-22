import java.util.Random;
import java.lang.Math;

class adcTSPSol { // Travelling Salesman Problem

  final int numTowns = 30;
  final int numGenotypes = 1000;
  final int genotypeLength = 31;
  final int numReproductions = 1000000;
  final int numMutationsPerReproduction = 1;

  // towns[numTowns][2]
  // This is the x and y position of each town.
  final int towns[][] = new int[][] {
      { 82, 7 }, { 91, 38 }, { 62, 32 }, { 71, 44 }, { 83, 69 }, { 68, 58 },
      { 54, 67 }, { 87, 76 }, { 13, 40 }, { 71, 71 }, { 44, 35 }, { 18, 54 },
      { 64, 60 }, { 37, 84 }, { 41, 94 }, { 2, 99 }, { 7, 64 }, { 22, 60 },
      { 25, 62 }, { 54, 62 }, { 4, 50 }, { 74, 78 }, { 18, 40 }, { 24, 42 },
      { 25, 38 }, { 41, 26 }, { 45, 21 }, { 58, 69 }, { 58, 35 }, { 83, 46 }
  };

 
  double distances[][] = new double[numTowns][numTowns];

  int genotypes[][] = new int[numGenotypes][genotypeLength];
  // This stores the fitness value for each generation population
  double fitness[] = new double[numGenotypes]; // fitness = -1 * route length
  int fittestIndividual = 0;
  int fittestIndex = 0;
  int midFittestIndex = 0;
  int leastFittestIndex = 0;


  Random rng = new Random();

  int random(int n) {
    return rng.nextInt(n);
  } // random integer between 0 and n-1

  void calculateFitness(int individual) // fitness = -1 * route length
  {
    /**
     *  Now, because the last gene is the starting gene, this more accurately
     *  calculates the fitness.
     */
    double routeLengthSum = 0.0;

  //  This gets the genes which represent town indices for every individual
  //  it calculates the distance between consecutive genes successfully
  //  Remember how the genotypes were modified to end with the town they started with
    int index1 = 0;
    int index2 = 0; 
    for (int i = 0; i < genotypeLength - 1; i+=1) {
      // distance between current index, `i`, and next, `i+1`
      index1 = genotypes[individual][i]; 
      index2 = genotypes[individual][i+1]; 
      routeLengthSum += distances[index1][index2];
    }

    // Store fitness of that individual
    fitness[individual] = -1 * routeLengthSum;
    // System.out.println("Fitness: " + fitness[individual]);
  }

  void calculateDistances()
  {
     for (int i=0; i<numTowns; i++){
      for (int j=0; j<numTowns; j++){
        int dx = towns[j][0] - towns[i][0];
        int dy = towns[j][1] - towns[i][1];
        //  Distance between town i and j
        //  which is magnitude of line vector, j - i
        distances[i][j] = Math.sqrt((double)(dx * dx + dy * dy));
        // double rounded = Math.round(distances[i][j] * Math.pow(10, 3)) / Math.pow(10, 3);
        // if (j % numTowns == 0){
        //   System.out.print(rounded + " \n");
        // }
        // else{
        //   System.out.print(rounded + " ");
        // }
      }
    }
  }

  void initialise()
  { 
    System.out.println("Started");

    this.calculateDistances();

    /* generate initial (random) population */
   
    for (int individual = 0; individual < numGenotypes; individual++) {
      /**
      * Create the array that stores indexes of all the towns to pick
      * from to randomly populate each genotype of the population
      */
      int remainingTowns[] = new int[numTowns];
      for (int i = 0; i < numTowns; i++){
        remainingTowns[i] = i;
      }

      // For each gene of an individual's genotype, apart from the last gene (hence -1)
      for (int g = 0; g < genotypeLength - 1; g++)
      {
        int index = random(numTowns); // randomly picked index value.
        /**
        *  If the random index choice for the remainingTowns to choose
        *  from is -1, it has previously been chosen. So keep
        *  in while loop until it chooses something different
        */
        while (remainingTowns[index] == -1){
          index = random(numTowns);
        }
        // then populate gene of individual with random index
        genotypes[individual][g] = remainingTowns[index];

        remainingTowns[index] = -1;
      }
      //  Then for the last genotype of the gene, which is the same as the starting.
      genotypes[individual][genotypeLength - 1] = genotypes[individual][0];
    }
    
    /* calculate fitness array for initial population */
    for (int individual = 0; individual < numGenotypes; individual++)
    {
      calculateFitness(individual);
    }
    
    System.out.println("Done Initializing.");
  }

  void mutate(int individual) // swap two towns in individual's route
  {
    //  Randomly choose two towns to swap
    int choice1 = random(genotypeLength - 1);
    int choice2 = random(genotypeLength - 1);
    //  Keep selecting a random choice1 and choice2 to until they're not the same
    while (choice1 == choice2) {
      choice1 = random(genotypeLength - 1);
      choice2 = random(genotypeLength - 1);
    }

    //  Swap Town Index in generation's individual's genotype
    //  According to the two randomly chosen indices to swap.
    int temp = genotypes[individual][choice1];
    genotypes[individual][choice1] = genotypes[individual][choice2];
    genotypes[individual][choice2] = temp;
}

  void crossover(int parentA, int parentB, int child)
  {
    //  Choose Cutpoint randomly

    /**
    *  Select random choice for index number around center of individual's
    *  array of genotype to use as cutpoint
    */
    int min = (int)Math.round((genotypeLength- 1) / 2) - random(3) - 1;
    int max = (int)Math.round((genotypeLength - 1) / 2) + random(4);

    int cutPointChoice = min + random(max - min);
    // int cutPointChoice = random(genotypeLength);


    for (int i=0; i<genotypeLength - 1; ++i){
      //  Modify Child
      if (i < cutPointChoice){
        genotypes[child][i] = genotypes[parentA][i];
      }
      else if (i >= cutPointChoice){
        genotypes[child][i] = genotypes[parentB][i];
      }
    }

    //  Now refine genotype; remove any that repeat

    //  Remaining Genes that can be chosen from by the child
    //  remainingTowns stores the indeices from 0->29 of each town
    int remainingTowns[] = new int[genotypeLength - 1];
    for (int i=0; i<genotypeLength - 1; ++i){
      remainingTowns[i] = i;
    }
    
    boolean noRepeat = true;
    //  Set the genes that have already been chosen by the child to -1
    for (int i=0; i<genotypeLength - 1; ++i){
      /**
      *  Each individual (in this case, the child) has a number of genes.
      *  Each gene is a town. The town is represented by an index from 0->29
      *  Hence why that value is used to see how many more towns can be chosen from
      */
      int index = genotypes[child][i];
      /**
      *   This ensures that if the town gene already exists in the child
      *   it is removed from `remainingTowns` by setting that town index
      *   to -1. Now if no town remains (that is, all the values that represent)
      *   the town indices are set to -1, it means that no gene in the child
      *   was repeated
      */
      remainingTowns[index] = -1;
    }
    /**
    *  So if there is any remainingtown value not set to -1, it means a
    * gene repeated in the child genome since all the genes in remainingTown were not used up
    */
   for (int i=0; i<genotypeLength - 1; ++i){
      if (remainingTowns[i] != -1){
        noRepeat = false;
      }
   }
    //  if !noRepeat
    if (noRepeat == false){
      for (int i=0; i<genotypeLength - 1; ++i){
        for (int j=0; j<genotypeLength - 1; ++j){
          //  For every other index
          if (i!=j){
            //  Check if the value of i is repeated
            //  in these other indices
            int choice = remainingTowns[random(genotypeLength - 1)];
            //  Make sure the random choice is not -1
            while (choice == -1){
              choice = remainingTowns[random(genotypeLength - 1)];
              // System.out.println("Crase");
            }
    
            //  For those genes in the genotype
            //  that have the value for i in the child repeated...
            if (genotypes[child][i] == genotypes[child][j]){
              genotypes[child][j] = choice;
            }
          }
        }
      }
    }
    //  Update the last value to be equal to the first.
    genotypes[child][genotypeLength - 1] = genotypes[child][0];
  }

  void calculateFittestRanges()
  {
    //  Find the Fittest Individual's Index.
    //  Find the Least Fittest Individual
    //  Find the sum for the mean fittest.
    int sum = 0;
    for (int i=0; i<numGenotypes; ++i){
      if (fitness[i] > fitness[fittestIndex]){
        fittestIndex = i;
      }
      if (fitness[i] < fitness[leastFittestIndex]){
        leastFittestIndex = i;
      }
      sum += fitness[i];
    }


    //  Ensure the mean is positive
    int mean = -1 * (int)Math.round(sum / numGenotypes);

    //  Then find index of fitness value closest to mean
    int diff = 0;
    for (int i=0; i<numGenotypes; ++i){
      int currentDiff = (int)Math.abs(Math.abs(fitness[i]) - mean);
      if (diff > currentDiff){
        diff = currentDiff;
        midFittestIndex = i;
        continue;
      }
      diff = currentDiff;
    }

    // System.out.println("Fittest: " + fittestIndex);
    // System.out.println("Mid: " + midFittestIndex);
    // System.out.println("Least: " + leastFittestIndex);

  }

  void steadyStateGaMainStep()
  {
    /**
     * Pick three individuals a,b,c at random
     * A is picked randomly between mean fittest index and fittest
     * B is picked randomly between mean fittest index and least fittst
     * C is picked randomly but is ensured to be neither A or B
    */
   this.calculateFittestRanges();
    
    //  Note bestFitness1 and bestFitness2 are index values
    int min1 = Math.min(midFittestIndex, fittestIndex);
    int max1 = Math.max(midFittestIndex, fittestIndex) + 1;

    int min2 = Math.min(midFittestIndex, leastFittestIndex);
    int max2 = Math.max(midFittestIndex, leastFittestIndex) + 1;

    
    int a = min1 + random(max1-min1);
    int b = min2 + random(max2-min2);

    //  Pick C randomly
    int c = random(numGenotypes);
    while (c == a || c == b){
      c = random(numGenotypes);
      a = min1 + random(max1-min1);
      b = min2 + random(max2-min2);
    }

    /**
     * reorder such that c is the least fit
     *  a and b just have to be fitter than c
     *  Get the fitness for each individual
    */
    double fitnessA = fitness[a];
    double fitnessB = fitness[b];
    double fitnessC = fitness[c];
    
    //  The fittest is with the smaller negative.
    int fittestValue = (int)Math.max(fitnessA, Math.max(fitnessB, fitnessC));
    fittestIndividual = fitnessA == fittestValue ? a : fitnessB == fittestValue ? b : fitnessC == fittestValue? c : a;

    double leastFit =  (int)Math.min(fitnessA, Math.min(fitnessB, fitnessC));

    //  So if c is not the least fit, make it the least fit
    if (fitnessC != leastFit){
      //  swap with the one that is least fit...
      boolean isA = fitnessA == leastFit;
      boolean isB = fitnessB == leastFit;
      int temp = c;
      //  If it is A, isA will be 1. If not it will be 0
      c = isA ? a : isB ? b : c;
      a = isA ? temp : a;
      b = isB ? temp : b;
    }

    /* but don't lose fittestIndividual */
    //  If c is the fittest, swap with b
    if (c==fittestIndividual) 
    {
      int temp=b;
      b=c;
      c=temp;
    }

    /* crossover a,b (in random order) to create child that replaces c */
    if (random(2)==1)
    {
      int temp=a; a=b;  b=temp;
    }
    crossover(a,b,c);
    /* mutate child */
    for (int m=0;m<numMutationsPerReproduction;m++) mutate(c);
    /* calculate fitness of child */
    calculateFitness(c);
  }

  void outputStatistics(int numRreproductionsSoFar) {
    if (numRreproductionsSoFar == 0)
      System.out.println("Remember that the output gene values have 1 added to them.");
      System.out.println("#repros\tbest\t: route");
    System.out.print("" + numRreproductionsSoFar + "\t" + (-fitness[fittestIndividual]) + "\t:");
    for (int g = 0; g < genotypeLength; g++)
      System.out.print(" " + (genotypes[fittestIndividual][g] + 1));
    System.out.println();
  }

  void run() {
    initialise();
    outputStatistics(0);

    for (int reproduction = 1; reproduction <= numReproductions; reproduction++) {
      steadyStateGaMainStep();
      if (reproduction % 20000 == 0)
        outputStatistics(reproduction);
    }
  }

  public static void main(String args[]) {
    new adcTSPSol().run();
  }

}