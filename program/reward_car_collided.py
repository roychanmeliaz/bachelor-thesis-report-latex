# Jika kendaraan menyentuk obyek lain, selesaikan episode
# dan beri reward senilai -1
if len(self.collision_hist) != 0:
    done = True
    reward = -1
