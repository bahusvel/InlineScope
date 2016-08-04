import numpy as np

binary_array = np.fromfile("test/inline", dtype=np.uint8)

result = np.correlate(binary_array, binary_array, mode="same")
print(result)
