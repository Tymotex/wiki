import * as fs from 'fs';

fs.readFile('sample.txt', { encoding: 'utf8' }, (err, data) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(data);
});
