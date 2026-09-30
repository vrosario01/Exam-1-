import numpy as np
def estimate_pi(n):
  """
  positive number -> positive number
  n = number of randomly generated points estimate_pi estimates the value of pi using n randomly generated points,
  a larger n yields, on average, a better approximation of pi.
  >>> estimate_pi(100)
  3.52
  >>> estimate_pi(1000)
  3.12
  >>> estimate_pi(10_000)
  3.102
  >>> estimate_pi(10_000_000)
  3.141136
  >>> estimate_pi(100_000_000)
  """
  np.random.seed(10)
  ### use seed to get same number everytime
  inside_circ = []
  outside_circ = []

  for i in range(n):
    x = 2 * np.random.rand()
    y = 2 * np.random.rand()

    if (x - 1)**2 + (y-1)**2 <= 1:
      ### math: equation of circle = (x - h)**2 + (y - k)**2 = r**2
      inside_circ.append((x,y))
    else:
      outside_circ.append((x,y))

  inside_points = len(inside_circ)
  total_points = len(inside_circ) + len(outside_circ)
  pi = (inside_points/total_points) * 4

  return pi

