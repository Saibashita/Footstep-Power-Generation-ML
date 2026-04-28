import numpy as np

# Walking (medium variation)
walking = np.random.normal(50, 10, 1000)

# Running (higher variation)
running = np.random.normal(80, 20, 1000)

# Jumping (spikes)
jumping = np.random.normal(120, 30, 1000)

# Standing (low values)
standing = np.random.normal(5, 2, 1000)

# Save each activity to a file
np.savetxt("walking.txt", walking)
np.savetxt("running.txt", running)
np.savetxt("jumping.txt", jumping)
np.savetxt("standing.txt", standing)

print("Dataset created!")