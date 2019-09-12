import java.util.Scanner;
public class ChangeMaker
{
    public static void main(String[] args)
        {
            int firstNum, secondNum

            System.out.println("Enter in two numbers to be added together.");
            Scanner keyboard = new Scanner(System.in);
            firstNum = keyboard.nextInt();
            secondNum = keyboard.nextInt();

            answer = firstNum + secondNum;

            System.out.println("The answer is:" + answer);

        }
}