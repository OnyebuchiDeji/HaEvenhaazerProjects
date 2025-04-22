import java.util.Random;
class adcHintonNowlan {

final int numGenotypes      = 1000;
final int genotypeLength    = 20;
final int numLearningTrials = 1000;
final int numGenerations    = 50;

Random rng = new Random();
int random(int n) { return rng.nextInt(n); } // random integer between 0 and n-1

final int zero=0, one=1, questionMark=2;

int genotypes[][] = new int[numGenotypes][genotypeLength];
int fitness[] = new int[numGenotypes];
// fitness = 1000*"1+19n/1000" where n = number of learning trials remaining
//           or rather numLearningTrials + 19 * n

void calculateFitnessArray() // calculate fitness[] *YOU DO NOT NEED TO UNDERSTAND THIS*
{ for (int i=0;i<numGenotypes;i++)
  { int numTrialsRemaining;
    for (numTrialsRemaining=numLearningTrials;numTrialsRemaining>0;numTrialsRemaining--)
    { int g;
      for (g=0;g<genotypeLength;g++)
        if (genotypes[i][g]==zero || (genotypes[i][g]==questionMark&&random(2)==0))
          break;
      if (g==genotypeLength) break;
    }
    fitness[i] = numLearningTrials + 19 * numTrialsRemaining;
  }
}

void nextGeneration()
{ calculateFitnessArray();

  int sumFitness=0; for (int i=0;i<numGenotypes;i++) sumFitness += fitness[i];
  int newGenotypes[][] = new int[numGenotypes][genotypeLength];
  for (int i=0;i<numGenotypes;i++) // for each new genotype
  { int parentA, parentB;

    // Select parents for reproduction.
    // The probability of a parent being selected should be proportional to its fitness.
    // Hint: calculating random(sumFitness) will help

    BBBB

    int cutPoint = 1+random(genotypeLength-1);

    // Crossover: newGenotypes[i] should copy genes before the cut point from
    // genotypes[parentA] and the from the cut point on from genotypes[parentB]

    CCCC
  }
  for (int i=0;i<numGenotypes;i++)
    for (int g=0;g<genotypeLength;g++) genotypes[i][g] = newGenotypes[i][g];
}

void outputStatistics(int generation)
{ int counters[] = new int[3];
  counters[0]=counters[1]=counters[2]=0;

  for (int i=0;i<numGenotypes;i++) for (int g=0;g<genotypeLength;g++) counters[(int)genotypes[i][g]]++;

  double d=numGenotypes*genotypeLength;
  System.out.println(""+generation+" "+counters[0]/d+" "+counters[1]/d+" "+counters[2]/d);
}

void run()
{ for (int i=0;i<numGenotypes;i++) for (int g=0;g<genotypeLength;g++) switch (random(4))
  { case 0 : genotypes[i][g] = zero         ; break; //25%
    case 1 : genotypes[i][g] = one          ; break; //25%
    default: genotypes[i][g] = questionMark ; break; //50%
  }
  outputStatistics(0);
  for (int generation=1;generation<=numGenerations;generation++)
  { nextGeneration();
    outputStatistics(generation);
  }
}

public static void main(String args[])
{ new adcHintonNowlan().run();
}

}