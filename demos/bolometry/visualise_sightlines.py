
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
from raysect.core import World
from raysect.primitive import Mesh
from raysect.optical import AbsorbingSurface

from cherab.tools.observers import find_wall_intersection
from cherab.aug.machine import plot_aug_wall_outline, import_aug_mesh
from cherab.aug.bolometry import FDC_TUBE, FLX_TUBE, FVC_TUBE, FHS_TUBE, load_default_bolometer_config


def plot_detectors(camera, world):

    plt.figure()
    plot_aug_wall_outline()

    for detector in camera.foil_detectors:

        centre_point = detector.centre_point
        sightline_vec = centre_point.vector_to(detector._slit.centre_point)

        try:
            intersection = find_wall_intersection(world, centre_point, sightline_vec)
            hit_point = intersection[0]
        except ValueError:
            hit_point = centre_point + sightline_vec.normalise() * 2

        # Traverse the ray with equation for a parametric line,
        # i.e. t=0->1 traverses the ray path.
        parametric_vector = centre_point.vector_to(hit_point)
        t_samples = np.arange(0, 1, 0.01)

        # Setup some containers for useful parameters along the ray trajectory
        ray_r_points = []
        ray_z_points = []

        # At each ray position sample the parameters of interest.
        for i, t in enumerate(t_samples):
            # Get new sample point location and log distance
            x = centre_point.x + parametric_vector.x * t
            y = centre_point.y + parametric_vector.y * t
            z = centre_point.z + parametric_vector.z * t
            ray_r_points.append(np.sqrt(x**2 + y**2))
            ray_z_points.append(z)

        plt.plot(ray_r_points, ray_z_points, 'k')
        plt.plot(ray_r_points[0], ray_z_points[0], 'b.')
        plt.plot(ray_r_points[-1], ray_z_points[-1], 'r.')

    plt.title(camera.name)


full_world = World()
import_aug_mesh(full_world, material=AbsorbingSurface())

fhc = load_default_bolometer_config('FHC', parent=full_world)
plot_detectors(fhc, full_world)

flh = load_default_bolometer_config('FLH', parent=full_world)
plot_detectors(flh, full_world)

fhs_world = World()
Mesh.from_file(FHS_TUBE[0], parent=fhs_world, material=AbsorbingSurface())
fhs = load_default_bolometer_config('FHS', parent=fhs_world)
plot_detectors(fhs, fhs_world)

fvc_world = World()
Mesh.from_file(FVC_TUBE[0], parent=fvc_world, material=AbsorbingSurface())
fvc = load_default_bolometer_config('FVC', parent=fvc_world)
plot_detectors(fvc, fvc_world)

fdc_world = World()
Mesh.from_file(FDC_TUBE[0], parent=fdc_world, material=AbsorbingSurface())
fdc = load_default_bolometer_config('FDC', parent=fdc_world)
plot_detectors(fdc, fdc_world)

flx_world = World()
Mesh.from_file(FLX_TUBE[0], parent=flx_world, material=AbsorbingSurface())
flx = load_default_bolometer_config('FLX', parent=flx_world)
plot_detectors(flx, flx_world)
