
import matplotlib.pyplot as plt
from cherab.aug.machine.wall_outline import plot_aug_wall_outline
from cherab.aug.bolometry import load_voxel_grid


grid = load_voxel_grid()

plt.ion()
plot_aug_wall_outline()
grid.plot(ax=plt.gca())
plt.ioff()
plt.show()
