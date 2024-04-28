import customtkinter
import os
from PIL import Image
from EPA import epa_submit
from tkcalendar import DateEntry
import datetime
# from Wr_reports import Wr_summit
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SMS ALL TOOLs")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="SMS TOOLS", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Time Sheet Reports",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.EPA_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="EPA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.EPA_button.grid(row=2, column=0, sticky="ew")

        self.HRM_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="HRM",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.HRM_button.grid(row=3, column=0, sticky="ew")

        self.MRTG_button = customtkinter.CTkButton(self.navigation_frame,corner_radius=0,height=40,border_spacing=10,text="MRTG",
                                                   fg_color="transparent",text_color=("gray10","gray90"),hover_color=("gray70", "gray30"),
                                                   anchor="w",)
        self.MRTG_button.grid(row=4, column=0, sticky="ew")
        self.Plotter_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Ping Plotter",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", )
        self.Plotter_button.grid(row=5, column=0, sticky="ew")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        pass_img_data = Image.open("password-icon.png")
        email_icon_data = Image.open("email-icon.png")
        self.pass_icon = customtkinter.CTkImage(dark_image=pass_img_data, light_image=pass_img_data, size=(17, 17))
        self.email_icon = customtkinter.CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
        # create home frame
        side_img_data = Image.open("side-.png")
        self.side_img = customtkinter.CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent",)
        self.home_frame.grid_rowconfigure(9, weight=2)

        self.Label=customtkinter.CTkLabel(self.home_frame,text="SMS",text_color="#5766F9", anchor="w", justify="center",
         font=("Arial Bold", 24) )
        self.Label.grid(row=0,column=1,sticky="nsew")
        self.User_label=customtkinter.CTkLabel(self.home_frame,text=" Username:",text_color="#5766F9", anchor="w", justify="left",
         font=("Arial Bold", 14), image=self.email_icon, compound="left")
        self.User_label.grid(row=1,column=0,pady=10,sticky="w")
        self.Username_Entry=customtkinter.CTkEntry(self.home_frame,width=225,fg_color="#EEEEEE", border_color="#5766F9", border_width=1,
                       text_color="#000000")
        self.Username_Entry.grid(row=1,column=1,pady=10,)
        self.Pass_wr_Label = customtkinter.CTkLabel(self.home_frame, text=" Password Domain:", text_color="#5766F9",
                                                     anchor="w",
                                                     justify="left",
                                                     font=("Arial Bold", 14), image=self.pass_icon, compound="left")
        self.Pass_wr_Label.grid(row=2,column=0,pady=10,sticky="w")
        self.Pass_wr_Entry = customtkinter.CTkEntry(self.home_frame, width=225, fg_color="#EEEEEE",
                                                     border_color="#5766F9", border_width=1,
                                                     text_color="#000000", show="*")
        self.Pass_wr_Entry.grid(row=2,column=1,pady=10)
        self.Pass_mail_Label = customtkinter.CTkLabel(self.home_frame, text=" Password Email:", text_color="#5766F9",
                                                     anchor="w",
                                                     justify="left",
                                                     font=("Arial Bold", 14), image=self.pass_icon, compound="left")
        self.Pass_mail_Label.grid(row=3,column=0,pady=10,sticky="w")
        self.Pass_mail_Entry = customtkinter.CTkEntry(self.home_frame, width=225, fg_color="#EEEEEE",
                                                     border_color="#5766F9", border_width=1,
                                                     text_color="#000000", show="*")
        self.Pass_mail_Entry.grid(row=3,column=1,pady=10)
        self.Label_Choose_date=customtkinter.CTkLabel(self.home_frame,text="Choose Date",text_color="#5766F9",
                                                     anchor="w",
                                                     justify="left",
                                                     font=("Arial Bold", 14),compound="left")
        self.Label_Choose_date.grid(row=4,column=0,pady=10,padx=80,sticky="w")
        self.DateShift=DateEntry(self.home_frame,selectmode='day',date_pattern="mm/dd/yyyy")
        self.DateShift.grid(row=4,column=1,pady=10,sticky="nsew")


        self.Label_Choose_Shift=customtkinter.CTkLabel(self.home_frame,text="Choose Shift",text_color="#5766F9",
                                                     anchor="w",
                                                     justify="left",
                                                     font=("Arial Bold", 14),compound="left")
        self.Label_Choose_Shift.grid(row=5,column=0,pady=10,sticky="w")
        self.Shift = customtkinter.CTkOptionMenu(self.home_frame, dynamic_resizing=False,
                                                 values=["Morning", "Afternoon", "Night"],command=self.update_date_entry)
        if self.Shift.get == "Night":
            self.DateShift.set_date(self.DateShift.get_date() - datetime.timedelta(days=1))
        self.Shift.grid(row=5,column=1,pady=10,sticky="nsew")
        self.Label_Leader=customtkinter.CTkLabel(self.home_frame,text="Leader",text_color="#5766F9",
                                                     anchor="w",
                                                     justify="left",
                                                     font=("Arial Bold", 14),compound="left")
        self.Label_Leader.grid(row=6, column=0, padx=100, pady=10,  columnspan=3)
        self.Leader_Trinh=customtkinter.CTkCheckBox(self.home_frame,text="Trinh")
        self.Leader_Trinh.grid(row=7,column=0)
        self.Leader_Jameslee=customtkinter.CTkCheckBox(self.home_frame,text="Jameslee")
        self.Leader_Jameslee.grid(row=7,column=1)

        self.WR_summit_Button = customtkinter.CTkButton(self.home_frame, text="Summit", command=self.Wr_Time_Sheet)
        self.WR_summit_Button.grid(row=9, column=0, padx=100, pady=10,  columnspan=3)
        # End Home Frame
        # create EPA frame
        epa_img_data = Image.open("epa_logo.png")
        self.epa_img_logo = customtkinter.CTkImage(dark_image=epa_img_data, light_image=epa_img_data, size=(180, 40))

        self.EPA_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.EPA_frame.grid_columnconfigure(0, weight=1)
        self.Label_EPA = customtkinter.CTkLabel(self.EPA_frame, text="", text_color="#5766F9", anchor="w",
                                            justify="center",
                                            font=("Arial Bold", 24), image=self.epa_img_logo)
        self.Label_EPA.grid(pady=(50, 5), padx=(25, 0))
        self.ID_EPA_Label=customtkinter.CTkLabel(self.EPA_frame,text=" ID:", text_color="#5766F9", anchor="w", justify="left",
         font=("Arial Bold", 14), image=self.email_icon, compound="left")
        self.ID_EPA_Label.grid(  padx=(25, 0))
        self.ID_EPA_Entry=customtkinter.CTkEntry(self.EPA_frame,width=225,fg_color="#EEEEEE", border_color="#5766F9", border_width=1,
                       text_color="#000000")
        self.ID_EPA_Entry.grid( padx=(30, 0))
        self.Pass_EPA_Label = customtkinter.CTkLabel(self.EPA_frame, text=" Password:", text_color="#5766F9", anchor="w",
                                                   justify="left",
                                                   font=("Arial Bold", 14), image=self.pass_icon, compound="left")
        self.Pass_EPA_Label.grid(padx=(25, 0))
        self.Pass_EPA_Entry = customtkinter.CTkEntry(self.EPA_frame, width=225, fg_color="#EEEEEE",
                                                   border_color="#5766F9", border_width=1,
                                                   text_color="#000000",show="*")
        self.Pass_EPA_Entry.grid(padx=(30, 0))
        self.EPA_summit_Button=customtkinter.CTkButton(self.EPA_frame,text="Summit",command=self.FIll_EPA)
        self.EPA_summit_Button.grid(pady=(25,0) ,padx=(30, 0))
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.EPA_button.configure(fg_color=("gray75", "gray25") if name == "EPA" else "transparent")
        self.HRM_button.configure(fg_color=("gray75", "gray25") if name == "HRM" else "transparent")
        self.MRTG_button.configure(fg_color=("gray75", "gray25") if name == "MRTG" else "transparent")
        self.Plotter_button.configure(fg_color=("gray75", "gray25") if name == "Ping Plotter" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "EPA":
            self.EPA_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.EPA_frame.grid_forget()
        if name == "HRM":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("EPA")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def FIll_EPA(self):
        ID=self.ID_EPA_Entry.get()
        PW=self.Pass_EPA_Entry.get()
        epa_submit(ID,PW)

    def update_date_entry(self,Shift):
        if Shift== "Night":
            current_date = datetime.date.today() - datetime.timedelta(days=1)
            self.DateShift.set_date(current_date)
        else:
            self.DateShift.set_date(datetime.date.today())
    def Wr_Time_Sheet(self):
        Username=self.Username_Entry.get()
        Pass_Wr=self.Pass_wr_Entry.get()
        Pass_mail=self.Pass_mail_Entry
        DateShift=self.DateShift.get_date()
        DateShift=DateShift.strftime("%m/%d/%Y")
        Shift=self.Shift.get()
        Leader = []
        if self.Leader_Trinh.get() == 1:
            Leader.append("TrinhHuynh@sms-vn.com")
        if self.Leader_Jameslee.get() == 1:
            Leader.append("JamesLee@sms-vn.com")

        # Wr_summit(Username,Pass_Wr,Pass_mail,DateShift,Shift,Leader)

if __name__ == "__main__":
    app = App()
    app.mainloop()