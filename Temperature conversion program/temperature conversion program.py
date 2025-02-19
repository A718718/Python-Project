import tkinter as tk
from tkinter import ttk, messagebox
class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Conversion formulas dictionary
        self.conversions = {
            ('Celsius', 'Fahrenheit'): lambda c: c * 9 / 5 + 32,
            ('Celsius', 'Kelvin'): lambda c: c + 273.15,
            ('Fahrenheit', 'Celsius'): lambda f: (f - 32) * 5 / 9,
            ('Fahrenheit', 'Kelvin'): lambda f: (f - 32) * 5 / 9 + 273.15,
            ('Kelvin', 'Celsius'): lambda k: k - 273.15,
            ('Kelvin', 'Fahrenheit'): lambda k: (k - 273.15) * 9 / 5 + 32,
        }

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Input frame
        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.pack(pady=10)

        # From temperature
        ttk.Label(input_frame, text="From:").grid(row=0, column=0, padx=5)
        self.from_unit = tk.StringVar()
        self.from_combobox = ttk.Combobox(input_frame, width=12, textvariable=self.from_unit,
                                          values=['Celsius', 'Fahrenheit', 'Kelvin'])
        self.from_combobox.grid(row=0, column=1, padx=5)
        self.from_combobox.current(0)

        # To temperature
        ttk.Label(input_frame, text="To:").grid(row=1, column=0, padx=5)
        self.to_unit = tk.StringVar()
        self.to_combobox = ttk.Combobox(input_frame, width=12, textvariable=self.to_unit,
                                        values=['Celsius', 'Fahrenheit', 'Kelvin'])
        self.to_combobox.grid(row=1, column=1, padx=5)
        self.to_combobox.current(1)

        # Temperature entry
        ttk.Label(input_frame, text="Temperature:").grid(row=2, column=0, padx=5, pady=10)
        self.temp_entry = ttk.Entry(input_frame, width=15)
        self.temp_entry.grid(row=2, column=1, padx=5, pady=10)

        # Button frame
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Convert", command=self.convert).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)

        # Result label
        self.result_label = ttk.Label(self.root, text="", font=('Arial', 12, 'bold'))
        self.result_label.pack(pady=10)

    def convert(self):
        try:
            temperature = float(self.temp_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            if from_unit == to_unit:
                result = temperature
            else:
                result = self.conversions[(from_unit, to_unit)](temperature)

            self.result_label.config(
                text=f"{temperature:.2f}°{from_unit[0]} = {result:.2f}°{to_unit[0]}"
            )
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
        except KeyError:
            messagebox.showerror("Error", "Conversion not supported!")

    def clear(self):
        self.temp_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.from_combobox.current(0)
        self.to_combobox.current(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()