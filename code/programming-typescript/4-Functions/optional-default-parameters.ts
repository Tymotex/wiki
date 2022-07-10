// Optional parameter.
const greet = (name: string, message?: string) => {
	console.log(`Hi ${name}!`);
    if (message) console.log(message);
}

// Default parameter. Notice that the parameter type can be inferred from the
// default value that you supply.
const greet = (name: string, message: string = "You rock.") => {
	console.log(`Hi ${name}! ${message}`);
}


greet("Linus Torvalds");
