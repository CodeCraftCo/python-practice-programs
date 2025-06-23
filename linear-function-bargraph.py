A #Python script that plots a bar graph of the linear equation y = 3x + 7 for user-provided x-values using matplotlib.
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