import random

class Enemy:
    # atkl=60
    # atkh=80
    # val = random.randrange(60,80)

    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
    
    def getAttack(self):
        print(self.atkl)
        # print(self.atkh)
        
    def getHp(self):
        print(self.hp)


enemy1 = Enemy(50, 100)
enemy1.getAttack()
enemy1.getHp()

enemy2 = Enemy(60, 120)
enemy2.getAttack()
enemy2.getHp()
# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80

# while playerhp > 0:
#     dmg = random.randrange(60,80)
#     playerhp = playerhp - dmg

#     if playerhp <= 30:
#         playerhp = 30

#     print("enemy strikes for", dmg, "for damage point. Current hp id", playerhp)

#     # if playerhp == 30:
#     #     print("You are been teleproted to the hospital")
#     #     break

#     if playerhp > 30:
#         continue

#     print("You are been teleproted to the hospital")
#     break


