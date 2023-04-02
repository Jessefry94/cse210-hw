// We Import the System namespace to access the Console class
using System;

namespace GoalTracker
{
    // Declaring the SimpleGoal class, which is derived from the Goal class
    public class SimpleGoal : Goal
    {
        // Override the RecordProgress method from the base class (Goal)
        public override void RecordProgress()
        {
            // Increment the Progress property by 1
            // This is tracking our progress for our goals
            Progress++;

            // Another way to write this that can be easier to understand is
            // Progress = Progress + 1;

            Console.WriteLine($"Progress recorded for {Name}. Points earned: {Points}");
        }
    }
}
