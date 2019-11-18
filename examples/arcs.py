# #!/usr/bin/python
# import numpy as np
# import wxmplot.interactive as wi
#
# x = np.linspace(0.0, 20.0, 201)
# wi.plot_arc(x=0, y=0, width=20, height=20, angle=0, theta1=45, theta2=135)
# wi.plot(x, np.sin(x)/(x+1), ylabel='response',  xlabel='T (sec)')


#!/usr/bin/python
#

import wx
import math
import wxmplot


app = wx.App()

pframe = wxmplot.PlotFrame(output_title='Plot Multiple')
# pframe.add_arc(x=0, y=0, width=0.20, height=0.20, angle=0, theta1=math.radians(45), theta2=math.radians(135))
pframe.add_arc(0, 0, 0.20, 0.20, 0, 0, 90)

pframe.write_message('WXMPlot PlotFrame example: Try Help->Quick Reference')
pframe.Show()
#
app.MainLoop()

