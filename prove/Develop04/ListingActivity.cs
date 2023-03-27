using System;
using System.Collections.Generic;

namespace MindfulnessActivities
{
    // This is inheriting from the Activity base class
    class ListingActivity : Activity
    {
        // a list of prompts for the ListingActivity which inherits from the abstract Activity class
        // Note: abstraction is applying a universal behaviors from activity to listingactivity
        private static readonly List<string> Prompts = new List<string>
        {
            "Who are people that you appreciate?",
            "What are personal strengths of yours?",
            "Who are people that you have helped this week?",
            "When have you felt the Holy Ghost this month?",
            "Who are some of your personal heroes?"
        };

        // Constructor for the ListingActivity class
        // This is really important: We make it public so it can be called from outside the class
        // we use the base which is the base class "Activity" to set the name and the description
        public ListingActivity() : base("Listing Activity", "This activity will help you reflect on the good things in your life by having you list as many things as you can in a certain area.") { }

        // Override the Execute method of the base Activity class
        protected override void Execute()
        {
            // Creating a Random object to randomize
            var random = new Random();
            // This is how we grab a random prompt from the list of prompts
            string prompt = Prompts[random.Next(Prompts.Count)];
            // Print the selected prompt to the console
            Console.WriteLine(prompt);

            // Inform the user to think about the prompt for a few seconds
            Console.WriteLine("You have a few seconds to think about the prompt...");
            // Pause for 5 seconds
            Pause(5);

            // Create a list to store the items listed by the user
            List<string> items = new List<string>();

            // Prompt the user to start listing items
            Console.WriteLine("Start listing items:");

            // Record the current time as the start time. We are doing this to compare the starting time 
            // to the current time as time continues on. and then we use the users duration to see if the time frame has been met.
            DateTime startTime = DateTime.Now;
            // This allows the program to continue to accept inputs from the user until the specified duration has runs out.
            // We use .totalseconds to compare/convert to seconds.
            while ((DateTime.Now - startTime).TotalSeconds < Duration)
            {
                // Read an item from the user and store it in the list of items
                string item = Console.ReadLine();
                items.Add(item);
            }

            // Display the total number of items listed by the user
            Console.WriteLine($"You listed {items.Count} items:");
        }
    }
}
