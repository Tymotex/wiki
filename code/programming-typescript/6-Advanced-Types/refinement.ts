type CssWidth = number | string | undefined;

const getPixelWidth = (width: CssWidth): number => {
	// At this point, TypeScript knows `width` is `number | string | undefined`.
	if (typeof width === 'undefined') return 0;

	// At this point, TypeScript knows `width` is `number | string`
	if (typeof width === 'number') return width;

	// At this point, TypeScript knows `width` is `string`
	return Number(width.slice(0, width.search('px')));
};

console.log(getPixelWidth(undefined)); // 0
console.log(getPixelWidth(10)); // 10
console.log(getPixelWidth('480px')); // 480
