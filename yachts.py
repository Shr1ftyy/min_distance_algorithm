import numpy as np
import math
import matplotlib.pyplot as plt

'''
This example uses 3 yachts
'''

has_pos_list = False
pos = []# multi-dimensional list containing positions of every yacht over time
inc = 0.001 #increments
time_lim = 100# time limit
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

for t in x_s:
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

  # v_d = np.array([[-3],[2]]) + (accel*t)# Velocity with acceleration
  # D = np.array([[-1],[-1]]) + (v_d*t)# Position with acceleration
  # yachts.append(D)

  if not has_pos_list:
    for y in range(len(yachts)):
      pos.append([])
    has_pos_list = True

  for y in range(len(yachts)):
    pos[y].append(yachts[y])

  dist = distance(yachts)
  if t % 10 == 0:
    print(f"Time: {t} | Distance: {dist}")
  distances.append(dist)
 
minimum = min(distances) # Minimum distance between boats
time_min = distances.index(minimum)*inc # Timestamp of when boats are closest to each other
print(f"Min. distance is {minimum} when t = {time_min} : 0≤t≤{time_lim}")
fig, (dist_fun, yacht_vis) = plt.subplots(2)
dist_fun.scatter(time_min, min(distances), color='orange')
dist_fun.plot(x_s, distances)
dist_fun.plot([time_min for x in range(len(np.arange(0, max(distances), 1)))], np.arange(0, max(distances), 1))
dist_fun.set_title('Total Distance over Time')
dist_fun.set_xlabel('Time')
dist_fun.set_ylabel('Distance')

# yacht_vis = fig.add_subplot(121)

for p_yacht in range(len(pos)):
  yacht_vis.plot([pos[p_yacht][j][0][0] for j in range(len(pos[0]))], [pos[p_yacht][k][1][0] for k in range(len(pos[0]))])
  yacht_vis.scatter([pos[p_yacht][j][0][0] for j in range(len(pos[0]))][-1:], [pos[p_yacht][k][1][0] for k in range(len(pos[0]))][-1:])

yacht_vis.set_title('Position of Yachts')
yacht_vis.set_xlabel('x')
yacht_vis.set_ylabel('y')

plt.show()
