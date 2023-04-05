// CharacterData.cs
using System;

namespace CharacterCreation
{
    [Serializable]
    public class CharacterData
    {
        public int Level { get; set; }
        public BootsOfSwiftness BootsOfSwiftness { get; set; }
        public CloakOfResistance CloakOfResistance { get; set; }
        public PattyCakeByRadcliff PattyCakeByRadcliff { get; set; }
    }
}
