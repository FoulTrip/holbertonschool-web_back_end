export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Array.isArray(students)) {
    const newArray = students.filter((value) => value.location === city);
    const arraUpdate = newArray.map((value) => {
      const obj = newGrades.find((val) => val.studentId === value.id);
      if (obj) {
        /* eslint-disable no-param-reassign */
        value.grade = obj.grade;
      } else {
        /* eslint-disable no-param-reassign */
        value.grade = 'N/A';
      }
      return value;
    });
    return arraUpdate;
  }
  return NaN;
}
