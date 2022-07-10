type Greeting = (a: string, b: string) => void;

// Note that the parameter names above don't need to match that of the assigned 
// callback's parameter names, they're purely for documentation.
const callback: Greeting = (name, message) => {
    console.log(`Hi, I'm ${name}. ${message}`);
}

callback("Linus", "F*** you, Nvidia.");
