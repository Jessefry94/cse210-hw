using System;

namespace MindfulnessActivities
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Mindfulness Activities!");
            Console.WriteLine("Choose an activity:");
            Console.WriteLine("1. Breathing");
            Console.WriteLine("2. Reflection");
            Console.WriteLine("3. Listing");
            Console.WriteLine("4. Exit");

            int choice = int.Parse(Console.ReadLine());
            Activity activity;

            switch (choice)
            {
                case 1:
                    activity = new BreathingActivity();
                    break;
                case 2:
                    activity = new ReflectionActivity();
                    break;
                case 3:
                    activity = new ListingActivity();
                    break;
                case 4:
                    Console.WriteLine("Exiting.");
                    return;
                default:
                    Console.WriteLine("Invalid choice. Exiting.");
                    return;
            }

            activity.Start();
        }
    }
}
