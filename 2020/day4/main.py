def input_iterator(input_file_path, string=""):
    input_file = open(input_file_path, "r")
    input_arr = []

    while (contents := input_file.read()) :
        passports = contents.split("\n\n")
        for passport in passports:
            input_arr.append(passport)
    return input_arr


def create_passports_from_input(input_arr):
    passports = []
    for elem in input_arr:
        passport = {}
        for field in elem.split():
            field_key, field_value = field.split(":")
            passport[field_key] = field_value
        passports.append(passport)
    return passports


def valid_byr(byr):
    try:
        byr = int(byr)
    except Exception:
        return False
    else:
        return 1920 <= byr <= 2002


def valid_iyr(iyr):
    try:
        byr = int(iyr)
    except Exception:
        return False
    else:
        return 2010 <= byr <= 2020


def valid_eyr(eyr):
    try:
        eyr = int(eyr)
    except Exception:
        return False
    else:
        return 2020 <= eyr <= 2030


def valid_hgt(hgt):
    if hgt.endswith("in"):
        hgt = hgt.rstrip("in")
        try:
            hgt = int(hgt)
        except Exception:
            return False
        else:
            return 59 <= hgt <= 76

    if hgt.endswith("cm"):
        hgt = hgt.rstrip("cm")
        try:
            hgt = int(hgt)
        except Exception:
            return False
        else:
            return 150 <= hgt <= 193

    return False


def valid_hcl(hcl):

    if not hcl.startswith("#"):
        return False

    hcl = hcl.lstrip("#")
    try:
        int(hcl, 16)
    except Exception:
        return False
    else:
        return True


def valid_ecl(ecl):
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def valid_pid(pid):
    if len(pid) != 9:
        return False

    try:
        int(pid)
    except Exception:
        return False

    return True


def validate_passports(passports):
    required_fields = {
        "byr": valid_byr,
        "iyr": valid_iyr,
        "eyr": valid_eyr,
        "hgt": valid_hgt,
        "hcl": valid_hcl,
        "ecl": valid_ecl,
        "pid": valid_pid,
        #        "cid",
    }
    valid_count = 0
    for pp in passports:
        missing = set(required_fields.keys()) - set(pp.keys())
        if missing != set():
            continue
        for k, v in required_fields.items():
            if not v(pp[k]):
                print(k, pp[k])
                break
        else:
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    pp_data = create_passports_from_input(
        input_iterator("/Users/john/random/advent_of_code/2020/day4/test_input")
    )
    print(validate_passports(pp_data))
    pp_data = create_passports_from_input(
        input_iterator("/Users/john/random/advent_of_code/2020/day4/input")
    )
    valid_p = validate_passports(pp_data)
    print(valid_p)
