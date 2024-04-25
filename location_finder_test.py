from location_test_liqapi import check_if_reem
import atexit
import random
import time

pk = 'YOUR_API_KEY'  
accuracy = []
def save_accuracy():
    with open('accuracy.txt', 'w') as f:
        for item in accuracy:
            f.write("%s\n" % item)
def is_inside(vertices, xp, yp):
    cnt = 0
    for edge in vertices:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1):
            cnt += 1
    return cnt % 2 == 1

def onclick(event):
    xp, yp = event.xdata, event.ydata
    check = (check_if_reem(yp, xp, pk))
    if is_inside(edges, xp, yp):
        try:
            if check[0] is None:
                pass
            elif check[0] is True:
                plt.plot(xp, yp, "go", markersize=5)
                print('inside', check[1])
                accuracy.append('t')
            elif check[0] is False:
                plt.plot(xp, yp, "ro", markersize=5)
                print('inside', check[1])
                accuracy.append('f')
            else:
                plt.plot(xp, yp, "bo", markersize=5)
        except TypeError as e:
            pass
    else:
        try:
            if check[0] is None:
                pass
            elif check[0] is True:
                plt.plot(xp, yp, "ro", markersize=5)
                print('outside', check[1])
                accuracy.append('f')
            elif check[0] is False:
                plt.plot(xp, yp, "go", markersize=5)
                print('outside', check[1])
                accuracy.append('t')
            else:
                plt.plot(xp, yp, "bo", markersize=5)
        except TypeError as e:
            pass
    plt.gcf().canvas.draw()

def generate_random_point():
    # Generate random latitude and longitude within the range of existing coordinates
    random_lat = random.uniform(min(lats), max(lats))
    random_lon = random.uniform(min(lons), max(lons))
    return random_lat, random_lon

def plot_random_point():
    # Generate a random point and call the onclick function with its coordinates
    random_point = generate_random_point()
    onclick_data = type('Event', (object,), {'xdata': random_point[1], 'ydata': random_point[0]})
    onclick(onclick_data)

import matplotlib.pyplot as plt

# Example latitude and longitude values for the vertices of the polygon
lats = [24.51278, 24.49694, 24.48779, 24.47374, 24.49008, 24.49220, 24.50380, 24.51189]
lons = [54.39717, 54.39322, 54.39357, 54.41790, 54.42446, 54.41386, 54.41916, 54.40901]

# Create a list of tuples representing the vertices of the polygon
vertices = list(zip(lons, lats))
vertices.append(vertices[0])  # add the vertix at the end
edges = ((vertices[0], vertices[1]), (vertices[1], vertices[2]), (vertices[2], vertices[3]), (vertices[3], vertices[4]), (vertices[4], vertices[5]), (vertices[5], vertices[6]), (vertices[6], vertices[7]), (vertices[7], vertices[0]))

atexit.register(save_accuracy)

# Plot the polygon
plt.figure(figsize=(8, 6))
plt.plot(*zip(*vertices), marker='o', color='b')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Polygon from Latitude and Longitude Values')
#plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.grid(True)

def test_run():
    # Generate and plot random points periodically
    for _ in range(10000):  # Plot 10 random points
        plot_random_point()
        plt.pause(.00000005)  # Pause for 1 second before plotting the next point

    plt.show()

def run_yourself():
    plt.gcf().canvas.mpl_connect('button_press_event', onclick)
    plt.show()

run_yourself()