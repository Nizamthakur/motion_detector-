from numpy import source
from motion_detector import df 
from bokeh.plotting import figure 
from bokeh.io import output_file, show
from bokeh.models import HoverTool,ColumnDataSource
df['start_time'] = df['Entered'].dt.strftime('%y-%m-%y %H:%M:%S')
df['end_time'] = df['Exited'].dt.strftime('%y-%m-%y %H:%M:%S')

cds = ColumnDataSource(df)
#Showing the graphs 
p = figure(width = 700, height = 200,  x_axis_type = "datetime", title = "motion graph")
q = p.quad(left = "Entered",right ="Exited",bottom =0  , top = 1 , color = "green", source = cds)
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1


#Hovaring effect 

hover = HoverTool(tooltips =[("Entered","@start_time"), ("Exited","@end_time")])
p.add_tools(hover)


output_file ("graph0.0.3.html")
show(p)