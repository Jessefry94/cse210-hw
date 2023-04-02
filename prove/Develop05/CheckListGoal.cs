// We are using the System namespace to use the string and int types, and Console
using System;

namespace GoalTracker
{
    public class ChecklistGoal : Goal
    {
        public int Target { get; set; }
        public int BonusPoints { get; set; }

        public override void RecordProgress()
        {
            Progress++;
            Console.WriteLine($"Progress recorded for {Name}. Points earned: {Points}");

            // Check if the Progress has reached or exceeded the Target
            if (Progress >= Target)
            {
                Console.WriteLine($"Goal {Name} completed. Bonus points earned: {BonusPoints}");
            }
        }
    }
}
