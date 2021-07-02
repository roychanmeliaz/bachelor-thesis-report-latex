# reward 1 arah start ===================================
car_trans = self.vehicle.get_transform()
car_yaw = car_trans.rotation.yaw
roundabout_to_car = angle_of_line(pusatx,pusaty,car_trans.location.x, car_trans.location.y)
alpha = angle_difference(roundabout_to_car, car_yaw)
alpha += 90
alpha = abs(alpha)
# untuk sudut 180-270
if alpha>180:
    alpha = abs(-180 + (alpha-180))
if alpha!=0:
    reward1 = 1/alpha
reward1 = min(1,reward)
# reward 1 arah end   ===================================