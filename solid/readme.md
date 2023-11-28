# PySolid
PySolid is a Python library that provides an interface for performing ground displacement calculations due to tidal effects based on the Solid code, created by Dennis Milbert. The original Fortran code has been adapted and incorporated into this library, enabling easy integration with Python.

## Installation
Before using PySolid, it is necessary to install the numpy and pandas libraries:

```bash
pip install numpy pandas
```

## How to Use
Below is a basic example of how to use PySolid to calculate ground displacement and generate a plot.

```python
from pysolid import PySolid
import matplotlib.pyplot as plt

# Create an instance of PySolid
ps = PySolid()

# Set coordinates (latitude and longitude)
ps.set_coordinates(-22.80719940, -47.05231470)

# Set the time range (start date, date format, calculation days)
ps.set_time_range('02/03/2028', date_format='%d/%m/%Y', days=7)

# Perform the ground displacement calculation
ps.tide_calculation()

# Save the DataFrame to a CSV file
ps.df_solid.to_csv("output.csv")

# Display the plot
ax = ps.df_solid.plot(x="date time", y=["north", "east", "radial"])
plt.legend(loc='best')
plt.show()
```

Make sure to adjust the coordinates and time range as needed for your application.

## Results
The tide_calculation() method returns a pandas DataFrame containing the following columns:

- ```date time```: Date and time in the "dd/mm/yyyy hh:mm:ss" format.
- ```seconds```: Time in seconds since the start of the calculation.
- ```north```: Ground displacement in the north direction.
- ```east```: Ground displacement in the east direction.
- ```radial```: Ground displacement in the radial direction.
You can use these results for further analysis or save them to a file for future reference.

## Contributions
Contributions are welcome! Feel free to open issues or send pull requests to improve PySolid.

## Contact
For more information or questions, please contact the creator Tanus Szabo (tanus.szabo@cnpem.br).

Have a great day!