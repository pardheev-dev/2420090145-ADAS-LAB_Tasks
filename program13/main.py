# PROGRAM 13: Automatic Emergency Braking (AEB) System
# Decides whether to apply emergency braking based on vehicle speed and obstacle distance.

reaction_time = 1.0     # driver reaction time in seconds
deceleration = 7.0      # braking deceleration in m/s^2

# (speed in km/h, obstacle distance in metres)
readings = [
    (40.0, 60.0),
    (40.0, 22.0),
    (60.0, 40.0),
    (60.0, 15.0),
    (80.0, 35.0),
    (100.0, 20.0),
]

for speed_kmph, distance in readings:

    speed_mps = speed_kmph * 1000 / 3600

    # Stopping distance = reaction distance + braking distance
    stopping_distance = speed_mps * reaction_time + (speed_mps ** 2) / (2 * deceleration)

    if distance > stopping_distance * 1.5:
        action = "NO ACTION - safe"
    elif distance > stopping_distance:
        action = "WARNING - obstacle ahead"
    elif distance > stopping_distance * 0.6:
        action = "PARTIAL BRAKING APPLIED"
    else:
        action = "EMERGENCY BRAKING APPLIED!"

    print(f"Speed: {speed_kmph:5.1f} km/h  Obstacle: {distance:5.1f} m  "
          f"Stopping: {stopping_distance:5.1f} m  ->  {action}")
