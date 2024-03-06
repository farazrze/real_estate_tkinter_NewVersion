from tkinter import *
from tkinter import ttk,messagebox
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


class Page3 :
    def __init__ (self,w3):
        self.w3=w3
        self.w3.title('Real Estate Update/Delete Item')
        self.w3.resizable(0,0)
        self.screen_height=w3.winfo_screenheight()
        self.screen_width=w3.winfo_screenwidth()
        self.w3.geometry(f'500x645+{self.screen_width//2-250}+{self.screen_height//2-350}')

        self.call_all3()


    def call_all3(self):
        self.menu()
        self.label()
        self.entry()
        self.radio_buttons()
        self.drop_down()
        self.text_box()
        self.buttons()
        self.database()
        

    def database(self):
        self.connector=sqlite3.connect('RealEstate_database.db')
        self.cursor=self.connector.cursor()


    def label (self):
        self.label_type=Label(w3,text='Type',font=("Aria",12,'bold'),foreground='#005441')
        self.label_type.place(x=10,y=35)

        self.label_area=Label(w3,text='Area(m)',font=("Aria",12,'bold'),foreground='#005441')
        self.label_area.place(x=10,y=70)

        self.label_num_of_rooms=Label(w3,text='Num of Rooms',font=("Aria",12,'bold'),foreground='#005441')
        self.label_num_of_rooms.place(x=10,y=110)

        self.label_price_per_meter=Label(w3,text='Price Per Meter',font=("Aria",12,'bold'),foreground='#005441')
        self.label_price_per_meter.place(x=10,y=150)

        self.label_total_price=Label(w3,text='Total Price',font=("Aria",12,'bold'),foreground='#005441')
        self.label_total_price.place(x=10,y=190)

        self.label_deposit=Label(w3,text='Deposit',font=("Aria",12,'bold'),foreground='#005441')
        self.label_deposit.place(x=10,y=230)

        self.label_monthly_rent=Label(w3,text='Monthly Rent',font=("Aria",12,'bold'),foreground='#005441')
        self.label_monthly_rent.place(x=10,y=270)

        self.label_address=Label(w3,text='Address',font=("Aria",12,'bold'),foreground='#005441')
        self.label_address.place(x=10,y=310)

        self.label_full_address=Label(w3,text='Full Address',font=("Aria",12,'bold'),foreground='#005441')
        self.label_full_address.place(x=10,y=350)
        
        self.label_floor=Label(w3,text='Floor',font=("Aria",12,'bold'),foreground='#005441')
        self.label_floor.place(x=10,y=440)

        self.label_unit=Label(w3,text='Unit',font=("Aria",12,'bold'),foreground='#005441')
        self.label_unit.place(x=150,y=440)

        self.label_cabinet=Label(w3,text='Cabinet :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_cabinet.place(x=10,y=480)

        self.label_floor_material=Label(w3,text='Floor :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_floor_material.place(x=10,y=520)

        self.label_other_options=Label(w3,text='Other :',font=("Aria",12,'bold'),foreground='#005441')
        self.label_other_options.place(x=10,y=560)

        self.label_file_code=Label(w3,text='File Code',font=("Aria",12,'bold'),foreground='#005441')
        self.label_file_code.place(x=10,y=8)


    def entry (self):

        self.entry_file_code=Entry(w3,font=("Arial",14),width=5,border='1px',relief='solid')
        self.entry_file_code.place(x=150,y=8)

        self.entry_area=Entry(w3,font=("Arial",14),border='1px',relief='solid',state='disabled')
        self.entry_area.place(x=150,y=70)

        self.entry_num_of_rooms=Entry(w3,font=("Arial",14),border='1px',relief='solid',state='disabled')
        self.entry_num_of_rooms.place(x=150,y=110)

        self.entry_price_per_meter=Entry(w3,font=("Arial",14),border='1px',relief='solid',state='disabled')
        self.entry_price_per_meter.place(x=150,y=150)

        self.entry_total_price=Entry(w3,font=("Arial",14),border='1px',relief='solid',state='disabled')
        self.entry_total_price.place(x=150,y=190)

        self.entry_deposit=Entry(w3,font=("Arial",14),border='1px',relief='solid',state='disabled')
        self.entry_deposit.place(x=150,y=230)

        self.entry_monthly_rent=Entry(w3,font=("Arial",14),border='1px',relief='solid',state='disabled')
        self.entry_monthly_rent.place(x=150,y=270)
        
        self.entry_floor=Entry(w3,font=("Arial",14),width=5,border='1px',relief='solid',state='disabled')
        self.entry_floor.place(x=60,y=440)

        self.entry_unit=Entry(w3,font=("Arial",14),width=5,border='1px',relief='solid',state='disabled')
        self.entry_unit.place(x=195,y=440)

        


    def radio_buttons (self):
        self.answer_type = IntVar()
        self.choice_type_rent = Radiobutton(w3,text='Rent',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_type,state='disabled')
        self.choice_type_rent.place(x=150 , y=35)
        self.choice_type_buy = Radiobutton(w3,text='Buy',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_type,state='disabled')
        self.choice_type_buy.place(x=230 , y=35)


        self.answer_cabinet_type = IntVar()
        self.choice_cabinet_type_mdf = Radiobutton(w3,text='MDF',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_cabinet_type,state='disabled')
        self.choice_cabinet_type_mdf.place(x=100 , y=480)
        self.choice_cabinet_type_clipboard = Radiobutton(w3,text='ClipBoard',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_cabinet_type,state='disabled')
        self.choice_cabinet_type_clipboard.place(x=185 , y=480)
        self.choice_cabinet_type_high_glass = Radiobutton(w3,text='High Glass',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_cabinet_type,state='disabled')
        self.choice_cabinet_type_high_glass.place(x=295 , y=480)
        self.choice_cabinet_type_other = Radiobutton(w3,text='Other',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_cabinet_type,state='disabled')
        self.choice_cabinet_type_other.place(x=407 , y=480)


        self.answer_floor_material = IntVar()
        self.choice_floor_material_ceramic = Radiobutton(w3,text='Ceramic',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_floor_material,state='disabled')
        self.choice_floor_material_ceramic.place(x=100 , y=520)
        self.choice_floor_material_parquet = Radiobutton(w3,text='Parquet',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_floor_material,state='disabled')
        self.choice_floor_material_parquet.place(x=195 , y=520)
        self.choice_floor_material_mosaic = Radiobutton(w3,text='Mosaic',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_floor_material,state='disabled')
        self.choice_floor_material_mosaic.place(x=300 , y=520)
        self.choice_floor_material_other = Radiobutton(w3,text='Other',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_floor_material,state='disabled')
        self.choice_floor_material_other.place(x=407 , y=520)

        self.answer_other_options= IntVar()
        self.choice_other_options_basement = Radiobutton(w3,text='Basement',font=("Aria",12),foreground='#005441',value=1,variable=self.answer_other_options,state='disabled')
        self.choice_other_options_basement.place(x=100 , y=560)
        self.choice_other_options_garage = Radiobutton(w3,text='Garage',font=("Aria",12),foreground='#005441',value=2,variable=self.answer_other_options,state='disabled')
        self.choice_other_options_garage.place(x=215 , y=560)
        self.choice_other_options_elevator = Radiobutton(w3,text='Elevator',font=("Aria",12),foreground='#005441',value=3,variable=self.answer_other_options,state='disabled')
        self.choice_other_options_elevator.place(x=310 , y=560)
        self.choice_other_options_none = Radiobutton(w3,text='None',font=("Aria",12),foreground='#005441',value=4,variable=self.answer_other_options,state='disabled')
        self.choice_other_options_none.place(x=407 , y=560)
        


    
    def drop_down (self):
        self.answer_zone = StringVar()
        self.zone = ttk.Combobox(w3 , width=6 , values = list(tehran.keys()) , textvariable = self.answer_zone ,state='disabled')
        self.zone.set('Zone')
        self.zone.place(x=150,y=314)
        self.zone.bind("<<ComboboxSelected>>", self.update_district_options)
        

        self.answer_district= StringVar()
        self.district=ttk.Combobox(w3,width=18, textvariable=self.answer_district , values='' , state='readonly')
        self.district.set('District')
        self.district.place(x=240,y=314)

        self.product_year_list = [i for i in range (1403,1341,-1)]
        self.answer_product_year=StringVar()
        self.product_year=ttk.Combobox(w3 , width=6 , values= self.product_year_list , textvariable = self.answer_product_year,state='disabled')
        self.product_year.set("Year")
        self.product_year.place(x=310,y=440)


    def update_district_options (self,x):
        selected_zone = int(self.answer_zone.get())
        if (selected_zone) in list(tehran.keys()):
            self.district.config(values=tehran[selected_zone])
            self.district.config(state='readonly')
        else:
            self.district.config(values='')
            self.district.config(state='disabled')

    
    def text_box (self):
        self.text_box_full_address = Text(w3,font=("Arial",10),width=31,height=4,border='1px',relief='solid',state='disabled')
        self.text_box_full_address.place(x=150,y=355)


    def buttons (self):
        self.button_reset=Button(w3,text='Reset',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',command=self.reset_all)
        self.button_reset.place(x=90,y=600)

        self.button_search=Button(w3,text='Search',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',state='normal',command=self.search_result)
        self.button_search.place(x=10,y=600)

        self.button_update=Button(w3,text='Update',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',state='disabled',command=self.update_record)
        self.button_update.place(x=340,y=600)

        self.button_delete=Button(w3,text='Delete',font=("Aria",12,'bold'),foreground='#005441',activebackground='green',state='disabled',command=self.delete_record)
        self.button_delete.place(x=425,y=600)


    def reset_all (self):
        self.entry_num_of_rooms.config(state='normal')
        self.entry_price_per_meter.config(state='normal')
        self.entry_total_price.config(state='normal')
        self.entry_deposit.config(state='normal')
        self.entry_monthly_rent.config(state='normal')
        self.entry_floor.config(state='normal')
        self.entry_unit.config(state='normal')
        self.choice_type_buy.config(state='normal')
        self.choice_type_rent.config(state='normal')
        self.choice_cabinet_type_clipboard.config(state='normal')
        self.choice_cabinet_type_high_glass.config(state='normal')
        self.choice_cabinet_type_mdf.config(state='normal')
        self.choice_cabinet_type_other.config(state='normal')
        self.choice_floor_material_ceramic.config(state='normal')
        self.choice_floor_material_mosaic.config(state='normal')
        self.choice_floor_material_parquet.config(state='normal')
        self.choice_floor_material_other.config(state='normal')
        self.choice_other_options_basement.config(state='normal')
        self.choice_other_options_elevator.config(state='normal')
        self.choice_other_options_garage.config(state='normal')
        self.choice_other_options_none.config(state='normal')
        self.text_box_full_address.config(state='normal')
        self.zone.config(state='normal')
        self.product_year.config(state='normal')
        self.button_delete.config(state='normal')
        self.button_update.config(state='normal')
        
        self.entry_area.delete(0,END)
        self.entry_num_of_rooms.delete(0,END)
        self.entry_price_per_meter.delete(0,END)
        self.entry_total_price.delete(0,END)
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

        self.entry_file_code.config(state='normal')
        self.entry_file_code.delete(0,END)
        self.entry_area.config(state='disabled')
        self.entry_num_of_rooms.config(state='disabled')
        self.entry_price_per_meter.config(state='disabled')
        self.entry_total_price.config(state='disabled')
        self.entry_deposit.config(state='disabled')
        self.entry_monthly_rent.config(state='disabled')
        self.entry_floor.config(state='disabled')
        self.entry_unit.config(state='disabled')
        self.choice_type_buy.config(state='disabled')
        self.choice_type_rent.config(state='disabled')
        self.choice_cabinet_type_clipboard.config(state='disabled')
        self.choice_cabinet_type_high_glass.config(state='disabled')
        self.choice_cabinet_type_mdf.config(state='disabled')
        self.choice_cabinet_type_other.config(state='disabled')
        self.choice_floor_material_ceramic.config(state='disabled')
        self.choice_floor_material_mosaic.config(state='disabled')
        self.choice_floor_material_parquet.config(state='disabled')
        self.choice_floor_material_other.config(state='disabled')
        self.choice_other_options_basement.config(state='disabled')
        self.choice_other_options_elevator.config(state='disabled')
        self.choice_other_options_garage.config(state='disabled')
        self.choice_other_options_none.config(state='disabled')
        self.text_box_full_address.config(state='disabled')
        self.zone.config(state='disabled')
        self.product_year.config(state='disabled')
        self.district.config(state='disabled')
        self.button_delete.config(state='disabled')
        self.button_update.config(state='disabled')
        



    def menu (self):
        self.menubar = Menu(self.w3)
        self.w3.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar,tearoff=0)
        self.file_menu.add_command(label='Add',command=self.add_page)
        self.file_menu.add_command(label='Search',command=self.search_page)
        self.file_menu.add_command(label='Update / Delete')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.w3.destroy)
        self.menubar.add_cascade(label="Action",menu=self.file_menu)

        help_menu = Menu(self.menubar,tearoff=0)
        help_menu.add_command(label='Light',command=self.light)
        help_menu.add_command(label='Dark',command=self.dark)
        self.menubar.add_cascade(label="Theme",menu=help_menu)




    def search_result(self):
        result_list=[]
        self.file_code = str(self.entry_file_code.get())
        self.cursor.execute("SELECT * FROM realestate WHERE id = ?", (self.file_code,))
        result = self.cursor.fetchone()
        if result:
            self.entry_file_code.config(state='disabled')
            self.entry_area.config(state='normal')
            self.entry_num_of_rooms.config(state='normal')
            self.entry_price_per_meter.config(state='normal')
            self.entry_total_price.config(state='normal')
            self.entry_deposit.config(state='normal')
            self.entry_monthly_rent.config(state='normal')
            self.entry_floor.config(state='normal')
            self.entry_unit.config(state='normal')
            self.choice_type_buy.config(state='normal')
            self.choice_type_rent.config(state='normal')
            self.choice_cabinet_type_clipboard.config(state='normal')
            self.choice_cabinet_type_high_glass.config(state='normal')
            self.choice_cabinet_type_mdf.config(state='normal')
            self.choice_cabinet_type_other.config(state='normal')
            self.choice_floor_material_ceramic.config(state='normal')
            self.choice_floor_material_mosaic.config(state='normal')
            self.choice_floor_material_parquet.config(state='normal')
            self.choice_floor_material_other.config(state='normal')
            self.choice_other_options_basement.config(state='normal')
            self.choice_other_options_elevator.config(state='normal')
            self.choice_other_options_garage.config(state='normal')
            self.choice_other_options_none.config(state='normal')
            self.text_box_full_address.config(state='normal')
            self.zone.config(state='readonly')
            self.product_year.config(state='readonly')
            self.button_delete.config(state='normal')
            self.button_update.config(state='normal')
            self.cursor.execute("SELECT * FROM realestate WHERE id = ?",(self.file_code))
            result1 = self.cursor.fetchone()
            for i in result1:
                result_list.append(i)


            if result_list[1] == 'Rent':
                self.answer_type.set(1)
            elif result_list[1] == 'Buy':
                self.answer_type.set(2)

            self.entry_area.insert(0,result_list[2])
            self.entry_num_of_rooms.insert(0,result_list[3])
            self.entry_price_per_meter.insert(0,result_list[4])
            self.entry_total_price.insert(0,result_list[5])
            self.entry_deposit.insert(0,result_list[6])
            self.entry_monthly_rent.insert(0,result_list[7])
            self.zone.set(result_list[8])
            self.district.set(result_list[9])
            selected_zone = int(self.answer_zone.get())
            if (selected_zone) in list(tehran.keys()):
                self.district.config(values=tehran[selected_zone])
            self.text_box_full_address.insert(1.0,result_list[10])
            self.entry_floor.insert(0,result_list[11])
            self.entry_unit.insert(0,result_list[12])
            self.product_year.set(result_list[13])

            if result_list[14] == 'MDF':
                self.answer_cabinet_type.set(1)
            if result_list[14] == 'ClipBoard':
                self.answer_cabinet_type.set(2)
            if result_list[14] == 'High Glass':
                self.answer_cabinet_type.set(3)
            if result_list[14] == 'Other':
                self.answer_cabinet_type.set(4)

            if result_list[15] == 'Ceramic':
                self.answer_floor_material.set(1)
            if result_list[15] == 'Parquet':
                self.answer_floor_material.set(2)
            if result_list[15] == 'Mosaic':
                self.answer_floor_material.set(3)
            if result_list[15] == 'Other':
                self.answer_floor_material.set(4)

            if result_list[16] == 'Basement':
                self.answer_other_options.set(1)
            if result_list[16] == 'Garage':
                self.answer_other_options.set(2)
            if result_list[16] == 'Elevator':
                self.answer_other_options.set(3)
            if result_list[16] == 'None':
                self.answer_other_options.set(4)
        else:
            error_message = messagebox.showerror('Error !!','No such Record!')
        


        
    def delete_record(self):
        message_delete = messagebox.askyesno("delete","Are you Sure you want to delete this Record??")
        if message_delete:
            self.cursor.execute("DELETE FROM realestate WHERE id=?",(self.file_code))
            self.cursor.connection.commit()
            message_delete2=messagebox.showinfo("Delete","Deleted successfully!!")
            self.reset_all()
        
    
    def update_record(self):
        message_update = messagebox.askyesno("Update","Save Changes??")
        if message_update:
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
                
                query1=f'''
                        UPDATE realestate SET
                        type = ?  ,
                        area = ?  ,
                        num_of_rooms = ?  ,
                        price_per_meter = ?  ,
                        total_price = ?  ,
                        deposit = ?  ,
                        monthly_rent = ?  ,
                        zone = ?  ,
                        district = ? ,
                        full_address = ? ,
                        floor = ? ,
                        unit = ?  ,
                        product_year = ?  ,
                        cabinet_type = ?  ,
                        floor_type = ?  ,
                        other_options = ? 
                        WHERE id = ? '''

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
                    self.text_box_full_address.get("1.0" , "end-1c"),
                    self.entry_floor.get(),
                    self.entry_unit.get(),
                    self.selected_year,
                    self.answer_cabinet_type2,
                    self.answer_floor_material2,
                    self.answer_other_options2,
                    self.file_code
                    )       
                        
                self.cursor.execute(query1 , values)
                self.connector.commit()
                

                message_change = messagebox.showinfo('Update Record','Updated successfully!!')
                self.reset_all()
            else : 
                self.message=messagebox.showerror('Authentication Error!!','\n'.join(self.error_list))      



    def add_page (self):
        self.w3.destroy()
        import main

    def search_page (self):
        self.w3.destroy()
        import page2 


    def dark(self):
        self.w3.config(bg='#242424')

        self.label_file_code.config(bg='#242424')
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

        self.label_file_code.config(fg='#fad502')
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

        self.entry_file_code.config(background='#8c8c8c')
        self.entry_total_price.config(background='#8c8c8c')
        self.entry_area.config(background='#8a8888')
        self.entry_num_of_rooms.config(background='#8a8888')
        self.entry_area.config(disabledbackground='#4f4b4b')
        self.entry_num_of_rooms.config(disabledbackground='#4f4b4b')
        self.entry_floor.config(disabledbackground='#4f4b4b')
        self.entry_unit.config(disabledbackground='#4f4b4b')
        self.entry_price_per_meter.config(background='#8a8888')
        self.entry_price_per_meter.config(disabledbackground='#4f4b4b')
        self.entry_total_price.config(readonlybackground='#4f4b4b')
        self.entry_total_price.config(disabledbackground='#4f4b4b')
        self.entry_deposit.config(background='#8a8888')
        self.entry_deposit.config(disabledbackground='#4f4b4b')
        self.entry_file_code.config(disabledbackground='#4f4b4b')
        self.entry_monthly_rent.config(background='#8a8888')
        self.entry_monthly_rent.config(disabledbackground='#4f4b4b')
        self.entry_floor.config(background='#8a8888')
        self.entry_unit.config(background='#8a8888')

        self.button_search.config(background='#8a8888')
        self.button_search.config(foreground='#fad502')
        self.button_search.config(disabledforeground='#4f4b4b')
        self.button_reset.config(background='#8a8888')
        self.button_reset.config(foreground='#fad502')
        self.button_reset.config(disabledforeground='#4f4b4b')
        self.button_delete.config(foreground='#fad502')
        self.button_delete.config(background='#8a8888')
        self.button_delete.config(disabledforeground='#4f4b4b')
        self.button_update.config(foreground='#fad502')
        self.button_update.config(background='#8a8888')
        self.button_update.config(disabledforeground='#4f4b4b')

        

        self.text_box_full_address.config(background='#8a8888')
        
        

    
    
    def light(self):
        self.w3.config(bg='#f0f0f0')

        self.label_file_code.config(bg='#f0f0f0')
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

        self.label_file_code.config(fg='#005441')
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

        self.entry_file_code.config(background='white')
        self.entry_total_price.config(background='white')
        self.entry_total_price.config(disabledbackground='#f0f0f0')
        self.entry_area.config(background='white')
        self.entry_num_of_rooms.config(background='white')
        self.entry_price_per_meter.config(background='white')
        self.entry_total_price.config(readonlybackground='#f0f0f0')
        self.entry_deposit.config(background='white')
        self.entry_monthly_rent.config(background='white')
        self.entry_floor.config(background='white')
        self.entry_unit.config(background='white')
        self.entry_file_code.config(disabledbackground='#f0f0f0')
        self.entry_area.config(disabledbackground='#f0f0f0')
        self.entry_num_of_rooms.config(disabledbackground='#f0f0f0')
        self.entry_price_per_meter.config(disabledbackground='#f0f0f0')
        self.entry_deposit.config(disabledbackground='#f0f0f0')
        self.entry_monthly_rent.config(disabledbackground='#f0f0f0')
        self.entry_floor.config(disabledbackground='#f0f0f0')
        self.entry_unit.config(disabledbackground='#f0f0f0')


        
        self.button_search.config(foreground='#005441')
        self.button_search.config(background='#f0f0f0')
        self.button_search.config(disabledforeground='#4f4b4b')
        self.button_reset.config(foreground='#005441')
        self.button_reset.config(background='#f0f0f0')
        self.button_reset.config(disabledforeground='#4f4b4b')
        self.button_delete.config(foreground='#005441')
        self.button_delete.config(background='#f0f0f0')
        self.button_delete.config(disabledforeground='#4f4b4b')
        self.button_update.config(foreground='#005441')
        self.button_update.config(background='#f0f0f0')
        self.button_update.config(disabledforeground='#4f4b4b')


        

        self.text_box_full_address.config(background='white')


    def mainloop(self):
        self.w3.mainloop()


w3 = Tk()
app = Page3(w3)
app.mainloop()
