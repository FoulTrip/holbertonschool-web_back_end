export default function cleanSet(set, startString) {
  if (!set || !startString || typeof startString !== 'string') {
    return '';
  }
  const newArray = Array.from(set);
  const filtered = newArray.filter((item) => item.includes(startString));
  const cutBon = filtered.map((item) => item.slice(startString.length));
  return String(cutBon).replace(/,/g, '-');
}
