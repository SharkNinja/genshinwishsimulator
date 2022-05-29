""""W06 Ponder: Developer"""
# Author: Jeriko Lagazo

"""Genshin Impact Wish Simulator"""
# Gensin Impact is a gacha game, where in the game you have to roll
# for various characters and weapons. This simulator is meant to
# test your luck as if you were rolling on the actual game. 
# You can use this simulator if you do not play the game, or to
# tese your luck if you do not wish to waste your primogems (the in game currency used to roll)

"""Requirements"""
#✔️ The program may be any type of game or interactive SIMULATION.
#✔️ The program should use classes and instances.
#✔️ The program should apply the four principles of programming with classes.
#✔️ The program should use the libraries chosen in the course.
#✔️ The program should be delivered through a version control system.
#✔️ The program should be able to be run from the command line.


import random
import math

from colorama import Fore, Style

class WishSimulation:
    """This is the main class, it is not a parent class
    as I cannot find any way it should be a parent class. This
    class  acts as the primary network for the other three classes
    and does the actual simulation"""
    def main():

        five_star_pity = 0
        four_star_pity = 0

        # helps pre-determine the set pity for your four star and five star character/weapon
        five_star_pity = int(input(f"{Fore.YELLOW}\033[1m" + "★ 5 Star Pity (1-89)" + "\033[0m" +  f"{Style.RESET_ALL}" + ": "))
        four_star_pity = int(input(f"{Fore.MAGENTA}\033[1m" + "✯ 4 Star Pity (1-9)" + "\033[0m" +  f"{Style.RESET_ALL}" + ": "))

        # helps pre-determined if the character/weapon is guranteed to be the promotional
        five_star_guranteed = int(input(f"{Fore.YELLOW}\033[1m" + "★ 5 Star Guaranteed" + "\033[0m" +  f"{Style.RESET_ALL}" + " | " + "\033[1m" + "(1) True" + "\033[0m" + " or " + "\033[1m" + "(2) False" + "\033[0m" + ": "))
        four_star_guranteed = int(input(f"{Fore.MAGENTA}\033[1m" + "✯ 4 Star Guaranteed" + "\033[0m" +  f"{Style.RESET_ALL}" + " | " + "\033[1m" + "(1) True" + "\033[0m" + " or " + "\033[1m" + "(2) False" + "\033[0m" + ": "))

        wish_type = int(input("\033[1m" + "1x" + "\033[0m" + " or " + "\033[1m" + "10x" + "\033[0m" + ": "))


        if wish_type == 1:
            print()

        elif wish_type == 10:

            if (four_star_pity > 10) or (five_star_pity > 90):

                print(f"{Fore.RED}\033[1m" + "ERROR | " + "\033[0m" + "Something has gone wrong, maximum pity has been exceeded.")
                print(f"\033[1m" + "✯ 4 Star Pity: " + "\033[0m" + f"{four_star_pity}") 
                print(f"\033[1m" + "★ 5 Star Pity: " + "\033[0m" + f"{five_star_pity}")

            else:

                for x in range(wish_type):
                
                    five_star_pity += 1 # pity is added on after every wish 
                    four_star_pity += 1 # pity is added on after every wish 

                    if five_star_pity == 90: # you are guranteed a 5 star after 90 wishes
                    
                        five_star_pull, five_star_guranteed = FiveStarRoll.roll_5_star(five_star_guranteed)
                        print(f"{Fore.YELLOW}★ {five_star_pull}{Style.RESET_ALL}") 

                        five_star_pity = 0 # five star pity resets to zero after getting a five star

                    elif four_star_pity == 10: # you are guranteed a 4 star after 10 wishes
                    
                        four_star_pull, four_star_guranteed = FourStarRoll.roll_4_star(four_star_guranteed)
                        print(f"{Fore.MAGENTA}✯ {four_star_pull}{Style.RESET_ALL}") 

                        four_star_pity = 0 # four star pity resets to zero after getting a four star

                    else:
                    
                        wish = round(random.uniform(0, 100), 3)

                        if (wish >= 0) and (wish <= 0.600): #five star
                        
                            five_star_pull, five_star_guranteed = FiveStarRoll.roll_5_star(five_star_guranteed)
                            print(f"{Fore.YELLOW}★ {five_star_pull}{Style.RESET_ALL}") 

                            five_star_pity = 0 # five star pity resets to zero after getting a five star

                        elif (wish > 0.600) and (wish <= 5.100): #four star 5.100%
                        
                            four_star_pull, four_star_guranteed = FourStarRoll.roll_4_star(four_star_guranteed   )
                            print(f"{Fore.MAGENTA}✯ {four_star_pull}{Style.RESET_ALL}") 

                            four_star_pity = 0 # four star pity resets to zero after getting a four star

                        elif (wish >= 5.100) and (wish < 100): #three star 94.300%
                        
                            three_star_pull = ThreeStarRoll.roll_3_star()
                            print(f"{Fore.CYAN}✰ {three_star_pull}{Style.RESET_ALL}") 

class ThreeStarRoll:
    """This class will hold and roll the three stars"""
    def roll_3_star():

        # 3 stars do not have a 50/50 or gurantee system, 
        # which is why it does not require code that would 
        # randomly decide the items in the list
    
        three_star_pool = ["Slingshot", "Raven Bow", "Thrilling Tales of Dragon Slayers", "Black Tassal", 
        "Bloodstained Greatsword", "Skyrider Sword", "Cool Steel", "Sharpshooter's Oath", "Emerald Orb",
        "Magic Guide", "Debate Club", "Ferrous Shadow", "Harbinger of Dawn"]

        three_star_pull = random.choice(three_star_pool)
        return three_star_pull

class FourStarRoll:
    """This class will hold and roll the four stars"""
    def roll_4_star(four_star_guranteed):
    
        if four_star_guranteed == 1:
        
            four_star_pool = ["Sayu", "Razor", "Rosaria"]
            four_star_guranteed == 2 # False as the guranteed has been used, meaning you'll have a 50/50 chance of winning the promotional character on the next 5 star pull
    
        else:
        
            coin_flip = random.randint(1, 3)
    
            if coin_flip == 1: # 50/50 won
            
                four_star_pool = ["Sayu", "Razor", "Rosaria"]
                four_star_guranteed == 2 # False as winning the 50/50 does not give you a guranteed 4* promotional character
    
            else: #50/50 lost
            
                coin_flip = random.randint(1, 3)
    
                if coin_flip == 1: # weapons from the 4 star pool since the base probability for winning a 4 star item: 5.1% (2.550% for weapons)  
                    four_star_pool = ["Rust", "The Stringless", "Eye of Perception", "Favonius Lance",
                    "Rainslasher", "The Bell", "Lion's Roar", "The Flute", "Sacrificial Bow",
                    "Favonius Warbow", "Sacrificial Fragments", "Favonius Codex", "Dragonsbane", 
                    "Sacrificial Greatsword", "Favonius Greatsword", "Favonius Sword"]
    
                elif coin_flip == 2: # characters from the 4 star pool since the base probability for winning a 4 star item: 5.1% (2.550% for characters)  
                
                    four_star_pool = ["Kujou Sara", "Thoma", "Xinyan", "Diona", 
                    "Noelle", "Fishcl", "Xingqiu", "Yun Jin", "Gorou", "Yanfei", 
                    "Sucrose", "Chongyun", "Bennett", "Ningguang", "Beidou", "Xiangling",
                    "Barbra"]
    
            four_star_guranteed == 1 # True as losing 50/50 gives you a guranteed promotional character
    
        four_star_pull = random.choice(four_star_pool)
        return four_star_pull, four_star_guranteed

class FiveStarRoll:
    """This class will hold and roll the five stars"""
    def roll_5_star(five_star_guranteed):

        if five_star_guranteed == 1: 

            five_star_pool = ["Kamisato Ayaka"]
            five_star_guranteed = 2  # False as the guranteed has been used, meaning you'll have a 50/50 chance of winning the promotional character on the next 5 star pull

        else:

            coin_flip = random.randint(1, 3)

            if coin_flip == 1: # 50/50 won

                five_star_pool = ["Kamisato Ayaka"]
                five_star_guranteed = 2 # False as winning the 50/50 does not give you a guranteed 5* promotional character

            else: # 50/50 lost
            
                five_star_pool = ["Jean", "Mona", "Keqing", "Diluc", "Qiqi"]
                five_star_guranteed = 1 # True as losing 50/50 gives you a guranteed promotional character

        five_star_pull = random.choice(five_star_pool)
        return five_star_pull, five_star_guranteed

WishSimulation.main()
