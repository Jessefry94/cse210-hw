using System;
using System.Collections.Generic; // Use for List and HashSet
using System.Linq; // Use for ToList()
namespace ScriptureMemory
{
    class ScriptureHider
    {
        // Setting things private
        private Scripture _scripture;
        private List<string> _words;
        private HashSet<int> _hiddenIndices;
        private Random _random;

        // class constructor
        public ScriptureHider(Scripture scripture)
        {
            // Initializing 
            _scripture = scripture;
            // Initializing and splitting the scripture texts into words for our list.
            _words = scripture.Text.Split(' ').ToList();
            // Using HashSet to store hidden words. 
            // Notes: Indices is a singular index of numeric values from a list or an array
            // This will allow the program to track which words are hidden in the index
            // HashSet is a O(1) constant. used for common operations such as adding, removing, or checking for elements
            _hiddenIndices = new HashSet<int>();
            // By adding this line of code I can improve the program by making the words randomize better.
            // selects the random words to hide
            _random = new Random();
        }

        // This is a method to hide the next word by grabbing grabbing a random index and adding it to hidden indices
        public void HideNextWord()
        {
            // I want to know if all the words are hidden
            if (AllWordsHidden()) return;

            // We need a variable so we will call it index
            int index;

            // This will be to find the random words that are not hidden using index
            do
            {
                index = _random.Next(_words.Count);
            } while (_hiddenIndices.Contains(index));

            // This will add the index to the hidden indices
            _hiddenIndices.Add(index);
        }

        // This will check if the words are hidden by comparing the count of hidden indices with the total count of words (This is a method)
        public bool AllWordsHidden()
        {
            return _hiddenIndices.Count == _words.Count;
        }

        // This is a method to get the hidden words and replace them with underscores
        public List<string> GetHiddenWords()
        {
            // This was tricky to switch things around. Important note.
            // We are creating a new list of words so that we can copy the original words
            List<string> currentWords = new List<string>(_words);

            // This is a loop to replace the hidden words with underscores
            foreach (int index in _hiddenIndices)
            {
                currentWords[index] = new string('_', _words[index].Length);
            }
            // Returning the list of hidden words
            return currentWords;
        }

        // Using a method to get the scripture object
        public Scripture GetScripture()
        {
            return _scripture;
        }
    }
}