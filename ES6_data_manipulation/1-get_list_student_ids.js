export default function getListStudentIds(arrayModel) {
  if (Array.isArray(arrayModel)) {
    return arrayModel.map((details) => details.id);
  }
  return [];
}
