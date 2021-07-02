# reward 2 jarak start ==================================
pusatx = -.5
pusaty = .5
dis = 21.5
car_trans = self.vehicle.get_transform()
dist = get_dist(pusatx,pusaty,car_trans.location.x,car_trans.location.y)
dist_proc = abs(dist-dis)
reward2 = 1/(dist_proc*10)
reward2 = min(1,reward2)
# reward 2 jarak end   ==================================
