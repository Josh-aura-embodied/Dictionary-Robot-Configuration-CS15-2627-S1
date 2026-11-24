robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}
# 1. Access the name and model
print("Robot Name:", robot["name"])
print("Robot Model:", robot["model"])

# 2. Change battery to 100
robot["battery"] = 100

# 3. Add a new color
robot["color"] = "Blue"

# 4. Remove mode
robot.pop("mode")

# 5. Count dictionary entries
print("Total settings:", len(robot))

# 6. Display all remaining information
for key, value in robot.items():
    print(key, ":", value)
