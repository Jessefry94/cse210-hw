import random
# I am putting this here for your own entertainment purposes. To show you what I have been working on

level = 11
feat_armor_training = True
weapon_focus = 1
weapon_training = True
sword_enchantment_level = 1
belt_of_strength_level = 1
focused_weapon = level
weapon_specialization = 2
power_attack = True

strength_score = 20
dexterity_score = 12
constitution_score = 18
intelligence_score = 14
wisdom_score = 10
charisma_score = 6

def calculate_strength_score(belt_of_strength_level, strength_score):
    strength_score = strength_score
    if belt_of_strength_level == 1:
        strength_score += 2
    elif belt_of_strength_level == 2:
        strength_score += 4
    elif belt_of_strength_level == 3:
        strength_score += 6

    return strength_score
# Update strength_score variable with calculated score including belt of strength
strength_score = calculate_strength_score(belt_of_strength_level, strength_score)

ability_scores = [strength_score, dexterity_score, constitution_score, intelligence_score, wisdom_score, charisma_score]
ability_modifiers = [(score - 10) // 2 for score in ability_scores]
strength_modifier, dexterity_modifier, constitution_modifier, intelligence_modifier, wisdom_modifier, charisma_modifier = ability_modifiers

def calculate_initiative_modifier(dexterity_modifier, d20_roll):
    return dexterity_modifier + d20_roll

class HitPoints:
    def __init__(self, level, constitution_modifier):
        self.level = level
        self.constitution_modifier = constitution_modifier
    
    def calculate(self):
        return (self.level * 1) + (self.constitution_modifier * level) + (6 * self.level)
    
    # def print(self):
    #     print("Hit points:", self.calculate())

hit_points = HitPoints(level, constitution_modifier)


d20_roll = random.randint(1, 20)
initiative = calculate_initiative_modifier(dexterity_modifier, d20_roll)

class ArmedBravery:
    def __init__(self):
        self.equipped = True
        self.levels = [2, 6, 10, 14, 18]
        self.bonus = 0
        self.sources = {"will": []}

    def add_bonus(self, level, saving_throws):
        if self.equipped:
            level = sum(1 for l in self.levels if l <= level)
            bonus = level * 1
            self.bonus = bonus
            self.sources["will"].append(f"bravery bonus({bonus})")
            saving_throws.add_will_bonus(self.bonus, self.sources["will"])

    def toggle_equipped(self):
        self.equipped = not self.equipped

armed_bravery = ArmedBravery()

class BootsOfSwiftness:
    def __init__(self):
        self.equipped = False

    def get_armor_bonus(self):
        if self.equipped:
            return 1
        return 0

    def get_cmd_bonus(self):
        if self.equipped:
            return 1
        return 0

    def get_attack_bonus(self):
        if self.equipped:
            return 1
        return 0
    
    def get_armor_check_penalty(self):
        return 0

    def get_reflex_bonus(self):
        if self.equipped:
            return 1
        return 0

    def __str__(self):
        if self.equipped:
            boots_str = "Name: {}\nArmor Bonus: +{}\nReflex Bonus: +{}\nAttack Bonus: +{}"
            return boots_str.format("Boots of Swiftness", self.get_armor_bonus(), self.get_reflex_bonus(), self.get_attack_bonus())
        else:
            return "Boots of Swiftness are unequipped"

    def toggle_equipped(self):
        self.equipped = not self.equipped

my_boots_of_swiftness = BootsOfSwiftness()

class CloakOfResistance:
    def __init__(self):
        self.equipped = True
        self.enchantment_bonus = 0
        self.max_enchantment_bonus = 5

    def get_resistance_bonus(self):
        if self.equipped:
            return self.enchantment_bonus
        return 0

    def toggle_equipped(self):
        self.equipped = not self.equipped

    def add_enchantment(self):
        if self.enchantment_bonus < 5:
            self.enchantment_bonus += 1

    def __str__(self):
        if self.equipped:
            return f"Cloak of Resistance: +{self.enchantment_bonus} towards all saving throws."
        else:
            return "Cloak of Resistance unequipped"

cloak_of_resistance = CloakOfResistance()

for i in range(2):#This determines the level enchantment
    cloak_of_resistance.add_enchantment()

class PattyCakeByRadcliff:
    def __init__(self):
        self.equipped = True

    def get_resistance_bonus(self):
        if self.equipped:
            return 2
        return 0

    def toggle_equipped(self):
        self.equipped = not self.equipped

    def __str__(self):
        if self.equipped:
            return "Patty Cake By Radcliff: +2 towards all saving throws."
        else:
            return "Patty Cake By Radcliff unequipped"

patty_cake_by_radcliff = PattyCakeByRadcliff()

class SavingThrows:
    def __init__(self, level, fortitude, reflex, will, dexterity_modifier, constitution_modifier, wisdom_modifier, armed_bravery, my_boots_of_swiftness, cloak_of_resistance, patty_cake_by_radcliff):
        self.fortitude = fortitude + 2 + (level // 2) + constitution_modifier
        self.reflex = reflex + (level // 3) + dexterity_modifier
        self.will = will + (level // 3) + wisdom_modifier
        self.dexterity_modifier = dexterity_modifier
        self.constitution_modifier = constitution_modifier
        self.wisdom_modifier = wisdom_modifier
        self.sources = {"fortitude": ["base (+2) + (level // 2)", f"ability modifier({constitution_modifier})"], 
                        "reflex": ["base (0) + (level // 3)", f"ability modifier({dexterity_modifier})"], 
                        "will": ["base (0) + (level // 3)", f"ability modifier({wisdom_modifier})"]}

        armed_bravery.add_bonus(level, self)

        self.my_boots_of_swiftness = my_boots_of_swiftness

        self.cloak_of_resistance = cloak_of_resistance

        self.patty_cake_by_radcliff = patty_cake_by_radcliff

    def add_fortitude_bonus(self, bonus):
        self.fortitude += bonus
        self.sources["fortitude"].append(f"bonus({bonus})")

    def add_reflex_bonus(self, bonus):
        self.reflex += bonus
        self.sources["reflex"].append(f"bonus({bonus})")

    def add_will_bonus(self, bonus, sources=None):
        self.will += bonus
        if sources is not None:
            self.sources["will"].extend(sources)
        else:
            self.sources["will"].append(f"bonus({bonus})")

    def add_global_bonus(self, bonus):
        self.fortitude += bonus
        self.reflex += bonus
        self.will += bonus
        self.sources["fortitude"].append(f"global bonus({bonus})")
        self.sources["reflex"].append(f"global bonus({bonus})")
        self.sources["will"].append(f"global bonus({bonus})")

    def add_item_bonus(self, fortitude_bonus=0, reflex_bonus=0, will_bonus=0):
            self.fortitude += fortitude_bonus + self.cloak_of_resistance.get_resistance_bonus() + self.patty_cake_by_radcliff.get_resistance_bonus() 
            self.reflex += reflex_bonus + self.cloak_of_resistance.get_resistance_bonus() + self.patty_cake_by_radcliff.get_resistance_bonus()
            self.will += will_bonus + self.cloak_of_resistance.get_resistance_bonus() + self.patty_cake_by_radcliff.get_resistance_bonus()
            if fortitude_bonus != 0:
                self.sources["fortitude"].append(f"item bonus({fortitude_bonus})")
            if reflex_bonus != 0:
                self.sources["reflex"].append(f"item bonus({reflex_bonus})")
            if will_bonus != 0:
                self.sources["will"].append(f"item bonus({will_bonus})")
            cloak_bonus = self.cloak_of_resistance.get_resistance_bonus()
            if cloak_bonus != 0:
                self.sources["fortitude"].append(f"Cloak of Resistance({cloak_bonus})")
                self.sources["reflex"].append(f"Cloak of Resistance({cloak_bonus})")
                self.sources["will"].append(f"Cloak of Resistance({cloak_bonus})")
            patty_cake_bonus = self.patty_cake_by_radcliff.get_resistance_bonus()
            if patty_cake_bonus != 0:
                self.sources["fortitude"].append(f"Patty Cake Bonus({patty_cake_bonus})")
                self.sources["reflex"].append(f"Patty Cake Bonus({patty_cake_bonus})")
                self.sources["will"].append(f"Patty Cake Bonus({patty_cake_bonus})")

    def __str__(self):
        output = []
        for save in ["fortitude", "reflex", "will"]:
            sources = ", ".join(self.sources[save])
            if save == "reflex":
                reflex_bonus = self.my_boots_of_swiftness.get_reflex_bonus()
                if reflex_bonus != 0:
                    item_bonus = f"Boots of Swiftness({reflex_bonus}"
                else:
                    item_bonus = ""

                bonus = self.reflex + reflex_bonus
                sources += f", {item_bonus}"
            else:
                bonus = self.__dict__[save]
            output.append(f"{save.capitalize()}: {bonus} ({sources})")

        return "\n".join(output)

saving_throws = SavingThrows(level, fortitude=0, reflex=0, will=0, dexterity_modifier=dexterity_modifier, constitution_modifier=constitution_modifier, wisdom_modifier=wisdom_modifier, armed_bravery=armed_bravery, my_boots_of_swiftness=my_boots_of_swiftness, cloak_of_resistance=cloak_of_resistance, patty_cake_by_radcliff=patty_cake_by_radcliff)
saving_throws.add_item_bonus()

class FullPlate:
    def __init__(self):
        self.equipped = True # new property to indicate if full plate is equipped
        self.name = "Full Plate"
        self.type = "Armor"
        self.armor_bonus = 9
        self.max_dex_modifier_bonus = 1
        self.base_armor_check_penalty = -6
        self.enhancement_bonus = 0
        self.enhancement_penalty_reduction = 0
        self.feat_armor_training = True
        self.is_made_of_adamantite = True

    def get_armor_check_penalty(self):
        if self.equipped:
            total_penalty = self.base_armor_check_penalty + self.enhancement_penalty_reduction + int(self.feat_armor_training)
            if self.is_made_of_adamantite:
                total_penalty += 1
            if total_penalty > 0:
                return 0
            else:
                return total_penalty
        else:
            return 0

    def get_max_dex_modifier_bonus(self):
        if self.equipped:
            if self.feat_armor_training:
                return self.max_dex_modifier_bonus + 1
            else:
                return self.max_dex_modifier_bonus
        else:
            return 0

    def get_armor_bonus(self):
        if self.equipped:
            return self.armor_bonus + self.enhancement_bonus
        else:
            return 0

    def add_enchantment(self):
        if self.equipped and self.enhancement_bonus < 5:
            self.enhancement_bonus += 1
            self.enhancement_penalty_reduction += 1
        return self.enhancement_bonus

    def __str__(self):
        if self.equipped:
            armor_str = "Name: {}\nType: {}\nArmor Bonus: +{}\nMax Dexterity Modifier Bonus: +{}\nArmor Check Penalty: {}\nFeat: {}\nEnchantments: {}"
            return armor_str.format(self.name, self.type, self.get_armor_bonus(), self.get_max_dex_modifier_bonus(), self.get_armor_check_penalty(), self.feat_armor_training, self.enhancement_bonus)
        else:
            return "Full Plate is unequipped"

    def toggle_equipped(self):
        self.equipped = not self.equipped
# create an instance of FullPlate
full_plate = FullPlate()

# add enchantments to full plate
for i in range(2):#This determines the level enchantment
    full_plate.add_enchantment()

class Shield:
    def __init__(self):
        self.name = "Shield Heavy Adamantite"
        self.type = "Shield"
        self.armor_bonus = 2
        self.base_armor_check_penalty = -2
        self.enhancement_bonus = 0
        self.enhancement_penalty_reduction = 0
        self.feat_shield_proficiency = True
        self.made_of_adamantite = True
        self.equipped = False

    def get_armor_check_penalty(self):
        if self.equipped:
            penalty = self.base_armor_check_penalty + self.enhancement_penalty_reduction
            if self.feat_shield_proficiency:
                penalty += 0
            else:
                penalty += 2
            if self.made_of_adamantite:
                penalty += 1
            if penalty > 0:
                return 0
            else:
                return penalty
        else:
            return 0

    def get_armor_bonus(self):
        if self.equipped:
            return self.armor_bonus + self.enhancement_bonus
        else:
            return 0

    def add_enchantment(self):
        if self.enhancement_bonus < 5: #This number determines the max enchantment level
            self.enhancement_bonus += 1
            self.enhancement_penalty_reduction += 1
        return self.enhancement_bonus


    def __str__(self):
        if self.equipped:
            shield_str = "Name: {}\nType: {}\nArmor Bonus: +{}\nArmor Check Penalty: {}\nFeat: {}\nEnchantments: {}"
            return shield_str.format(self.name, self.type, self.get_armor_bonus(), self.get_armor_check_penalty(), self.feat_shield_proficiency, self.enhancement_bonus)
        else:
            return "Shield is unequipped"

    def toggle_equipped(self):
        self.equipped = not self.equipped

# create an instance of the Shield
shield = Shield()

# add enchantments to the shield
for i in range(0): #This determins the level enchantment
    shield.add_enchantment()


class RingOfProtection:
    def __init__(self):
        self.equipped = False
        self.name = "Ring of Protection"
        self.type = "Ring"
        self.armor_bonus = 0
        self.enhancement_bonus = 0
        self.max_enhancement_bonus = 5

    def get_armor_bonus(self):
        if self.equipped:
            return self.armor_bonus + self.enhancement_bonus
        else:
            return 0

    def add_enchantment(self):
            if self.enhancement_bonus < 5: #This number determines the max enchantment level
                self.enhancement_bonus += 1
            return self.enhancement_bonus


    def __str__(self):
        if self.equipped:
            ring_str = "Name: {}\nType: {}\nArmor Bonus: +{}\nEnchantments: {}"
            return ring_str.format(self.name, self.type, self.get_armor_bonus(), self.enhancement_bonus)
        else:
            return "Ring of Protection is unequipped"

ring_of_protection = RingOfProtection()

for i in range(0): #This determins the level enchantment
    ring_of_protection.add_enchantment()

class AmuletOfNaturalArmor:
    def __init__(self):
        self.equipped = True
        self.name = "Amulet of Natural Armor"
        self.type = "Neck"
        self.armor_bonus = 0
        self.enhancement_bonus = 0
        self.max_enhancement_bonus = 5

    def get_armor_bonus(self):
        if self.equipped:
            return self.armor_bonus + self.enhancement_bonus
        else:
            return 0

    def add_enchantment(self):
            if self.enhancement_bonus < 5: #This number determines the max enchantment level
                self.enhancement_bonus += 1
            return self.enhancement_bonus


    def __str__(self):
        if self.equipped:
            amulet_str = "Name: {}\nType: {}\nArmor Bonus: +{}\nEnchantments: {}"
            return amulet_str.format(self.name, self.type, self.get_armor_bonus(), self.enhancement_bonus)
        else:
            return "Amulet of Natural Armor is unequipped"

amulet_of_natural_armor = AmuletOfNaturalArmor()

for i in range(2): #This determines the level enchantment
    amulet_of_natural_armor.add_enchantment()


class ArmorClass:
    def __init__(self, full_plate, shield, dexterity_modifier, my_boots_of_swiftness, feat_armor_training, ring_of_protection, amulet_of_natural_armor):
        self.full_plate = full_plate
        self.shield = shield
        self.dexterity_modifier = dexterity_modifier
        self.my_boots_of_swiftness = my_boots_of_swiftness
        self.ring_of_protection = ring_of_protection
        self.amulet_of_natural_armor = amulet_of_natural_armor
        self.feat_armor_training = feat_armor_training
        self.armor_bonus, self.armor_bonus_sources = self.calculate_armor_bonus()
        self.armor_check_penalty = self.calculate_armor_check_penalty()
        self.armor_class = 9 + self.armor_bonus + self.dexterity_modifier
        self.armor_class_modifiers = { 
            "Blinded": False,
            "Cowering": False,
            "Entangled": False,
            "Flat-footed": False,
            "Helpless": False,
            "Kneeling or Sitting": False,
            "Pinned": False,
            "Prone": False,
            "Squeezing": False,
            "Stunned": False,
            "Behind Cover": False
        }
        self.calculate_armor_modifiers() # <-- call the new method here

    def calculate_armor_modifiers(self):
        armor_bonus = self.armor_bonus
        armor_bonus_sources = self.armor_bonus_sources.copy()

        if self.armor_class_modifiers["Blinded"]:
            armor_bonus -= 2 + self.dexterity_modifier
            armor_bonus_sources.append("Blinded (-2)")
            armor_bonus_sources.append(f"-{self.dexterity_modifier} Dexterity Modifier")

        if self.armor_class_modifiers["Cowering"]:
            armor_bonus -= 2 + self.dexterity_modifier
            armor_bonus_sources.append("Cowering (-2)")
            armor_bonus_sources.append(f"-{self.dexterity_modifier} Dexterity Modifier")

        if self.armor_class_modifiers["Entangled"]:
            armor_bonus -= 2
            armor_bonus_sources.append("Entangled (-2)")

        if self.armor_class_modifiers["Flat-footed"]:
            armor_bonus -= self.dexterity_modifier
            armor_bonus_sources.append("Flat-footed")
            armor_bonus_sources.append(f"-{self.dexterity_modifier} Dexterity Modifier")

        if self.armor_class_modifiers["Helpless"]:
            armor_bonus -= 4 + self.dexterity_modifier
            armor_bonus_sources.append("Helpless (-4)")
            armor_bonus_sources.append(f"-{self.dexterity_modifier} Dexterity Modifier")

        if self.armor_class_modifiers["Kneeling or Sitting"]:
            armor_bonus -= 2
            armor_bonus_sources.append("Kneeling or Sitting (-2)")

        if self.armor_class_modifiers["Pinned"]:
            armor_bonus -= 4 + self.dexterity_modifier
            armor_bonus_sources.append("Pinned (-4)")
            armor_bonus_sources.append(f"-{self.dexterity_modifier} Dexterity Modifier")

        if self.armor_class_modifiers["Prone"]:
            armor_bonus -= 4
            armor_bonus_sources.append("Prone (-4)")

        if self.armor_class_modifiers["Squeezing"]:
            armor_bonus -= 4
            armor_bonus_sources.append("Squeezing into a tight space (-4)")

        if self.armor_class_modifiers["Stunned"]:
            armor_bonus -= 2 + self.dexterity_modifier
            armor_bonus_sources.append("Stunned (-2)")
            armor_bonus_sources.append(f"-{self.dexterity_modifier} Dexterity Modifier")

        if self.armor_class_modifiers["Behind Cover"]:
                armor_bonus += 4
                armor_bonus_sources.append("Behind Cover (+4)")

        self.armor_bonus = armor_bonus
        self.armor_bonus_sources = armor_bonus_sources
        self.armor_class = 10 + self.armor_bonus
        return armor_bonus, armor_bonus_sources

    def calculate_armor_bonus(self):
        armor_bonus = 0
        armor_bonus_sources = []

        # Check for full plate armor
        if self.full_plate.equipped:
            full_plate_bonus = FullPlate().get_armor_bonus()
            armor_bonus_sources.append(f"Full Plate (+{full_plate_bonus})")
            armor_bonus += full_plate_bonus

            # Calculate dexterity modifier for full plate armor
            max_dex_modifier_bonus = self.full_plate.get_max_dex_modifier_bonus()
            if self.dexterity_modifier > max_dex_modifier_bonus:
                dex_mod = max_dex_modifier_bonus
            else:
                dex_mod = self.dexterity_modifier
            armor_bonus += dex_mod
            armor_bonus_sources.append(f"Dexterity Modifier (+{dex_mod})")

            # Check for full plate armor enchantments
            if self.full_plate.enhancement_bonus > 0:
                full_plate_enchantment_bonus = self.full_plate.enhancement_bonus
                armor_bonus_sources.append(f"Full Plate Enchantment (+{full_plate_enchantment_bonus})")
                armor_bonus += full_plate_enchantment_bonus
        else:
            armor_bonus += self.dexterity_modifier
            armor_bonus_sources.append(f"Dexterity Modifier (+{self.dexterity_modifier})")
        # Boots of Swiftness
        armor_bonus += self.my_boots_of_swiftness.get_armor_bonus()
        armor_bonus_sources.append(f"Boots of Swiftness (+{self.my_boots_of_swiftness.get_armor_bonus()})")
        # Ring of Protection
        armor_bonus += self.ring_of_protection.get_armor_bonus()
        armor_bonus_sources.append(f"Ring of Protection (+{self.ring_of_protection.get_armor_bonus()})")
        # Amulet Of Natural Armor
        armor_bonus += self.amulet_of_natural_armor.get_armor_bonus()
        armor_bonus_sources.append(f"Amulet of Natural Armor (+{self.amulet_of_natural_armor.get_armor_bonus()})")

        if self.shield and self.shield.equipped:
            shield_bonus = Shield().get_armor_bonus()
            armor_bonus_sources.append(f"Shield (+{shield_bonus})")
            armor_bonus += shield_bonus
            if self.shield.enhancement_bonus > 0:
                shield_enchantment_bonus = self.shield.enhancement_bonus
                armor_bonus_sources.append(f"Shield Enchantment (+{shield_enchantment_bonus})")
                armor_bonus += shield_enchantment_bonus

        return armor_bonus, armor_bonus_sources

    def calculate_armor_check_penalty(self):
        full_plate_check_penalty = 0
        full_plate_check_penalty_sources = []
        shield_check_penalty = 0
        shield_check_penalty_sources = []
        if self.full_plate:
            full_plate_check_penalty = FullPlate().get_armor_check_penalty()
            full_plate_check_penalty_sources.append(f"Full Plate ({full_plate_check_penalty})")
            if self.full_plate.enhancement_penalty_reduction > 0:
                full_plate_enchantment_penalty_reduction = self.full_plate.enhancement_penalty_reduction
                full_plate_check_penalty_sources.append(f"Full Plate Enchantment (+{full_plate_enchantment_penalty_reduction})")
                full_plate_check_penalty += full_plate_enchantment_penalty_reduction
        if self.shield:
            shield_check_penalty = Shield().get_armor_check_penalty()
            shield_check_penalty_sources.append(f"Shield ({shield_check_penalty})")
            if self.shield.enhancement_penalty_reduction > 0:
                shield_enchantment_penalty_reduction = self.shield.enhancement_penalty_reduction
                shield_check_penalty_sources.append(f"Shield Enchantment (+{shield_enchantment_penalty_reduction})")
                shield_check_penalty += shield_enchantment_penalty_reduction
        total_check_penalty = min(full_plate_check_penalty, shield_check_penalty)
        check_penalty_sources = []
        if total_check_penalty > 0:
            return 0, check_penalty_sources
        else:
            if full_plate_check_penalty == total_check_penalty:
                check_penalty_sources.extend(full_plate_check_penalty_sources)
            if shield_check_penalty == total_check_penalty:
                check_penalty_sources.extend(shield_check_penalty_sources)
            return total_check_penalty, check_penalty_sources

    def get_armor_bonus(self):
        return self.armor_bonus

    def get_armor_class(self):
        return 9 + self.get_armor_bonus() + self.dexterity_modifier

    def get_armor_check_penalty(self):
        return self.armor_check_penalty

    def __str__(self):
        armor_bonus_str = ", ".join(self.armor_bonus_sources)
        return f"Armor class: {self.armor_class}, armor bonus: {self.armor_bonus} ({armor_bonus_str}), armor check penalty: {self.armor_check_penalty}"

my_armor = ArmorClass(full_plate, shield, dexterity_modifier, my_boots_of_swiftness, feat_armor_training, ring_of_protection, amulet_of_natural_armor)


enemy_cmd = 15  # or whatever value you want as the default
# This stun is for CMB
enemy_stunned = False
def calculate_combat_maneuver_bonus(level, strength_modifier, size, weapon_training, enemy_stunned, enemy_cmd):
    base_attack_bonus = level
    special_size_modifier = 0
    attack_maneuvers = ["Bull Rush", "Dirty Trick", "Disarm", "Drag", "Grapple", "Overrun", "Reposition", "Steal", "Trip"]
    bonuses = {}
    # This does not switch out dex for strength if you are "Fine", "Diminutive", or "Tiny".
    # You will have to manually figure that out. This is strength modifier based/calculated.
    if size == "Fine":
        special_size_modifier = -8
        bonuses["Special Size Modifier"] = -8
    elif size == "Diminutive":
        special_size_modifier = -4
        bonuses["Special Size Modifier"] = -4
    elif size == "Tiny":
        special_size_modifier = -2
        bonuses["Special Size Modifier"] = -2
    elif size == "Small":
        special_size_modifier = -1
        bonuses["Special Size Modifier"] = -1
    elif size == "Medium":
        special_size_modifier = 0
        bonuses["Special Size Modifier"] = 0
    elif size == "Large":
        special_size_modifier = 1
        bonuses["Special Size Modifier"] = 1
    elif size == "Huge":
        special_size_modifier = 2
        bonuses["Special Size Modifier"] = 2
    elif size == "Gargantuan":
        special_size_modifier = 4
        bonuses["Special Size Modifier"] = 4
    elif size == "Colossal":
        special_size_modifier = 8
        bonuses["Special Size Modifier"] = 8

    cmb = base_attack_bonus + strength_modifier + special_size_modifier
    bonuses["Base Attack Bonus"] = base_attack_bonus
    bonuses["Strength Modifier"] = strength_modifier
    bonuses["Combat Maneuver Bonus"] = cmb

    if weapon_training:
        if level >= 5:
            cmb += 1
            bonuses["Weapon Training"] = 1
        if level >= 9:
            cmb += 1
            bonuses["Weapon Training"] += 1
        if level >= 13:
            cmb += 1
            bonuses["Weapon Training"] += 1
        if level >= 17:
            cmb += 1
            bonuses["Weapon Training"] += 1

    if enemy_stunned:
        cmb += 4
        bonuses["Enemy Stunned"] = 4

    # Bull Rush
    if "Bull Rush" in attack_maneuvers:
        d20_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        improved_bull_rush = False
        greater_bull_rush = False
        bull_rush_bonus = cmb + d20_roll
        if improved_bull_rush:
            bull_rush_bonus += 2
        if greater_bull_rush:
            bull_rush_bonus += 2
            bonuses["Greater Bull Rush"] = 2
        difference = bull_rush_bonus - opponent_cmd
        push_distance = 0
        if difference >= 0:
            num_moves = (difference // 5) + 1
            push_distance = num_moves * 5
        bonuses["Bull Rush"] = {"Total": bull_rush_bonus, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd, "Push Distance": push_distance}
    
    if "Dirty Trick" in attack_maneuvers:
        d20_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        improved_dirty_trick = False
        greater_dirty_trick = False
        dirty_trick_bonus = cmb + d20_roll
        if improved_dirty_trick:
            dirty_trick_bonus += 2
        if greater_dirty_trick:
            dirty_trick_bonus += 2
            bonuses["Greater Dirty Trick"] = 2
        difference = dirty_trick_bonus - opponent_cmd
        rounds = 0
        if difference >= 0:
            number_of_rounds = (difference // 5) + 1
            rounds = number_of_rounds
        if greater_dirty_trick:
            additional_rounds = random.randint(1, 4)
            print(f"This is the random 1-4 dice roll for Dirty Trick: {additional_rounds}")
            rounds += additional_rounds
        bonuses["Dirty Trick"] = {"Total": dirty_trick_bonus, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd, "Rounds": rounds}

# Check if Disarm is in the list of maneuvers
    if "Disarm" in attack_maneuvers:
        unarmed = False
        if unarmed:
            disarm_bonus = cmb - 4
        else:
            disarm_bonus = cmb
        d20_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        disarm_check = disarm_bonus + d20_roll
        difference = disarm_check - opponent_cmd
        if difference >= 0:
            success_msg = "Disarm successful!"
            if difference >= 10:
                success_msg += " Target drops 2 items from their hands."
            else:
                success_msg += " Target drops 1 item from their hand."
            bonuses["Disarm"] = {"Success": True, "Message": success_msg, "Total": disarm_check, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd}
        else:
            failure_msg = "Disarm failed!"
            if difference <= -10:
                failure_msg += " You drop 1 item from your hand."
            bonuses["Disarm"] = {"Success": False, "Message": failure_msg, "Total": disarm_check, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd}
            
    if "Drag" in attack_maneuvers:
        d20_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        improved_drag = False
        greater_drag = False
        drag_bonus = cmb + d20_roll
        if improved_drag:
            drag_bonus += 2
            bonuses["Improved Drag"] = 2
        if greater_drag:
            drag_bonus += 2
            bonuses["Greater Drag"] = 2
        difference = drag_bonus - opponent_cmd
        drag_distance = 0
        if difference >= 0:
            num_moves = (difference // 5) + 1
            drag_distance = num_moves * 5
        bonuses["Drag"] = {"Total": drag_bonus, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd, "Drag Distance": drag_distance, "Message": ""}
        if drag_distance > 0:
            bonuses["Drag"]["Message"] = f"You successfully drag the enemy {drag_distance} feet."
        else:
            bonuses["Drag"]["Message"] = "You failed to drag the enemy."


    if "Grapple" in attack_maneuvers:
        both_hands_free = False # replace with your code for checking if both hands are free
        grapple_roll = random.randint(1, 20)
        pinned_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        improved_grapple = False # replace with your code for checking if Improved Grapple is available
        greater_grapple = False # replace with your code for checking if Greater Grapple is available
        grapple_bonus = cmb + grapple_roll
        pinned_bonus = cmb + pinned_roll
        if not both_hands_free:
            grapple_bonus -= 4
        if improved_grapple:
            grapple_bonus += 2
        if greater_grapple:
            grapple_bonus += 2
            bonuses["Greater Grapple"] = 2
        grapple_difference = grapple_bonus - opponent_cmd
        pinned_difference = pinned_bonus - opponent_cmd
        grappled = False
        pinned = False
        grapple_msg = ""
        pinned_msg = ""
        if grapple_difference >= 0:
            grappled = True
            grapple_msg = f"Grapple successful! Total: {grapple_bonus}, Dice Roll: {grapple_roll}, Opponent's CMD: {opponent_cmd}"
            bonuses["Grapple"] = {"Success": True, "Message": grapple_msg, "Total": grapple_bonus, "Dice Roll": grapple_roll, "Opponent's CMD": opponent_cmd}
        else:
            bonuses["Grapple"] = {"Success": False, "Message": "Grapple failed!", "Total": grapple_bonus, "Dice Roll": grapple_roll, "Opponent's CMD": opponent_cmd}
            pinned_difference = -1

        if pinned_difference >= 0 and grappled:
            pinned = True
            pinned_msg = f"Pinned successful! Total: {pinned_bonus}, Dice Roll: {pinned_roll}, Opponent's CMD: {opponent_cmd}"
            bonuses["Pinned"] = {"Success": True, "Message": pinned_msg, "Total": pinned_bonus, "Dice Roll": pinned_roll, "Opponent's CMD": opponent_cmd}
        else:
            bonuses["Pinned"] = {"Success": False, "Message": "Pinned failed!", "Total": pinned_bonus, "Dice Roll": pinned_roll, "Opponent's CMD": opponent_cmd}

    if "Overrun" in attack_maneuvers:
        overrun_roll = random.randint(1, 20)
        overrun_bonus = cmb + overrun_roll
        improved_overrun = False
        greater_overrun = False
        number_of_legs = 2
        enemy_cmd += (number_of_legs * 2) - 4
        if improved_overrun:
            overrun_bonus += 2
            bonuses["Improved Overrun"] = 2
        if greater_overrun:
            overrun_bonus += 2
            bonuses["Greater Overrun"] = 2
        overrun_difference = overrun_bonus - enemy_cmd
        overrun_msg = ""
        if overrun_difference >= 0:
            overrun_msg = "You succeed at moving through."
            if overrun_difference >= 5:
                overrun_msg += " They are knocked prone."
        else:
            overrun_msg = "You failed to move through."
        bonuses["Overrun"] = {"Success": overrun_difference >= 0, "Message": overrun_msg, "Total": overrun_bonus, "Dice Roll": overrun_roll, "Opponent's CMD": enemy_cmd}

    if "Reposition" in attack_maneuvers:
        reposition_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        improved_reposition = False
        greater_reposition = False
        reposition_bonus = cmb + reposition_roll
        if improved_reposition:
            reposition_bonus += 2
            bonuses["Improved Reposition"] = 2
        if greater_reposition:
            reposition_bonus += 2
            bonuses["Greater Reposition"] = 2
        reposition_difference = reposition_bonus - opponent_cmd
        reposition_distance = 0  # initialize reposition_distance to 0
        reposition_msg = ""
        if reposition_difference >= 0:
            num_moves = (reposition_difference // 5) + 1
            reposition_distance = num_moves * 5
            reposition_msg = f"You succeed at repositioning {reposition_distance} feet."
        else:
            reposition_msg = "You failed to reposition."
        bonuses["Reposition"] = {"Success": reposition_difference >= 0, "Message": reposition_msg, "Total": reposition_bonus, "Dice Roll": reposition_roll, "Opponent's CMD": opponent_cmd, "Reposition Distance": reposition_distance}

    if "Steal" in attack_maneuvers:
        d20_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        whip = False
        take_difficulty = False
        improved_steal = False
        greater_steal = False
        steal_bonus = cmb + d20_roll
        if whip:
            steal_bonus -= 4
        if take_difficulty:
            opponent_cmd += 5
        if improved_steal:
            steal_bonus += 2
        if greater_steal:
            steal_bonus += 2
        steal_difference = steal_bonus - opponent_cmd
        steal_msg = ""
        if steal_difference >= 0:
            steal_msg = "You succeed at stealing one item."
        else:
            steal_msg = "You failed to steal an item."
        bonuses["Steal"] = {"Success": steal_difference >= 0, "Message": steal_msg, "Total": steal_bonus, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd}

    if "Trip" in attack_maneuvers:
        d20_roll = random.randint(1, 20)
        opponent_cmd = enemy_cmd
        number_of_legs = 2
        enemy_cmd += (number_of_legs * 2) - 4
        improve_trip = False
        greater_trip = False
        trip_bonus = cmb + d20_roll
        if improve_trip:
            trip_bonus += 2
        if greater_trip:
            trip_bonus += 2
        trip_difference = trip_bonus - opponent_cmd
        trip_msg = ""
        if trip_difference >= 0:
            trip_msg = "They are knocked prone."
        elif trip_difference < -9:
            trip_msg = "You are knocked prone."
        else:
            trip_msg = "The trip attempt fails."
        bonuses["Trip"] = {"Success": trip_difference >= 0, "Message": trip_msg, "Total": trip_bonus, "Dice Roll": d20_roll, "Opponent's CMD": opponent_cmd}

    return bonuses
# This one is CMB!!! Replace "Medium" with your size name.
bonuses = calculate_combat_maneuver_bonus(level, strength_modifier, "Medium" , weapon_training, enemy_stunned, enemy_cmd)

# CMD
def calculate_cmd(base_attack_bonus, strength_modifier, dexterity_modifier, size_modifier, my_boots_of_swiftness, flat_footed, elven_curve_blade, level, improved_bull_rush, improved_dirty_trick, improved_disarm, improved_drag, improved_grapple, improved_overrun, improved_reposition, improved_steal, improved_sunder, improved_trip, greater_bull_rush, greater_dirty_trick, greater_disarm, greater_drag, greater_grapple, greater_overrun, greater_reposition, greater_steal, greater_sunder, greater_trip):
    size_modifiers = {"Fine": -8, "Diminutive": -4, "Tiny": -2, "Small": -1, "Medium": 0, "Large": 1, "Huge": 2, "Gargantuan": 4, "Colossal": 8}

    cmd_totals = {}
    for maneuver in ["Bull Rush", "Dirty Trick", "Disarm", "Drag", "Grapple", "Overrun", "Reposition", "Steal", "Sunder", "Trip"]:
        misc_mods = misc_modifiers(maneuver, elven_curve_blade, level, improved_bull_rush, improved_dirty_trick, improved_disarm, improved_drag, improved_grapple, improved_overrun, improved_reposition, improved_steal, improved_sunder, improved_trip, greater_bull_rush, greater_dirty_trick, greater_disarm, greater_drag, greater_grapple, greater_overrun, greater_reposition, greater_steal, greater_sunder, greater_trip)
        if flat_footed:
            cmd_total = 10 + base_attack_bonus + strength_modifier + size_modifiers[size_modifier] + misc_mods
            # if my_boots_of_swiftness and my_boots_of_swiftness.equipped:
            #     cmd_total -= my_boots_of_swiftness.get_cmd_bonus() - my_boots_of_swiftness.get_cmd_bonus()
        else:
            cmd_total = 10 + base_attack_bonus + strength_modifier + dexterity_modifier + size_modifiers[size_modifier] + misc_mods
            # if my_boots_of_swiftness and my_boots_of_swiftness.equipped:
            #     cmd_total += my_boots_of_swiftness.get_cmd_bonus()
        
        cmd_totals[maneuver] = cmd_total
    
    return cmd_totals


# CMD
def misc_modifiers(maneuver, elven_curve_blade, level, improved_bull_rush, improved_dirty_trick, improved_disarm, improved_drag, improved_grapple, improved_overrun, improved_reposition, improved_steal, improved_sunder, improved_trip, greater_bull_rush, greater_dirty_trick, greater_disarm, greater_drag, greater_grapple, greater_overrun, greater_reposition, greater_steal, greater_sunder, greater_trip):
    misc_mods = 0
    if maneuver in ["Sunder", "Disarm"]:
        if level >= 5:
            misc_mods += 1
        if level >= 9:
            misc_mods += 1
        if level >= 13:
            misc_mods += 1
        if level >= 17:
            misc_mods += 1
    if maneuver == "Sunder" and elven_curve_blade:
        misc_mods += 2
    if maneuver == "Bull Rush":
        if improved_bull_rush:
            misc_mods += 2
        if greater_bull_rush:
            misc_mods += 2
    if maneuver == "Dirty Trick":
        if improved_dirty_trick:
            misc_mods += 2
        if greater_dirty_trick:
            misc_mods += 2
    if maneuver == "Disarm":
        if improved_disarm:
            misc_mods += 2
        if greater_disarm:
            misc_mods += 2
    if maneuver == "Drag":
        if improved_drag:
            misc_mods += 2
        if greater_drag:
            misc_mods += 2
    if maneuver == "Grapple":
        if improved_grapple:
            misc_mods += 2
        if greater_grapple:
            misc_mods += 2
    if maneuver == "Overrun":
        if improved_overrun:
            misc_mods += 2
        if greater_overrun:
            misc_mods += 2
    if maneuver == "Reposition":
        if improved_reposition:
            misc_mods += 2
        if greater_reposition:
            misc_mods += 2
    if maneuver == "Steal":
        if improved_steal:
            misc_mods += 2
        if greater_steal:
            misc_mods += 2
    if maneuver == "Sunder":
        if improved_sunder:
            misc_mods += 2
        if greater_sunder:
            misc_mods += 2
    if maneuver == "Trip":
        if improved_trip:
            misc_mods += 2
        if greater_trip:
            misc_mods += 2
    return misc_mods
# Change these to true or False for CMD
cmd_totals = calculate_cmd(base_attack_bonus=level, 
                           strength_modifier=strength_modifier, 
                           dexterity_modifier=dexterity_modifier, 
                           size_modifier="Medium", 
                           my_boots_of_swiftness=my_boots_of_swiftness, 
                           flat_footed=False, 
                           elven_curve_blade=True, 
                           level=level, 
                           improved_bull_rush=False, 
                           improved_dirty_trick=False, 
                           improved_disarm=False, 
                           improved_drag=False, 
                           improved_grapple=False, 
                           improved_overrun=False, 
                           improved_reposition=False, 
                           improved_steal=False, 
                           improved_sunder=False, 
                           improved_trip=False, 
                           greater_bull_rush=False, 
                           greater_dirty_trick=False, 
                           greater_disarm=False, 
                           greater_drag=False, 
                           greater_grapple=False, 
                           greater_overrun=False, 
                           greater_reposition=False, 
                           greater_steal=False, 
                           greater_sunder=False, 
                           greater_trip=False)


def elven_curve_blade():
    return random.randint(1, 10)

def elven_curve_blade_shock():
    return random.randint(1, 6)

def elven_curve_blade_shocking_burst():
    return random.randint(1, 10)

# These Bonuses applied are specific to me and not an enemy.
def calculate_attack_bonus(level, strength_modifier, boots_of_swiftness, weapon_focus, weapon_training, sword_enchantment_level, 
dazzled=False, entangled=False, flanking_defender=False, invisible=False, on_high_ground=False,
prone=False, shaken_or_frightened=False, squeezing_through_space=False):
    base_attack_bonus = level

    if level <= 5:
        number_of_attacks = 1
    elif level <= 10:
        number_of_attacks = 2
    elif level <= 15:
        number_of_attacks = 3
    elif level <= 20:
        number_of_attacks = 4
    else:
        return "Invalid level"

    attack_bonuses = []
    attack_bonus = base_attack_bonus + strength_modifier + boots_of_swiftness.get_attack_bonus() + weapon_focus + sword_enchantment_level

    bonuses_applied = []
    if strength_modifier != 0:
        bonuses_applied.append(f"Strength Modifier ({strength_modifier})")
    if boots_of_swiftness.get_attack_bonus() != 0:
        bonuses_applied.append(f"Boots of Swiftness ({boots_of_swiftness.get_attack_bonus()})")
    if weapon_focus != 0:
        bonuses_applied.append(f"Weapon Focus ({weapon_focus})")
    if sword_enchantment_level != 0:
        bonuses_applied.append(f"Sword Enchantment Level ({sword_enchantment_level})")
    if weapon_training:
        if level >= 5:
            attack_bonus += 1
            bonuses_applied.append("Weapon Training (+1)")
        if level >= 9:
            attack_bonus += 1
            bonuses_applied.append("Weapon Training (+1)")
        if level >= 13:
            attack_bonus += 1
            bonuses_applied.append("Weapon Training (+1)")
        if level >= 17:
            attack_bonus += 1
            bonuses_applied.append("Weapon Training (+1)")

    if dazzled:
        attack_bonus -= 1
        bonuses_applied.append("Dazzled (-1)")
    if entangled:
        attack_bonus -= 2
        bonuses_applied.append("Entangled (-2)")
    if flanking_defender:
        attack_bonus += 2
        bonuses_applied.append("Flanking Defender (+2)")
    if invisible:
        attack_bonus += 2
        bonuses_applied.append("Invisible (+2, defender loses any dexterity bonus to AC)")
    if on_high_ground:
        attack_bonus += 1
        bonuses_applied.append("On High Ground (+1)")
    if prone:
        attack_bonus -= 4
        bonuses_applied.append("Prone (-4)")
    if shaken_or_frightened:
        attack_bonus -= 2
        bonuses_applied.append("Shaken or Frightened (-2)")
    if squeezing_through_space:
        attack_bonus -= 4
        bonuses_applied.append("Squeezing Through A Space (-4)")

    for i in range(number_of_attacks):
        attack_bonuses.append(attack_bonus - 5 * i)

    if boots_of_swiftness.equipped:
        attack_bonuses.append(attack_bonuses[0])

    if bonuses_applied:
        bonuses_string = ", ".join(bonuses_applied)
        print(f"Total attack bonus mod: {attack_bonus} ({bonuses_string})")
    else:
        print(f"Total attack bonus mod: {attack_bonus}")
    return attack_bonuses

# Call calculate_attack_bonus function with Combat Modifiers. Being Set True or Flase doesnt matter.
attack_bonuses = calculate_attack_bonus(level, strength_modifier, my_boots_of_swiftness, weapon_focus, weapon_training, sword_enchantment_level,
dazzled=False, entangled=False, flanking_defender=False, invisible=False, on_high_ground=False,
prone=False, shaken_or_frightened=False, squeezing_through_space=False)

def calculate_damage(strength_modifier, sword_enchantment_level, weapon_training, weapon_specialization, focused_weapon, power_attack, level, d20_roll):
    physical_damage = (strength_modifier * 1.5) + sword_enchantment_level + weapon_specialization + focused_weapon
    weapon_training_damage = 0
    
    if weapon_training:
        if level >= 5:
            weapon_training_damage += 1
        if level >= 9:
            weapon_training_damage += 1
        if level >= 13:
            weapon_training_damage += 1
        if level >= 17:
            weapon_training_damage += 1
        
    if power_attack:
        if level >= 4:
            physical_damage += 3
        if level >= 8:
            physical_damage += 3
        if level >= 12:
            physical_damage+= 3
        if level >= 16:
            physical_damage += 3
        if level >= 20:
            physical_damage += 3

    physical_damage += weapon_training_damage
    weapon_damage = elven_curve_blade()
    magic_damage = elven_curve_blade_shock()
    crit_magic_damage = elven_curve_blade_shocking_burst()

    return physical_damage, weapon_damage, magic_damage, crit_magic_damage

def calculate_damage_sources(strength_modifier, sword_enchantment_level, weapon_training, weapon_specialization, focused_weapon, power_attack, level):
    damage_sources = {
        "Strength Modifier": strength_modifier * 1.5,
        "Sword Enchantment": sword_enchantment_level,
        "Weapon Specialization": weapon_specialization,
        "Focused Weapon": focused_weapon}
        
    if weapon_training:
        if level >= 5:
            damage_sources["Weapon Training"] = 1
        if level >= 9:
            damage_sources["Weapon Training"] = 2
        if level >= 13:
            damage_sources["Weapon Training"] = 3
        if level >= 17:
            damage_sources["Weapon Training"] = 4
        
    if power_attack:
        if level >= 4:
            damage_sources["Power Attack"] = 3
        if level >= 8:
            damage_sources["Power Attack"] = 6
        if level >= 12:
            damage_sources["Power Attack"] = 9
        if level >= 16:
            damage_sources["Power Attack"] = 12
        if level >= 20:
            damage_sources["Power Attack"] = 15

    return damage_sources

damage_sources = calculate_damage_sources(strength_modifier, sword_enchantment_level, weapon_training, weapon_specialization, focused_weapon, power_attack, level)
print("")
print("Health:",hit_points.calculate())
print("")
print("Strength:", strength_score)
print("Strength Modifier:", strength_modifier)

print("Dexterity:", dexterity_score)
print("Dexterity Modifier:", dexterity_modifier)

print("Constitution:", constitution_score)
print("Constitution Modifier:", constitution_modifier)

print("Intelligence:", intelligence_score)
print("Intelligence Modifier:", intelligence_modifier)

print("Wisdom:", wisdom_score)
print("Wisdom Modifier:", wisdom_modifier)

print("Charisma:", charisma_score)
print("Charisma Modifier:", charisma_modifier)
print("")
if bonuses:
    bull_rush_bonuses = bonuses.get("Bull Rush", {})
    if bull_rush_bonuses:
        total = bull_rush_bonuses["Total"]
        dice_roll = bull_rush_bonuses["Dice Roll"]
        opponent_cmd = bull_rush_bonuses["Opponent's CMD"]
        push_distance = bull_rush_bonuses["Push Distance"]
        print(f"Combat Maneuver Bonus for Bull Rush: {total}")
        print(f"Dice Roll: {dice_roll}")
        print(f"Opponent's CMD: {opponent_cmd}")
        print(f"Push Distance: {push_distance} feet")
        print("If you run into another person you must make another roll with a -4. You must use the lowest of the two rolls.")
        print("You must take into account how far you have traveled and then deduct that into your new roll information to determine how far you can go.")
        print("If you have Improved Bull Rush then you do not provoke an attack of opportunity")
        print("If you have Greater Bull Rush then the enemy you are moving gives attacks of opportunity's to your allies")
else:
    print("No bonus calculated for Bull Rush")
print("")

if bonuses:
    dirty_trick_bonuses = bonuses.get("Dirty Trick", {})
    if dirty_trick_bonuses:
        total = dirty_trick_bonuses["Total"]
        dice_roll = dirty_trick_bonuses["Dice Roll"]
        opponent_cmd = dirty_trick_bonuses["Opponent's CMD"]
        rounds = dirty_trick_bonuses["Rounds"]
        if "Greater Dirty Trick" in dirty_trick_bonuses:
            greater_dirty_trick_bonus = dirty_trick_bonuses["Greater Dirty Trick"]
            additional_rounds = dirty_trick_bonuses["Additional Rounds"]
            print(f"Combat Maneuver Bonus for Dirty Trick: {total} (+{greater_dirty_trick_bonus} with Greater Dirty Trick)")
            print(f"Dice Roll: {dice_roll}")
            print(f"Opponent's CMD: {opponent_cmd}")
            print(f"Number of Rounds: {rounds}")
        else:
            print(f"Combat Maneuver Bonus for Dirty Trick: {total}")
            print(f"Dice Roll: {dice_roll}")
            print(f"Opponent's CMD: {opponent_cmd}")
            print(f"Number of Rounds: {rounds}")
        print("If you have the Improved Overrun you do not provoke an attack of opportunity.")
else:
    print("No bonus calculated for Dirty Trick")

print("")

if bonuses:
    disarm_bonuses = bonuses.get("Disarm", {})
    if disarm_bonuses:
        total = disarm_bonuses["Total"]
        dice_roll = disarm_bonuses["Dice Roll"]
        opponent_cmd = disarm_bonuses["Opponent's CMD"]
        success = disarm_bonuses["Success"]
        message = disarm_bonuses["Message"]
        print(f"Combat Maneuver Bonus for Disarm: {total}")
        print(f"Dice Roll: {dice_roll}")
        print(f"Opponent's CMD: {opponent_cmd}")
        print(message)
        print("If you have the Improved Disarm you do not provoke an attack of opportunity.")

    else:
        print("No bonus calculated for Disarm")
else:
    print("No bonuses calculated yet")    

print("")
if bonuses:
    drag_bonuses = bonuses.get("Drag", {})
    if drag_bonuses:
        total = drag_bonuses["Total"]
        dice_roll = drag_bonuses["Dice Roll"]
        opponent_cmd = drag_bonuses["Opponent's CMD"]
        drag_distance = drag_bonuses["Drag Distance"]
        message = drag_bonuses["Message"]
        print(f"Combat Maneuver Bonus for Drag: {total}")
        print(f"Dice Roll: {dice_roll}")
        print(f"Opponent's CMD: {opponent_cmd}")
        print(f"Drag Distance: {drag_distance} feet")
        print(message)
        print("If you have Improved Drag, then you do not provoke an attack of opportunity.")
        print("If you have Greater Drag, then dragging the enemy past or by your teammates gives them attacks of opportunity.")
    else:
        print("No bonus calculated for Drag")
else:
    print("No bonuses calculated yet.")

print("")
if 'Grapple' in bonuses or 'Pinned' in bonuses:
    if 'Grapple' in bonuses:
        grapple_total = bonuses['Grapple']['Total']
        grapple_dice_roll = bonuses['Grapple']['Dice Roll']
        grapple_opponent_cmd = bonuses['Grapple']["Opponent's CMD"]
        print(f"Combat Maneuver Bonus Total for Grapple: {grapple_total}")
        print(f"Dice Roll: {grapple_dice_roll}")
        print(f"Opponent's CMD: {grapple_opponent_cmd}")
    
    if 'Pinned' in bonuses:
        pinned_total = bonuses['Pinned']['Total']
        pinned_dice_roll = bonuses['Pinned']['Dice Roll']
        pinned_opponent_cmd = bonuses['Pinned']["Opponent's CMD"]
        print(f"Combat Maneuver Bonus Total for Pinned: {pinned_total}")
        print(f"Dice Roll: {pinned_dice_roll}")
        print(f"Opponent's CMD: {pinned_opponent_cmd}")
    
    if 'Grapple' in bonuses and 'Pinned' in bonuses:
        if grapple_total >= enemy_cmd:
            print("The enemy is grappled.")
            if pinned_total >= enemy_cmd:
                print("The enemy is pinned.")
        else:
            print("The enemy is not grappled or pinned.")
    elif 'Grapple' in bonuses:
        if grapple_total >= enemy_cmd:
            print("The enemy is grappled.")
        else:
            print("The enemy is not grappled.")
    else:
        print("The enemy is not grappled or pinned.")
    print("If you have the Improved Grapple you do not provoke an attack of opportunity.")
print("")

overrun_bonuses = bonuses.get("Overrun", {})
if overrun_bonuses:
    total = overrun_bonuses["Total"]
    dice_roll = overrun_bonuses["Dice Roll"]
    opponent_cmd = overrun_bonuses["Opponent's CMD"]
    success = overrun_bonuses["Success"]
    message = overrun_bonuses["Message"]
    print(f"Combat Maneuver Bonus for Overrun: {total}")
    print(f"Dice Roll: {dice_roll}")
    print(f"Opponent's CMD: {opponent_cmd}")
    print(message)
    print("If you have the Improved Overrun you do not provoke an attack of opportunity.")
    print("If you knock the enemy over/prone, the enemy provoke attacks of opportunity for your allies.")
else:
    print("No bonus calculated for Overrun")

print("")
if bonuses:
    reposition_bonuses = bonuses.get("Reposition", {})
    if reposition_bonuses:
        total = reposition_bonuses["Total"]
        dice_roll = reposition_bonuses["Dice Roll"]
        opponent_cmd = reposition_bonuses["Opponent's CMD"]
        reposition_distance = reposition_bonuses["Reposition Distance"]
        message = reposition_bonuses["Message"]
        print(f"Combat Maneuver Bonus for Reposition: {total}")
        print(f"Dice Roll: {dice_roll}")
        print(f"Opponent's CMD: {opponent_cmd}")
        print(f"Reposition Distance: {reposition_distance} feet")
        print(f"{message}")
        print("If you have Improved Reposition, then you do not provoke an attack of opportunity.")
        print("If you have Greater Reposition, then the enemy provokes attacks of opportunity for your allies.")
    else:
        print("No bonus calculated for Reposition")
else:
    print("No bonuses calculated yet")
print("")

steal_bonuses = bonuses.get("Steal", {})
if steal_bonuses:
    total = steal_bonuses["Total"]
    dice_roll = steal_bonuses["Dice Roll"]
    opponent_cmd = steal_bonuses["Opponent's CMD"]
    message = steal_bonuses["Message"]
    print(f"Combat Maneuver Bonus for Steal: {total}")
    print(f"Dice Roll: {dice_roll}")
    print(f"Opponent's CMD: {opponent_cmd}")
    print(message)
    print("If you have Improved Steal, then you do not provoke an attack of opportunity.")
    print("If you successfully steal an item from a foe during combat, it does not notice the theft until after combat is over or if it attempts to use the missing item.")
else:
    print("No bonus calculated for Steal")
print("")
trip_bonuses = bonuses.get("Trip", {})
if trip_bonuses:
    total = trip_bonuses["Total"]
    dice_roll = trip_bonuses["Dice Roll"]
    opponent_cmd = trip_bonuses["Opponent's CMD"]
    message = trip_bonuses["Message"]
    print(f"Combat Maneuver Bonus for Trip: {total}")
    print(f"Dice Roll: {dice_roll}")
    print(f"Opponent's CMD: {opponent_cmd}")
    print(message)
else:
    print("No bonus calculated for Trip")
print("")
# example usage
# This is where I determine what is happening to me for my CMD!

# print out the CMD totals for each maneuver
for maneuver, cmd_total in cmd_totals.items():
    print(f"{maneuver} CMD: {cmd_total}")
print("")
print(saving_throws)
print("The DC of Intimidate checks to demoralize him increases by an amount equal to twice his bonus from bravery.")
print("Half-elves are immune to magic sleep effects and gain a +2 racial saving throw bonus against enchantment spells and effects.")
print("")
print(cloak_of_resistance)
print("")
print("You rolled a natural:", d20_roll, "Your initiative is:", initiative)
print("")
# print full plate to console
print(full_plate)
print("")
print(shield)
print("")
print(my_boots_of_swiftness)
print("")
print(ring_of_protection)
print("")
print(amulet_of_natural_armor)
print("")
#This prints all aspects of my current armor class.
print("Your", my_armor)
print("")
# print(f"Combat Maneuver Bonus: {cmb}")
print("")
attack_bonuses = calculate_attack_bonus(level, strength_modifier, BootsOfSwiftness(), weapon_focus, weapon_training, sword_enchantment_level)
print("Attack Bonuses for level", level, ":", attack_bonuses)
print("Attack Bonuses with boots of swiftness:", attack_bonuses[0])
print("")
# Print out the damage sources
print("Damage Sources:")
for name, value in damage_sources.items():
    print(f"{name}: {value}")

total_damage = sum(damage_sources.values())
print(f"Total Base Damage: {total_damage}")

print("")
for attack_bonus in attack_bonuses:
    d20_roll = random.randint(1, 20)
    if d20_roll == 1:
        print("You CRITICALLY FAIL!!!")
    else:
        physical_damage = calculate_damage(strength_modifier, sword_enchantment_level, weapon_training, weapon_specialization, focused_weapon, power_attack, level, d20_roll)
        weapon_damage = elven_curve_blade()
        magic_damage = elven_curve_blade_shock()
        crit_magic_damage = elven_curve_blade_shocking_burst()
        print("")
        print("Attack Bonus:", attack_bonus) 
        print("D20 Roll:", d20_roll)
        total_dice_roll = attack_bonus + d20_roll
        print("Your dice total is:", total_dice_roll)
        print("Weapon Damage Roll:", weapon_damage)
        total_physical_damage = physical_damage[0] + weapon_damage
        print("Physical Damage:", total_physical_damage, "Magic Damage:", magic_damage)
        if 15 <= d20_roll <= 20:
            total_physical_damage *= 2
            magic_damage *= 2
            print("Critical Hit! Physical Damage Doubled to:", total_physical_damage)
            print("Magic Damage Doubled to:", magic_damage) 
            print("Shocking Burst:", crit_magic_damage)
            print("Total Shock Damage:", magic_damage + crit_magic_damage)
            print("")
