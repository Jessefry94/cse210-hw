using System;

class Program
{
    static void Main(string[] args)
    {
        // Console.WriteLine("Hello Prep4 World!");
        Console.WriteLine("Enter a list of numbers, type 0 when finished.");
        // Create a list of integers make sure to use "new" for the List
        List<int> numbers = new List<int>();
            // grab the list and append/add and we need to conver the 
            while (true)
            {
            Console.Write("Enter number: ");
            // we add console.readline to read the user input.
            string userInput = Console.ReadLine();
            // we use the parse method to help us convert the userinput which is a string to an int.
            int number = int.Parse(userInput);
            if (number == 0){
                break;
            }
            numbers.Add(number);
            }

            int sum = 0;
            foreach (int num in numbers){
                sum += num;
            }
            double average = ((float)sum) / numbers.Count;
            int maxNumber = numbers.Max();

            int smallestPostitiveNumber = 9999999;
            foreach (int num in numbers) {
                //&& means 'and'
                if (num < smallestPostitiveNumber && num >= 0){
                    smallestPostitiveNumber = num;
                }
            }

            numbers.Sort();
            Console.WriteLine("This is the sorted list: ");
            foreach (int num in numbers)
            {
                Console.WriteLine(num + "");
            }
            Console.WriteLine($"The sum is {sum}");
            Console.WriteLine($"The average is: {average:00}");
            Console.WriteLine($"The largest number is: {maxNumber}");
            Console.WriteLine($"The smallest positive number is: {smallestPostitiveNumber}");
            // numbers.add(int.Parse(console.readline())); (How to write on one line)
            // If we want to append something there are a few ways to do so. we can use 
            // the += operator to concatenate two different strings together
            // we can also use String.Concat(s1, s2) s1 could mean hello and s2 could mean world and they are put together.
    }
}