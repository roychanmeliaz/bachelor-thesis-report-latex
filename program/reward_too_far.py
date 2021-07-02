# Punishment 1 jarak start ==============================
reward3 = 0
pusatx = -.5
pusaty = .5
car_trans = self.vehicle.get_transform()
dist = get_dist(pusatx,pusaty,car_trans.location.x,car_trans.location.y)
if dist > 30:
    reward3 = -0.5
# Punishment 1 jarak end   ==============================
