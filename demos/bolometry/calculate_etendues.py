
import numpy as np
import matplotlib.pyplot as plt
from raysect.optical import World

from cherab.aug.bolometry import load_bolometer


world = World()
fvc = load_bolometer('FVC', parent=world)
flx = load_bolometer('FLX', parent=world)
fdc = load_bolometer('FDC', parent=world)
fhs = load_bolometer('FHS', parent=world)
flh = load_bolometer('FLH', parent=world)
fhc = load_bolometer('FHC', parent=world)


plt.ion()

fvc_etendues = []
fvc_etendue_errors = []
for detector in fvc:
    etendue, etendue_error = detector.calculate_etendue(ray_count=100000)
    fvc_etendues.append(etendue)
    fvc_etendue_errors.append(etendue_error)
    print(detector.name, 'etendue:', '{:.4G} +- {:.2G} m^2 str'.format(etendue, etendue_error))
plt.figure()
plt.errorbar(np.linspace(1, len(fvc_etendues), len(fvc_etendues)), fvc_etendues, fvc_etendue_errors)
plt.xlabel('Detector Index')
plt.ylabel('Detector etendue (m^2 str)')
plt.legend()
plt.title('FVC etendues')


flx_etendues = []
flx_etendue_errors = []
for detector in flx:
    etendue, etendue_error = detector.calculate_etendue(ray_count=100000)
    flx_etendues.append(etendue)
    flx_etendue_errors.append(etendue_error)
    print(detector.name, 'etendue:', '{:.4G} +- {:.2G} m^2 str'.format(etendue, etendue_error))
plt.figure()
plt.errorbar(np.linspace(1, len(flx_etendues), len(flx_etendues)), flx_etendues, flx_etendue_errors)
plt.xlabel('Detector Index')
plt.ylabel('Detector etendue (m^2 str)')
plt.legend()
plt.title('FLC etendues')


fdc_etendues = []
fdc_etendue_errors = []
for detector in fdc:
    etendue, etendue_error = detector.calculate_etendue(ray_count=100000)
    fdc_etendues.append(etendue)
    fdc_etendue_errors.append(etendue_error)
    print(detector.name, 'etendue:', '{:.4G} +- {:.2G} m^2 str'.format(etendue, etendue_error))
plt.figure()
plt.errorbar(np.linspace(1, len(fdc_etendues), len(fdc_etendues)), fdc_etendues, fdc_etendue_errors)
plt.xlabel('Detector Index')
plt.ylabel('Detector etendue (m^2 str)')
plt.legend()
plt.title('FDC etendues')


fhs_etendues = []
fhs_etendue_errors = []
for detector in fhs:
    etendue, etendue_error = detector.calculate_etendue(ray_count=100000)
    fhs_etendues.append(etendue)
    fhs_etendue_errors.append(etendue_error)
    print(detector.name, 'etendue:', '{:.4G} +- {:.2G} m^2 str'.format(etendue, etendue_error))
plt.figure()
plt.errorbar(np.linspace(1, len(fhs_etendues), len(fhs_etendues)), fhs_etendues, fhs_etendue_errors)
plt.xlabel('Detector Index')
plt.ylabel('Detector etendue (m^2 str)')
plt.legend()
plt.title('FHS etendues')


flh_etendues = []
flh_etendue_errors = []
for detector in flh:
    etendue, etendue_error = detector.calculate_etendue(ray_count=100000)
    flh_etendues.append(etendue)
    flh_etendue_errors.append(etendue_error)
    print(detector.name, 'etendue:', '{:.4G} +- {:.2G} m^2 str'.format(etendue, etendue_error))
plt.figure()
plt.errorbar(np.linspace(1, len(flh_etendues), len(flh_etendues)), flh_etendues, flh_etendue_errors)
plt.xlabel('Detector Index')
plt.ylabel('Detector etendue (m^2 str)')
plt.legend()
plt.title('FLH etendues')


fhc_etendues = []
fhc_etendue_errors = []
for detector in fhc:
    etendue, etendue_error = detector.calculate_etendue(ray_count=100000)
    fhc_etendues.append(etendue)
    fhc_etendue_errors.append(etendue_error)
    print(detector.name, 'etendue:', '{:.4G} +- {:.2G} m^2 str'.format(etendue, etendue_error))
plt.figure()
plt.errorbar(np.linspace(1, len(fhc_etendues), len(fhc_etendues)), fhc_etendues, fhc_etendue_errors)
plt.xlabel('Detector Index')
plt.ylabel('Detector etendue (m^2 str)')
plt.legend()
plt.title('FHC etendues')
