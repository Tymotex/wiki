interface Theme {
	colour: {
		mode: 'light' | 'dark';
		palette: {
			primary: string[];
			secondary: string[];
		};
	};
}

type ColourProperties = keyof Theme['colour'];              // → 'mode' | 'palette'
type PaletteProperties = keyof Theme['colour']['palette'];  // → 'primary' | 'secondary'
