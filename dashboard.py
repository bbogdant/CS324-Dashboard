from tkinter import *
from PIL import ImageTk
from datetime import *
import time



def show_graph():
     
        import pandas as pd
        from bs4 import BeautifulSoup as bs
        import requests
        from matplotlib import pyplot as plt
        import csv
        import seaborn as sns
        
        pd.set_option('display.max_colwidth', 500)
        page = requests.get('https://carsalesbase.com/european-sales-2021-upper-class/')
        soup = bs(page.text, 'html.parser')

        cars = {}
        
        cols = ['Brand', 'Data_2020', 'Data_2021', 'Change']

        with open('Cars.csv', 'w', newline='') as result:
         write = csv.DictWriter(result, fieldnames=cols)
         write.writeheader()

        with open('Cars.csv', 'a', newline='') as result:
         while True:
           for i in range(2, 7):
            index = str(i)
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(2)'):
                print(cell.text)
                brand = cell.text
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(3)'):
                print(cell.text)
                data_2021 = cell.text
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(4)'):
                print(cell.text)
                data_2020 = cell.text
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(5)'):
                print(cell.text)
                change = cell.text

            cars[brand] = {'Data_2021':data_2021, 'Data_2020':data_2020, 'Change':change}
            write = csv.DictWriter(result, fieldnames=cols)
            car_csv = {'Brand':brand, 'Data_2021':data_2021, 'Data_2020':data_2020, 'Change':change}
            write.writerow(car_csv)
            print('\n')
           break

     

        Data=pd.read_csv(r'./Cars.csv')
        

        sns.set_style("darkgrid")
        sns.set_palette("Pastel1")

        
        sns.barplot(x=Data.Data_2021, y=Data.Brand)
        plt.title("Prodaja luksuznih automobila Europe")
        plt.xlabel("Data")
        plt.ylabel("Brand")

        
        plt.grid(True)
        for i, v in enumerate(Data.Data_2021):
            plt.text(v + 3, i + .25, str(v), color='black', fontweight='bold')

        plt.legend(["Brand"])
        plt.savefig("images/plotbar1.png")
        plt.show()


       
        brand = Data["Brand"]
        data_2021 = Data["Data_2021"]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
        explode = (0, 0, 0, 0, 0.1) 

        
        plt.pie(data_2021, labels=brand, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)

        
        plt.title("Prodaja luksuznih automobila\n"+"u 2021 godini EUROPE.")

        
        plt.legend(title = "Brands")

        plt.axis('equal')

        
        plt.savefig("images/pie1.png")
        plt.show()

def show_graph1():
      
        import pandas as pd
        from bs4 import BeautifulSoup as bs
        import requests
        from matplotlib import pyplot as plt
        import csv
        import seaborn as sns
        
        pd.set_option('display.max_colwidth', 500)
        page = requests.get('https://carsalesbase.com/us-car-sales-analysis-2021-large-cars/')
        soup = bs(page.text, 'html.parser')

        cars = {}
        car = {}
        cols = ['Brand', 'Data_2020', 'Data_2021', 'Change']

        with open('Cars1.csv', 'w', newline='') as result:
         write = csv.DictWriter(result, fieldnames=cols)
         write.writeheader()

        with open('Cars1.csv', 'a', newline='') as result:
         while True:
           for i in range(2, 7):
            index = str(i)
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(2)'):
                print(cell.text)
                brand = cell.text
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(3)'):
                print(cell.text)
                data_2021 = cell.text
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(4)'):
                print(cell.text)
                data_2020 = cell.text
            for cell in soup.select('#primary > div > div.single-content.contents-wrap.tipi-row.content-bg.clearfix.article-layout-1 > div > main > article > div > div > table > tbody > tr:nth-child(' + index + ') > td:nth-child(5)'):
                print(cell.text)
                change = cell.text

            cars[brand] = {'Data_2021':data_2021, 'Data_2020':data_2020, 'Change':change}
            write = csv.DictWriter(result, fieldnames=cols)
            car_csv = {'Brand':brand, 'Data_2021':data_2021, 'Data_2020':data_2020, 'Change':change}
            write.writerow(car_csv)
            print('\n')
            
           break

      

        Data=pd.read_csv(r'./Cars1.csv')
        
        sns.set_style("darkgrid")
        sns.set_palette("Pastel1")

        
        sns.barplot(x=Data.Data_2021, y=Data.Brand)
        plt.title("Prodaja luksuznih automobila USA")
        plt.xlabel("Data")
        plt.ylabel("Brand")

        
        plt.grid(True)
        for i, v in enumerate(Data.Data_2021):
            plt.text(v + 3, i + .25, str(v), color='black', fontweight='bold')

        plt.legend(["Brand"])
        plt.savefig("images/plotbar2.png")
        plt.show()


       
        brand = Data["Brand"]
        data_2021 = Data["Data_2021"]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
        explode = (0, 0, 0, 0, 0.1) 

        
        plt.pie(data_2021, labels=brand, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)

        
        plt.title("Prodaja luksuznih automobila\n"+"u 2021 godini EUROPE.")

        
        plt.legend(title = "Brands")

        plt.axis('equal')

        
        plt.savefig("images/pie2.png")
        plt.show()

        


class Dashboard2:


    
    def __init__(self, window):
        self.window = window
        self.window.title("Car Selling Dashboard")
        self.window.geometry("1920x1080")
        self.window.resizable(1920, 1080)
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        icon = PhotoImage(file='./images/pic-icon.png')
        self.window.iconphoto(True, icon)
        self.window.withdraw()

        
        self.login_form = Toplevel(self.window)
        self.login_form.wm_attributes("-topmost", 1)
        self.login_form.title("Login")
        self.login_form.geometry("300x200")
        self.login_form.resizable(False, False)

    
        self.username_label = Label(self.login_form, text="Username:")
        self.username_label.pack()

        
        self.username_entry = Entry(self.login_form)
        self.username_entry.pack()

        
        self.password_label = Label(self.login_form, text="Password:")
        self.password_label.pack()

        
        self.password_entry = Entry(self.login_form, show="*")
        self.password_entry.pack()
          
        self.login_button = Button(self.login_form, text="Login", command=self.login)
        self.login_button.pack()
    

    

    def check_credentials(self, username, password):
         with open("./data.txt", "r") as f:
            contents = f.read()
         if f"{username}:{password}" in contents:
            return True
         else:
            return False

    def login(self):
        from tkinter import messagebox
        username = self.username_entry.get()
        password = self.password_entry.get()
        

        if self.check_credentials(username, password):
            self.login_form.destroy()
            self.window.deiconify()
        else:
            
            messagebox.showinfo("Login", "Incorrect username or password")
            
    

        #head

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

       

        #sidebar
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        #body
        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=500)

       
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=630, width=200, height=120)

       
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=700, y=630, width=200, height=120)

        
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=630, width=200, height=120)

        #sidebar
        
        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        
        self.brandName = Label(self.sidebar, text='Bogdan Trajkovic', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

       
        self.dashboardImage = ImageTk.PhotoImage(file='images/eu.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Europe", bg='#ffffff', font=("", 13, "bold"), bd=0,cursor='hand2', activebackground='#ffffff', command=self.change_img)
        self.dashboard_text.place(x=80, y=287)

       
        self.manageImage = ImageTk.PhotoImage(file='images/us.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text="USA", bg='#ffffff', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#ffffff',command=self.change_img1)
        self.manage_text.place(x=80, y=345)


        
        self.ExitImage = ImageTk.PhotoImage(file='images/exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=30, y=390)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#ffffff', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#ffffff',command=self.window.destroy)
        self.Exit_text.place(x=80, y=402)

        #body

       

        
        self.total_people = Label(self.bodyFrame2, text='14', bg='#009aa5', font=("", 25, "bold"))
        self.total_people.place(x=5, y=20)

        self.totalPeopleImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.totalPeople = Label(self.bodyFrame2, image=self.totalPeopleImage, bg='#009aa5')
        self.totalPeople.place(x=50, y=50)

        self.totalPeople_label = Label(self.bodyFrame2, text="Total Cars", bg='#009aa5', font=("", 12, "bold"),fg='white')
        self.totalPeople_label.place(x=5, y=5)

        
        self.people_left = Label(self.bodyFrame3, text='2021', bg='#e21f26', font=("", 25, "bold"))
        self.people_left.place(x=5, y=20)

        
        self.LeftImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#e21f26')
        self.Left.place(x=50, y=50)

        self.peopleLeft_label = Label(self.bodyFrame3, text="Year", bg='#e21f26', font=("", 12, "bold"),fg='white')
        self.peopleLeft_label.place(x=5, y=5)

        
        self.total_earnings = Label(self.bodyFrame4, text='$40,000.00', bg='#ffcb1f', font=("", 25, "bold"))
        self.total_earnings.place(x=5, y=20)

        self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#ffcb1f', font=("", 12, "bold"),fg='white')
        self.earnings_label.place(x=5, y=5)
       
        self.earningsIcon_image = ImageTk.PhotoImage(file='images/earn3.png')
        self.earningsIcon = Label(self.bodyFrame4, image=self.earningsIcon_image, bg='#ffcb1f')
        self.earningsIcon.place(x=50, y=50)




        
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

  


    def change_img(self):
        show_graph()

        self.graph_image = ImageTk.PhotoImage(file='images/plotbar1.png')
        self.graph = Label(self.bodyFrame1, image=self.graph_image, bg='#ffffff')
        self.graph.place(x=0, y=-50)
     
        self.pieChart_image = ImageTk.PhotoImage(file='images/pie1.png')
        self.pieChart = Label(self.bodyFrame1, image=self.pieChart_image, bg='#ffffff')
        self.pieChart.place(x=550, y=0)
    
    def change_img1(self):
        show_graph1()

        
        self.graph_image = ImageTk.PhotoImage(file='images/plotbar2.png')
        self.graph = Label(self.bodyFrame1, image=self.graph_image, bg='#ffffff')
        self.graph.place(x=0, y=-50)

        self.pieChart_image = ImageTk.PhotoImage(file='images/pie2.png')
        self.pieChart = Label(self.bodyFrame1, image=self.pieChart_image, bg='#ffffff')
        self.pieChart.place(x=550, y=0)

    

    def show_time(self):

        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)


def wind():
    window = Tk()
    Dashboard2(window)
    window.mainloop()
    

if __name__ == '__main__':
    wind()



