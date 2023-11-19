import math

def main():
    time = 5          # time gap
    midpoint = time / 2 # describes midpoint of time
    vs = 26.8             # set speed
    v0 = 29             # initial speed
    if vs > v0:
        # accelerate
        mesh_data = []
        accel_mid = (vs - v0) / 2
        mesh_data = [accel_mid]
        y_val = accel_mid
        # build first part of acceleration mesh
        for i in range(int(midpoint * 10)):
            # scaling with time to ensure convergence
            y_val = y_val / ((time + 1) / time)
            mesh_data.insert(0, y_val)
        # This functions by taking the midpoint, and scaling it down repeatedly,
        # inserting smaller and smaller values in the front until it converges
        # to 0 (within tolerance)

        # Reset variables, declare second half of mesh
        y_val = accel_mid
        sec_mesh = []
        set_tmp = vs - v0
        # construct second half of acceleration mesh
        for i in range(int(midpoint * 10)):
            # remove next smallest increment obtained from set speed
            set_tmp = set_tmp - mesh_data[i]
            sec_mesh.insert(0, set_tmp)
            set_tmp = vs - v0
        # concatenate meshes to form one mesh with h = 0.1
        mesh_data = mesh_data + sec_mesh
        for i in range(int(time * 10)):
            print("(" + str(i * 0.1) + ", " + str(mesh_data[i]) + ")")
    elif vs < v0:
        # decel
        mesh_data = []
        decel_mid = (v0 - vs) / 2
        mesh_data = [decel_mid]
        y_val = decel_mid
        # build second half of mesh
        for i in range(int(midpoint * 10)):
            # scale with time
            y_val = y_val / ((time + 1) / time)
            mesh_data.append(y_val)
        # Reset variables, init first half of mesh
        y_val = decel_mid
        sec_mesh = []
        set_tmp = v0 - vs
        mesh_data.reverse()
        # reversed to obtain smallest values first
        for i in range(int(midpoint * 10)):
            # similar in construction to first
            set_tmp = set_tmp - mesh_data[i]
            sec_mesh.append(set_tmp)
            set_tmp = v0-vs
        # Reversed such that it decays from midpoint again
        mesh_data.reverse()
        # Concatenate meshes
        mesh_data = sec_mesh + mesh_data
        for i in range(int(time * 10)):
            print("(" + str(i * 0.1) + ", " + str(mesh_data[i]) + ")")
    elif vs == v0:
        print("Nothing to do!")



if __name__ == "__main__":
    main()
