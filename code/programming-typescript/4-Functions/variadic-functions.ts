const max = (...nums: number[]): number => {
	if (!nums || nums.length === 0) return -Infinity;
	return nums.reduce((maxSoFar, currNum) => (maxSoFar > currNum) ? maxSoFar : currNum, -Infinity);
}

console.log(max(5, 3, 1, 10, 3, 11, 5, 9));
