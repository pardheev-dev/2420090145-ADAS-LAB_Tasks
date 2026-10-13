# PROGRAM 11: Lane Keeping Assist (LKA) System
# Recommends steering left, right or straight based on the lane offset value.

# Offset of the vehicle from the lane centre, in metres.
# Negative = drifting left, positive = drifting right.
offsets = [0.02, -0.15, -0.45, -0.80, 0.20, 0.55, 0.95]

dead_zone = 0.10        # ignore tiny offsets
warn_limit = 0.50       # beyond this the driver is warned

for offset in offsets:

    if abs(offset) <= dead_zone:
        steering = "STRAIGHT"
        status = "Centred in lane"
    elif offset < 0:
        steering = "STEER RIGHT"
        status = "Drifting LEFT"
    else:
        steering = "STEER LEFT"
        status = "Drifting RIGHT"

    if abs(offset) > warn_limit:
        status += " - LANE DEPARTURE WARNING"

    print(f"Offset: {offset:+5.2f} m  ->  {steering:12s} | {status}")
