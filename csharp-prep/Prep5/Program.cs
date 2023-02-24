using System;

class Program
{
    static void Main(string[] args)
    {
        DisplayWelcomeMessage(); // Display a welcome message to the user

        string userName = PromptUserName(); // Prompt the user for their name
        int userNumber = PromptUserNumber(); // Prompt the user for their favorite number

        int squaredNumber = SquareNumber(userNumber); // Calculate the square of the user's number

        DisplayResult(userName, squaredNumber); // Display the results to the user
        Console.WriteLine("Hello Prep5 World!");
    }

    static void DisplayWelcomeMessage()
    {
        Console.WriteLine("Welcome to the program!"); // Display a welcome message to the user
    }

    static string PromptUserName()
    {
        Console.Write("Please enter your name: "); // Prompt the user for their name
        string name = Console.ReadLine(); // Read the user's name from the console

        return name; // Return the user's name
    }

    static int PromptUserNumber()
    {
        Console.Write("Please enter your favorite number: "); // Prompt the user for their favorite number
        int number = int.Parse(Console.ReadLine()); // Read the user's number from the console and convert it to an integer

        return number; // Return the user's number
    }

    static int SquareNumber(int number)
    {
        int square = number * number; // Calculate the square of the input number
        return square; // Return the square
    }

    static void DisplayResult(string name, int square)
    {
        Console.WriteLine($"{name}, the square of your number is {square}"); // Display the results to the user
    }
}
