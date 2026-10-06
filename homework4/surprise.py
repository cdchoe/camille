# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
for name in targets.keys():
    print(name)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
for name in targets:
    print(name, targets[name]["Spectral Type"])

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_stars(targets):
    for name in targets:
        if targets[name]["Magnitude"] > 0.1:
            return(name)

print(find_stars(targets))

# 4) Look up another target, add all the necessary information to the targets list. 
# Procyon: RA = 07h 39m 18.1s, Dec = +05° 13′ 30″, Magnitude = 0.34, Spectral Type = F5IV-V
targets["Procyon"] = {"RA": "07h 39m 18.1s", "Dec": "+05° 13′ 30″", "Magnitude": 0.34, "Spectral Type": "F5IV-V"}
print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_star_closest_to_20(targets):
    closest_star = None
    closest_declination = float('inf')
    brightest_magnitude = float('inf')

    for name, info in targets.items():
        declination = float(info["Dec"][1:3].replace("°", ""))
        magnitude = info["Magnitude"]

        if abs(declination - 20) < closest_declination or (abs(declination - 20) == closest_declination and magnitude < brightest_magnitude):
            closest_declination = abs(declination - 20)
            brightest_magnitude = magnitude
            closest_star = name

    return closest_star

print(brightest_star_closest_to_20(targets))

# 6) What is your favorite constellation?
print("Orion")