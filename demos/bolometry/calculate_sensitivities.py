
import numpy as np
import matplotlib.pyplot as plt
from raysect.primitive import Mesh
from raysect.optical import World, AbsorbingSurface

from cherab.aug.machine import plot_aug_wall_outline, import_aug_mesh
from cherab.aug.bolometry import FDC_TUBE, FLX_TUBE, FVC_TUBE, FHS_TUBE
from cherab.aug.bolometry import load_bolometer, load_voxel_grid


plt.ion()


# Calculate FLX camera sensitivities
flx_world = World()
grid = load_voxel_grid(parent=flx_world)
Mesh.from_file(FLX_TUBE[0], parent=flx_world, material=AbsorbingSurface())
flx = load_bolometer('FLX', parent=flx_world)
for detector in flx:
    print('calculating detector {}'.format(detector.name))
    sensitivity = detector.calculate_sensitivity(grid)
    # np.save('{}_sensitivity'.format(detector.name), sensitivity)
    plt.figure()
    plot_aug_wall_outline()
    grid.plot(title=detector.name, voxel_values=sensitivity, ax=plt.gca())
input('waiting...')
plt.close('all')


# Calculate FDC camera sensitivities
fdc_world = World()
grid = load_voxel_grid(parent=fdc_world)
Mesh.from_file(FDC_TUBE[0], parent=fdc_world, material=AbsorbingSurface())
fdc = load_bolometer('FDC', parent=fdc_world)
for detector in fdc:
    print('calculating detector {}'.format(detector.name))
    sensitivity = detector.calculate_sensitivity(grid)
    # np.save('{}_sensitivity'.format(detector.name), sensitivity)
    plt.figure()
    plot_aug_wall_outline()
    grid.plot(title=detector.name, voxel_values=sensitivity, ax=plt.gca())
input('waiting...')
plt.close('all')


# Calculate FVC camera sensitivities
fvc_world = World()
grid = load_voxel_grid(parent=fvc_world)
Mesh.from_file(FVC_TUBE[0], parent=fvc_world, material=AbsorbingSurface())
fvc = load_bolometer('FVC', parent=fvc_world)
for detector in fvc:
    print('calculating detector {}'.format(detector.name))
    sensitivity = detector.calculate_sensitivity(grid)
    # np.save('{}_sensitivity'.format(detector.name), sensitivity)
    plt.figure()
    plot_aug_wall_outline()
    grid.plot(title=detector.name, voxel_values=sensitivity, ax=plt.gca())
input('waiting...')
plt.close('all')


# Calculate FHS camera sensitivities
fhs_world = World()
grid = load_voxel_grid(parent=fhs_world)
Mesh.from_file(FHS_TUBE[0], parent=fhs_world, material=AbsorbingSurface())
fhs = load_bolometer('FHS', parent=fhs_world)
for detector in fhs:
    print('calculating detector {}'.format(detector.name))
    sensitivity = detector.calculate_sensitivity(grid)
    # np.save('{}_sensitivity'.format(detector.name), sensitivity)
    plt.figure()
    plot_aug_wall_outline()
    grid.plot(title=detector.name, voxel_values=sensitivity, ax=plt.gca())
input('waiting...')
plt.close('all')


# # FHC and FLH use the full AUG mesh structure
# full_world = World()
# grid = load_voxel_grid(parent=full_world)
# import_aug_mesh(full_world, material=AbsorbingSurface())
#
# # Calculate FHC camera sensitivities
# fhc = load_bolometer('FHC', parent=full_world)
# for detector in fhc:
#     print('calculating detector {}'.format(detector.detector_id))
#     sensitivity = detector.calculate_sensitivity(grid)
#     # np.save('{}_sensitivity'.format(detector.name), sensitivity)
#     plt.figure()
#     plot_aug_wall_outline()
#     grid.plot(title=detector.name, voxel_values=sensitivity, ax=plt.gca())
# input('waiting...')
# plt.close('all')
#
# # Calculate FLH camera sensitivities
# flh = load_bolometer('FLH', parent=full_world)
# for detector in flh:
#     print('calculating detector {}'.format(detector.detector_id))
#     sensitivity = detector.calculate_sensitivity(grid)
#     np.save('{}_sensitivity'.format(detector.name), sensitivity)
#     plt.figure()
#     plot_aug_wall_outline()
#     grid.plot(title=detector.name, voxel_values=sensitivity, ax=plt.gca())
# input('waiting...')
# plt.close('all')
