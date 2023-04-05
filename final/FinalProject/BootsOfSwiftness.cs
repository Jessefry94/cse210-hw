using System;

[Serializable]
public class BootsOfSwiftness
{
    public bool Equipped { get; private set; }

    public BootsOfSwiftness()
    {
        Equipped = false;
    }

    public void ToggleEquipped()
    {
        Equipped = !Equipped;
    }

    public int GetReflexBonus()
    {
        return Equipped ? 1 : 0;
    }
}
