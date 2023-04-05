using System;

[Serializable]
public class PattyCakeByRadcliff
{
    public bool Equipped { get; private set; }

    public PattyCakeByRadcliff()
    {
        Equipped = false;
    }

    public void ToggleEquipped()
    {
        Equipped = !Equipped;
    }

    public int GetFortitudeBonus()
    {
        return Equipped ? 2 : 0;
    }

    public int GetReflexBonus()
    {
        return Equipped ? 2 : 0;
    }

    public int GetWillBonus()
    {
        return Equipped ? 2 : 0;
    }
}
