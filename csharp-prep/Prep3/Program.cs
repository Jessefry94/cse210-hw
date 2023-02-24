using System;

class Program {
    static void Main(string[] args) {
        Console.WriteLine("Hello Prep3 World!");

        // Define a variable to store the player's response
        string playAgain;

        // Define a do-while loop to allow the player to play again
        do {
            // Generate a new random number and reset the guess count
            Random randomGenerator = new Random();
            int correctNumber = randomGenerator.Next(1, 101);
            int countGuesses = 0;
            int guess = -1;

            // Play the game until the player guesses correctly
            while (guess != correctNumber) {
                Console.WriteLine("What is your guess? ");
                guess = int.Parse(Console.ReadLine());
                countGuesses += 1;

                if (correctNumber > guess) {
                    Console.WriteLine("Guess Higher! ");
                }
                else if (correctNumber < guess) {
                    Console.WriteLine("Guess Lower! ");
                }
                else {
                    Console.WriteLine("You guessed correctly ");
                    Console.WriteLine($"You guessed {countGuesses} times");
                }
            }

            // Ask the player if they want to play again
            Console.WriteLine("Do you want to play again? (yes/no)");
            playAgain = Console.ReadLine();
        } while (playAgain.ToLower() == "yes");
    }
}
