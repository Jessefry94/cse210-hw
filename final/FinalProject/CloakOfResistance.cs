// CloakOfResistance.cs
using System;

namespace CharacterCreation
{
    public class CloakOfResistance : Item
    {
        private int resistanceBonus;

        public CloakOfResistance() : base("Cloak of Resistance", "A magical cloak that increases the wearer's resistance.")
        {
            resistanceBonus = 0;
        }

        public override int GetResistanceBonus()
        {
            return resistanceBonus;
        }

        public void AddEnchantment()
        {
            if (resistanceBonus < 5)
            {
                resistanceBonus++;
            }
            else
            {
                Console.WriteLine("Maximum resistance bonus of 5 already reached.");
            }
        }

        public void RemoveEnchantment()
        {
            if (resistanceBonus > 0)
            {
                resistanceBonus--;
            }
            else
            {
                Console.WriteLine("Minimum resistance bonus of 0 already reached.");
            }
        }
    }
}
