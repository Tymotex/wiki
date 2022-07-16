interface EngineeringStudent {
	name: string;
	discipline: string;
}
interface FirstYearEngineeringStudent {
	name: string;
	discipline?: string;
}

const clearDiscipline = (student: FirstYearEngineeringStudent) => {
	delete student.discipline;
};

const csStudent: EngineeringStudent = { name: 'Linus', discipline: 'Computer Science' };
clearDiscipline(csStudent);

console.log(csStudent.discipline);
