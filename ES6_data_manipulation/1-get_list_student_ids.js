export default function getListStudentIds(arrayModel) {
  if (arrayModel.isArray(arrayModel)) {
    return arrayModel.map((details) => details.id);
  }
  return [];
}
