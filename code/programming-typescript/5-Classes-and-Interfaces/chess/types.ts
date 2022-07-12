type Colour = 'Black' | 'White';
type X = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H';
type Y = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8;
type Coordinate = { x: number; y: number };

// Core:
class Game {}

abstract class Piece {
	protected position: Position;

	constructor(private readonly colour: Colour, x: X, y: Y) {
		this.position = new Position(x, y);
	}

	public moveTo(position: Position): void {
		this.position = position;
	}

	public abstract canMoveTo(position: Position): boolean;
}

class Position {
	constructor(private x: X, private y: Y) {}

	public distanceFrom(position: Position) {
		return {
			x: Math.abs(position.x.charCodeAt(0) - this.x.charCodeAt(0)),
			y: Math.abs(position.y - this.y),
		};
	}
}

// Pieces:
class King extends Piece {
	public canMoveTo(position: Position): boolean {
		const distance = this.position.distanceFrom(position);
		return distance.x < 2 && distance.y < 2;
	}
}

// class Queen extends Piece {}
// class Bishop extends Piece {}
// class Knight extends Piece {}
// class Rook extends Piece {}
// class Pawn extends Piece {}
