from solid import solid_module
from numpy import pi, array, int32, float64
from pandas import DataFrame, to_datetime, concat
from datetime import date, datetime

class PySolid:
    def __init__(self):
        self.set_coordinates(0, 0)
        today = date.today()
        self.set_time_range(today, date_format='%Y-%m-%d')

    def set_coordinates(self, latitude, longitude):
        if not(-90<=latitude<=90): return print("Set a latitude value between -90.0 and 90.0")
        if not(-360<=longitude<=360): return print("Set a longitude value between -360.0 and 360.0")

        if longitude < 0.0:
            longitude += 360.0
        if longitude >= 360.0:
            longitude -= 360.0
        self.gla0 = latitude / (180.0 / pi)
        self.glo0 = longitude / (180.0 / pi)

    def set_time_range(self, date, date_format="%d/%m/%Y", daytime="00:00:00", daytime_format="%H:%M:%S", step=3600, days=1):

        try: self.date_obj = to_datetime(date, format=date_format)
        except Exception as e: return print(str(e))
        self.date = array([self.date_obj.year, self.date_obj.month, self.date_obj.day], int32)

        try: self.daytime_obj = to_datetime(daytime, format=daytime_format)
        except Exception as e: return print(str(e))
        self.daytime = array([self.daytime_obj.hour, self.daytime_obj.minute, self.daytime_obj.second], float64)

        self.time_step = step / 60.0 / 60.0 / 24.0
        self.step = step
        self.days = days
        


    def tide_calculation(self):

        rsun    = array([0.0, 0.0, 0.0], float64)
        rmoon   = array([0.0, 0.0, 0.0], float64)
        etide   = array([0.0, 0.0, 0.0], float64)
        xsta    = array([0.0, 0.0, 0.0], float64)
        vvt     = array([0.0, 0.0, 0.0], float64)
        mjda    = array([0]    , int32)
        fmjda   = array([0.0]  , float64)
        eht0    = 0.0
        gla0    = self.gla0
        glo0    = self.glo0
        date    = self.date
        daytime = self.daytime
        days    = self.days
        step    = self.step
        time_step = self.time_step
        self.df_solid = DataFrame({"date time": [], "seconds":[], "north":[], "east":[], "radial":[]})

        solid_module.fmodule.init_contants()
        solid_module.fmodule.geoxyz(gla0, glo0, eht0, xsta)

        solid_module.fmodule.civmjd(date, daytime, mjda, fmjda)
        solid_module.fmodule.mjdciv(mjda, fmjda, date, daytime)
        solid_module.fmodule.setjd0(date, mjda)

        for _ in range(0, 86400*days, int(step)):
            lflag = array([0], int32)
            solid_module.fmodule.sunxyz(mjda, fmjda, rsun, lflag)
            solid_module.fmodule.moonxyz(mjda, fmjda, rmoon, lflag)
            solid_module.fmodule.detide(xsta, mjda, fmjda, rsun, rmoon, etide, lflag)
            solid_module.fmodule.rge(gla0, glo0, vvt, etide[0], etide[1], etide[2])
            fmjda[0] += 0.001/86400.0
            daytime[2] -= 0.001
            solid_module.fmodule.mjdciv(mjda, fmjda, date, daytime)

            tsec = daytime[0] * 3600.0 + daytime[1] * 60.0 + daytime[2]
            daytime_forcado = daytime.astype(int)
            daytime_forcado[0] = daytime_forcado[0] % 24
            date_time = datetime(*date, *daytime_forcado).strftime("%d/%m/%Y %H:%M:%S")
            
            new_row = DataFrame({"date time": [date_time], "seconds":[tsec], "north":[vvt[0]], "east":[vvt[1]], "radial":[vvt[2]]})
            self.df_solid = concat([self.df_solid, new_row])
            fmjda[0] = int((fmjda[0]+time_step) * 86400.0) / 86400.0

        if lflag[0]:
            pass
        #     print('Mild Warning -- time crossed leap second table')
        #     print('  boundaries.  Boundary edge value used instead')

        # print('End Of Processing -------------------------------')
        return self.df_solid

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    ps = PySolid()
    ps.set_coordinates(-22.811476100, 312.93596200)
    ps.set_time_range('02/03/2028', date_format='%d/%m/%Y', days=7)
    ps.tide_calculation()
    ax = ps.df_solid.plot(x="date time", y=["north", "east", "radial"])
    print(ps.df_solid)
    plt.legend(loc='best')
    plt.show()