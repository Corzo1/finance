import tkinter as tk

results = {}


def finish():
    with open("text.txt", 'w') as txt:

        for key, value in results.items():
            txt.write(f"expense {key}; amount {value:.2f}\n")

    exit()


class IncomeInputFrame(tk.Frame):
    def __init__(self, master, on_submit):
        super().__init__(master)

        self.income1_label = tk.Label(self, text="Income 1:")
        self.income1_label.pack()
        self.income1_entry = tk.Entry(self)
        self.income1_entry.pack()

        self.income2_label = tk.Label(self, text="Income 2:")
        self.income2_label.pack()
        self.income2_entry = tk.Entry(self)
        self.income2_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=on_submit)
        self.submit_button.pack()


class ExpenseInputFrame(tk.Frame):
    def __init__(self, master, income1, income2, on_finished):
        super().__init__(master)

        self.income1 = income1
        self.income2 = income2
        self.on_finished = on_finished

        self.expense_label = tk.Label(self, text="Expense:")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(self)
        self.expense_entry.pack()

        self.calculate_button = tk.Button(
            self, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.pack()

        self.finished_button = tk.Button(
            self, text="Finished", command=finish,)
        self.finished_button.pack()

    def calculate(self):
        total = self.income1 + self.income2
        rate = self.income1 / total
        try:
            expense = int(self.expense_entry.get())
            result = rate * expense
            results[expense] = result
            # print(results)
            self.result_label.config(text=f"Result: {result:.2f}")
        except ValueError:
            self.result_label.config(text="Invalid input")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.income_input_frame = IncomeInputFrame(self, self.on_income_submit)
        self.income_input_frame.pack()

        self.expense_input_frame = None

    def on_income_submit(self):
        income1 = int(self.income_input_frame.income1_entry.get())
        income2 = int(self.income_input_frame.income2_entry.get())

        self.expense_input_frame = ExpenseInputFrame(
            self, income1, income2, self.on_expense_finished)
        self.income_input_frame.pack_forget()
        self.expense_input_frame.pack()

    def on_expense_finished(self):
        self.expense_input_frame.pack_forget()
        self.income_input_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
