print "A monster approaches! Prepare to fight!"

playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30

print "You have 100 health. The monster has 100 health."

print "What attack do you wish to use?"

print "Choose punch, sword, or fireball."



while monsterHealth >= 0 and playerHealth >= 0:
    userInput = raw_input()
    punch = punchDmg
    sword = swordDmg
    fireball = fireballDmg
    print "Choose punch, sword, or fireball."    
    if userInput == "punch":
        monsterHealth = monsterHealth - punch
        print "The monster has been punched. The monster's health is " + str(monsterHealth)
        import random
        damageByMonster = random.randint(1, 35)
        print "The monster has attacked you. You lose " + str(damageByMonster)
        playerHealth = playerHealth - damageByMonster
        print "Your health is " + str(playerHealth)
    if userInput == "sword":
        monsterHealth = monsterHealth - sword
        print "The monster has been stabbed. The monster's health is " + str(monsterHealth)
        import random
        damageByMonster = random.randint(1, 35)
        print "The monster has attacked you. You lose " + str(damageByMonster)
        playerHealth = playerHealth - damageByMonster
        print "Your health is " + str(playerHealth)
    if userInput == "fireball":
        monsterHealth = monsterHealth - fireball
        print "The monster has been burned. The monster's health is " + str(monsterHealth)
        import random
        damageByMonster = random.randint(1, 35)
        print "The monster has attacked you. You lose " + str(damageByMonster)
        playerHealth = playerHealth - damageByMonster
        print "Your health is " + str(playerHealth)
    if playerHealth < 1:
        print "Sorry, the monster has killed you."
    if monsterHealth < 1:
        print "Congrats! The monster is dead. You win!"