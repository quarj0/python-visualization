import requests
from tkinter import *
import tkinter as tk
from matplotlib import markers
from tkinter.ttk import *
from tkintermapview import TkinterMapView as tkv

# root = Tk()
# root.title("Test Map")
# root.geometry(f"{800}x{600}")

# mapWidget = tkv(root, width=800, height=600, corner_radius=0)

# mapWidget.place(relx=0.5, rely=0.5, anchor=CENTER)

# # mapWidget.set_address("University of Cape Coast",marker=True)
# mapWidget.set_position(5.1187091, -1.2981071, "Oye Inn Hostel", marker=True)
# mapWidget.set_marker(5.1098743, -1.2948525,"College of Agricultural and Natural Science")
# mapWidget.set_marker(5.1113635, -1.2957418, "Amisah Arthur Language Theatre")
# mapWidget.set_marker(5.1204066, -1.2962282, "College of Distance Education")
# mapWidget.set_marker(5.1224212, -1.29755, "New Lecture Theatre")
# mapWidget.set_path()
#
#
# def search_items():
#     search_value = variable.get()
#     if search_value == "" or search_value == " ":
#         combo['values'] = item_names
#     else:
#         value_to_display = []
#         for value in item_names:
#             if search_value in value:
#                 value_to_display.append(value)
#         combo['values'] = value_to_display
#
# item_names = list([str(a) for _ in range(100) for a in range(10)])
#
# combo = Combobox(root, state='readonly')
# combo['values'] = item_names
# combo.pack(side=LEFT)
#
# variable = StringVar()
# entry1 = Entry(root, textvariable=variable)
# entry1.pack(side=LEFT)
#
# button = Button(root, text="search", command=search_items)
# button.pack(side=LEFT)
#
#
# root.mainloop()
# # '''
# # oye inn to nlt 5.1187091,-1.2981071
# # oye inn to IT department 5.1098743,-1.2948525
# # IT Depart to Amisah arthur 5.1113635,-1.2957418
# # Amisah to Code 5.1204066,-1.2962282
# # code to nlt 5.1224212,-1.29755
#
#
# # '''
#
#
# # points = [(5.1187091, -1.2981071), (5.1098743, -1.2948525), (5.1113635, -1.2957418), (5.1204066, -1.2962282), (5.1224212, -1.29755)]
#
#
# # url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=YOUR_API_KEY"
#
# # payload = {}
# # headers = {}
#
# # response = requests.request("GET", url, headers=headers, data=payload)
#
# # print(response.text)
# # def euclideanDistance(coordinate1, coordinate2):
# #     return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)
#
#
# # distances = []
# # for i in range(len(points)-1):
# #     for j in range(i+1, len(points)):
# #         distances += [euclideanDistance(points[i], points[j])]
# # print(min(distances))


# import matplotlib.pyplot as plt
# import numpy as np 
# import matplotlib.animation as mpla

# t= np.linspace(0, 2*np.pi, 100)
# s=np.sin(t)
# x=np.tan(s)
# y=np.cos(x)
# line, = plt.plot(x,t)
# def animate(i):
#     line.set_ydata(np.sin(t+i/50))
#     line.set_xdata(np.cos(y+i/50))
#     line.set_ydata(np.tan(s+i/50))
#     line.set_xdata(np.cos(x+i/50))
# anim = mpla.FuncAnimation(plt.gcf(), animate, interval=5)
# # plt.subplot(line)
# # plt.style.use('ggplot')
# plt.show()

# x= np.linspace(0,2*np.pi,100)
# y= np.cos(x)
#
# fig, ax = plt.subplots()
# ax.plot(x,y,color='green')
#
# fig.savefig("figure.pdf")
# fig.show()

















