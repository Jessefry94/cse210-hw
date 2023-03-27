using System;
using System.Threading;

namespace MindfulnessActivities
{
    // Defining the abstract base class called Activity
    abstract class Activity
    {
        // Define class properties
        protected string Name;
        protected string Description;
        protected int Duration;

        // Constructor for the Activity class, which takes a name and a description as parameters
        protected Activity(string name, string description)
        {
            // Assign the name and description to the class properties
            Name = name;
            Description = description;
        }

        // Public method to start the activity
        public void Start()
        {
            // Print the name and description of the activity
            Console.WriteLine($"{Name}\n{Description}");
            // Ask the user for the duration of the session in seconds
            Console.Write("How long, in seconds, would you like your session? ");
            // Parse the user input as an integer and store it in the Duration property
            Duration = int.Parse(Console.ReadLine());

            // Call the Prepare method
            Prepare();
            // Call the execute method
            Execute();
            // Call the Finish method
            Finish();
        }

        protected abstract void Execute();

        // Method to prepare the user for the activity
        protected void Prepare()
        {
            // This will print in prearation for each activity
            Console.WriteLine("Prepare to begin...");
            // Pause for 5 seconds
            Pause(5);
        }

        // Method to finish the activity
        protected void Finish()
        {
            // Giving them encouraging words
            Console.WriteLine("Good job!");
            // Inform the user about the completion of the activity and its duration
            Console.WriteLine($"You have completed {Name} for {Duration} seconds.");
            // Pause for 5 seconds
            Pause(5);
        }

        // Method to pause. We are using this for prepare and finish so that we can create a time frame program
        protected void Pause(int seconds)
        {
            // Loop for the specified number of seconds
            for (int i = 0; i < seconds; i++)
            {
                // This is how we let the user know the program is running every second with a new dot
                Console.Write(".");
                // Sleep pasuing the program and we have it set to count by 1 second.
                Thread.Sleep(1000);
            }
            // This is how we see that the program is working each second.
            Console.WriteLine();
        }
    }
}
