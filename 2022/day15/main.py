from collections import namedtuple
import string

pos = namedtuple("pos", ["x", "y"])


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.split(" ") for l in input_file.read().split("\n")]


def parse_sensors_and_beacons(raw):
    final = []
    for r in raw:
        parts = [
            int(p.split("=")[1].translate(str.maketrans("", "", ":,")))
            for p in [r[2], r[3], r[8], r[9]]
        ]
        final.append(parts)
    return [(pos(i[0], i[1]), pos(i[2], i[3])) for i in final]


# TODO: get negative vals
def get_grid_dimensions(beacons_sensors):
    x = -float("inf")
    y = -float("inf")
    for beacon, sensor in beacons_sensors:
        x = max(x, beacon.x)
        y = max(y, beacon.y)
        x = max(x, sensor.x)
        y = max(y, sensor.y)
    return x, y


if __name__ == "__main__":
    print("# part 1------------------")
    beacon_sensors = parse_sensors_and_beacons(get_input("test_input"))
    x, y = get_grid_dimensions(beacon_sensors)
    print(x, y)
