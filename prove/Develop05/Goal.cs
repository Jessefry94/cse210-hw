// We are using the System namespace to use the string and int types
using System;

namespace GoalTracker
{
    // Declare an abstract class called Goal
    public abstract class Goal
    {
        // Declaring
        // Declare a public property of type string to store the goal's name
        public string Name { get; set; }

        // Declare a public property of type string to store the goal's description
        public string Description { get; set; }

        // Declare a public property of type int to store the points earned for the goal
        public int Points { get; set; }

        // Declare a public property of type int to store the progress of the goal
        public int Progress { get; set; }

        // Declare an abstract method called RecordProgress we are going to use no implementation
        // This method will be implemented by the derived classes to handle recording progress
        public abstract void RecordProgress();
    }
}
