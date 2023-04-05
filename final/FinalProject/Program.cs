using System;
using System.IO;
using Newtonsoft.Json;

namespace CharacterCreation
{
    
    class Program
    {
        static string SavePath = "characterData.json";

        static void SaveCharacterData(CharacterData characterData)
        {
            using (StreamWriter writer = new StreamWriter(SavePath))
            {
                string json = JsonConvert.SerializeObject(characterData, Formatting.Indented);
                writer.Write(json);
            }
        }

        static CharacterData LoadCharacterData()
        {
            if (File.Exists(SavePath))
            {
                using (StreamReader reader = new StreamReader(SavePath))
                {
                    string json = reader.ReadToEnd();
                    return JsonConvert.DeserializeObject<CharacterData>(json);
                }
            }
            else
            {
                return new CharacterData
                {
                    Level = 1,
                    BootsOfSwiftness = new BootsOfSwiftness(),
                    CloakOfResistance = new CloakOfResistance(),
                    PattyCakeByRadcliff = new PattyCakeByRadcliff()
                };
            }
        }

        static void Main(string[] args)
        {
            CharacterData characterData = LoadCharacterData();
            int choice;

            do
            {
                Console.WriteLine("Let's build your character!");
                Console.WriteLine("1. Change level");
                Console.WriteLine("2. Equip/Unequip items");
                Console.WriteLine("3. List current gear");
                Console.WriteLine("4. Save");
                Console.WriteLine("5. Load");
                Console.WriteLine("6. Exit");
                Console.Write("Enter your choice: ");
                choice = int.Parse(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        Console.Write("Enter your new level: ");
                        characterData.Level = int.Parse(Console.ReadLine());
                        break;
                    case 2:
                        ManageItems(characterData);
                        break;
                    case 3:
                        ListGear(characterData);
                        break;
                    case 4:
                        SaveCharacterData(characterData);
                        Console.WriteLine("Character data saved.");
                        break;
                    case 5:
                        characterData = LoadCharacterData();
                        Console.WriteLine("Character data loaded.");
                        break;
                    case 6:
                        Console.WriteLine("Exiting...");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            } while (choice != 6);
        }

        static void ManageItems(CharacterData characterData)
        {
            int itemChoice;

            do
            {
                Console.WriteLine("1. Equip/Unequip Boots of Swiftness");
                Console.WriteLine("2. Equip/Unequip Cloak of Resistance");
                Console.WriteLine("3. Equip/Unequip Patty Cake By Radcliff");
                Console.WriteLine("4. Change Cloak of Resistance bonus");
                Console.WriteLine("5. Back to main menu");
                Console.Write("Enter your choice: ");
                itemChoice = int.Parse(Console.ReadLine());

                switch (itemChoice)
                {
                    case 1:
                        characterData.BootsOfSwiftness.ToggleEquipped();
                        Console.WriteLine($"Boots of Swiftness: {(characterData.BootsOfSwiftness.Equipped ? "Equipped" : "Unequipped")}");
                        break;
                    case 2:
                        characterData.CloakOfResistance.ToggleEquipped();
                        Console.WriteLine($"Cloak of Resistance: {(characterData.CloakOfResistance.Equipped ? "Equipped" : "Unequipped")}");
                        break;
                    case 3:
                        characterData.PattyCakeByRadcliff.ToggleEquipped();
                        Console.WriteLine($"Patty Cake By Radcliff: {(characterData.PattyCakeByRadcliff.Equipped ? "Equipped" : "Unequipped")}");
                        break;
                    case 4:
                        ChangeCloakOfResistanceBonus(characterData.CloakOfResistance);
                        break;
                    case 5:
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            } while (itemChoice != 5);
        }

        static void ChangeCloakOfResistanceBonus(CloakOfResistance cloak)
        {
            Console.WriteLine("Current Cloak of Resistance bonus: " + cloak.GetResistanceBonus());
            Console.Write("Enter the new bonus (0-5): ");
            int newBonus = int.Parse(Console.ReadLine());

            if (newBonus >= 0 && newBonus <= 5)
            {
                while (cloak.GetResistanceBonus() != newBonus)
                {
                    if (cloak.GetResistanceBonus() < newBonus)
                    {
                        cloak.AddEnchantment();
                    }
                    else
                    {
                        cloak.RemoveEnchantment();
                    }
                }
                Console.WriteLine($"Cloak of Resistance bonus changed to {cloak.GetResistanceBonus()}");
            }
            else
            {
                Console.WriteLine("Invalid bonus value. Please try again.");
            }
        }
        static void ListGear(CharacterData characterData)
        {
            Console.WriteLine("Current gear:");
            Console.WriteLine($"Boots of Swiftness: {(characterData.BootsOfSwiftness.Equipped ? "Equipped" : "Unequipped")}");
            Console.WriteLine($"Cloak of Resistance: {(characterData.CloakOfResistance.Equipped ? "Equipped" : "Unequipped")}");
            Console.WriteLine($"Patty Cake By Radcliff: {(characterData.PattyCakeByRadcliff.Equipped ? "Equipped" : "Unequipped")}");
        }
    }
}