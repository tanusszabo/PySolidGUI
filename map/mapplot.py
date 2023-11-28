from geopandas import read_file
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

class MapCoordinates:
    def __init__(self):
        self.press = None
        self.motion = True
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None

    def init_plot(self, ax=None, figsize=(10,6), mapfile="map/mapfiles/ne_110m_admin_0_countries_lakes.dbf", x=0, y=0):
        if ax: fig = ax.get_figure()
        else: fig, ax = plt.subplots(figsize=figsize)
        fig.tight_layout()
        fig.subplots_adjust(0, 0, 1, 1)

        self.world = read_file(mapfile)
        self.world.plot(ax=ax, zorder=-1.0)
        self.gdfplot = ax.scatter(x, y, marker='o', color='red', s=15, zorder=3.0)

        acel_data = {"Sirius":  [-47.05231470, -22.80719940],
                     "LHC":     [  6.0499998,   46.2333324],
                     "MAX IV":  [ 13.233,       55.727],
                     "NSLS-II": [-72.872142,    40.865383],
                     "PETRA":   [  9.8837,      53.579049],
                     "Australian Synchrotron": [145.1426421, -37.9140752],
                     "NSRRC":   [120.99388,     24.7822],
                     "HiSOR":   [132.717511834, 34.40116078735],
                     "SSLS":    [103.776667,     1.295556],
                     "SESAME":  [35.736808,     32.11024050523],
                     "iThemba": [18.716,       -34.025],
                     "GAEC":    [-0.2194584051,  5.6781000252]}
        
        self.acel_data_points = [[xi for xi,_ in acel_data.values()], [yi for _,yi in acel_data.values()]]
        self.acel_data_names = list(acel_data.keys())
        self.gdfplot_back = ax.scatter(self.acel_data_points[0], self.acel_data_points[1], marker='*', color='black', s=50, zorder=2.0)
        self.annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)

        self.set_plot_limit(ax)
        ax.grid(True, linestyle='dotted', color='gray', zorder=1.0)
        ax.tick_params(axis="y", labelsize=8, direction="in", pad=-22)
        ax.tick_params(axis="x", labelsize=8, direction="in", pad=-15)
        
        self.zoom_factory(ax)
        self.pan_factory(ax)

    def show_plot(self):
        plt.show()

    def set_plot_limit(self, ax):
        ax.set_xlim((-180,180))
        ax.set_ylim((-90,90))

    def zoom_factory(self, ax, base_scale = 1.1):
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata
            ydata = event.ydata

            if event.button == 'up':     scale_factor = 1 / base_scale
            elif event.button == 'down': scale_factor = base_scale
            else:                        scale_factor = 1

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
            ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        fig = ax.get_figure()
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def place_point(self, ax, x, y):
        if not(-180 <= x <= 180) or not(-90 <= y<= 90): return

        self.gdfplot.remove()
        self.gdfplot = ax.scatter(x, y, marker='o', color='red', s=15, zorder=3.0)

    def get_point(self):
        return self.gdfplot.get_offsets()[0]

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press
            self.static = True

        def onRelease(event):
            if event.inaxes != ax: return
            self.press = None
            x, y = [None, None]
            if self.static:
                if event.button == MouseButton.RIGHT: self.set_plot_limit(ax)
                else:
                    cont, ind = self.gdfplot_back.contains(event)
                    if cont: x, y = self.gdfplot_back.get_offsets()[ind["ind"][0]]
                    else: x, y = event.xdata, event.ydata
                    if x and y: self.place_point(ax, x, y)
            self.static = True
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)
            self.static = False

            ax.figure.canvas.draw()

        def onHover(event):
            if event.inaxes != ax: return
            vis = self.annot.get_visible()
            cont, ind = self.gdfplot_back.contains(event)
            if cont:
                pos = self.gdfplot_back.get_offsets()[ind["ind"][0]]
                self.annot.xy = pos
                text = f"{' '.join([self.acel_data_names[n] for n in ind['ind']])}\nLat: {pos[1]}\nLon: {pos[0]}"
                self.annot.set_text(text)
                self.annot.get_bbox_patch().set_alpha(0.4)
                self.annot.set_visible(True)
            elif vis:
                self.annot.set_visible(False)
            ax.figure.canvas.draw()

        fig = ax.get_figure()

        fig.canvas.mpl_connect('button_press_event',onPress)
        fig.canvas.mpl_connect('button_release_event',onRelease)
        fig.canvas.mpl_connect('motion_notify_event',onMotion)
        fig.canvas.mpl_connect("motion_notify_event", onHover)


if __name__ == "__main__":

    zp = MapCoordinates()
    zp.init_plot()
    zp.show_plot()