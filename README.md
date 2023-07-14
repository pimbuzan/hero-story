# Hero Story App
# Author: Paul Imbuzan
## Built with
* Python 3.11

## Usage
python main.py

## Tests

pytest -s -v test.py

## Requirements

The Story
Once upon a time, there was a legendary hero known by any name you desire. This hero possessed unique strengths and weaknesses, as all heroes do. After engaging in countless battles against various monsters for over a century, the hero has acquired the following stats, which are generated upon summoning or initialization:

Health: 70 - 100
Strength: 70 - 80
Defence: 45 - 55
Speed: 40 - 50
Luck: 10% - 30% (0% indicates no luck, while 100% means being lucky all the time)
Additionally, the hero possesses two extraordinary skills:

Critical Strike: This skill enables the hero to strike twice during their turn to attack. There is a 10% chance of using this skill every time the hero attacks. If the skill is activated, there is an additional 1% chance of striking three times instead of two.
Resilience: When the hero defends, this skill allows them to endure only half of the usual damage inflicted by enemies. There is a 20% chance of utilizing this skill while defending, but it cannot be used two turns in a row.
Gameplay
As our hero traverses the enchanting forests of The Terminal Valley, they come across wicked villains with the following properties:

Health: 60 - 90
Strength: 60 - 90
Defence: 40 - 60
Speed: 40 - 60
Luck: 25% - 40%
Your task is to simulate battles between the hero and these nefarious villains. The battles can be executed either through the command line or a web browser. Each battle requires initializing the hero and villain with random properties within their respective ranges.

The first attack is conducted by the player with the higher speed. If both players have the same speed, the attacker is determined based on the highest luck attribute. After each attack, the roles of attacker and defender are swapped.

Damage inflicted by the attacker is calculated using the following formula:

Damage = Attacker strength - Defender defence
The defender's health is reduced by the calculated damage. However, there is a chance for the attacker to miss and deal no damage if the defender gets lucky during that turn.

The hero's skills occur randomly based on their individual chances, so their impact must be considered on each turn.

Game Over
The game concludes when one of the players runs out of health or when the number of turns reaches 20.

At the end of each turn, the application should display the following information: the events of the turn, any skills used, the damage inflicted, and the remaining health of the defender.

If a winner emerges before reaching the maximum number of rounds, they must be declared as the victor.

Rules
Write your code in plain Python (you can utilize third-party libraries or frameworks if desired).
Ensure that your application is decoupled, features reusable code, and is scalable. For example, adding a new skill to our hero should be straightforward.
Thoroughly test your code and make sure it is free of bugs.