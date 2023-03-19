using System.Collections.Generic; // Use for List

namespace ScriptureMemory
{
        // Personal note. Learn more about fields.
    class ScriptureFormatter
    {
        // This is a private fields meant to store the object from scripture hider
        private ScriptureHider _hider;

        // We have another constructor
        public ScriptureFormatter(ScriptureHider hider)
        {
            _hider = hider;
        }

        // We are using the method get current scripture using hidden words
        public string GetCurrentScripture(bool revealFirstLetters = false)
        {
            // Getting the hidden words from the list
            List<string> hiddenWords = _hider.GetHiddenWords();
            if (revealFirstLetters)
            {
            for (int i = 0; i < hiddenWords.Count; i++)
            {
                if (hiddenWords[i].Length > 0)
                {
                    hiddenWords[i] = _hider.GetOriginalWords()[i][0] + hiddenWords[i].Substring(1);
                }
            }
            }
            Scripture scripture = _hider.GetScripture();

            // Formatting so we can have the reference visable
            return $"{scripture.Reference}\n\n{string.Join(" ", hiddenWords)}";
        }
    }
}