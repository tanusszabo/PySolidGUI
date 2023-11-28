# MapCoordinates
## Overview
This Python script, mapplot.py, implements a simple interactive map visualization using ```GeoPandas``` and ```Matplotlib```. The script allows users to zoom in/out and pan across the map, as well as interact with specific data points.

## Dependencies
Ensure you have the required Python packages installed. You can install them using the following command:

```bash
pip install geopandas matplotlib
```

## Usage
To use the script, run it as the main module:

```bash
python mapplot.py
```
This will initialize a map with default settings and display it interactively. You can zoom using the scroll wheel and pan by clicking and dragging. Additionally, right-clicking resets the view, and left-clicking places a red marker at the clicked location.

Also, you could use it as a module, as in the example below:

```python
from mapplot import MapCoordinates
zp = MapCoordinates()
zp.init_plot()
zp.show_plot()
```

## Configuration
The script is designed to work with a world map shapefile, and the default map file is set to [mapfiles/ne_110m_admin_0_countries_lakes.dbf](map/mapfiles/ne_110m_admin_0_countries_lakes.dbf). You can change the map file by modifying the mapfile parameter in the ```init_plot``` method.

The map shapefiles was acquired from [https://www.naturalearthdata.com](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).

The script also includes predefined data points of accelerator facilities. You can customize this data in the ```acel_data``` dictionary. Each key-value pair represents the facility name and its corresponding longitude and latitude.

## Functionality
### Zooming
The script supports zooming in and out of the map using the scroll wheel. Scroll up to zoom in and down to zoom out.

### Panning
Pan the map by clicking and dragging. The current view can be reset to the initial limits by right-clicking on the map.

### Placing Markers
Left-click on the map to place a red marker at the clicked location. The marker represents a user-selected point on the map.

### Hover Information
Hovering over predefined data points (black markers) displays information about the facility, including its name, latitude, and longitude.

## Notes
Ensure that the map file exists in the specified location or provide the correct path.

Adjust the ```acel_data``` dictionary as needed for your specific data points.

The script uses ```GeoPandas``` for map plotting and ```Matplotlib``` for interactive visualization.

Feel free to explore and modify the script to suit your specific use case. If you encounter any issues or have suggestions for improvements, please let me know!

Enjoy exploring the interactive map!