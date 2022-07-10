type Student = { id: string; degree: string };
type Tutor = { id: string; courses: string[] };

type StudentOrTutor = Student | Tutor; // Set of all objects that are either `Student`, `Tutor`, or both.
type StudentAndTutor = Student & Tutor; // Set of all objects containing all fields of `Student` AND `Tutor`.

const student: Student = { id: '111', degree: 'Bachelor of Science' };
const tutor: Tutor = { id: '222', courses: ['CS101'] };
const studentTutor: StudentAndTutor = {
	id: '333',
	degree: 'Bachelor of Computer Science',
	courses: ['CS201'],
};

// For `Student | Tutor`: you can assign any of: `Student`, `Tutor`, or `Student & Tutor`
const uniGoers: StudentOrTutor[] = [student, tutor, studentTutor];

// For `Student & Tutor`: you can only have people who are simultaneously `Student` and `Tutor`.
const studentTutors: StudentAndTutor[] = [studentTutor];
