from tkinter import *
from tkinter import ttk  ,messagebox
import sqlite3

tehran={1:['Hesarbuali','Rostamabad- Farmaniyeh','Evin','darakeh','zaaferaniyeh','Mahmoudiyah','Velenjek','Imam Zadeh Qasem' ,'darband','Gulabdare','Jamaran','Dezashib','Niavaran','Araj','Kashanak','shahrak daneshgah','shahrak naft','Darabad','bagh pardisan','Tajrish','Qeitariye','Cheezer','Sohank','Sadr highway','elahiye'],
        2:['Bu Ali','Saadat Abad','Punak','Sadeghie','Shahrara','Koi Nasr','Tehran Villa','Homayunshahr','Zanjan','Shadmehr','Ivank','Farahzad','Hakim highway','Sheikh Fazlullah Nouri highway','Mohammad Ali Jinnah Highway','Yadgar Imam highway','Jalal Al-e Ahmad'],
        3:['Ararat','Zargande','Seyed Khandan','ekhtiyariye','Jordan','Jolfa','Khajeh Abdullah','Sheikh Bahaie','Shiraz','Zafar','Mulla Sadra'],
        4:['Mehran','Kazem Abad','Majidiyeh and Shamsabad','Hossein Abad and Mubarak Abad','Narmak','West Tehran Pars','Javadieh','Tehran Pars East','Qasem Abad ','Hakimiye','Qanat Kausar','Majid Abad','Babai highway','Bagheri highway','Sayad Shirazi highway','Bani Hashem','Police','Shamsabad','Sayyad Shirazi'],
        5:['Moradabad','Abazar','Ferdows','Mehran','Ekbatan','Bimeh','Apadana','South Jannatabad','North Jannatabad','Jantabad Central','Ayatollah Kashani','Ashrafi Isfahani','Ferdows Blvd','Shahid Mehdi Bakri'],
        6:['Iranshahr','Laleh park','Keshavarz blvd','Nusrat','16 Azar','Behjatabad','Abbas Abad','Gandhi','Saie','Yousef Abad','Argentina','Hemmat highway','Amirabad','Tavanir'],
        7:['Gorgan','Nezamabad','Amjadiya Khaqani','Nilofar','Abbas Abad - Andisheh','Heshmatiye','Apadana','Imam Hossein','Sohrevardi','Shariati'],
        8:['Tehran Pars','Fadak','Narmak','Majidiyeh','Kerman','Vahidiye','Sabalan'],
        9:['Dastgheib','Imamzadeh Abdullah','Mehrabad','South Mehrabad','Ostad Moein','Fath'],
        10:['Briyank','Soleimani Timuri','Southern Selsabil','Southern Karun','Hashemi','South Zanjan','Northern Selsabil','Northern Karun','Azerbaijan','Azadi','Imam Khomeini','Jeyhoon','Rodaki','Qasr al-Dasht','Malek Ashtar','Nawab','Komeil'],
        11:['Sheikh Hadi','Enghelab','Amirieh','Moniriye','Hor','Abbasi','Abu Saeed','pastor','Hasan Abad','Waliasr','Southern kargar','Kashan'],
        12:['Baharestan','Ferdowsi','Imamzadeh Yahya','Pamenar','Sangelaj','Shemiran Gate','Amin Hozur','Khorasan','Rey','Saadi','Lale Zarno','Molavi'],
        13:['Safa','niroo havayie','piroozi','zeynabiyeh','sorkhe hesar','Tehran no','Damavand'],
        14:['400 dastgah','Dejcom','Borujerdi','Farzaneh','Shiva','Shahrabi','Shakib','Mahalati highway','Fallah'],
        15:['Minabi','Tayyab','Motahari','Hashem Abad','Atabak','North Kianshahr','South Kianshahr','Razavi','Moshiriya','Masoudia','Wal Fajr','Qiamadasht','Khavarshahr','Baath highway'],
        16:['Javadiyeh','Nazi Abad','Khazaneh','North Aliabad','Yakhchiabad','South Aliabad','Rajai'],
        17:['Azari','Imamzadeh Hasan','Yaftabad','Jalili','Zahtabi','Abu zar','Qazvin'],
        18:['Ferdows','Valiasr North','Rajai','Southern Waliasr','Sadeghie','Sahib al-Zaman','South Yaftabad','Northern Yaftabad','Shad Abad','Imam Khomeini','Shamsabad','North Persian Gulf','South Persian Gulf','Azadegan highway','Shahrak-e Vali Asr'],
        19:['Khani Abad ','Esfandiari and Bostan','Bahmanyar','New South Khani Abad','South Shariati','North Shariati','Nematabad','Shahid Kazemi','New Khani Abad','Abdul Abad'],
        20:['Zaheer Abad','Hamza Abad','Dillman','Firouzabadi','Mansooriyah','Dolat abad','Vali Abad','Amin Abad','Taghiabad','Abbas Abad','Kahrizak'],
        21:['West Tehransar','Tehransar East','Central Tehransar','shahrak azadi','Farhangian ','North Chitgar','South Chitgar','city villa','Tehran Karaj highway','Fatah Highway','Tehransar','Shahrak 22 Bahman','Sharif University'],
        22:['Olympic','Eastern Golestan','Zibadasht' ,'Sharif','West Golestan','Omid - Dezhban''Azadshahr','Chitgar'],}


class Page2 :
    def __init__ (self,w2):
        self.w2=w2
        self.w2.title('Real Estate Search Item')
        self.w2.resizable(0,0)
        self.screen_height=w2.winfo_screenheight()
        self.screen_width=w2.winfo_screenwidth()
        self.w2.geometry(f'500x645+{self.screen_width//2-250}+{self.screen_height//2-350}')

        self.call_all2()


    def call_all2(self):
        self.label2()
        self.menu2()
        self.radio_buttons2()
        self.entry2()
        self.drop_down2()
        self.buttons2()
        self.create_database2()
        self.checkbox2()
        
    

    def create_database2 (self):
        self.connector=sqlite3.connect('RealEstate_database.db')
        self.cursor=self.connector.cursor()
        query = '''
                CREATE TABLE IF NOT EXISTS realestate
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT , 
                area INTEGER,
                num_of_rooms INTEGER,
                price_per_meter TEXT,
                total_price TEXT,
                deposit TEXT,
                monthly_rent TEXT,
                zone INTEGER,
                district TEXT,
                full_address TEXT,
                floor INTEGER,
                unit INTEGER,
                product_year INTEGER,
                cabinet_type TEXT,
                floor_type TEXT,
                other_options TEXT)'''
        self.cursor.execute(query)
        self.connector.commit()


    def label2 (self):
        self.label_type=Label(w2,text='Type',font=("Aria",12,'bold'),foreground='#005441')
        self.label_type.place(x=10,y=10)

        self.label_area=Label(w2,text='Area(m)',font=("Aria",12,'bold'),foreground='#005441')
        self.label_area.place(x=10,y=100)

        self.label_num_of_rooms=Label(w2,text='Num of Rooms',font=("Aria",12,'bold'),foreground='#005441')
        self.label_num_of_rooms.place(x=10,y=140)

        self.label_price_per_meter=Label(w2,text='Price Per Meter',font=("Aria",12,'bold'),foreground='#005441')
        self.label_price_per_meter.place(x=10,y=180)

        self.label_total_price=Label(w2,text='Total Price',font=("Aria",12,'bold'),foreground='#005441')
        self.label_total_price.place(x=10,y=220)

        self.label_deposit=Label(w2,text='Deposit',font=("Aria",12,'bold'),foreground='#005441')
        self.label_deposit.place(x=10,y=260)

        self.label_monthly_rent=Label(w2,text='Monthly Rent',font=("Aria",12,'bold'),foreground='#005441')
        self.label_monthly_rent.place(x=10,y=300)

        self.label_address=Label(w2,text='Address',font=("Aria",12,'bold'),foreground='#005441')
        self.label_address.place(x=10,y=340)
        
        self.label_floor=Label(w2,text='Floor',font=("Aria",12,'bold'),foreground='#005441')
        self.label_floor.place(x=10,y=380)

        self.label_unit=Label(w2,text='Unit',font=("Aria",12,'bold'),foreground='#005441')
        self.label_unit.place(x=150,y=380)

        self.label_cabinet=Label(w2,text='Cabinet :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_cabinet.place(x=10,y=430)

        self.label_floor_material=Label(w2,text='Floor :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_floor_material.place(x=10,y=470)

        self.label_other_options=Label(w2,text='Other :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_other_options.place(x=10,y=510)

        self.label_minimum=Label(w2,text='Minimum',font=("Aria",12),foreground='#005441')
        self.label_minimum.place(x=188,y=65)

        self.label_maximum=Label(w2,text='Maximum',font=("Aria",12),foreground='#005441')
        self.label_maximum.place(x=340,y=65)


    def entry2 (self):
        self.entry_area_min=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_area_min.place(x=170,y=100)

        self.entry_num_of_rooms_min=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_num_of_rooms_min.place(x=170,y=140)

        self.entry_price_per_meter_min=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_price_per_meter_min.place(x=170,y=180)

        self.entry_total_price_min=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_total_price_min.place(x=170,y=220)

        self.entry_deposit_min=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_deposit_min.place(x=170,y=260)

        self.entry_monthly_rent_min=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_monthly_rent_min.place(x=170,y=300)

        self.entry_area_max=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_area_max.place(x=323,y=100)

        self.entry_num_of_rooms_max=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_num_of_rooms_max.place(x=323,y=140)

        self.entry_price_per_meter_max=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_price_per_meter_max.place(x=323,y=180)

        self.entry_total_price_max=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_total_price_max.place(x=323,y=220)

        self.entry_deposit_max=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_deposit_max.place(x=323,y=260)

        self.entry_monthly_rent_max=Entry(w2,font=("Arial",10),width=15,border='1px',relief='solid')
        self.entry_monthly_rent_max.place(x=323,y=300)

        self.entry_floor=Entry(w2,font=("Arial",14),width=5,border='1px',relief='solid')
        self.entry_floor.place(x=65,y=380)

        self.entry_unit=Entry(w2,font=("Arial",14),width=5,border='1px',relief='solid')
        self.entry_unit.place(x=200,y=380)



    def checkbox2 (self):
        self.answer_type = IntVar()
        self.choice_type_rent = Checkbutton(w2,text='Rent',font=("Aria",12),foreground='#005441',offvalue=0,onvalue=1,variable=self.answer_type,command=self.rent_options)
        self.choice_type_rent.place(x=150 , y=10)
        self.choice_type_buy = Checkbutton(w2,text='Buy',font=("Aria",12),foreground='#005441',offvalue=0,onvalue=2,variable=self.answer_type,command=self.buy_options)
        self.choice_type_buy.place(x=230 , y=10)

    def rent_options (self):
        if self.answer_type.get()==1:
            self.entry_price_per_meter_min.delete(0,END)
            self.entry_total_price_min.delete(0,END)
            self.entry_price_per_meter_max.delete(0,END)
            self.entry_total_price_max.delete(0,END)
            self.entry_price_per_meter_min.config(state='disabled')
            self.entry_total_price_min.config(state='disabled')
            self.entry_price_per_meter_max.config(state='disabled')
            self.entry_total_price_max.config(state='disabled')
            self.entry_monthly_rent_min.config(state='normal')
            self.entry_deposit_min.config(state='normal')
            self.entry_monthly_rent_max.config(state='normal')
            self.entry_deposit_max.config(state='normal')
        else:
            self.entry_price_per_meter_min.config(state='normal')
            self.entry_total_price_min.config(state='normal')
            self.entry_price_per_meter_max.config(state='normal')
            self.entry_total_price_max.config(state='normal')


    def buy_options (self):
        if self.answer_type.get()==2:
            self.entry_monthly_rent_min.delete(0,END)
            self.entry_deposit_min.delete(0,END)
            self.entry_monthly_rent_max.delete(0,END)
            self.entry_deposit_max.delete(0,END)
            self.entry_monthly_rent_min.config(state='disabled')
            self.entry_deposit_min.config(state='disabled')
            self.entry_monthly_rent_max.config(state='disabled')
            self.entry_deposit_max.config(state='disabled')
            self.entry_price_per_meter_min.config(state='normal')
            self.entry_total_price_min.config(state='normal')
            self.entry_price_per_meter_max.config(state='normal')
            self.entry_total_price_max.config(state='normal')
        else:
            self.entry_monthly_rent_min.config(state='normal')
            self.entry_deposit_min.config(state='normal')
            self.entry_monthly_rent_max.config(state='normal')
            self.entry_deposit_max.config(state='normal')




    def radio_buttons2 (self):
        self.answer_cabinet_type = IntVar()
        self.choice_cabinet_type_mdf = Radiobutton(w2,text='MDF',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_mdf.place(x=100 , y=430)
        self.choice_cabinet_type_clipboard = Radiobutton(w2,text='ClipBoard',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_clipboard.place(x=185 , y=430)
        self.choice_cabinet_type_high_glass = Radiobutton(w2,text='High Glass',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_high_glass.place(x=295 , y=430)
        self.choice_cabinet_type_other = Radiobutton(w2,text='Other',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_other.place(x=407 , y=430)


        self.answer_floor_material = IntVar()
        self.choice_floor_material_ceramic = Radiobutton(w2,text='Ceramic',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_floor_material)
        self.choice_floor_material_ceramic.place(x=100 , y=470)
        self.choice_floor_material_parquet = Radiobutton(w2,text='Parquet',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_floor_material)
        self.choice_floor_material_parquet.place(x=195 , y=470)
        self.choice_floor_material_mosaic = Radiobutton(w2,text='Mosaic',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_floor_material)
        self.choice_floor_material_mosaic.place(x=300 , y=470)
        self.choice_floor_material_other = Radiobutton(w2,text='Other',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_floor_material)
        self.choice_floor_material_other.place(x=407 , y=470)

        self.answer_other_options= IntVar()
        self.choice_other_options_basement = Radiobutton(w2,text='Basement',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_other_options)
        self.choice_other_options_basement.place(x=100 , y=510)
        self.choice_other_options_garage = Radiobutton(w2,text='Garage',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_other_options)
        self.choice_other_options_garage.place(x=215 , y=510)
        self.choice_other_options_elevator = Radiobutton(w2,text='Elevator',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_other_options)
        self.choice_other_options_elevator.place(x=310 , y=510)
        self.choice_other_options_none = Radiobutton(w2,text='None',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_other_options)
        self.choice_other_options_none.place(x=407 , y=510)


    def reset_all (self):
        self.entry_area_min.delete(0,END)
        self.entry_area_max.delete(0,END)
        self.entry_num_of_rooms_min.delete(0,END)
        self.entry_num_of_rooms_max.delete(0,END)
        self.entry_price_per_meter_min.delete(0,END)
        self.entry_price_per_meter_max.delete(0,END)
        self.entry_total_price_min.delete(0,END)
        self.entry_total_price_max.delete(0,END)
        self.entry_deposit_min.delete(0,END)
        self.entry_deposit_max.delete(0,END)
        self.entry_monthly_rent_min.delete(0,END)
        self.entry_monthly_rent_max.delete(0,END)
        self.entry_floor.delete(0,END)
        self.entry_unit.delete(0,END)
        self.zone.set('Zone')
        self.district.set('District')
        self.product_year.set('Year')
        self.answer_type.set(0)
        self.answer_cabinet_type.set(0)
        self.answer_floor_material.set(0)
        self.answer_other_options.set(0)
        self.entry_deposit_min.config(state='normal')
        self.entry_deposit_max.config(state='normal')
        self.entry_total_price_min.config(state='normal')
        self.entry_total_price_max.config(state='normal')
        self.entry_monthly_rent_min.config(state='normal')
        self.entry_monthly_rent_max.config(state='normal')
        self.entry_price_per_meter_min.config(state='normal')
        self.entry_price_per_meter_max.config(state='normal')
        
        

    def drop_down2 (self):
        self.answer_zone = StringVar()
        self.zone = ttk.Combobox(w2 , width=6 , values = list(tehran.keys()) , textvariable = self.answer_zone ,state='readonly')
        self.zone.set('Zone')
        self.zone.place(x=170,y=340)
        self.zone.bind("<<ComboboxSelected>>", self.update_district_options)
        

        self.answer_district= StringVar()
        self.district=ttk.Combobox(w2,width=18, textvariable=self.answer_district , values='' , state='disabled')
        self.district.set('District')
        self.district.place(x=302,y=340)

        self.product_year_list = [i for i in range (1403,1341,-1)]
        self.answer_product_year=StringVar()
        self.product_year=ttk.Combobox(w2 , width=6 , values= self.product_year_list , textvariable = self.answer_product_year,state='readonly')
        self.product_year.set("Year")
        self.product_year.place(x=310,y=380)
    
    def update_district_options (self,x):
        selected_zone = int(self.answer_zone.get())
        if (selected_zone) in list(tehran.keys()):
            self.district.config(values=tehran[selected_zone])
            self.district.config(state='readonly')
        else:
            self.district.config(values='')
            self.district.config(state='disabled')



    def buttons2 (self):
        self.button_reset=Button(w2,text='Reset',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',command=self.reset_all)
        self.button_reset.place(x=110,y=590)

        self.button_save=Button(w2,text='Search',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',command=self.search2)
        self.button_save.place(x=10,y=590)

    def address_show(self, address):
                messagebox.showinfo('Full Address', address)

    def search2 (self):
        self.search_window = Tk()
        self.search_window.title('Search Results')
        self.search_window.resizable(0,0)
        self.screen_height=self.search_window.winfo_screenheight()
        self.screen_width=self.search_window.winfo_screenwidth()
        self.search_window.geometry(f'1088x500+{self.screen_width//2-544}+{self.screen_height//2-250}')

        self.label_type=Label(self.search_window,text='Row',font=("Aria",9,'bold'),foreground='#005441')
        self.label_type.grid(row=0,column=0,pady=10)

        self.label_type=Label(self.search_window,text='Type',font=("Aria",9,'bold'),foreground='#005441')
        self.label_type.grid(row=0,column=1,pady=10)

        self.label_area=Label(self.search_window,text='Area(m)',font=("Aria",9,'bold'),foreground='#005441')
        self.label_area.grid(row=0,column=2,padx=6)

        self.label_num_of_rooms=Label(self.search_window,text='Rooms',font=("Aria",9,'bold'),foreground='#005441')
        self.label_num_of_rooms.grid(row=0,column=3)

        self.label_price_per_meter=Label(self.search_window,text='Per Meter',font=("Aria",8,'bold'),foreground='#005441')
        self.label_price_per_meter.grid(row=0,column=4,pady=10)

        self.label_total_price=Label(self.search_window,text='Total',font=("Aria",9,'bold'),foreground='#005441')
        self.label_total_price.grid(row=0,column=5,pady=10)

        self.label_deposit=Label(self.search_window,text='Deposit',font=("Aria",9,'bold'),foreground='#005441')
        self.label_deposit.grid(row=0,column=6,pady=10)

        self.label_monthly_rent=Label(self.search_window,text='Rent',font=("Aria",9,'bold'),foreground='#005441')
        self.label_monthly_rent.grid(row=0,column=7,pady=10)

        self.label_zone=Label(self.search_window,text='Zone',font=("Aria",9,'bold'),foreground='#005441')
        self.label_zone.grid(row=0,column=8,pady=10)

        self.label_full_district=Label(self.search_window,text='District',font=("Aria",9,'bold'),foreground='#005441')
        self.label_full_district.grid(row=0,column=9,pady=10)

        self.label_address=Label(self.search_window,text='Address',font=("Aria",9,'bold'),foreground='#005441')
        self.label_address.grid(row=0,column=10,pady=10)

        self.label_floor=Label(self.search_window,text='Floor',font=("Aria",9,'bold'),foreground='#005441')
        self.label_floor.grid(row=0,column=11,pady=10)

        self.label_unit=Label(self.search_window,text='Unit',font=("Aria",9,'bold'),foreground='#005441')
        self.label_unit.grid(row=0,column=12,pady=10)

        self.label_unit=Label(self.search_window,text='Year',font=("Aria",9,'bold'),foreground='#005441')
        self.label_unit.grid(row=0,column=13,pady=10)

        self.label_cabinet=Label(self.search_window,text='Cabinet',font=("Aria",9,'bold'),foreground='#005441')
        self.label_cabinet.grid(row=0,column=14,pady=10)

        self.label_floor_material=Label(self.search_window,text='Floor',font=("Aria",9,'bold'),foreground='#005441')
        self.label_floor_material.grid(row=0,column=15,pady=10)

        self.label_other_options=Label(self.search_window,text='Other',font=("Aria",9,'bold'),foreground='#005441')
        self.label_other_options.grid(row=0,column=16,pady=10)



        conditions = []
        parameters = []

        self.min_area=self.entry_area_min.get()
        self.max_area=self.entry_area_max.get()
        self.min_num_of_rooms=self.entry_num_of_rooms_min.get()
        self.max_num_of_rooms=self.entry_num_of_rooms_max.get()
        self.min_price_per_meter=self.entry_price_per_meter_min.get()
        self.max_price_per_meter=self.entry_price_per_meter_max.get()
        self.min_total_price=self.entry_total_price_min.get()
        self.max_total_price=self.entry_total_price_max.get()
        self.min_deposit=self.entry_deposit_min.get()
        self.max_deposit=self.entry_deposit_max.get()
        self.min_monthly_rent=self.entry_monthly_rent_min.get()
        self.max_monthly_rent=self.entry_monthly_rent_max.get()
        self.min_floor=self.entry_floor.get()
        self.min_unit=self.entry_unit.get()

        
        if self.answer_type.get() == 0:
            self.min_type = False
        else:
            if self.answer_type.get() == 1:  
                self.answer_answer='Rent'
            if self.answer_type.get() == 2:
                self.answer_answer='Buy'
            self.min_type = self.answer_answer

        if self.answer_zone.get() == 'Zone' :
            self.min_zone = False
        else:
            self.min_zone=self.answer_zone.get()
        
        if self.district['state']=='disabled' or self.answer_district.get() == 'District':
            self.min_district = False
        else:
            self.min_district = self.answer_district.get()

        if self.answer_product_year.get() == 'Year' :
            self.min_year = False
        else:
            self.min_year=self.answer_product_year.get()
        
        if self.answer_cabinet_type.get() == 0 :
            self.min_cabinet = False
        else:
            if self.answer_cabinet_type.get() == 1 :
                self.cabinet_answer = 'MDF'
            if self.answer_cabinet_type.get() == 2 :
                self.cabinet_answer = 'ClipBoard'
            if self.answer_cabinet_type.get() == 3 :
                self.cabinet_answer = 'High Glass'
            if self.answer_cabinet_type.get() == 4 :
                self.cabinet_answer = 'Other'
            self.min_cabinet = self.cabinet_answer

        if self.answer_floor_material.get() == 0 :
            self.min_floor = False
        else:
            if self.answer_floor_material.get() == 1 :
                self.floor_answer = 'Ceramic'
            if self.answer_floor_material.get() == 2 :
                self.floor_answer = 'Parquet'
            if self.answer_floor_material.get() == 3 :
                self.floor_answer = 'Mosaic'
            if self.answer_floor_material.get() == 4 :
                self.floor_answer = 'Other'
            self.min_floor = self.floor_answer

        if self.answer_other_options.get() == 0 :
            self.min_other = False
        else:
            if self.answer_other_options.get() == 1 :
                self.other_answer = 'Basement'
            if self.answer_other_options.get() == 2 :
                self.other_answer = 'Garage'
            if self.answer_other_options.get() == 3 :
                self.other_answer = 'Elevator'
            if self.answer_other_options.get() == 4 :
                self.other_answer = 'None'
            self.min_other = self.other_answer
        

             
        

        if self.min_area:
            conditions.append("area >= ?")
            parameters.append(str(self.min_area))


        if self.max_area:
            conditions.append("area <= ?")
            parameters.append(str(self.max_area))
        

        if self.min_num_of_rooms:
            conditions.append("num_of_rooms >= ?")
            parameters.append(str(self.min_num_of_rooms))
        if self.max_num_of_rooms:
            conditions.append("num_of_rooms <= ?")
            parameters.append(str(self.max_num_of_rooms))


        if self.min_price_per_meter:
            conditions.append("price_per_meter >= ?")
            parameters.append(str(self.min_price_per_meter))
        if self.max_price_per_meter:
            conditions.append("price_per_meter <= ?")
            parameters.append(str(self.max_price_per_meter))


        if self.min_total_price:
            conditions.append("total_price >= ?")
            parameters.append(str(self.min_total_price))
        if self.max_total_price:
            conditions.append("total_price <= ?")
            parameters.append(str(self.max_total_price))


        if self.min_deposit:
            conditions.append("deposit >= ?")
            parameters.append(str(self.min_deposit))
        if self.max_deposit:
            conditions.append("deposit <= ?")
            parameters.append(str(self.max_deposit))


        if self.min_monthly_rent:
            conditions.append("monthly_rent >= ?")
            parameters.append(str(self.min_monthly_rent))
        if self.max_monthly_rent:
            conditions.append("monthly_rent <= ?")
            parameters.append(str(self.max_monthly_rent))


        if self.min_zone:
            conditions.append("zone = ?")
            parameters.append(str(self.min_zone))

        
        if self.min_district:
            conditions.append("district = ?")
            parameters.append(str(self.min_district))


        if self.min_floor:
            conditions.append("floor = ?")
            parameters.append(str(self.min_floor))


        if self.min_unit:
            conditions.append("unit = ?")
            parameters.append(str(self.min_unit))

        if self.min_year:
            conditions.append("year = ?")
            parameters.append(str(self.min_year))

        
        if self.min_type:
            conditions.append("type = ?")
            parameters.append(str(self.min_type))

        
        if self.min_cabinet:
            conditions.append("cabinet_type = ?")
            parameters.append(str(self.min_cabinet))


        if self.min_floor:
            conditions.append("floor_type = ?")
            parameters.append(str(self.min_floor))

        
        if self.min_other:
            conditions.append("other_options = ?")
            parameters.append(str(self.min_other))


        





        self.query = "SELECT id,type,area,num_of_rooms,price_per_meter,total_price,deposit,monthly_rent,zone,district,floor,unit,product_year,cabinet_type,floor_type,other_options FROM realestate"
        if conditions:
            self.query += " WHERE " + " AND ".join(conditions)

        self.query2 = "SELECT full_address from realestate"
        if conditions:
            self.query2 += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(self.query, parameters)
        self.res = self.cursor.fetchall()

        self.cursor.execute(self.query2, parameters)
        self.add = self.cursor.fetchall()

        row_counter=1
        column_counter=0
        for record in self.res:
            for i in record: 
                answers = Entry(self.search_window,font=("Arial",8),border='1px',relief='solid',width=10,justify="center")
                answers.grid(row=row_counter,column=column_counter)
                answers.insert(0,i)
                column_counter+=1
                if column_counter==10:
                    column_counter=11
                if column_counter==17:
                    column_counter=0
                    row_counter+=1
                answers.config(state='readonly')
        row_counter2 = 1
        column_counter2 = 10
        for add_count in self.add:
            add_button = Button(self.search_window, text='Address', font=("Aria", 7),activebackground='green', command=lambda addr=add_count[0]: self.address_show(addr))
            add_button.grid(row=row_counter2, column=column_counter2)
            row_counter2 += 1
            
        self.search_window.mainloop()
        
    def menu2 (self):
        self.menubar = Menu(self.w2)
        self.w2.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar,tearoff=0)
        self.file_menu.add_command(label='Add',command=self.add_page)
        self.file_menu.add_command(label='Search')
        self.file_menu.add_command(label='Update / Delete',command=self.update_page)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.w2.destroy)
        self.menubar.add_cascade(label="Action",menu=self.file_menu)

        help_menu = Menu(self.menubar,tearoff=0)
        help_menu.add_command(label='Light',command=self.light)
        help_menu.add_command(label='Dark',command=self.dark)
        self.menubar.add_cascade(label="Theme",menu=help_menu)    

    def add_page (self):
       self.w2.destroy()
       import main

    def update_page (self):
        self.w2.destroy()
        import page3

    def dark(self):
        self.w2.config(bg='#242424')

        self.label_minimum.config(bg='#242424')
        self.label_maximum.config(bg='#242424')
        self.label_type.config(bg='#242424')
        self.label_area.config(bg='#242424')
        self.label_num_of_rooms.config(bg='#242424')
        self.label_price_per_meter.config(bg='#242424')
        self.label_total_price.config(bg='#242424')
        self.label_deposit.config(bg='#242424')
        self.label_monthly_rent.config(bg='#242424')
        self.label_address.config(bg='#242424')
        self.label_floor.config(bg='#242424')
        self.label_unit.config(bg='#242424')
        self.label_cabinet.config(bg='#242424')
        self.label_other_options.config(bg='#242424')
        self.label_floor_material.config(bg='#242424')

        self.label_minimum.config(fg='#fad502')
        self.label_maximum.config(fg='#fad502')
        self.label_type.config(fg='#fad502')
        self.label_area.config(fg='#fad502')
        self.label_num_of_rooms.config(fg='#fad502')
        self.label_price_per_meter.config(fg='#fad502')
        self.label_total_price.config(fg='#fad502')
        self.label_deposit.config(fg='#fad502')
        self.label_monthly_rent.config(fg='#fad502')
        self.label_address.config(fg='#fad502')
        self.label_floor.config(fg='#fad502')
        self.label_unit.config(fg='#fad502')
        self.label_cabinet.config(fg='#fad502')
        self.label_other_options.config(fg='#fad502')
        self.label_floor_material.config(fg='#fad502')

        self.choice_cabinet_type_clipboard.config(bg='#242424')
        self.choice_cabinet_type_high_glass.config(bg='#242424')
        self.choice_cabinet_type_mdf.config(bg='#242424')
        self.choice_cabinet_type_other.config(bg='#242424')
        self.choice_other_options_basement.config(bg='#242424')
        self.choice_other_options_elevator.config(bg='#242424')
        self.choice_other_options_garage.config(bg='#242424')
        self.choice_other_options_none.config(bg='#242424')
        self.choice_floor_material_ceramic.config(bg='#242424')
        self.choice_floor_material_mosaic.config(bg='#242424')
        self.choice_floor_material_other.config(bg='#242424')
        self.choice_floor_material_parquet.config(bg='#242424')
        self.choice_type_buy.config(bg='#242424')
        self.choice_type_rent.config(bg='#242424')

        self.choice_cabinet_type_clipboard.config(fg='#fad502')
        self.choice_cabinet_type_high_glass.config(fg='#fad502')
        self.choice_cabinet_type_mdf.config(fg='#fad502')
        self.choice_cabinet_type_other.config(fg='#fad502')
        self.choice_other_options_basement.config(fg='#fad502')
        self.choice_other_options_elevator.config(fg='#fad502')
        self.choice_other_options_garage.config(fg='#fad502')
        self.choice_other_options_none.config(fg='#fad502')
        self.choice_floor_material_ceramic.config(fg='#fad502')
        self.choice_floor_material_mosaic.config(fg='#fad502')
        self.choice_floor_material_other.config(fg='#fad502')
        self.choice_floor_material_parquet.config(fg='#fad502')
        self.choice_type_buy.config(fg='#fad502')
        self.choice_type_rent.config(fg='#fad502')

        self.entry_area_min.config(background='#8a8888')
        self.entry_area_max.config(background='#8a8888')
        self.entry_num_of_rooms_min.config(background='#8a8888')
        self.entry_num_of_rooms_max.config(background='#8a8888')
        self.entry_price_per_meter_min.config(background='#8a8888')
        self.entry_price_per_meter_max.config(background='#8a8888')
        self.entry_price_per_meter_min.config(disabledbackground='#4f4b4b')
        self.entry_price_per_meter_max.config(disabledbackground='#4f4b4b')
        self.entry_total_price_min.config(background='#8a8888')
        self.entry_total_price_max.config(background='#8a8888')
        self.entry_total_price_min.config(disabledbackground='#4f4b4b')
        self.entry_total_price_max.config(disabledbackground='#4f4b4b')
        self.entry_deposit_min.config(background='#8a8888')
        self.entry_deposit_max.config(background='#8a8888')
        self.entry_deposit_min.config(disabledbackground='#4f4b4b')
        self.entry_deposit_max.config(disabledbackground='#4f4b4b')
        self.entry_monthly_rent_min.config(background='#8a8888')
        self.entry_monthly_rent_max.config(background='#8a8888')
        self.entry_monthly_rent_min.config(disabledbackground='#4f4b4b')
        self.entry_monthly_rent_max.config(disabledbackground='#4f4b4b')
        self.entry_floor.config(background='#8a8888')
        self.entry_unit.config(background='#8a8888')

        self.button_save.config(background='#8a8888')
        self.button_reset.config(background='#8a8888')
        self.button_save.config(foreground='#fad502')
        self.button_reset.config(foreground='#fad502')
        

        


    def light(self):
        self.w2.config(bg='#f0f0f0')

        self.label_minimum.config(bg='#f0f0f0')
        self.label_maximum.config(bg='#f0f0f0')
        self.label_type.config(bg='#f0f0f0')
        self.label_area.config(bg='#f0f0f0')
        self.label_num_of_rooms.config(bg='#f0f0f0')
        self.label_price_per_meter.config(bg='#f0f0f0')
        self.label_total_price.config(bg='#f0f0f0')
        self.label_deposit.config(bg='#f0f0f0')
        self.label_monthly_rent.config(bg='#f0f0f0')
        self.label_address.config(bg='#f0f0f0')
        self.label_floor.config(bg='#f0f0f0')
        self.label_unit.config(bg='#f0f0f0')
        self.label_cabinet.config(bg='#f0f0f0')
        self.label_other_options.config(bg='#f0f0f0')
        self.label_floor_material.config(bg='#f0f0f0')

        self.label_minimum.config(fg='#005441')
        self.label_maximum.config(fg='#005441')
        self.label_type.config(fg='#005441')
        self.label_area.config(fg='#005441')
        self.label_num_of_rooms.config(fg='#005441')
        self.label_price_per_meter.config(fg='#005441')
        self.label_total_price.config(fg='#005441')
        self.label_deposit.config(fg='#005441')
        self.label_monthly_rent.config(fg='#005441')
        self.label_address.config(fg='#005441')
        self.label_floor.config(fg='#005441')
        self.label_unit.config(fg='#005441')
        self.label_cabinet.config(fg='#005441')
        self.label_other_options.config(fg='#005441')
        self.label_floor_material.config(fg='#005441')

        self.choice_cabinet_type_clipboard.config(bg='#f0f0f0')
        self.choice_cabinet_type_high_glass.config(bg='#f0f0f0')
        self.choice_cabinet_type_mdf.config(bg='#f0f0f0')
        self.choice_cabinet_type_other.config(bg='#f0f0f0')
        self.choice_other_options_basement.config(bg='#f0f0f0')
        self.choice_other_options_elevator.config(bg='#f0f0f0')
        self.choice_other_options_garage.config(bg='#f0f0f0')
        self.choice_other_options_none.config(bg='#f0f0f0')
        self.choice_floor_material_ceramic.config(bg='#f0f0f0')
        self.choice_floor_material_mosaic.config(bg='#f0f0f0')
        self.choice_floor_material_other.config(bg='#f0f0f0')
        self.choice_floor_material_parquet.config(bg='#f0f0f0')
        self.choice_type_buy.config(bg='#f0f0f0')
        self.choice_type_rent.config(bg='#f0f0f0')

        self.choice_cabinet_type_clipboard.config(fg='#005441')
        self.choice_cabinet_type_high_glass.config(fg='#005441')
        self.choice_cabinet_type_mdf.config(fg='#005441')
        self.choice_cabinet_type_other.config(fg='#005441')
        self.choice_other_options_basement.config(fg='#005441')
        self.choice_other_options_elevator.config(fg='#005441')
        self.choice_other_options_garage.config(fg='#005441')
        self.choice_other_options_none.config(fg='#005441')
        self.choice_floor_material_ceramic.config(fg='#005441')
        self.choice_floor_material_mosaic.config(fg='#005441')
        self.choice_floor_material_other.config(fg='#005441')
        self.choice_floor_material_parquet.config(fg='#005441')
        self.choice_type_buy.config(fg='#005441')
        self.choice_type_rent.config(fg='#005441')

        self.entry_area_min.config(background='white')
        self.entry_area_max.config(background='white')
        self.entry_num_of_rooms_min.config(background='white')
        self.entry_num_of_rooms_max.config(background='white')
        self.entry_price_per_meter_min.config(background='white')
        self.entry_price_per_meter_max.config(background='white')
        self.entry_price_per_meter_min.config(disabledbackground='#f0f0f0')
        self.entry_price_per_meter_max.config(disabledbackground='#f0f0f0')
        self.entry_total_price_min.config(background='white')
        self.entry_total_price_max.config(background='white')
        self.entry_total_price_min.config(disabledbackground='#f0f0f0')
        self.entry_total_price_max.config(disabledbackground='#f0f0f0')
        self.entry_deposit_min.config(background='white')
        self.entry_deposit_max.config(background='white')
        self.entry_deposit_min.config(disabledbackground='#f0f0f0')
        self.entry_deposit_max.config(disabledbackground='#f0f0f0')
        self.entry_monthly_rent_min.config(background='white')
        self.entry_monthly_rent_max.config(background='white')
        self.entry_monthly_rent_min.config(disabledbackground='#f0f0f0')
        self.entry_monthly_rent_max.config(disabledbackground='#f0f0f0')
        self.entry_floor.config(background='white')
        self.entry_unit.config(background='white')

        self.button_save.config(background='white')
        self.button_reset.config(background='white')
        self.button_save.config(foreground='#005441')
        self.button_reset.config(foreground='#005441')

    
    def mainloop(self):
        self.w2.mainloop()

w2 = Tk()
app = Page2(w2)
app.mainloop()