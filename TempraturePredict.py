import tensorflow as tf
#tf.logging.set_verbosity(tf.logging.ERROR)
import numpy as np

celsius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype = float)
fahrenheit_a = np.array([-40, -14, 32, 46, 59, 72, 100], dtype = float)

for i,c in enumrate (celsius_q):
    print("{}")