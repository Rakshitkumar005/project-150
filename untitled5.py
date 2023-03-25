from tkinter import *
import random
    
root=Tk()
root.title("RANDOM COUNTRIES AND CAPITALS")
root.geometry("500x500")

country=[]
capital=[]
        
def display():
    countryName=enter_country.get()
    country.append(countryName)
    country_name["text"]="Country Name :"+str(country)
    capitalName=enter_capital.get()
    capital.append(capitalName)
    capital_name["text"]="Capital Name :"+str(capital)
    
def randomNum():
    length=len(country)
    randomCountry=random.randint(0, length-1)
    randomCountryname=country[randomCountry]
    random_country["text"]="Random Country :"+str(randomCountryname)
    length=len(capital)
    randomCapital=random.randint(0, length-1)
    randomCapitalname=capital[randomCapital]
    random_capital["text"]="Random Capital :"+str(randomCapitalname)

enter_country=Entry(root)
enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)
enter_capital=Entry(root)
enter_capital.place(relx=0.5,rely=0.3,anchor=CENTER)

display_btn=Button(root,text="Display Country And City Name",command=display)
display_btn.place(relx=0.5,rely=0.4,anchor=CENTER)

country_name=Label(root)
country_name.place(relx=0.5,rely=0.5,anchor=CENTER)
capital_name=Label(root)
capital_name.place(relx=0.5,rely=0.6,anchor=CENTER)

display_random=Button(root,text="Display Country And City Name Randomly",command=randomNum)
display_random.place(relx=0.5,rely=0.7,anchor=CENTER)

random_country=Label(root)
random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital=Label(root)
random_capital.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()