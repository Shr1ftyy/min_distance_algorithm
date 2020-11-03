import numpy as np
import math
import matplotlib.pyplot as plt

'''
This example uses 3 yachts
'''

inc = 0.01 #increments
t = 0 # time
time_lim = 10 # time limit
distances = [] # Distance values
x_s = np.arange(0, time_lim+inc, inc) # All values of time when relevant computations are performed

def distance(yachts):
  total_dist = 0 # Total distance between each unique pair of boat
  # This function traverses through the list of yachts in combinatorial fashion, so it traverses (n!/(n-r)!r!) times
  for i in range(len(yachts)):
    for j in range(i+1, len(yachts)):
      d = math.sqrt((yachts[i][0] - yachts[j][0])**2 + (yachts[i][1] - yachts[j][1])**2) # Distance formula
      total_dist += d  
  return total_dist

while t<=time_lim:
  yachts = []

  accel = np.array([[0.1],[0.2]])
  v_a = np.array([[-2],[3]]) + (accel*t)# Velocity with acceleration
  A = np.array([[1],[2]]) + (v_a*t)# Position with acceleration
  yachts.append(A)

  v_b = np.array([[3],[-2]]) + (accel*t)# Velocity with acceleration
  B = np.array([[-4],[3]]) + (v_b*t)# Position with acceleration
  yachts.append(B)

  v_c = np.array([[1],[-1]]) + (accel*t)# Velocity with acceleration
  C = np.array([[-5],[1]]) + (v_c*t)# Position with acceleration
  yachts.append(C)

  dist = distance(yachts)
  print(f"Time: {t} | Distance: {dist}")
  distances.append(dist)
  t += inc
 
minimum = min(distances) # Minimum distance between boats
time_min = distances.index(minimum)*inc # Timestamp of when boats are closest to each other
print(f"Min. distance is {minimum} when t = {time_min} : 0≤t≤{time_lim}")
# plt.scatter(np.arange(0, time_lim+inc, inc), distances)
plt.scatter(time_min, min(distances), color='orange')
plt.plot(x_s, distances)
plt.plot([time_min for x in range(len(np.arange(0, max(distances), 1)))], np.arange(0, max(distances), 1))
plt.title('Total Distance over Time')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.show()
