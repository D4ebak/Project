import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class FrontPageGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GJK Phone Satisfaction Survey")
        self.window.geometry("1169x656")
        self.window.configure(bg="white")
        self.window.resizable(False, False)

        self.background_image1 = tk.PhotoImage(file=r"C:\\Users\\Glen Umadhay\\FOR FINALS\\FRONTPAGE.png")
        self.background_label = tk.Label(self.window, image=self.background_image1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button_check = tk.Button(self.window, text="Continue", bg='#068FFF', fg='#000000', command=self.button_clicked, bd=0, font=('Arial', 15))
        self.button_check.place(relx=0.78, rely=0.75, relwidth=0.10, relheight=0.1, anchor='n')
        
    def button_clicked(self):
        self.background_image = tk.PhotoImage(file=r"C:\\Users\\Glen Umadhay\\FOR FINALS\\MAINPAGE.png")
        self.background_label.configure(image=self.background_image)
        self.button_check.destroy()
        
        frame = tk.Frame(self.window, bg='#F8B195', bd=5)
        frame.place(relx=0.5, rely=0, relwidth=100, relheight=0.0, anchor='n')
        
        self.brands = [
            'ACER', 'ALCATEL', 'ALLVIEW', 'AMAZON', 'AMOI', 'APPLE', 'ARCHOS', 'ASUS',
            'AT&T', 'BENEFON', 'BENQ', 'BENQ-SIEMENS', 'BIRD', 'BLACKBERRY', 'BLACKVIEW', 'BLU', 'BOSCH',
            'BQ', 'CASIO', 'CAT', 'CELKON', 'CHEA', 'CHERRY MOBILE', 'COOLPAD', 'DELL', 'DOOGEE', 'EMPORIA',
            'ENERGIZER', 'ERICSSON', 'ETEN', 'FAIRPHONE', 'FUJITSU SIEMENS', 'GARMIN-ASUS', 'GIGABYTE',
            'GIONEE', 'GOOGLE', 'HAIER', 'HONOR', 'HP', 'HTC', 'HUAWEI', 'I-MATE', 'I-MOBILE', 'ICEMOBILE',
            'INFINIX', 'INNOSTREAM', 'INQ', 'INTEX', 'JOLLA', 'KARBONN', 'KYOCERA', 'LAVA', 'LEECO',
            'LENOVO', 'LG', 'MAXON', 'MAXWEST', 'MEIZU', 'MICROMAX', 'MICROSOFT', 'MITAC', 'MITSUBISHI',
            'MODU', 'MOTOROLA', 'MWG', 'MY PHONE', 'NEC', 'NEONODE', 'NIU', 'NOKIA', 'NOTHING', 'NVIDIA',
            'O2', 'ONEPLUS', 'OPPO', 'ORANGE', 'PALM', 'PANASONIC', 'PANTECH', 'PARLA', 'PHILIPS', 'PLUM',
            'POSH', 'PRESTIGIO', 'QMOBILE', 'QTEK', 'RAZER', 'REALME', 'SAGEM', 'SAMSUNG', 'SENDO', 'SEWON',
            'SHARP', 'SIEMENS', 'SKK MOBILE', 'SKY MOBILE', 'SKYWORTH', 'SONIM', 'SONY', 'SONY ERICSSON',
            'SPICE', 'STARMOBILE', 'T-MOBILE', 'TCL', 'TECNO', 'TEL.ME.', 'TELIT', 'THURAYA', 'TOSHIBA',
            'ULEFONE', 'UNNECTO', 'VERTU', 'VERYKOOL', 'VIVO', 'VK MOBILE', 'VODAFONE', 'WIKO', 'WND',
            'XCUTE', 'XIAOMI', 'XOLO', 'YEZZ', 'YOTA', 'YU', 'ZTE', 'POCO'
        ]
        self.rate = ["VERY UNSATISFIED", "UNSATISFIED", "NEUTRAL", "SATISFIED", "VERY SATISFIED"]
        self.rating_labels = {
            "VERY UNSATISFIED": "VERY UNSATISFIED",
            "UNSATISFIED": "UNSATISFIED",
            "NEUTRAL": "NEUTRAL",
            "SATISFIED": "SATISFIED",
            "VERY SATISFIED": "VERY SATISFIED"
        }
        self.report = {}
        self.load_report()

        frame = tk.Frame(self.window, bg='#F8B195', bd=5)
        frame.place(relx=0.5, rely=0.60, relwidth=0.5, relheight=0.70, anchor='center')

        self.brand_label = tk.Label(frame, text="Phone Brand:", font=("Arial", 14), fg="#6C5B7B", bg="#F8B195")
        self.brand_label.place(relx=0.5, rely=0.15, anchor='center')

        self.brand_var = tk.StringVar(self.window)
        self.brand_var.set("Choose Here")
        self.brand_dropdown = tk.OptionMenu(frame, self.brand_var, *self.brands)
        self.brand_dropdown.config(font=("Arial", 12), fg="#6C5B7B", bg="#F67280", bd=0)
        self.brand_dropdown.place(relx=0.5, rely=0.25, anchor='center')
        
        self.rating_label = tk.Label(frame, text="Rating:", font=("Arial", 14), fg="#6C5B7B", bg="#F8B195")
        self.rating_label.place(relx=0.5, rely=0.35, anchor='center')

        self.rating_var = tk.StringVar(self.window)
        self.rating_var.set("Choose Here") 
        self.rating_dropdown = tk.OptionMenu(frame, self.rating_var, *self.rate)
        self.rating_dropdown.config(font=("Arial", 12), fg="#6C5B7B", bg="#F67280", bd=0)
        self.rating_dropdown.place(relx=0.5, rely=0.45, anchor='center')
        
        self.name_label = tk.Label(frame, text="Enter Your Name:", font=("Arial", 14), fg="#6C5B7B", bg="#F8B195")
        self.name_label.place(relx=0.5, rely=0.55, anchor='center')
        self.name_entry = tk.Entry(frame, font=("Arial", 12), bg="green", fg="#6C5B7B")
        self.name_entry = tk.Entry(frame, font=("Arial", 12), bg="#F67280", fg="#6C5B7B")
        self.name_entry.config(fg="#6C5B7B")
        self.name_entry.place(relx=0.5, rely=0.65, anchor='center')
        
        self.submit_button = tk.Button(frame, text="Submit Survey", command=self.submit_survey, font=("Arial", 14), fg="#6C5B7B", bg="#F67280", bd=0)
        self.submit_button.place(relx=0.5, rely=0.75, anchor='center')
        
        self.view_report_button = tk.Button(frame, text="View Report", command=self.print_report, font=("Arial", 14), fg="#6C5B7B", bg="#F67280", bd=0)
        self.view_report_button.place(relx=0.1, rely=0.75, anchor='w')
        
        def quitapp():
            self.window.destroy()
            
        button_exit = tk.Button( text="Exit", command=quitapp, font=("Arial", 14), fg="#6C5B7B", bg="#F67280", bd=0)
        button_exit.place(relx=0.69, rely=0.775, relwidth=0.1 ,anchor='e' )

    def load_report(self):
        try:
            with open("survey_report.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    brand, rating, name = line.strip().split(',')
                    if brand not in self.report:
                        self.report[brand] = {}
                    if rating not in self.report[brand]:
                        self.report[brand][rating] = []
                    self.report[brand][rating].append(name)
        except FileNotFoundError:
            pass

    def save_report(self):
        with open("survey_report.txt", "w") as file:
            for brand, ratings in self.report.items():
                for rating, names in ratings.items():
                    for name in names:
                        file.write(f"{brand},{rating},{name}\n")

    def submit_survey(self):
        brand = self.brand_var.get()
        rating = self.rating_var.get()
        name = self.name_entry.get().upper()

        if brand == "Choose Here" or rating == "Choose Here" or name == "":
            messagebox.showerror("Error", "Please fill in all the fields!")
        else:
            if brand not in self.report:
                self.report[brand] = {}
            if rating not in self.report[brand]:
                self.report[brand][rating] = []
            self.report[brand][rating].append(name)
            self.save_report()
            messagebox.showinfo("Success", "Survey submitted successfully!")
            self.reset_fields()

    def reset_fields(self):
        self.brand_var.set("Choose Here")
        self.rating_var.set("Choose Here")
        self.name_entry.delete(0, 'end')

    def print_report(self):
        report_text = "Survey Report:\n\n"
        for brand, ratings in self.report.items():
            report_text += f"{brand}:\n"
            for rating, names in ratings.items():
                report_text += f"\t{self.rating_labels[rating]}: {len(names)} RESPONDENTS\n"
                for name in names:
                    report_text += f"\t\t{name}\n"
            report_text += "\n"
        messagebox.showinfo("Report", report_text)

if __name__ == '__main__':
    survey_gui1 = FrontPageGUI()
    survey_gui1.window.mainloop()