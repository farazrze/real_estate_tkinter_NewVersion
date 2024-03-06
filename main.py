from tkinter import *
from tkinter import ttk , messagebox 
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

class Real_Estate:
    def __init__ (self,w):
        self.w=w
        self.w.title('Real Estate Add Item')
        self.w.resizable(0,0)
        self.screen_height=w.winfo_screenheight()
        self.screen_width=w.winfo_screenwidth()
        self.w.geometry(f'500x645+{self.screen_width//2-250}+{self.screen_height//2-350}')
    
        self.call_all1()


    def call_all1(self):
        self.label()
        self.entry()
        self.radio_buttons()
        self.drop_down()
        self.text_box()
        self.buttons()
        self.create_database()
        self.menu()
        
        
    def create_database (self):
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


    
    def label (self):
        self.label_type=Label(w,text='Type',font=("Aria",12,'bold'),foreground='#005441')
        self.label_type.place(x=10,y=10)

        self.label_area=Label(w,text='Area(m)',font=("Aria",12,'bold'),foreground='#005441')
        self.label_area.place(x=10,y=50)

        self.label_num_of_rooms=Label(w,text='Num of Rooms',font=("Aria",12,'bold'),foreground='#005441')
        self.label_num_of_rooms.place(x=10,y=90)

        self.label_price_per_meter=Label(w,text='Price Per Meter',font=("Aria",12,'bold'),foreground='#005441')
        self.label_price_per_meter.place(x=10,y=130)

        self.label_total_price=Label(w,text='Total Price',font=("Aria",12,'bold'),foreground='#005441')
        self.label_total_price.place(x=10,y=170)

        self.label_deposit=Label(w,text='Deposit',font=("Aria",12,'bold'),foreground='#005441')
        self.label_deposit.place(x=10,y=210)

        self.label_monthly_rent=Label(w,text='Monthly Rent',font=("Aria",12,'bold'),foreground='#005441')
        self.label_monthly_rent.place(x=10,y=250)

        self.label_address=Label(w,text='Address',font=("Aria",12,'bold'),foreground='#005441')
        self.label_address.place(x=10,y=290)

        self.label_full_address=Label(w,text='Full Address',font=("Aria",12,'bold'),foreground='#005441')
        self.label_full_address.place(x=10,y=330)
        
        self.label_floor=Label(w,text='Floor',font=("Aria",12,'bold'),foreground='#005441')
        self.label_floor.place(x=10,y=440)

        self.label_unit=Label(w,text='Unit',font=("Aria",12,'bold'),foreground='#005441')
        self.label_unit.place(x=150,y=440)

        self.label_cabinet=Label(w,text='Cabinet :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_cabinet.place(x=10,y=480)

        self.label_floor_material=Label(w,text='Floor :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_floor_material.place(x=10,y=520)

        self.label_other_options=Label(w,text='Other :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_other_options.place(x=10,y=560)


    def entry (self):
        self.entry_area=Entry(w,font=("Arial",14),border='1px',relief='solid')
        self.entry_area.place(x=150,y=50)

        self.entry_num_of_rooms=Entry(w,font=("Arial",14),border='1px',relief='solid')
        self.entry_num_of_rooms.place(x=150,y=90)

        self.entry_price_per_meter=Entry(w,font=("Arial",14),border='1px',relief='solid')
        self.entry_price_per_meter.place(x=150,y=130)

        self.entry_total_price=Entry(w,font=("Arial",14),border='1px',relief='solid',state='readonly')
        self.entry_total_price.place(x=150,y=170)

        self.entry_deposit=Entry(w,font=("Arial",14),border='1px',relief='solid')
        self.entry_deposit.place(x=150,y=210)

        self.entry_monthly_rent=Entry(w,font=("Arial",14),border='1px',relief='solid')
        self.entry_monthly_rent.place(x=150,y=250)
        
        self.entry_floor=Entry(w,font=("Arial",14),width=5,border='1px',relief='solid')
        self.entry_floor.place(x=60,y=440)

        self.entry_unit=Entry(w,font=("Arial",14),width=5,border='1px',relief='solid')
        self.entry_unit.place(x=195,y=440)



    def radio_buttons (self):
        self.answer_type = IntVar()
        self.choice_type_rent = Radiobutton(w,text='Rent',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_type,command=self.rent_options)
        self.choice_type_rent.place(x=150 , y=10)
        self.choice_type_buy = Radiobutton(w,text='Buy',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_type,command=self.buy_options)
        self.choice_type_buy.place(x=230 , y=10)


        self.answer_cabinet_type = IntVar()
        self.choice_cabinet_type_mdf = Radiobutton(w,text='MDF',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_mdf.place(x=100 , y=480)
        self.choice_cabinet_type_clipboard = Radiobutton(w,text='ClipBoard',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_clipboard.place(x=185 , y=480)
        self.choice_cabinet_type_high_glass = Radiobutton(w,text='High Glass',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_high_glass.place(x=295 , y=480)
        self.choice_cabinet_type_other = Radiobutton(w,text='Other',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_cabinet_type)
        self.choice_cabinet_type_other.place(x=407 , y=480)


        self.answer_floor_material = IntVar()
        self.choice_floor_material_ceramic = Radiobutton(w,text='Ceramic',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_floor_material)
        self.choice_floor_material_ceramic.place(x=100 , y=520)
        self.choice_floor_material_parquet = Radiobutton(w,text='Parquet',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_floor_material)
        self.choice_floor_material_parquet.place(x=195 , y=520)
        self.choice_floor_material_mosaic = Radiobutton(w,text='Mosaic',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_floor_material)
        self.choice_floor_material_mosaic.place(x=300 , y=520)
        self.choice_floor_material_other = Radiobutton(w,text='Other',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_floor_material)
        self.choice_floor_material_other.place(x=407 , y=520)

        self.answer_other_options= IntVar()
        self.choice_other_options_basement = Radiobutton(w,text='Basement',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_other_options)
        self.choice_other_options_basement.place(x=100 , y=560)
        self.choice_other_options_garage = Radiobutton(w,text='Garage',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_other_options)
        self.choice_other_options_garage.place(x=215 , y=560)
        self.choice_other_options_elevator = Radiobutton(w,text='Elevator',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_other_options)
        self.choice_other_options_elevator.place(x=310 , y=560)
        self.choice_other_options_none = Radiobutton(w,text='None',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_other_options)
        self.choice_other_options_none.place(x=407 , y=560)




    def rent_options (self):
        self.entry_price_per_meter.delete(0,END)
        self.entry_total_price.delete(0,END)
        self.entry_price_per_meter.config(state='disabled')
        self.entry_total_price.config(state='disabled')
        self.entry_monthly_rent.config(state='normal')
        self.entry_deposit.config(state='normal')

        

    def buy_options (self):
        self.entry_monthly_rent.delete(0,END)
        self.entry_deposit.delete(0,END)
        self.entry_monthly_rent.config(state='disabled')
        self.entry_deposit.config(state='disabled')
        self.entry_price_per_meter.config(state='normal')
        self.entry_total_price.config(state='readonly')
        


    
    def drop_down (self):
        self.answer_zone = StringVar()
        self.zone = ttk.Combobox(w , width=6 , values = list(tehran.keys()) , textvariable = self.answer_zone ,state='readonly')
        self.zone.set('Zone')
        self.zone.place(x=150,y=291)
        self.zone.bind("<<ComboboxSelected>>", self.update_district_options)
        

        self.answer_district= StringVar()
        self.district=ttk.Combobox(w,width=18, textvariable=self.answer_district , values='' , state='disabled')
        self.district.set('District')
        self.district.place(x=240,y=291)

        self.product_year_list = [i for i in range (1403,1341,-1)]
        self.answer_product_year=StringVar()
        self.product_year=ttk.Combobox(w , width=6 , values= self.product_year_list , textvariable = self.answer_product_year,state='readonly')
        self.product_year.set("Year")
        self.product_year.place(x=310,y=440)


    
    def text_box (self):
        self.text_box_full_address = Text(w,font=("Arial",10),width=31,height=5,border='1px',relief='solid')
        self.text_box_full_address.place(x=150,y=335)


    def buttons (self):
        self.button_reset=Button(w,text='Reset',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',command=self.reset_all)
        self.button_reset.place(x=90,y=600)

        self.button_save=Button(w,text='Save',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',state='normal' ,command=self.save )
        self.button_save.place(x=10,y=600)

        self.button_note=Button(w,text=' ! ',font=("Aria",8,'bold'),foreground='#005441',activebackground='green',state='normal' ,command=self.note )
        self.button_note.place(x=380,y=170)

    def note (self):
        self.note1=messagebox.showinfo('Total Price Calculation','Total Price will be calculated automatically after pressing Save button (Area * Price Per Meter)')

    def save (self):
        self.error_list=[]
        self.auth_type = False
        self.auth_area=False
        self.auth_num_of_rooms=False
        self.auth_price_per_meter=False
        self.auth_total_price=False
        self.auth_deposit=False
        self.auth_monthly_rent=False
        self.auth_zone=False
        self.auth_district=False
        self.auth_full_address=False
        self.auth_floor=False
        self.auth_unit=False
        self.auth_product_year=False
        self.auth_cabinet=False
        self.auth_floor=False
        self.auth_other=False

        if self.answer_type.get() == 0:
            self.error_list.append('Type : Choose one option ')
        else:
            if self.answer_type.get()==1:
                self.answer_type2 = 'Rent'
                self.auth_type = True
            elif self.answer_type.get()==2:
                self.answer_type2 = 'Buy'
                self.auth_type = True
                



        if len(self.entry_area.get())==0:
            self.error_list.append('Area : can not be empty')
        elif not all(char.isdigit() for char in self.entry_area.get()):
            self.error_list.append('Area : You can only use numbers')
        else :
            self.auth_area = True





        if len(self.entry_num_of_rooms.get())==0:
            self.error_list.append('Num of rooms : can not be empty')
        elif not all(char.isdigit() for char in self.entry_num_of_rooms.get()):
            self.error_list.append('Num of rooms : You can only use numbers')
        else :
            self.auth_num_of_rooms = True




        if self.entry_price_per_meter['state'] == 'normal':
            if len(self.entry_price_per_meter.get())==0:
                self.error_list.append('Price per meter : can not be empty')
            elif not all(char.isdigit() for char in self.entry_price_per_meter.get()):
                self.error_list.append('Price per meter : You can only use numbers')
            else :
                self.auth_price_per_meter = True
                self.entry_price_per_meter2 = self.entry_price_per_meter.get()
        else:
            self.auth_price_per_meter = True
            self.entry_price_per_meter2 = '0'




        if self.entry_total_price['state'] == 'readonly' and self.auth_price_per_meter == True and self.auth_area == True:
            self.entry_total_price.config(state='normal')
            self.entry_total_price.insert(0,int(self.entry_area.get())*int(self.entry_price_per_meter.get()))
            self.entry_total_price.config(state='readonly')
            self.entry_total_price2 = self.entry_total_price.get()
            self.auth_total_price = True
        else:
            self.auth_total_price = True
            self.entry_total_price2 = '0'




        if self.entry_deposit['state'] == 'normal':
            if len(self.entry_deposit.get())==0:
                self.error_list.append('Deposit : can not be empty')
            elif not all(char.isdigit() for char in self.entry_deposit.get()):
                self.error_list.append('Deposit : You can only use numbers')
            else :
                self.auth_deposit = True
                self.entry_deposit2 = self.entry_deposit.get()
        else:
            self.auth_deposit = True
            self.entry_deposit2 = '0'




        if self.entry_monthly_rent['state'] == 'normal':
            if len(self.entry_monthly_rent.get())==0:
                self.error_list.append('Monthly rent : can not be empty')
            elif not all(char.isdigit() for char in self.entry_monthly_rent.get()):
                self.error_list.append('Monthly rent : You can only use numbers')
            else :
                self.auth_monthly_rent = True
                self.entry_monthly_rent2 = self.entry_monthly_rent.get()
        else:
            self.auth_monthly_rent = True
            self.entry_monthly_rent2 = '0'




        if not self.text_box_full_address.get("1.0", "end-1c").strip():
            self.error_list.append('Full address : can not be empty')
        else:
            self.auth_full_address = True




        if len(self.entry_floor.get())==0:
            self.error_list.append('Floor : can not be empty')
        elif not all(char.isdigit() for char in self.entry_floor.get()):
            self.error_list.append('Floor : You can only use numbers')
        else :
            self.auth_floor = True




        if len(self.entry_unit.get())==0:
            self.error_list.append('Unit : can not be empty')
        elif not all(char.isdigit() for char in self.entry_unit.get()):
            self.error_list.append('Unit : You can only use numbers')
        else :
            self.auth_unit = True
        


        self.selected_year = self.answer_product_year.get()
        if self.selected_year not in map(str, self.product_year_list):
            self.error_list.append('Year : Please choose one option')
        else:
            self.auth_product_year = True

        


        self.selected_zone = self.answer_zone.get()
        if self.selected_zone not in map(str, list(tehran.keys())):
            self.error_list.append('Zone : Please choose one option')
        else:
            self.auth_zone = True
        


        self.selected_district = any(self.answer_district.get() in x for x in tehran.values())
        if self.selected_district:
            self.auth_district = True
            self.selected_district2 = self.answer_district.get()
        else:
            self.error_list.append('District : Please choose one option')

        

        if self.answer_cabinet_type.get()==0:
            self.error_list.append('Cabinet types : Choose one option')
        else:
            self.auth_cabinet = True

        if self.answer_cabinet_type.get() == 1 :
            self.answer_cabinet_type2 = 'MDF'
        elif self.answer_cabinet_type.get() == 2 :
            self.answer_cabinet_type2 = 'ClipBoard'
        elif self.answer_cabinet_type.get() == 3 :
            self.answer_cabinet_type2 = 'High Glass'
        elif self.answer_cabinet_type.get() == 4 :
            self.answer_cabinet_type2 = 'Other'
        



        if self.answer_floor_material.get()==0:
            self.error_list.append('Floor types : Choose one option')
        else:
            self.auth_floor = True
        
        if self.answer_floor_material.get() == 1 :
            self.answer_floor_material2 = 'Ceramic'
        elif self.answer_floor_material.get() == 2 :
            self.answer_floor_material2 = 'Parquet'
        elif self.answer_floor_material.get() == 3 :
            self.answer_floor_material2 = 'Mosaic'
        elif self.answer_floor_material.get() == 4 :
            self.answer_floor_material2 = 'Other'
        




        if self.answer_other_options.get()==0:
            self.error_list.append('Other options : Choose one option')
        else:
            self.auth_other = True

        if self.answer_other_options.get() == 1 :
            self.answer_other_options2 = 'Basement'
        elif self.answer_other_options.get() == 2 :
            self.answer_other_options2 = 'Garage'
        elif self.answer_other_options.get() == 3 :
            self.answer_other_options2 = 'Elevator'
        elif self.answer_other_options.get() == 4 :
            self.answer_other_options2 = 'None'


        
        self.counter = sum([self.auth_type,self.auth_area, self.auth_num_of_rooms, self.auth_price_per_meter, self.auth_total_price,
                            self.auth_deposit, self.auth_monthly_rent, self.auth_zone, self.auth_district,
                            self.auth_full_address, self.auth_floor, self.auth_unit, self.auth_product_year,
                            self.auth_cabinet, self.auth_floor, self.auth_other])
        if self.counter==16:
            query = '''
                    INSERT INTO realestate 
                    (
                    type,
                    area,
                    num_of_rooms,
                    price_per_meter,
                    total_price,
                    deposit,
                    monthly_rent,
                    zone,
                    district,
                    full_address,
                    floor,
                    unit,
                    product_year,
                    cabinet_type,
                    floor_type,
                    other_options
                    )
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    '''
            values = (
                self.answer_type2,
                self.entry_area.get(),
                self.entry_num_of_rooms.get(),
                self.entry_price_per_meter2,
                self.entry_total_price2,
                self.entry_deposit2,
                self.entry_monthly_rent2,
                self.selected_zone,
                self.selected_district2,
                self.text_box_full_address.get("1.0", "end-1c"),
                self.entry_floor.get(),
                self.entry_unit.get(),
                self.selected_year,
                self.answer_cabinet_type2,
                self.answer_floor_material2,
                self.answer_other_options2
                )
            
            self.cursor.execute(query,values)
            self.connector.commit()
            self.message=messagebox.showinfo('Save information','Added successfully!!')
            print(self.answer_type2)

            self.entry_area.delete(0,END)
            self.entry_num_of_rooms.delete(0,END)
            self.entry_price_per_meter.delete(0,END)
            self.entry_total_price.config(state='normal')
            self.entry_total_price.delete(0,END)
            self.entry_total_price.config(state='disabled')
            self.entry_deposit.delete(0,END)
            self.entry_monthly_rent.delete(0,END)
            self.entry_floor.delete(0,END)
            self.entry_unit.delete(0,END)
            self.zone.set('Zone')
            self.district.set('District')
            self.product_year.set('Year')
            self.text_box_full_address.delete(1.0,END)
            self.answer_type.set(None)
            self.answer_cabinet_type.set(None)
            self.answer_floor_material.set(None)
            self.answer_other_options.set(None)

        else :
            self.message=messagebox.showerror('Authentication Error!!','\n'.join(self.error_list))
        
        

    def reset_all (self):
        self.entry_area.delete(0,END)
        self.entry_num_of_rooms.delete(0,END)
        self.entry_price_per_meter.delete(0,END)
        self.entry_total_price.config(state='normal')
        self.entry_total_price.delete(0,END)
        self.entry_total_price.config(state='disabled')
        self.entry_deposit.config(state='normal')
        self.entry_monthly_rent.config(state='normal')
        self.entry_price_per_meter.config(state='normal')
        self.entry_deposit.delete(0,END)
        self.entry_monthly_rent.delete(0,END)
        self.entry_floor.delete(0,END)
        self.entry_unit.delete(0,END)
        self.zone.set('Zone')
        self.district.set('District')
        self.product_year.set('Year')
        self.text_box_full_address.delete(1.0,END)
        self.answer_type.set(0)
        self.answer_cabinet_type.set(0)
        self.answer_floor_material.set(0)
        self.answer_other_options.set(0)



    def update_district_options (self,x):
        selected_zone = int(self.answer_zone.get())
        if (selected_zone) in list(tehran.keys()):
            self.district.config(values=tehran[selected_zone])
            self.district.config(state='readonly')
        else:
            self.district.config(values='')
            self.district.config(state='disabled')
        

    def mainloop (self):
        self.w.mainloop()



    def menu (self):
        self.menubar = Menu(self.w)
        self.w.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar,tearoff=0)
        self.file_menu.add_command(label='Add')
        self.file_menu.add_command(label='Search',command=self.search_page)
        self.file_menu.add_command(label='Update / Delete',command=self.update_page)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.w.destroy)
        self.menubar.add_cascade(label="Action",menu=self.file_menu)

        help_menu = Menu(self.menubar,tearoff=0)
        help_menu.add_command(label='Light',command=self.light)
        help_menu.add_command(label='Dark',command=self.dark)
        self.menubar.add_cascade(label="Theme",menu=help_menu)

    
    def search_page (self):
        self.w.destroy()
        import page2
        


    def update_page (self):
        self.w.destroy()
        import page3
    
    def dark(self):
        self.w.config(bg='#242424')

        self.label_type.config(bg='#242424')
        self.label_area.config(bg='#242424')
        self.label_num_of_rooms.config(bg='#242424')
        self.label_price_per_meter.config(bg='#242424')
        self.label_total_price.config(bg='#242424')
        self.label_deposit.config(bg='#242424')
        self.label_monthly_rent.config(bg='#242424')
        self.label_address.config(bg='#242424')
        self.label_full_address.config(bg='#242424')
        self.label_floor.config(bg='#242424')
        self.label_unit.config(bg='#242424')
        self.label_cabinet.config(bg='#242424')
        self.label_other_options.config(bg='#242424')
        self.label_floor_material.config(bg='#242424')

        self.label_type.config(fg='#fad502')
        self.label_area.config(fg='#fad502')
        self.label_num_of_rooms.config(fg='#fad502')
        self.label_price_per_meter.config(fg='#fad502')
        self.label_total_price.config(fg='#fad502')
        self.label_deposit.config(fg='#fad502')
        self.label_monthly_rent.config(fg='#fad502')
        self.label_address.config(fg='#fad502')
        self.label_full_address.config(fg='#fad502')
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

        self.entry_area.config(background='#8a8888')
        self.entry_num_of_rooms.config(background='#8a8888')
        self.entry_price_per_meter.config(background='#8a8888')
        self.entry_price_per_meter.config(disabledbackground='#4f4b4b')
        self.entry_total_price.config(readonlybackground='#4f4b4b')
        self.entry_total_price.config(disabledbackground='#4f4b4b')
        self.entry_deposit.config(background='#8a8888')
        self.entry_deposit.config(disabledbackground='#4f4b4b')
        self.entry_monthly_rent.config(background='#8a8888')
        self.entry_monthly_rent.config(disabledbackground='#4f4b4b')
        self.entry_floor.config(background='#8a8888')
        self.entry_unit.config(background='#8a8888')

        self.button_save.config(background='#8a8888')
        self.button_reset.config(background='#8a8888')
        self.button_note.config(background='#8a8888')
        self.button_save.config(foreground='#fad502')
        self.button_reset.config(foreground='#fad502')
        self.button_note.config(foreground='#fad502')

        self.text_box_full_address.config(background='#8a8888')
         
    def light(self):
        self.w.config(bg='#f0f0f0')

        self.label_type.config(bg='#f0f0f0')
        self.label_area.config(bg='#f0f0f0')
        self.label_num_of_rooms.config(bg='#f0f0f0')
        self.label_price_per_meter.config(bg='#f0f0f0')
        self.label_total_price.config(bg='#f0f0f0')
        self.label_deposit.config(bg='#f0f0f0')
        self.label_monthly_rent.config(bg='#f0f0f0')
        self.label_address.config(bg='#f0f0f0')
        self.label_full_address.config(bg='#f0f0f0')
        self.label_floor.config(bg='#f0f0f0')
        self.label_unit.config(bg='#f0f0f0')
        self.label_cabinet.config(bg='#f0f0f0')
        self.label_other_options.config(bg='#f0f0f0')
        self.label_floor_material.config(bg='#f0f0f0')

        self.label_type.config(fg='#005441')
        self.label_area.config(fg='#005441')
        self.label_num_of_rooms.config(fg='#005441')
        self.label_price_per_meter.config(fg='#005441')
        self.label_total_price.config(fg='#005441')
        self.label_deposit.config(fg='#005441')
        self.label_monthly_rent.config(fg='#005441')
        self.label_address.config(fg='#005441')
        self.label_full_address.config(fg='#005441')
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

        self.entry_area.config(background='white')
        self.entry_num_of_rooms.config(background='white')
        self.entry_price_per_meter.config(background='white')
        self.entry_price_per_meter.config(disabledbackground='#f0f0f0')
        self.entry_total_price.config(readonlybackground='#f0f0f0')
        self.entry_total_price.config(disabledbackground='#f0f0f0')
        self.entry_deposit.config(background='white')
        self.entry_deposit.config(disabledbackground='#f0f0f0')
        self.entry_monthly_rent.config(background='white')
        self.entry_monthly_rent.config(disabledbackground='#f0f0f0')
        self.entry_floor.config(background='white')
        self.entry_unit.config(background='white')

        self.button_save.config(background='#f0f0f0')
        self.button_reset.config(background='#f0f0f0')
        self.button_note.config(background='#f0f0f0')
        self.button_save.config(foreground='#005441')
        self.button_reset.config(foreground='#005441')
        self.button_note.config(foreground='#005441')

        self.text_box_full_address.config(background='white')



w = Tk()
app = Real_Estate(w)
app.mainloop()

