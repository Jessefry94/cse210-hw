using System;

namespace GoalTracker
{
    public class EternalGoal : Goal
    {
        public override void RecordProgress()
        {
            Progress++;
            Console.WriteLine($"Progress recorded for {Name}. Points earned: {Points}");
        }
    }
}
