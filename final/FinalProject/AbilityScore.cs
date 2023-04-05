using System;

namespace CharacterCreation
{
    public class AbilityScore
    {
        public int BaseScore { get; private set; }
        public int Modifier => (BaseScore - 10) / 2;

        public AbilityScore(int baseScore)
        {
            BaseScore = baseScore;
        }
    }
}
