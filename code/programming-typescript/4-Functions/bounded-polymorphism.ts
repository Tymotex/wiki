type Enemy = { health: number };
type Alien = Enemy & { galaxy: string };
type Cyborg = Enemy & { model: string };

type AttackEnemy = <T extends Enemy>(enemy: T, damage: number) => void;
const attackEnemy: AttackEnemy = <T extends Enemy>(enemy: T, damage: number) => {
	enemy.health -= damage;
	console.log(`Dealt ${damage}. Enemy now has ${enemy.health} HP left.`);
};

const enemy: Enemy = { health: 20 };
const alienEnemy: Alien = { health: 50, galaxy: 'Andromed' };
const cyborgEnemy: Cyborg = { health: 100, model: 'Terminator Mk. II' };
attackEnemy(enemy, 15);
attackEnemy(alienEnemy, 10);
attackEnemy(cyborgEnemy, 8);
// attackEnemy(null, 2);  // Error.
