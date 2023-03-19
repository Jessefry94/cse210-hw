using System;
using System.Collections.Generic;
using System.Linq;

namespace ScriptureMemory
{
    class Program
    {
        static void Main(string[] args) 
        {
            // This is where we Instantiate 
            // Connecting scripture with the reference and text
            Scripture scripture = new Scripture("Proverbs 3:5-6", "Trust in the Lord with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths.");
            
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
                Console.WriteLine(formatter.GetCurrentScripture());

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