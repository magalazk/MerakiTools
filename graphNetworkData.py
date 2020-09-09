import networkStatus
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row
from dateutil import parser



def graphMerakiTraffic(networkId, serial):
    netdata = networkStatus.getTrafficStats(networkId,serial) # returns json formatted meraki api response of network stats

    output_file = ("hour_graph.html")
    
    lossPlot = figure(
       tools="pan,box_zoom,reset,save",
       x_axis_type="datetime",
       x_axis_label="Percent Loss",
       y_axis_label="Hours",
       y_range=(0,100)
    )
    
    latencyPlot = figure(
       tools="pan,box_zoom,reset,save",
       x_axis_type="datetime",
       x_axis_label="Latency",
       y_axis_label="milliseconds"
    )
    
    # build the plot data
    
    xval = []
    y0val = []
    y1val = []
    
    for i in netdata: # loop through the traffic data and format it into bokeh plot structure
        xval.append(parser.parse(i["startTs"].replace("T"," ").strip("Z")))
        y0val.append(i["lossPercent"])
        y1val.append(i["latencyMs"])
    
    
    lossPlot.line(xval, y0val, legend_label="Loss percent", line_width=3,line_color="red")
    latencyPlot.line(xval, y1val, legend_label="latencyMs", line_width=3)
    
    
    show(row(lossPlot,latencyPlot))
