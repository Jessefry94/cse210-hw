namespace CharacterCreation
{
    public abstract class Item
    {
        public string Name { get; }
        public string Description { get; }
        public bool Equipped { get; private set; }

        protected Item(string name, string description)
        {
            Name = name;
            Description = description;
            Equipped = false;
        }

        public virtual int GetArmorBonus() => 0;

        public virtual int GetAttackBonus() => 0;

        public virtual int GetReflexBonus() => 0;

        public virtual int GetResistanceBonus() => 0;

        // Added virtual methods for saving throw bonuses
        public virtual int GetFortitudeBonus() => 0;

        public virtual int GetWillBonus() => 0;

        public void ToggleEquipped() => Equipped = !Equipped;
    }
}
