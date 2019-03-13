
import os
import json
import numpy as np

from raysect.core import Point2D, Point3D, Vector3D
from cherab.tools.observers.bolometry import BolometerCamera, BolometerSlit, BolometerFoil
from cherab.tools.inversions.voxels import ToroidalVoxelGrid


_DATA_PATH = os.path.split(__file__)[0]


def _load_csv(file):

    rows = []
    with open(file, 'r') as fh:
        lines = fh.readlines()
        for line in lines:
            if line:
                if line[0] == '#':
                    continue
                rows.append(line.strip().split(','))
    return rows


def load_bolometer(bolometer_id, parent=None):

    if bolometer_id == 'FDC':
        foils = _load_csv(os.path.join(_DATA_PATH, 'detectors/FDC_foils.csv'))
        slits = _load_csv(os.path.join(_DATA_PATH, 'detectors/FDC_slits.csv'))
    elif bolometer_id == 'FHC':
        foils = _load_csv(os.path.join(_DATA_PATH, 'detectors/FHC_foils.csv'))
        slits = _load_csv(os.path.join(_DATA_PATH, 'detectors/FHC_slits.csv'))
    elif bolometer_id == 'FHS':
        foils = _load_csv(os.path.join(_DATA_PATH, 'detectors/FHC_foils.csv'))
        slits = _load_csv(os.path.join(_DATA_PATH, 'detectors/FHC_slits.csv'))
    elif bolometer_id == 'FLH':
        foils = _load_csv(os.path.join(_DATA_PATH, 'detectors/FLH_foils.csv'))
        slits = _load_csv(os.path.join(_DATA_PATH, 'detectors/FLH_slits.csv'))
    elif bolometer_id == 'FLX':
        foils = _load_csv(os.path.join(_DATA_PATH, 'detectors/FLX_foils.csv'))
        slits = _load_csv(os.path.join(_DATA_PATH, 'detectors/FLX_slits.csv'))
    elif bolometer_id == 'FVC':
        foils = _load_csv(os.path.join(_DATA_PATH, 'detectors/FVC_foils.csv'))
        slits = _load_csv(os.path.join(_DATA_PATH, 'detectors/FVC_slits.csv'))
    else:
        raise ValueError("Unrecognised bolometer camera_id '{}'.".format(bolometer_id))

    num_slits = len(slits)
    num_foils = len(foils)

    bolometer_camera = BolometerCamera(name=bolometer_id, parent=parent)

    slit_objects = {}
    for i in range(num_slits):
        slit_data = slits[i]
        slit_id = str(slit_data[0])
        centre_point = Point3D(float(slit_data[1]), float(slit_data[2]), float(slit_data[3]))
        basis_x = Vector3D(float(slit_data[4]), float(slit_data[5]), float(slit_data[6])).normalise()
        basis_y = Vector3D(float(slit_data[7]), float(slit_data[8]), float(slit_data[9])).normalise()
        dx = float(slit_data[10])
        dy = float(slit_data[11])
        dz = float(slit_data[12])

        slit_objects[slit_id] = BolometerSlit(slit_id, centre_point, basis_x, dx, basis_y, dy, dz, parent=bolometer_camera)

    for i in range(num_foils):
        foil_data = foils[i]
        foil_id = str(foil_data[0])

        centre_point = Point3D(float(foil_data[1]), float(foil_data[2]), float(foil_data[3]))
        basis_x = Vector3D(float(foil_data[4]), float(foil_data[5]), float(foil_data[6])).normalise()
        basis_y = Vector3D(float(foil_data[7]), float(foil_data[8]), float(foil_data[9])).normalise()
        dx = float(foil_data[10])
        dy = float(foil_data[11])
        slit_id = str(foil_data[12])

        foil = BolometerFoil(foil_id, centre_point, basis_x, dx, basis_y, dy, slit_objects[slit_id],
                             parent=bolometer_camera)

        bolometer_camera.add_foil_detector(foil)

    return bolometer_camera


def load_voxel_grid(parent=None, name=None):

    directory = os.path.split(__file__)[0]
    voxel_grid_file = os.path.join(directory, "standard_grid.json")

    with open(voxel_grid_file, 'r') as fh:
        grid_description = json.load(fh)

    voxel_coordinates = []
    for voxel in grid_description['cells']:
        v1 = Point2D(voxel['p1'][0], voxel['p1'][1])
        v2 = Point2D(voxel['p2'][0], voxel['p2'][1])
        v3 = Point2D(voxel['p3'][0], voxel['p3'][1])
        v4 = Point2D(voxel['p4'][0], voxel['p4'][1])
        voxel_coordinates.append((v1, v2, v3, v4))

    voxel_grid = ToroidalVoxelGrid(voxel_coordinates, parent=parent, name=name)

    return voxel_grid


# A boolean mask array. Helps map cells in the original 2D AUG grid to the 1D CHERAB grid.
mask_file = os.path.join(os.path.split(__file__)[0], 'grid_mask.ndarray')
AUG_2D_TO_CHERAB_1D_GRID_MASK = np.load(open(mask_file, 'rb'))
