import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


def plot_function():
    function = entry.get()

    try:
        x = np.linspace(-10, 10, 400)
        y = eval(function)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Graph of the Function")
        plt.grid(True)
        plt.show()
    except Exception as e:
        error_label.config(text=str(e))


# Create the main window
window = tk.Tk()
window.title("Function Grapher")

# Create a label and an entry for the function
label = tk.Label(window, text="Enter a function:")
label.pack()

entry = tk.Entry(window, width=30)
entry.pack()

# Create a button to plot the function
plot_button = tk.Button(window, text="Plot", command=plot_function)
plot_button.pack()

# Create a label to display any errors
error_label = tk.Label(window, fg="red")
error_label.pack()

# Start the main event loop
window.mainloop()