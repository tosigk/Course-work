/*
 NOTE: You CANNOT import ANY other classes or packages!

 NOTE: You CANNOT change the names of any of the existing methods,
 variables, or constants!  Also, you CANNOT add any methods, nor can
 you add/remove any parameters to the existing methods.

 NOTE: You CANNOT add any other classes to this assignment/project.
 There are only two classes: Dice.java and TestDice.java (this
 file).  Dice.java is already written for you and must be used in
 your solution unchanged.

 NOTE: You CANNOT modify the main method below.  It is already
 completely written for you.

 Violating any of the rules above will incur a severe point penalty!

 Your assignment is to complete the code within the three methods
 below so that your program creates a histogram of dice rolls, given
 numits and maxheight (see main method below).  See example output
 in the two image files: out1.jpg and out2.jpg.

 A grade (out of 10 points) will be assessed based on the output
 results of your program, for one or more example inputs (numits,
 maxheight).  The weight in points of each of the three methods is
 listed beside each method you will be writing (see below).  Of
 course, violating the rules above will also affect your grade.
*/
//Giuliana Tosi, 221 (02), 1/31/2019

public class TestDice 
{
    // declare an array attribute (member variable) for frequency of dice rolls
    // (Think also about how big it needs to be)
    int[] diceRolls;  //the array for how many times the dice are rolled
    
    // for a short description of arrays, see:
    //   https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html

    // NOTE:  No other attributes are necessary.
    
    // write a method to perform a simulation of numits rolls of the dice
    public void doSim(int numits)  // 3 points
    {
	// initialize frequency counters to zeros
	diceRolls = new int[11];  //Dice can roll 11 different combinations (2-12)
	for (int i=0; i <= 10; i++)  //counts from 0-10 which includes all 11 combinations
	{
		diceRolls[i] = 0;
	}

	// simulate numits rolling of the dice and track the frequencies:
	//   first, construct a Dice (pair of dice) object
	Dice twoDie = new Dice();  //retrieves data from Dice.java and renamed it twoDie
	
	//   second, roll the dice numits times and record the number of
	//   times each value is rolled in the frequency array, freq
	for (int i=numits; i>0; i--)  //for loop to count how many times each value is rolled
	{
		twoDie.roll();                     //rolls the dice
		int rollValue = twoDie.getSum();  //calculates sum of dice 
		diceRolls[rollValue - 2] += 1;   //subtracts two to get position of dice value and adds one to the frequency
	}
	
    }

    // write a method to find the maximum frequency value in the freq array
    public int maxFreq()  // 2 points
    {
	// initialize a maximum frequency variable
	int maxFrequency = 0;
	
	// go through each element of freq and update max if value is larger
	for (int i=0; i <= 10; i++)  //for loop to determine what value has the max number of times it was rolled
	{
		int currentFreq = diceRolls[i];   //initialize a current freq so I can compair to the current maxFreq
		if (maxFrequency < currentFreq)
		{
			maxFrequency = currentFreq;   //establishes the new maxFrequency by equaling current freq to max freq
		}
	}
	// return the maximum frequency
	return maxFrequency;

    }

    // output a histogram of maxheight stars (*) using the frequency array
    public void doHist(int maxheight)  // 5 points
    {
	final int MAXFREQ = maxFreq();           // get maximum frequency
	final int FPS = MAXFREQ / maxheight + 1; // FPS = Frequency Per Star (increment per row)

	// output histogram from the top, down
	
	// HINT:  you will need a nested loop
	for (int i = MAXFREQ; i > FPS; i -= FPS)   //outer loop to print each row
	 {
	 	System.out.printf("%" + Integer.toString(MAXFREQ).length() + "d", i);
	 	for (int c = 0; c <= 10; c++)//c = collumn as it is inner loop to write each collum row by row
	 	{
	 		if (i <= diceRolls[c])
	 		{
	 			System.out.print(" ***");   //if value number is in the row of freq, then print *** 
	 		}	
	 		else
	 		{
	 			System.out.print("    ");  //if value number is not in the freq row, then print nothing because its frequency is lower
	 		}
	 	}	
	 	System.out.println();   // prints y-axis (max freq intervals)
	 }
	 for (int i = 0; Integer.toString(MAXFREQ).length() > i; i++)
	 {
	 	System.out.print(" ");
	 }
	 System.out.println("  2   3   4   5   6   7   8   9  10  11  12 ");   //prints x-axis (value of rolled dice)
	// in addition to System.out.print() and System.out.println()
	// a useful output method is (as an example):
	//    System.out.printf("%8d", f);
	//
	// this will print the value of (int) f, right justified in a
	// field width of 8.  For more information on printf, see here:
	//   https://docs.oracle.com/javase/tutorial/java/data/numberformat.html
    }

    public static void main(String[] args) {
	// for more on command-line arguments, see here:
	// https://docs.oracle.com/javase/tutorial/essential/environment/cmdLineArgs.html
	if (args.length != 2) {
	    System.out.println("USAGE: java TestDice <numits> <maxheight>");
	    return;
	}
	// get command-line arguments, convert to int, and store
	int numits = Integer.parseInt(args[0]);
	int maxheight = Integer.parseInt(args[1]);

	TestDice td = new TestDice();	// create a TestDice object
	
	td.doSim(numits);         // run simulation
	td.doHist(maxheight);     // output histogram of maxheight
    }
}
