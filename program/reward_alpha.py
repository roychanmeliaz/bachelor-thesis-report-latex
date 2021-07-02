pusatx = -.5
pusaty = .5
car_trans = self.vehicle.get_transform()
dist = get_dist(pusatx,pusaty,car_trans.location.x,car_trans.location.y)

# mencari waypoint terdekat
jarak_min = 1000.0
for i, waypoint in enumerate(self.bunderan_waypoints):
    jarak_temp = get_dist(car_trans.location.x,car_trans.location.y,waypoint[0],waypoint[1])
    if jarak_temp<=jarak_min:
        nearest_id = i
        jarak_min = jarak_temp
if nearest_id==95:
    done = True

# reward
target_id = min(100,nearest_id+5)
angle_to_target = angle_of_line(car_trans.location.x,car_trans.location.y,self.bunderan_waypoints[target_id][0],self.bunderan_waypoints[target_id][1])
alpha = abs(angle_difference(car_yaw,angle_to_target))
reward = 1/alpha
reward = min(1,reward)