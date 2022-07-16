interface UserTextEvent {
	type: 'TextEvent';
	value: string;
	target: HTMLInputElement;
}
interface UserMouseEvent {
	type: 'MouseEvent';
	value: [number, number];
	target: HTMLElement;
}

type UserEvent = UserTextEvent | UserMouseEvent;

const handle = (event: UserEvent): void => {
	if (event.type === 'TextEvent') {
		// At this point, TypeScript is certain that `event` is `UserTextEvent`.
		// ...
	} else {
		// At this point, TypeScript is certain that `event` is `UserMouseEvent`.
		// ...
	}
};
