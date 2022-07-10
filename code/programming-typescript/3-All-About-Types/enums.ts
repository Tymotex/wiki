enum Theme {
	Light = '#CCCCCC',
	Dark = '#333333',
	HighContrastLight = '#FFFFFF',
	HighContrastDark = '#000000',
}

// You access the fields of the enum in the same way that you'd access an object.
const theme: Theme = Theme.HighContrastDark;

console.log(theme);
