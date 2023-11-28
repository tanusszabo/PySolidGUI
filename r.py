from solid import pysolid
import matplotlib.pyplot as plt

ps = pysolid.PySolid()
ps.set_coordinates(-22.811476100, 312.93596200)
ps.set_time_range('02/03/2028', date_format='%d/%m/%Y', days=7)
ps.tide_calculation()

ps.df_solid.to_csv("teste.csv")

ax = ps.df_solid.plot(x="date time", y=["north", "east", "radial"])
plt.legend(loc='best')
plt.show()