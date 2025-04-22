import java.util.Random;
import java.lang.Math;

class adcTSPSol { // Travelling Salesman Problem

  final int numTowns = 30;
  final int numGenotypes = 1000;
  final int genotypeLength = numTowns;
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

  // This sotres the distance between one each town and all the other towns.
  // Distance is calculated using pythagorean.
  double distances[][] = new double[numTowns][numTowns];

  // numOfGenotypes represents the population number for a generation.
  // genotypeLength stores the index for each town distance combination
  // such that it covers every town
  int genotypes[][] = new int[numGenotypes][genotypeLength];
  // This stores the fitness value for each generation population
  double fitness[] = new double[numGenotypes]; // fitness = -1 * route length
  int fittestIndividual = 0;
  int bestFitness1 = 0;
  int bestFitness2 = 0;

  Random rng = new Random();

  int random(int n) {
    return rng.nextInt(n);
  } // random integer between 0 and n-1

  void calculateFitness(int individual) // fitness = -1 * route length
  {
    // An individual's genotype consists of all the town visiting
    // combinations required to have gone through all towns and come back.

    // Works on the `genotypes` of an individual
    int individualGenotype[] = new int[genotypeLength];
    // Copy into `individualGenotype`
    System.arraycopy(genotypes[individual], 0, individualGenotype, 0, genotypeLength);

    double routeLengthSum = 0.0;
    int startTown = individualGenotype[0];
    int endTown = individualGenotype[genotypeLength - 1];

    for (int i = 0; i < genotypeLength - 1; ++i) {
      // distance between current index, `i`, and next, `i+1`
      double dist = distances[i][i + 1];
      routeLengthSum += dist;
    }
    // Finally, add the distance between the startTown and the
    // endTown using their indices.
    routeLengthSum += distances[startTown][endTown];

    // Store fitness of that individual
    fitness[individual] = -1 * routeLengthSum;
  }

  void initialise()
  { 
    System.out.println("Started");
    /*
      * calculate distances between towns
      * That is, for Town 0 (town of index 0), calculate the distance
      * between it and all the other towns.
      */
    // for (int i = 0; i < numTowns; i++)
    //   for (int j = 0; j <= i; j++) {
    //     int dx = towns[j][0] - towns[i][0], dy = towns[j][1] - towns[i][1];
    //     distances[i][j] = distances[j][i] = Math.sqrt((double) (dx * dx + dy * dy));
    //       double rounded = Math.round(distances[i][j] * Math.pow(10, 3)) / Math.pow(10, 3);
    //     if (j % numTowns == 0){
    //       System.out.print(rounded + " \n");
    //     }
    //     else{
    //       System.out.print(rounded + " ");
    //     }
    //   }

    //  This work very well 
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
    // System.out.println("\n");

    /* generate initial (random) population */
    // For every individual of the population (a genotype represents an individual)
    for (int individual = 0; individual < numGenotypes; individual++) {
      // Create the array that stores indexes of all the towns to pick
      // from to randomly populate each genotype of the population
      int remainingTowns[] = new int[numTowns];
      for (int i = 0; i < numTowns; i++)
        remainingTowns[i] = i;

      // For each gene of an individual's genotype
      for (int g = 0; g < genotypeLength; g++) {
        int index = random(numTowns); // randomly picked index value.
        //  If the random index choice for the remaingTowns to choose
        //  from is -1, it has previously been chosen. So keep
        //  in while loop until it chooses something different
        while (remainingTowns[index] == -1){
          index = random(numTowns);
        }
        // then populate gene of individual with random index
        genotypes[individual][g] = remainingTowns[index];

        /**
         * Then the randomly chosen index's value is removed
         * from remaining towns by populating it with the last value of the
         * remainingTowns array; it moves this last value to the left by subtracting
         * by `g`
         * remainingTowns[0...31] = [0...31].
         * SO if remainingTowns[index 2] is randomly chosen, then
         * remainingTowns[2] is changed to = 31. For g = 0
         * g=1, when remainingTowns[5] is randomly chosen
         * remainingTowns[5] is changed to = 30 and so on.
         */
        // remainingTowns[index] = remainingTowns[numTowns - g - 1];
        //  If a choice has been made, remove it from remaining sample
        //  of towns to choose from to prevent repeated choices,
        remainingTowns[index] = -1;
      }
    }
    /* calculate fitness array for initial population */
    for (int individual = 0; individual < numGenotypes; individual++)
      calculateFitness(individual);
  }

void mutate(int individual) // swap two towns in individual's route
{
  //  Randomly choose two towns to swap
  int choice1 = random(genotypeLength);
  int choice2 = random(genotypeLength);
  //  Keep selecting a random choice 2 to make sure they're not the same
  while (choice1 == choice2) {choice2 = random(genotypeLength);}

  //  Swap Town Index in generation's individual's genotype
  //  According to the two randomly chosen indices to swap.
  int temp = genotypes[individual][choice1];
  genotypes[individual][choice1] = genotypes[individual][choice2];
  genotypes[individual][choice2] = temp;
}

void crossover(int parentA, int parentB, int child)
{
  //  Choose Cutpoint randomly
  //  to choose a cut point between a and b
  /**
   *  a + random(b - a)
   * 
   *  So if a = 2, and b = 7
   *  Random value generated is between
   *  2 and 7. Since only 5 possible integers can be randomly
   *  chosen between 2 and 7, random(7 - 2) = random(5) is done.
   *  The return value can be a, the minimum, and so is min inclusinve.
   *  But it can only return max - 1.
   *  This is because the implementation of `random` returns a value between 0 and n-1.
   *  So since 7-2 = 5, random (5) returns [0,4], 0 to 4 (4 included).
   *  This is 5 different integers.
   *  that returns a value between 0 and n-1, n being the parameter supplied.
   */
  //  Select random choice for index number around center of individual's
  //  array of genotype to use as cutpoint
  int min = (int)Math.round(genotypeLength / 2) - random(3) - 1;
  int max = (int)Math.round(genotypeLength / 2) + random(3);

  // System.out.println("Min: " + min);
  // System.out.println("Max: " + max);
  int cutPointChoice = min + random(max - min);
  // int cutPointChoice = random(genotypeLength);

  int[] parentAGenotype = new int[genotypeLength];
  System.arraycopy(genotypes[parentA], 0, parentAGenotype, 0, genotypeLength);
  // System.out.println("ParentA:");
  // for (int i=0; i<genotypeLength;++i){
  //   System.out.print(parentAGenotype[i] + " ");
  // }
  // System.out.println("\n");
  int[] parentBGenotype = new int[genotypeLength];
  System.arraycopy(genotypes[parentB], 0, parentBGenotype, 0, genotypeLength);
  // System.out.println("ParentB:");
  // for (int i=0; i<genotypeLength;++i){
  //   System.out.print(parentBGenotype[i] + " ");
  // }
  // System.out.println("\n");


  for (int i=0; i<genotypeLength; ++i){
    //  Modify Child
    if (i < cutPointChoice){
      genotypes[child][i] = parentAGenotype[i];
    }
    else if (i >= cutPointChoice){
      genotypes[child][i] = parentBGenotype[i];
    }
  }
  //  Now refine genotype; remove any that repeat

  //  Remaining Genes that can be chosen from by the child
  int remainingTowns[] = new int[genotypeLength];
  for (int i=0; i<genotypeLength; ++i){
    remainingTowns[i] = i;
  }
  
  boolean noRepeat = true;
  //  Set the genes that have already been chosen by the child to -1
  for (int i=0; i<genotypeLength; ++i){
    //  Each individual (in this case, the child)
    //  has a number of genes.
    //  Each gene is a town.
    //  The town is represented by an index from 0->29
    //  Hence why that value is used to see how many more
    //  towns can be chosen from
    remainingTowns[genotypes[child][i]] = -1;
  }
  //  FOr every gene, or town
  for (int i=0; i<genotypeLength; i++){
    //  IF there is any town in the child's genotype
    //  that had not been used from `remainingTowns`
    //  then noRepeat is false since if all the towns where
    //  used, noRepeat will be true because all values in
    //  remainingTowns will be -1
    if (remainingTowns[i] != -1){
      noRepeat = false;
      break;
    }
  }
  
  if (noRepeat != true){
    for (int i=0; i<genotypeLength; ++i){
      for (int j=0; j<genotypeLength; ++j){
        //  For every other index
        if (i!=j){
          //  Check if the value of i is repeated
          //  in these other indices
          int choice = remainingTowns[random(genotypeLength)];
          //  Make sure the random choice is not -1
          while (choice == -1){
            choice = remainingTowns[random(genotypeLength)];
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
}

void steadyStateGaMainStep()
{ /* pick three individuals a,b,c at random */

  //  Pick a and b randomly but from the range of inidivduals
  //  that perform well.
  //  So first, loop through fitness for each individual
  //  and get the index start and end range within which
  //  best and worst exist

  int fittestFirst = 0;
  int fittestSecond = 0;
  for (int i=0; i< numGenotypes;++i){
    if (fitness[i] >= fitness[fittestFirst]){
      fittestFirst = i;
    }
  }
  //  For second fittest
  for (int i=0; i<numGenotypes;++i){
    if (fitness[i] != fitness[fittestFirst]){
      if (fitness[i] >= fitness[fittestSecond]){
        fittestSecond = i;
      }
    }
    else{
      continue;
    }
  }
  
  //  Note bestFitness1 and bestFitness2 are index values
  int min = Math.min(fittestFirst, fittestSecond);
  int max = Math.max(fittestFirst, fittestSecond) + 1;
  int range = max - min;
  
  int a = min + random(range);
  int b = min + random(range);

  //  Pick C randomly
  int c = random(numGenotypes);
  while (c == a || c == b){
    c = random(numGenotypes);
  }

  /* reorder such that c is the least fit */
  //  a and b just have to be fitter than c
  //  Get the fitness for each individual
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