// Unlike in languages like Python, TypeScript tuples' items can be reassigned.
// To prevent this, use the `readonly` modifier.

type Coordinate = readonly [number, number];
const point: Coordinate = [1, 2];

point[0] = 3; // Error.
