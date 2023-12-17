import json
import sys
from collections import defaultdict


class dd(defaultdict):
    def __missing__(self, __key):
        self[__key] = __key
        return __key


# def advent_of_code(file: list[str]):
def advent_of_code(file: str):
    ans_01 = 0
    print(ans_01)
    ans_02 = 0

    data = file.split("\n\n")
    # print("data:", json.dumps(data, indent=4))

    seeds = [int(s) for s in data[0].split(":")[1].split()]
    print("seeds:", seeds)

    location_data = [
        [[int(n) for n in i.split()] for i in data[j].split("\n")[1:]]
        for j in range(1, 8)
    ]
    # print("location_data:", json.dumps(location_data, indent=4))

    # seeds_to_soil = [i.split() for i in data[1].split("\n")[1:]]
    # print("seeds_to_soil:", seeds_to_soil)
    # soil_to_fertilizer = [i.split() for i in data[2].split("\n")[1:]]
    # print("soil_to_fertilizer:", soil_to_fertilizer)
    # fertilizer_to_water = [i.split() for i in data[3].split("\n")[1:]]
    # print("fertilizer_to_water:", fertilizer_to_water)
    # water_to_light = [i.split() for i in data[4].split("\n")[1:]]
    # print("water_to_light:", water_to_light)
    # light_to_temperature = [i.split() for i in data[5].split("\n")[1:]]
    # print("light_to_temperature:", light_to_temperature)
    # temperature_to_humidity = [i.split() for i in data[6].split("\n")[1:]]
    # print("temperature_to_humidity:", temperature_to_humidity)
    # humiditiy_to_location = [i.split() for i in data[7].split("\n")[1:]]
    # print("humiditiy_to_location:", humiditiy_to_location)

    location_map: list[dd] = []

    for location_data_set in location_data:
        loc_map = dd()

        for loc in location_data_set:
            source = loc[0]
            destination = loc[1]
            _range = loc[2]

            for _ in range(_range):
                ans_01 += 1
                print(ans_01)
                loc_map[destination] = source
                destination += 1
                source += 1

        location_map.append(loc_map)

    locations: list[int] = []
    lowest_location = sys.maxsize

    for seed in seeds:
        position = location_map[0][seed]
        for i in range(1, len(location_map)):
            ans_01 += 1
            print(ans_01)
            position = location_map[i][position]
        locations.append(position)

        lowest_location = min(lowest_location, position)

    print("locations:", locations)
    print("lowest_location:", lowest_location)

    print(" " * 3, "=" * 5, "PART_01:", ans_01, "=" * 5, "")
    print(" " * 3, "=" * 5, "PART_02:", ans_02, "=" * 5, "\n")


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print("\n", "#" * 10, file, "#" * 10)
        F = open(file).read().strip()
        advent_of_code(F)
