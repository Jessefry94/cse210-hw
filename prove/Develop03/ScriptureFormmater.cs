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
        public string GetCurrentScripture()
        {
            // Getting the hidden words from the list
            List<string> hiddenWords = _hider.GetHiddenWords();
            // Getting the scripture object
            Scripture scripture = _hider.GetScripture();

            // Formatting so we can have the reference visable
            return $"{scripture.Reference}\n\n{string.Join(" ", hiddenWords)}";
        }
    }
}