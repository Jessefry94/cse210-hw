// These are key features for the program. 
// Importing the System imports namespace and other c# basics
using System; 
// Contains generic collection classes like List<T>
using System.Collections.Generic;
// Allows us to use namespace for reading and writing to files
using System.IO;
// Updated ?
namespace DailyJournal
{
    class Entry
    {
        // Read only propertys that return the prompt
        public string Prompt {get;}
        public string Response {get;}
        public string Date {get;}
        public string Mood {get;}

        //Constructor to initialize prompt, response and date (Note:Learn more about initializing)
        public Entry(string prompt, string response, string date, string mood)
        {
            Prompt = prompt;
            Response = response;
            Date = date;
            Mood = mood;
        }
    
        // Override ToString method to get formatted string representation of Entry object
        public override string ToString()
        {
            return $"{Date} - {Prompt}: {Response} ({Mood})";
        }
    }

    // Constructor to initialize entries
    class Journal
    {
        private List<Entry> _entries;

        public Journal()
        {
            _entries = new List<Entry>();
        }

        // AddEntry method to add new entry to journal with provided prompt, response and today's date
        public void AddEntry(string prompt, string response, string mood)
        {
            // Get todays date
            string date = DateTime.Today.ToString("d");
            // create a new Entry object
            Entry entry = new Entry(prompt, response, date, mood);
            // Add the Entry object to the list of entries
            _entries.Add(entry);
        }

        // DisplayEntries method to iterate through all entries in the journal and display them
        public void DisplayEntries()
        {
            // Iterating through list of entries
            foreach (Entry entry in _entries)
            {
                // Print all Entrys to console
                Console.WriteLine(entry);
            }
        }

        // SaveToFile method to save current journal (entries list) to provided file name
        public void SaveToFile(string filename)
        {
            // Open file writer object
            using (StreamWriter writer = new StreamWriter(filename))
            {
                foreach (Entry entry in _entries)
                {
                    writer.WriteLine($"{entry.Prompt}|{entry.Response}|{entry.Date}|{entry.Mood}");
                }
            }
        }

        // LoadFromFile method to load entries from provided file name and replace any entries currently stored in the journal
        public void LoadFromFile(string filename)
        {
            // Clear the enteries list
            _entries.Clear();
            // Open the file reader object
            using (StreamReader reader = new StreamReader(filename))
            {
                string line;
                // Read each line of file until there are none left.
                while ((line = reader.ReadLine()) != null)
                {
                    // Splitting 
                    string[] fields = line.Split('|');
                    // Looking for all 3 prompts
                    if (fields.Length == 4)
                    {
                        // Grabbing the prompts from all 4
                        string prompt = fields[0];
                        string response = fields[1];
                        string date = fields[2];
                        string mood = fields[3];
                        Entry entry = new Entry(prompt, response, date, mood);
                        _entries.Add(entry);
                    }
                }
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Journal journal = new Journal();

            string[] prompts = {
                "What did I learn from class today?",
                "What was the best part of my day?",
                "Name three things that I love?",
                "How am I taking care of myself today?",
                "If I had one thing I could do over today, what would it be?"
            };
            // This names and tracts to see if the user quits
            bool done = false;
            // Loop until the user quits.
            while (!done)
            {
                Console.WriteLine("Daily Journal\n");
                Console.WriteLine("1. Write a new entry");
                Console.WriteLine("2. Display the journal");
                Console.WriteLine("3. Save the journal to a file");
                Console.WriteLine("4. Load the journal from a file");
                Console.WriteLine("5. Quit\n");

                Console.Write("Enter your choice (1-5): ");
                string choice = Console.ReadLine();
                // This allows us to switch between the users choices of 1-5
                switch (choice)
                {
                    case "1":
                        string prompt = prompts[new Random().Next(prompts.Length)];
                        Console.WriteLine($"Prompt: {prompt}");
                        Console.Write("Response: ");
                        string response = Console.ReadLine();
                        Console.Write("Mood: ");
                        string mood = Console.ReadLine();
                        // Object.Method(arguments) (This is known as a method call or function call)
                        journal.AddEntry(prompt, response, mood);
                        Console.WriteLine("Entry added.\n");
                        break;

                    case "2":
                        Console.WriteLine("Journal entries:\n");
                        journal.DisplayEntries();
                        Console.WriteLine();
                        break;

                    case "3":
                        Console.Write("Enter filename to save to: ");
                        string saveFilename = Console.ReadLine();
                        journal.SaveToFile(saveFilename);
                        Console.WriteLine("Journal saved.\n");
                        break;

                    case "4":
                        Console.Write("Enter filename to load from: ");
                        string loadFilename = Console.ReadLine();
                        journal.LoadFromFile(loadFilename);
                        Console.WriteLine("Journal loaded.\n");
                        break;

                    case "5":
                        done = true;
                        break;
                default:
                    Console.WriteLine("Invalid choice. Try again.\n");
                    break;
                }
            }
        }
    }
}