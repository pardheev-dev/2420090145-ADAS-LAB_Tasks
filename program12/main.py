# PROGRAM 12: Driver Attention Monitoring System
# Generates an alert when the driver's eye closure duration exceeds a threshold.

threshold = 1.5     # seconds of continuous eye closure before alerting

# Eye closure duration measured for each frame window (in seconds)
closure_durations = [0.15, 0.20, 0.60, 1.20, 1.60, 2.40, 3.10, 0.18]

for duration in closure_durations:

    if duration < threshold * 0.5:
        level = "ATTENTIVE"
        alert = "-"
    elif duration < threshold:
        level = "DISTRACTED"
        alert = "Eyes on the road"
    elif duration < threshold * 2:
        level = "DROWSY"
        alert = "ALERT: DRIVER ATTENTION REQUIRED"
    else:
        level = "ASLEEP"
        alert = "CRITICAL ALERT: PULL OVER SAFELY"

    print(f"Eye closure: {duration:4.2f} s  ->  {level:11s} | {alert}")
