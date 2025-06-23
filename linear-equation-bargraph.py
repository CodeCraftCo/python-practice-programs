#A Python program that takes user input for x-values, computes y = 3x + 7, and displays the results as a bar graph using matplotlib.
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

    plt.bar(x_values, y_values)
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.title('Bar Graph of y = mx + c')
    plt.show()

plot_graph()