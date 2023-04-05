namespace CharacterCreation
{
    public class ArmedBravery
    {
        public bool Equipped { get; private set; }
        public int Bonus { get; private set; }

        private int[] Levels = { 2, 6, 10, 14, 18 };

        public ArmedBravery()
        {
            Equipped = true;
            Bonus = 0;
        }

        public void AddBonus(int level, SavingThrows savingThrows)
        {
            if (Equipped)
            {
                int count = Levels.Length;
                for (int i = 0; i < count; i++)
                {
                    if (Levels[i] > level)
                    {
                        count = i;
                        break;
                    }
                }

                Bonus = count;
                savingThrows.AddWillBonus(Bonus, $"Armed Bravery Bonus ({Bonus})");
            }
        }

        public void ToggleEquipped() => Equipped = !Equipped;
    }
}
