def cast_spell(heroes, name, mp_needed, spell_name):
    if heroes[name]["mp"] >= mp_needed:
        heroes[name]["mp"] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mp']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")


def take_damage(heroes, name, damage, attacker):
    heroes[name]["hp"] -= damage
    if heroes[name]["hp"] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hp']} HP left!")
    else:
        del heroes[name]
        print(f"{name} has been killed by {attacker}!")


def recharge(heroes, name, amount):
    current_mp = heroes[name]["mp"]
    heroes[name]["mp"] = min(200, current_mp + amount)
    recovered = heroes[name]["mp"] - current_mp
    print(f"{name} recharged for {recovered} MP!")


def heal(heroes, name, amount):
    current_hp = heroes[name]["hp"]
    heroes[name]["hp"] = min(100, current_hp + amount)
    recovered = heroes[name]["hp"] - current_hp
    print(f"{name} healed for {recovered} HP!")

n = int(input())

heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    heroes[name] = {"hp": int(hp), "mp": int(mp)}

while True:
    line = input()
    if line == "End":
        break

    parts = line.split(" - ")
    action = parts[0]
    name = parts[1]

    if action == "CastSpell":
        mp_needed = int(parts[2])
        spell_name = parts[3]
        cast_spell(heroes, name, mp_needed, spell_name)

    elif action == "TakeDamage":
        damage = int(parts[2])
        attacker = parts[3]
        take_damage(heroes, name, damage, attacker)

    elif action == "Recharge":
        amount = int(parts[2])
        recharge(heroes, name, amount)

    elif action == "Heal":
        amount = int(parts[2])
        heal(heroes, name, amount)

for hero_name, stats in heroes.items():
    print(hero_name)
    print(f"  HP: {stats['hp']}")
    print(f"  MP: {stats['mp']}")
print(heroes)