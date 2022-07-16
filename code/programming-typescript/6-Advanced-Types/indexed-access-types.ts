interface Theme {
	colour: {
		mode: 'light' | 'dark';
		palette: {
			primary: string[];
			secondary: string[];
		};
	};
}

type ColourOptions = Theme['colour'];
type Palette = Theme['colour']['palette'];
