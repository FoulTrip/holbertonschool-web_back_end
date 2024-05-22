import getNeighborhoodsList from "./2-arrow";

test("returns the list of neig", () => {
  const neighborhoodsList = new getNeighborhoodsList();
  expect(neighborhoodsList.addNeighborhood("Tenderloin")).toEqual([
    "SOMA",
    "Union Square",
    "Tenderloin",
  ]);
});
