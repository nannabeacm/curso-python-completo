### 92
print("\n===== 92 ======\n")

import random

hero_hp = 100
enemy_hp = 100

def characters_hp():
    print(
        "HERO HP:", max(0, hero_hp),
        "\nENEMY HP:", max(0, enemy_hp)
    )

print("The HERO and the ENEMY are fighting!") 

while hero_hp > 0 and enemy_hp > 0:
    attack = random.randint(5, 20)
    print("The ENEMY attacked the HERO! ", attack, " of DAMAGE!")
    hero_hp -= attack
    characters_hp()
    if hero_hp <= 0:
        print("The ENEMY has won!")
        break
    attack = random.randint(5, 20)
    print("The HERO attacked the ENEMY!", attack, " of DAMAGE!")
    enemy_hp -= attack
    characters_hp()
    if enemy_hp <= 0:
        print("The HERO has won!")
        break
