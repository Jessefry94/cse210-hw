using System;

namespace MindfulnessActivities
{
    // Defining my class
    // This is inheriting from the Activity base class
    class BreathingActivity : Activity
    {
        // Constructor for the BreathingActivity class
        // This is really important: We make it public so it can be called from outside the class
        // we use the base which is the base class "Activity" to set the name and the description
        public BreathingActivity() : base("Welcome to the Breathing Activity", "This activity will help you relax by walking your through breathing in and out slowly. Clear your mind and focus on your breathing.") { }

        // We need to Override the Execute method from the Activity base class so we can add
        // Our own/additional code to this activity
        // note: the execute method is called at the start from the program file and this overrides.
        protected override void Execute()
        {
            // Loop through based on the the time put in by the user for Duration divided by 10 for breaths
            for (int i = 0; i < Duration / 10; i++)
            {
                Console.WriteLine("Breathe in...");
                Pause(5);

                Console.WriteLine("Breathe out...");
                Pause(5);
            }
        }
    }
}
