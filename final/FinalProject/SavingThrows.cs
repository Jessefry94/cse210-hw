using System;
using System.Collections.Generic;

namespace CharacterCreation
{
    public class SavingThrows
    {
        public int Fortitude { get; private set; }
        public int Reflex { get; private set; }
        public int Will { get; private set; }
        public int Level { get; }

        public const int BaseFortitudeValue = 2;
        public const int BaseReflexValue = 0;
        public const int BaseWillValue = 0;

        private int BaseFortitude { get; }
        private int BaseReflex { get; }
        private int BaseWill { get; }
        private int ConstitutionModifier { get; }
        private int DexterityModifier { get; }
        private int WisdomModifier { get; }

        private BootsOfSwiftness BootsOfSwiftness { get; }
        private CloakOfResistance CloakOfResistance { get; }
        private PattyCakeByRadcliff PattyCakeByRadcliff { get; }
        private ArmedBravery ArmedBravery { get; }

        public Dictionary<string, List<string>> Sources { get; }

        public SavingThrows(int level, int fortitude, int reflex, int will, 
                            int dexterityModifier, int constitutionModifier, int wisdomModifier,
                            BootsOfSwiftness bootsOfSwiftness, CloakOfResistance cloakOfResistance, PattyCakeByRadcliff pattyCakeByRadcliff,
                            ArmedBravery armedBravery)
        {
            Level = level;
            BaseFortitude = fortitude;
            BaseReflex = reflex;
            BaseWill = will;
            ConstitutionModifier = constitutionModifier;
            DexterityModifier = dexterityModifier;
            WisdomModifier = wisdomModifier;

            BootsOfSwiftness = bootsOfSwiftness;
            CloakOfResistance = cloakOfResistance;
            PattyCakeByRadcliff = pattyCakeByRadcliff;
            ArmedBravery = armedBravery;

            Sources = new Dictionary<string, List<string>>()
            {
                { "fortitude", new List<string>() },
                { "reflex", new List<string>() },
                { "will", new List<string>() },
            };

            UpdateSavingThrowBonuses();
        }

        public void UpdateSavingThrowBonuses()
        {
            // Reset saving throws
            Fortitude = BaseFortitude + (Level / 2) + ConstitutionModifier;
            Reflex = BaseReflex + (Level / 3) + DexterityModifier;
            Will = BaseWill + (Level / 3) + WisdomModifier;

             // Add bonuses from Armed Bravery
            ArmedBravery.AddBonus(Level, this);

            // Add bonuses from equipped items
            if (BootsOfSwiftness.Equipped)
            {
                Reflex += BootsOfSwiftness.GetReflexBonus();
            }

            if (CloakOfResistance.Equipped)
            {
                int resistanceBonus = CloakOfResistance.GetResistanceBonus();
                Fortitude += resistanceBonus;
                Reflex += resistanceBonus;
                Will += resistanceBonus;
            }

            if (PattyCakeByRadcliff.Equipped)
            {
                Fortitude += PattyCakeByRadcliff.GetFortitudeBonus();
                Reflex += PattyCakeByRadcliff.GetReflexBonus();
                Will += PattyCakeByRadcliff.GetWillBonus();
            }
        }

        public void AddWillBonus(int bonus, string source)
        {
            Will += bonus;
            if (!Sources["will"].Contains(source))
            {
                Sources["will"].Add(source);
            }
        }

        public override string ToString()
        {
            string FormatSources(string save)
            {
                List<string> sources = new List<string>();

                if (ConstitutionModifier != 0 && save == "fortitude")
                    sources.Add($"Constitution Modifier: {ConstitutionModifier}");
                if (DexterityModifier != 0 && save == "reflex")
                    sources.Add($"Dexterity Modifier: {DexterityModifier}");
                if (WisdomModifier != 0 && save == "will")
                    sources.Add($"Wisdom Modifier: {WisdomModifier}");

                if (BootsOfSwiftness.Equipped && save == "reflex")
                    sources.Add($"Boots of Swiftness: {BootsOfSwiftness.GetReflexBonus()}");
                if (CloakOfResistance.Equipped)
                    sources.Add($"Cloak of Resistance: {CloakOfResistance.GetResistanceBonus()}");
                if (PattyCakeByRadcliff.Equipped)
                    sources.Add($"Patty Cake By Radcliff: {PattyCakeByRadcliff.GetFortitudeBonus()}");

                foreach (string source in Sources[save])
                {
                    sources.Add(source);
                }

                return $"{save}: {sources.Count} sources ({string.Join(", ", sources)})";
            }

            return $"Fortitude: {Fortitude} ({FormatSources("fortitude")})\n" +
                $"Reflex: {Reflex} ({FormatSources("reflex")})\n" +
                $"Will: {Will} ({FormatSources("will")})";
        }
    }
}
