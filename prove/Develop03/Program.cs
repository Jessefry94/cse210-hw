using System;
using System.Collections.Generic;
using System.Linq;

namespace ScriptureMemory
{
    class Program
    {
        static void Main(string[] args) 
        {
             List<Scripture> scriptureLibrary = new List<Scripture>
            {
                new Scripture("Proverbs 3:5-6", "Trust in the Lord with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths."),
                new Scripture("John 3:5", "Jesus answered, Verily, verily, I say unto thee, Except a man be born of water and of the Spirit, he cannot enter into the kingdom of God."),
                new Scripture("John 17:3", "And this is life eternal, that they might know thee the only true God, and Jesus Christ, whom thou hast sent."),
                new Scripture("1 Corinthians 15:20-22", "But now is Christ risen from the dead, and become the firstfruits of them that slept. For since by man came death, by man came also the resurrection of the dead. For as in Adam all die, even so in Christ shall all be made alive.")
                // Add more scriptures here
            };

            Random random = new Random();
            int randomIndex = random.Next(scriptureLibrary.Count);
            Scripture scripture = scriptureLibrary[randomIndex];
            
            // Combining scriptureformatter and scripture hidder to run a loop
            // Connecting the two objects together
            ScriptureHider hider = new ScriptureHider(scripture);
            
            // Connecting the two objects together
            ScriptureFormatter formatter = new ScriptureFormatter(hider);
            
            // I am using a loop to track the words that are hidden until no more words are hidden
            while (true)
            {
                // This will clear the console. Blank slate.
                Console.Clear();
                // This will grab my current scripture and display it in the console
                Console.WriteLine(formatter.GetCurrentScripture(hider.AllWordsHidden()));

                // Checking to see if all the words are hiden
                if (hider.AllWordsHidden())
                {
                    Console.WriteLine("\nAll words are hidden! Press any key to exit.");
                    // Use ReadKey to know when the user presses a key
                    Console.ReadKey();
                    // using break to exit the loop
                    break;
                }
                // If all the words are not hidden then we will continue 
                else
                {
                    Console.WriteLine("\nPress ENTER to hide a word.");
                    // This is really important. The loop is waiting for use to hit a button
                    // Once we hit a button then 
                    Console.ReadLine();
                    // The next word will be hidden
                    hider.HideNextWord();
                }
            }
        }
    }
}