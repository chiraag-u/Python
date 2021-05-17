import matplotlib.pyplot as Graph
Bars = [1, 2, 3, 4]
Production = [5, 13, 8, 20]
FontHeader = {'family':'Segoe UI', 'size':18}
FontAxis = {'family':'Segoe UI', 'size':15}
Labels = ['A Car', 'B Car', 'C Car', 'D Car']
Frame = Graph.figure(frameon=False)
Frame.canvas.toolbar.pack_forget()
Graph.bar(Bars, Production, tick_label = Labels, width = 0.5, color = ['#EF4D4D', '#42CCFF', '#42B983', '#FAE786'])
Graph.title('Car Production of Companies per Year (1 Unit = 1 Million)', **FontHeader)
Graph.xlabel('Cars', **FontAxis)
Graph.ylabel('Production', **FontAxis)
Graph.show()
