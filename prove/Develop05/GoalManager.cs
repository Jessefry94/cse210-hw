// We include the System.Collections.Generic namespace to use List<>
using System.Collections.Generic;

namespace GoalTracker
{
    public class GoalManager
    {
        // Declare a public property of type List<Goal> to store the goals, and initialize it with an empty list
        public List<Goal> Goals { get; set; } = new List<Goal>();

        // Declare a public property of type int to store the total points earned
        public int TotalPoints { get; set; }

        // Make a Constructor for the GoalManager class
        public GoalManager()
        {
            // Initialize the Goals property with an empty list of goals
            Goals = new List<Goal>();
        }

        // AddGoal method to add a goal to the Goals list
        public void AddGoal(Goal goal)
        {
            // Add the specified goal to the Goals list
            Goals.Add(goal);
        }

        // Make the RecordEvent method public
        // Make a RecordEvent method to record progress for a goal and update the total points
        public void RecordEvent(int goalIndex)
        {
            // Get the goal at the specified index from the Goals list
            var goal = Goals[goalIndex];

            // Call the RecordProgress method of the goal to update its progress
            goal.RecordProgress();

            // Check if the goal is a ChecklistGoal to determine the current progress
            if (goal is ChecklistGoal checklistGoal)
            {
                // If the progress is equal to the target, add points and bonus points to the total points
                if (checklistGoal.Progress == checklistGoal.Target)
                {
                    // Adding the bonus points and progress points to the total
                    TotalPoints += checklistGoal.Points + checklistGoal.BonusPoints;
                }

                // If the progress is greater than the target, only add points to the total points
                // We don't want to give someone 500 points everytime they clean the dishes after they have met their long term goal
                else if (checklistGoal.Progress > checklistGoal.Target)
                {
                    TotalPoints += checklistGoal.Points;
                }
            }

            // If the goal is not a ChecklistGoal, add points to the total points
            else
            {
                TotalPoints += goal.Points;
            }
        }
        // Make a DeleteGoal method to remove a goal from the Goals list (Extra Credit)
        public void DeleteGoal(int goalIndex)
        {
            // Remove the goal at the specified index from the Goals list
            Goals.RemoveAt(goalIndex);
        }
    }
}
