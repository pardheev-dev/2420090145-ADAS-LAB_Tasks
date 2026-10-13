# PROGRAM 10: Adaptive Cruise Control (ACC) System
# Adjusts the vehicle speed according to the distance from the vehicle ahead.

set_speed = 80.0        # speed set by the driver (km/h)
current_speed = 80.0    # current vehicle speed (km/h)
time_gap = 1.8          # desired following time gap (seconds)

# Distance to the vehicle ahead (in metres), one reading per cycle
distances = [120.0, 90.0, 65.0, 45.0, 30.0, 18.0, 10.0]

for distance in distances:

    safe_distance = (current_speed * 1000 / 3600) * time_gap

    if distance > safe_distance * 1.5:
        action = "ACCELERATE"
        current_speed = min(current_speed + 5, set_speed)
    elif distance > safe_distance:
        action = "MAINTAIN SPEED"
    elif distance > safe_distance * 0.5:
        action = "DECELERATE"
        current_speed = max(current_speed - 8, 0)
    else:
        action = "BRAKE HARD"
        current_speed = max(current_speed - 20, 0)

    print(f"Gap: {distance:6.1f} m (safe {safe_distance:5.1f} m)  ->  {action:15s} speed = {current_speed:5.1f} km/h")
