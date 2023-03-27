using System;
using System.Collections.Generic;

namespace MindfulnessActivities
{
    // ReflectionActivity class, which inherits from the abstract Activity class
    // Note: abstraction is applying a universal behaviors from activity to reflection
    class ReflectionActivity : Activity
    {
        // A list of prompts for the reflection activity
        private static readonly List<string> Prompts = new List<string>
        {
            "Think of a time when you stood up for someone else.",
            "Think of a time when you did something really difficult.",
            "Think of a time when you helped someone in need.",
            "Think of a time when you did something truly selfless."
        };

        // A list of questions for the reflection activity
        private static readonly List<string> Questions = new List<string>
        {
            "Why was this experience meaningful to you?",
            "Have you ever done anything like this before?",
            "How did you get started?",
            "How did you feel when it was complete?",
            "What made this time different than other times when you were not as successful?",
            "What is your favorite thing about this experience?",
            "What could you learn from this experience that applies to other situations?",
            "What did you learn about yourself through this experience?",
            "How can you keep this experience in mind in the future?"
        };

        // A list to track unused questions
        private List<string> unusedQuestions;

        // Constructor for the ReflectionActivity class
        // This is really important: We make it public so it can be called from outside the class
        // we use the base which is the base class "Activity" to set the name and the description
        public ReflectionActivity() : base("Reflection Activity", "This activity will help you reflect on times in your life when you have shown strength and resilience. This will help you recognize the power you have and how you can use it in other aspects of your life.")
        {
            // We create a new instance of the List<string> and we put the questions in as an argument allowing 
            // us to have the same list as the questions being used. So we can track which questions have been used.
            unusedQuestions = new List<string>(Questions);
        }

        // Override the Execute method of the base Activity class
        protected override void Execute()
        {
            // random number generator
            var random = new Random();
            
            // This selects a random prompt from the Prompts list
            string prompt = Prompts[random.Next(Prompts.Count)];
            
            // This prints the prompt to the console
            Console.WriteLine(prompt);
            Console.WriteLine("When you have something in mind, press enter to continue.");
            
            // Wait for the user to press enter before continuing since they had this in the example
            Console.ReadLine();

            // Write a message about pondering on the questions
            Console.WriteLine("Now ponder on each of the following questions as they relate to this experience.");
            
            // Pause for 5 seconds before displaying the questions
            Pause(5);
            
            // Calculate the number of questions to display based on the user-defined duration
            // I did this because all the questions were shooting out every second so I did this to solve that issue
            int questionDuration = 10;
            int questionCount = Duration / questionDuration;

            // Loop through the number of questions to display
            for (int i = 0; i < questionCount; i++)
            {
                // Check if there are no more unused questions
                if (unusedQuestions.Count == 0)
                {
                    // If so, add all questions back to the unusedQuestions list
                    // I wasn't sure if this was the best way to solve this issue or if I needed to. I was looking into Shuffle.
                    // If you have any advise on how I should use shuffle please let me know. Thanks.
                    unusedQuestions.AddRange(Questions);
                }

                // We are using the random generator with a next method to select a random number (the Index) (Which this number is a question) from the unusedQuestions list
                int index = random.Next(unusedQuestions.Count);
                
                // This grabs/retrieves the question at the selected index/number
                string question = unusedQuestions[index];
                
                // We then Remove the question from the unusedQuestions list
                unusedQuestions.RemoveAt(index);

                // Write the selected question to the console
                Console.WriteLine(question);
                
                // Pause before displaying the next question
                Pause(questionDuration);
            }
        }
    }
}
