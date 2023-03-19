namespace ScriptureMemory
{
    class Scripture
    // This class stores the reference and text
    {
        // This is how we auto implement properties
        public string Reference { get; private set; }
        public string Text { get; private set; }

        // Here we have the constructor taking two parameters reference and text
        public Scripture(string reference, string text)
        {
            Reference = reference;
            Text = text;
        }
    }
}