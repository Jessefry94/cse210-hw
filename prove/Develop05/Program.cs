using System;
using System.IO;
using GoalTracker;

namespace GoalTracker
{
    class Program
    {
        static void Main(string[] args)
        {
            GoalManager goalManager = new GoalManager();

            while (true)
            {
                Console.WriteLine($"Total Points: {goalManager.TotalPoints}");
                Console.WriteLine("Select a choice from the menu:");
                Console.WriteLine("1. Create New Goal");
                Console.WriteLine("2. List Goals");
                Console.WriteLine("3. Save Goals");
                Console.WriteLine("4. Load Goals");
                Console.WriteLine("5. Record Event");
                Console.WriteLine("6. Quit");
                Console.WriteLine("7. Delete Goal");

                int choice = int.Parse(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        CreateNewGoal(goalManager);
                        break;
                    case 2:
                        ListGoals(goalManager);
                        break;
                    case 3:
                        SaveGoals(goalManager);
                        break;
                    case 4:
                        LoadGoals(goalManager);
                        break;
                    case 5:
                        RecordEvent(goalManager);
                        break;
                    case 6:
                        // Exit the program
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                    case 7:
                        DeleteGoal(goalManager);
                        break;
                }
            }
        }

        // This method creates a new goal based on user input
        private static void CreateNewGoal(GoalManager goalManager)
        {
            // Ask the user to select the goal type
            Console.WriteLine("Select goal type (1: Simple, 2: Eternal, 3: Checklist):");
            // We need to convert ("Parse") This way the number is associated with the variable type
            int goalType = int.Parse(Console.ReadLine());

            // Ask the user to input goal name
            Console.WriteLine("Enter goal name:");
            string name = Console.ReadLine();

            // Ask the user to input goal description
            Console.WriteLine("Enter goal description:");
            string description = Console.ReadLine();

            // Ask the user to input points earned per goal/event
            Console.WriteLine("Enter points earned per event:");
            int points = int.Parse(Console.ReadLine());

            Goal newGoal;

            // Create the goal based on the selected type
            switch (goalType)
            {
                case 1:
                    newGoal = new SimpleGoal { Name = name, Description = description, Points = points };
                    break;
                case 2:
                    newGoal = new EternalGoal { Name = name, Description = description, Points = points };
                    break;
                case 3:
                    // Ask the user to input target number of events for ChecklistGoal
                    Console.WriteLine("Enter target number of events:");
                    int target = int.Parse(Console.ReadLine());

                    // Prompt the user to input bonus points for ChecklistGoal
                    Console.WriteLine("Enter bonus points earned after reaching the target:");
                    int bonusPoints = int.Parse(Console.ReadLine());

                    newGoal = new ChecklistGoal { Name = name, Description = description, Points = points, Target = target, BonusPoints = bonusPoints };
                    break;
                default:
                    Console.WriteLine("Invalid goal type. Please try again.");
                    return;
            }
            // Add the new goal to the GoalManager
            goalManager.AddGoal(newGoal);
            Console.WriteLine($"Goal {name} created.");
        }

        // This method lists all goals in the GoalManager
        private static void ListGoals(GoalManager goalManager)
        {
            // Check if there are any goals
            if (goalManager.Goals.Count == 0)
            {
                Console.WriteLine("No goals created yet.");
                return;
            }
            // Iterate through each goal so we can display the details of each goal
            for (int i = 0; i < goalManager.Goals.Count; i++)
            {
                Goal goal = goalManager.Goals[i];
                string goalType = goal.GetType().Name;

                // If the goal is a ChecklistGoal, display progress as 'current progress/target'
                string progressDisplay;
                if (goal is ChecklistGoal checklistGoal)
                {
                    progressDisplay = $"{checklistGoal.Progress}/{checklistGoal.Target}";
                }
                else
                {
                    progressDisplay = $"{goal.Progress}";
                }

                // Check if the goal is completed
                ChecklistGoal checklistGoalForCompletionCheck = goal as ChecklistGoal;
                bool isGoalCompleted = (goal is SimpleGoal && goal.Progress > 0) || (checklistGoalForCompletionCheck != null && checklistGoalForCompletionCheck.Progress >= checklistGoalForCompletionCheck.Target);

                // This is how I display if a goal is completed or not
                // This is another way we can write if, else statments (Honestly can be confusing but keeping it here for learning purposes)
                string completionStatus = isGoalCompleted ? "[X]" : "[ ]";

                // The other way to write this which is a lot more normal to me.
                // string completionStatus;
                // if (isGoalCompleted)
                // {
                //     completionStatus = "[X]";
                // }
                // else
                // {
                //     completionStatus = "[ ]";
                // }

                // Print the goal details
                Console.WriteLine($"{completionStatus} [{i + 1}] {goalType}: {goal.Name} ({goal.Description}) - Points: {goal.Points}, Progress: {progressDisplay}");
            }
        }

        private static void SaveGoals(GoalManager goalManager)
        {
            // Defining the file path for the saved goals (Which I made automatic. Was having a few issues earlier so I decided I did this)
            // filePath and StreamWrite are very important for files and is connected to System.IO (Reminder)
            string filePath = "goals.txt";

            // Create a StreamWriter to write to the file
            using (StreamWriter writer = new StreamWriter(filePath))
            {
                // Write the total points to the file
                writer.WriteLine(goalManager.TotalPoints);

                // Write the number of goals to the file
                writer.WriteLine(goalManager.Goals.Count);

                // Iterate through all the goals
                foreach (Goal goal in goalManager.Goals)
                {
                    // Write the goal type SimpleGoal, EternalGoal, ChecklistGoal to the file
                    writer.WriteLine(goal.GetType().Name);

                    // Write the goal name, description, points, and progress to the file
                    writer.WriteLine(goal.Name);
                    writer.WriteLine(goal.Description);
                    writer.WriteLine(goal.Points);
                    writer.WriteLine(goal.Progress);

                    // If the goal is a ChecklistGoal we want to write the target and bonus points to the file
                    if (goal is ChecklistGoal checklistGoal)
                    {
                        writer.WriteLine(checklistGoal.Target);
                        writer.WriteLine(checklistGoal.BonusPoints);
                    }
                }
            }
            // Tell the user the goals have been saved to the file
            Console.WriteLine("Goals saved to file.");
        }

        private static void LoadGoals(GoalManager goalManager)
        {
            // This is the file path for the saved goals
            string filePath = "goals.txt";

            // Check if the file exists; if not, inform the user and return
            if (!File.Exists(filePath))
            {
                Console.WriteLine("File not found. Please save goals before attempting to load.");
                return;
            }

            // We need to create a StreamReader to read from the file
            using (StreamReader reader = new StreamReader(filePath))
            {
                // Read the total points from the file and then we will assign them to the goal manager
                goalManager.TotalPoints = int.Parse(reader.ReadLine());

                // Read the number of goals from the file
                int goalCount = int.Parse(reader.ReadLine());

                // Clear the current list of goals in the goal manager
                // This is really important to have. If we do not have this then we could end up with duplicates or other issues
                goalManager.Goals.Clear();

                // Iterate through all the goals in the file
                for (int i = 0; i < goalCount; i++)
                {
                    // We want to read the goal type, name, description, points, and progress from the file
                    string goalType = reader.ReadLine();
                    string name = reader.ReadLine();
                    string description = reader.ReadLine();
                    int points = int.Parse(reader.ReadLine());
                    int progress = int.Parse(reader.ReadLine());

                    // We need a variable to hold the loaded goal (Declaring a variable)
                    Goal loadedGoal;

                    // Create a new goal instance based on the goal type and fill its properties
                    switch (goalType)
                    {
                        case "SimpleGoal":
                            loadedGoal = new SimpleGoal { Name = name, Description = description, Points = points, Progress = progress };
                            break;
                        case "EternalGoal":
                            loadedGoal = new EternalGoal { Name = name, Description = description, Points = points, Progress = progress };
                            break;
                        case "ChecklistGoal":
                            int target = int.Parse(reader.ReadLine());
                            int bonusPoints = int.Parse(reader.ReadLine());
                            loadedGoal = new ChecklistGoal { Name = name, Description = description, Points = points, Progress = progress, Target = target, BonusPoints = bonusPoints };
                            break;
                        default:
                            Console.WriteLine("Invalid goal type found in the file. Skipping.");
                            continue;
                    }

                    // Add the loaded goal to the goal manager
                    goalManager.AddGoal(loadedGoal);
                }
            }

            Console.WriteLine("Goals loaded from file.");
        }

        private static void RecordEvent(GoalManager goalManager)
        {
            // Checking to see if there are any goals in the goal manager
            if (goalManager.Goals.Count == 0)
            {
                Console.WriteLine("No goals created yet.");
                return;
            }

            // Listing all the existing goals
            ListGoals(goalManager);

            // Ask the user to select a goal to record progress for
            Console.WriteLine("Enter the number of the goal you want to record progress for:");
            
            // Read the user input and convert it to an integer, then minus by 1 to use as an index
            // Super important to know/remember. 
            // When we display our ListGoals we are starting from 1 but when we are accessing our index (Elements in a list)
            // we are starting at 0. So, we are subtracting 1 from input value to match the index
            int goalIndex = int.Parse(Console.ReadLine()) - 1;

            // Checking if the provided index is within the range of the list of goals
            if (goalIndex < 0 || goalIndex >= goalManager.Goals.Count)
            {
                Console.WriteLine("Invalid goal number. Please try again.");
                return;
            }
            // Record the progress for the selected goal
            goalManager.RecordEvent(goalIndex);
            Console.WriteLine("Progress recorded.");
        }

        private static void DeleteGoal(GoalManager goalManager)
        {
            // Check if there are any goals in the goal manager
            if (goalManager.Goals.Count == 0)
            {
                Console.WriteLine("No goals created yet.");
                return;
            }

            // List all the existing goals
            ListGoals(goalManager);
            Console.WriteLine("Enter the number of the goal you want to delete:");

            // Read the user input and convert it to an integer, then minus by 1 to use as an index (Same as before)
            int goalIndex = int.Parse(Console.ReadLine()) - 1;

            // Checking if the provided index is within the correct range of the list of goals
            if (goalIndex < 0 || goalIndex >= goalManager.Goals.Count)
            {
                Console.WriteLine("Invalid goal number. Please try again.");
                return;
            }

            // Delete the selected goal
            goalManager.DeleteGoal(goalIndex);
            Console.WriteLine("Goal deleted.");
        }
    }
}
