# Tutorial

This is a tutorial on how to use the PySolidGUI graphical interface, based on Dennis Milbert's Solid program [https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm).

PySolidGUI uses time and Earth coordinates parameters to calculate Earth tide displacement. This calculation returns the latitudinal, longitudinal, and radial components of the Earth tide displacement in meters.

----
## Setting up the Time Frame
To set up the start and end times for the tide calculation, you can use the calendar or the text boxes below.

### Calendar:
Simply clicking will set a single start day.

Holding down Shift and clicking will set a time range.
### Text Boxes:
You can set the start or end days by writing the date in the format **day/month/year**.

----
## Setting up the Coordinates
To set up the coordinates for the tide calculation, you can use the interactive map or the text boxes below.
### Map:
Clicking on the map will set the latitude and longitude of where you clicked. Some accelerators around the world have been highlighted and can be observed by hovering the mouse over them.

If you want to move the map, by clicking and holding with the left mouse button, you can drag the position of the map. With the mouse scroll, you can zoom in and out. Right-clicking will return the map to its original position.
### Text Boxes:
You can set the latitude and longitude by typing them in the text box. The values are in degrees, the decimal separator is a period ( **.** ), not a comma ( **,** ), latitude ranges from -90 to 90, and longitude from -180 to 180.

----
## Graph
After selecting a single day or a time range, along with the coordinates for which you would like to plot the graph, simply click the **Plot** button and the calculation will be performed, with the graph appearing in a few moments.

The more days you select, the longer the calculation will take.

Each of the Earth tide displacement components, radial, latitudinal, and longitudinal, can be shown or hidden using the checkboxes above the graph.

----
## Save
To save the graph or the graph data, use the **Save** button in the menu above.
### Save Data
Clicking **Save Data** will open a window to define the location and name for saving the data.

The saved file will have the first 3 lines consisting of the latitude, longitude, and days used for the calculations, and the following lines will have the graph values, with each line representing a point, separated by:

    day and time, seconds from the start of the calculation, latitudinal component (north), longitudinal component (east), radial component (radial).
### Save Image
Clicking **Save Image** will open a window to define the location and name for saving the graph.

For more information about the program, check the information in the **Help > About** menu, or contact the creator Tanus Szabo (tanus.szabo@cnpem.br).
