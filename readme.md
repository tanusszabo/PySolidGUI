# PySolidGUI: Graphical Interface for the Solid Program

PySolidGUI is a graphical interface based on the Solid code created by Dennis Milbert ([https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm)). It allows for the calculation of Earth displacement due to tidal effects on a specific day and terrestrial coordinates.

The interface is written in Python, using the PyQt5 library, while the backend for Earth displacement calculations is implemented in Fortran90, based on Dennis Milbert's original Fortran code. The main GUI is in Brazilian Portuguese, but with this tutorial you can use it perfectly.

The original Solid code was modified only in syntax to enable its use in communication with Python through Fortran90 subroutines. To understand its operation, refer to the Solid manual: [https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm).

If you wish to use the routines as a module, the file [pysolid.py](solid/pysolid.py) can be used. The tutorial/readme for its module usage can be found at [solid/readmeEn.md](solid/readmeEn.md). Also can [mapplot.py](map/mapplot.py), which the readme can be found at [map/readmeEn.md](map/readmeEn.md)

To stay updated, even I don't believing there will be updates, you can follow the project [here](https://github.com/tanusszabo/PySolidGUI). For more information, feel free to contact, Tanus Szabo (tanus.szabo@cnpem.br).

## Contributions
Contributions are welcome! Feel free to open issues or send pull requests to improve PySolid.

- Version 1.0
- Last update: 11/23/2023
- Creator: Tanus Szabo (tanus.szabo@cnpem.br)

---
# "Installation"
To use this software, you can clone this repository directly or use the git command to download the files:
``` bash
git clone https://github.com/tanusszabo/PySolidGUI
```

After obtaining the repository files, navigate to the folder where the files were downloaded and execute the main script, main.py, using the following command:
``` bash
python3 main.py
```

## Dependencies
Ensure you have the required Python packages installed, it is:
- ```PyQt5``` (GUI)
- ```pandas``` (data analysis)
- ```matplotlib``` (data visualization)
- ```numpy``` (just for the log function, you can remove, if you prefer)
- ```geopandas``` (geospatial analysis)

You can install them using the following command:

```bash
pip install PyQt5 pandas matplotlib numpy geopandas
```

---
# Tutorial
PySolidGUI uses parameters of days and terrestrial coordinates to calculate Earth displacement due to tidal effects, returning the latitudinal, longitudinal, and radial components of displacement in meters.

To perform the calculations, simply define a day or a set of days and the terrestrial coordinates.


## Configuration of Days

To set the start and end days for tide calculation, you can use the built-in calendar or the text boxes below.

### Calendar:

- Click to set a single initial day.
- Hold Shift and click to set a range of days.

### Text Boxes:

- You can set the initial or final days by typing the date in the format **day/month/year**.


## Configuration of Coordinates

To set the coordinates for tide calculation, you can use the interactive map or the text boxes below.

### Map:

- Click on the map to set the latitude and longitude.
- Some world accelerators have been highlighted and can be observed by hovering over them.
- To move the map, click and hold the left mouse button and drag. Use the mouse scroll wheel to zoom. Right-click to return the map to its original position.

### Text Boxes:

- You can set the latitude and longitude by typing in the text box. Values are in degrees, the decimal separator is a period ( **.** ), latitude ranges from -90 to 90, and longitude from -180 to 180.

## Graph

Select a day or a set of days and the desired coordinates for the graph. Click the **Plot** button, and the calculation will be performed, displaying the graph shortly.

The more days you select, the longer the calculation will take.

You can show or hide each of the components of Earth displacement (radial, latitudinal, and longitudinal) in the checkboxes above the graph.


## Save

To save the graph or graph data, use the **Save** button in the menu above.

### Save Data

Click **Save Data** to open a window and set the location and filename to save the data. The file will contain the first three lines with latitude, longitude, and days used in the calculations. The following lines will have the graph values, with each line representing a point and separated by:

    day and time, seconds from the start of the calculation, latitudinal component (north), longitudinal component (east), radial component (radial).

### Save Image

Click **Save Image** to open a window and set the location and filename to save the graph.

---

### Have a great day!
