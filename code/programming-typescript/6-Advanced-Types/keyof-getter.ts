interface Theme {
	colour: {
		mode: 'light' | 'dark';
		palette: {
			primary: string[];
			secondary: string[];
		};
	};
}

const theme: Theme = {
	colour: {
		mode: 'dark',
		palette: {
			primary: ['#0000FF', '#0044FF', '#0066FF', '#3388FF'],
			secondary: ['#464646', '#616161', '#7E7E7E', '#AAAAAA'],
		},
	},
};

const getPalette = (theme: Theme, palette: keyof Theme['colour']['palette']): string[] => {
	return theme['colour']['palette'][palette];
};

console.log(getPalette(theme, 'primary'));
