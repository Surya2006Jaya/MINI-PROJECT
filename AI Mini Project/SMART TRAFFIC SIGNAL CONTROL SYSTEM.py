import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Train the ML model
vehicle_counts = np.array([5, 10, 15, 20, 25, 30, 40, 50]).reshape(-1, 1)
green_time = np.array([10, 20, 30, 40, 50, 60, 80, 100])
model = LinearRegression()
model.fit(vehicle_counts, green_time)

# GUI window
root = tk.Tk()
root.title("Smart Traffic Signal Control System using Machine Learning")
root.geometry("600x500")
root.configure(bg="#e9f5f5")

tk.Label(root, text="🚦 Smart Traffic Signal Control System 🚦",
         font=("Arial", 16, "bold"), fg="darkgreen", bg="#e9f5f5").pack(pady=10)

tk.Label(root, text="Enter number of lanes:", font=("Arial", 12), bg="#e9f5f5").pack()
lane_entry = tk.Entry(root, font=("Arial", 12))
lane_entry.pack(pady=5)

lane_entries = []


def create_lane_inputs():
    global lane_entries
    for widget in lane_entries:
        widget.destroy()
    lane_entries = []
    try:
        lanes = int(lane_entry.get())
        for i in range(lanes):
            frame = tk.Frame(root, bg="#e9f5f5")
            tk.Label(frame, text=f"Vehicle count for Lane {i+1}:", font=("Arial", 12), bg="#e9f5f5").pack(side=tk.LEFT, padx=5)
            e = tk.Entry(frame, font=("Arial", 12), width=10)
            e.pack(side=tk.LEFT)
            frame.pack(pady=3)
            lane_entries.append(e)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of lanes.")


def calculate_signal_times():
    try:
        lane_data = [int(e.get()) for e in lane_entries]
        if not lane_data:
            messagebox.showerror("Error", "Please enter vehicle counts for all lanes.")
            return

        predicted_times = model.predict(np.array(lane_data).reshape(-1, 1))
        total_vehicles = sum(lane_data)
        avg_wait = np.mean(predicted_times)
        congestion_level = total_vehicles / (len(lane_data) * 25)

        result_text = "\n--- Predicted Signal Timings ---\n"
        for i, t in enumerate(predicted_times):
            result_text += f"Lane {i+1}: {lane_data[i]} vehicles → {t:.2f} sec green light\n"

        result_text += f"\nTotal Vehicles: {total_vehicles}\nAverage Waiting Time: {avg_wait:.2f} sec\n"

        if congestion_level > 0.8:
            status = " High Congestion! Prioritizing heavy lanes."
            color = "red"
        elif congestion_level > 0.5:
            status = " Moderate Traffic Flow."
            color = "orange"
        else:
            status = " Smooth Traffic Flow."
            color = "green"

        result_text += f"\nTraffic Status: {status}"

        result_label.config(text=result_text, fg=color)

        # Visualization chart
        plt.figure(figsize=(6,4))
        plt.bar([f"Lane {i+1}" for i in range(len(lane_data))],
                predicted_times, color="green")
        plt.xlabel("Lanes")
        plt.ylabel("Predicted Green Time (sec)")
        plt.title("Smart Traffic Signal Prediction")
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid vehicle numbers for all lanes.")


# Buttons
tk.Button(root, text="Create Lane Inputs", font=("Arial", 12, "bold"),
          bg="lightblue", command=create_lane_inputs).pack(pady=10)

tk.Button(root, text="Predict Signal Times", font=("Arial", 12, "bold"),
          bg="lightgreen", command=calculate_signal_times).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e9f5f5", justify="left")
result_label.pack(pady=10)

root.mainloop()
