#A Python program that plots the graph of the linear equation y = 3x + 7 for user-input x-values using matplotlib with grid and markers.
import matplotlib.pyplot as plt

def plot_graph():
    m = 3
    c = 7
    x_values = []
    y_values = []

    for i in range(1, 11):
        x = int(input(f"Enter x-value {i} (1-10): "))
        x_values.append(x)
        y = m * x + c
        y_values.append(y)

    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.title('Graph of y = mx + c')
    plt.grid(True)
    plt.show()

plot_graph()
