# TFLN PDK

A PSI Python library for generating PDK elements programmatically in KLayout.


## Goals

This library utilizes the generic PDK from [GDS Factory](https://gdsfactory.github.io/gdsfactory/index.html). The new PDK is developed with existing elements to generate PSI designs while maintaining customizability.

Many of the generic elements are nearly ready to be used in PSI designs. The PSI_PDK library makes minor tweaks to the default parameters of these elements, i.e. the length of mmi, the waveguide width, etc.

Other more advanced elements, such as a star coupler, are not shipped with GDS factory and are implemented in this library from scratch.

## Poetry

As of version 0.2 (7/2/2024) we have begun using [Poetry](https://python-poetry.org/docs/) as our package manager. Please see the website to learn how to install this package which will ensure all code can be run on everyone's machine using identical dependency versions. To download, you must use [pipx](https://pipx.pypa.io/stable/installation/) which in turn must be installed using [scoop](https://scoop.sh/) on the Powershell. All of this can be found by following the Poetry website.

This project only requires the correct version of python and GDS Factory (7.22) to run. Poetry will ensure that all users of this software will be able to run the code without any hiccups.

## Getting Started

Ensure you download [Poetry](https://python-poetry.org/docs/) on your machine. After pulling the repository to a local folder, navigate to the directory in a command prompt and run ``` poetry install ```. This will gather all of the packages necessary for you to run the project in a virtual environment. Then, type ``` poetry run python test.py ``` in the same command window to open a new virtual environment. Make sure to have KLayout open with Klive and GDSFactory plugins installed. ``` test.py ``` is a "dummy" script that I have used to pull in new designs, but we can make new sandbox files in the future. Just be sure the file that you are running has a line to show() the designs in KLayout so that you can see your results.

## Structure

### Main Files

The first of the two main files of interest in the root directory is [config.py](./config.py), which should be looked through and possibly changed. Config contains all of the layer maps as well as typical geometry values used in our modulator designs of the past. If you pull in config.py to every device file you make, you can easily pass in the geometries, etc. as parameters from this file, rather than needing to memorize and/or check old KLayout designs for the right values...  

i.e. instead of

``` layer = (1, 0) ```

use this

```
import config as cf
...
layer = cf.SIN_WG_LAYER
```

The other file of interest is [test.py](./test.py), which I have used thus far as an effective sandbox for testing all of my block/device designs. This file is essentially just a window to KLayout, and I would recommend everyone use this as such moving forward.

[PSI_PDK.py](./PSI_PDK.py) should largely be ignored for now as it contains useful designs that need to be migrated to new files in either [blocks](./psi_elements/blocks/) or [devices](./psi_elements/devices/) for better organization.

### Folder Organization

The main folder for developing the elements is [psi_elements](./psi_elements/)

Within psi_elements are [blocks](./psi_elements/blocks/) and [devices](./psi_elements/devices/) which correspond to smaller elements and full devices, respectively. For illustration, the blocks folder contains building blocks like mmi's, unit cells for segmented electrodes, and simple grating couplers, while devices will contain full MZM designs that utilize the blocks.

So far, this PDK contains preliminary programmatically-defined designs for the following elements:

**mmi_1x2**

Creates 3-port mmi coupler in either nitride loaded or ridge for either handle. Can adjust taper length and width, mmi region length and width, and length of straights after tapers, along with gap between output tapers.

![mmi1x2sin](./photos/mmi1x2.png)

**mmi_1x2_sbend**

Creates 3-port mmi coupler with s-bends extending from output ports whose x/y geometries can be varied.

![mmi1x2sbend](./photos/mmi_1x2_sbend.png)

**mmi_2x2**

Creates a 4-port mmi coupler in either nitride loaded or ridge for either handle. Can adjust all geometries as with the 1x2 mmi.

![mmi2x2ridge](./photos/mmi_2x2.png)

**mmi_2x2_sbend**

Creates a 4-point mmi coupler in either nitride loaded or ridge for either handle with customizable s-bend geometries for input and output sides.

![mmi2x2sbend](./photos/mmi_2x2_sbend.png)

**create_electrode_Ucell**

Creates a unit cell for our segmented electrodes that can easily be used to generate an array for a full push-pull device. Full customization of the electrode geometry is available, including 'T' width, gaps, and periodicity of the cells.

![electrodeucell](./photos/create_electrode_ucell.png)

**grating_coupler**

Creates a tapered grating coupler with options for changing taper length, grating width, and waveguide width.

![gratingcoupler](./photos/grating_coupler.png)


Many of the files are currently incomplete, as should be evident from the sparse/nonexistent code. Feel free to start contributing!


## Future Actions

Updated documentation for all parameters is necessary before enabling PDK for interested parties.

- Name parameter for each device
- Add ability to easily design for SiN loaded / Ridge on Qz / Si handle and easily define 22 vs 40mm device (and custom length subject to DRC)
- Add launch pads for electrodes
- Add ports for everything (maybe a low priority right now)
- For full device, add VTC coupler region, SiN to LiNbO3 transition region, dicing kerfs, chip boundary, oxide cladding
- Make sure everything is on proper layer
- Alignment marks
- Fill pattern - automate fill pattern on wafer and chip scale for everything outside of devices
- Determine how to add ports to end of an array of references if necessary


## Important

If you choose to contribute to the PSI_PDK, please heavily document your code. I am working on a contributing.md file to provide a tutorial for best practices so that we can keep our library clean. In the meantime, the PSI_PDK.py file has a few examples.

