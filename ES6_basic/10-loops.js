export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const idx of array) {
    // const value = array2[idx];
    // value = appendString + value;
    newArray.push(appendString + idx);
  }

  return newArray;
}
