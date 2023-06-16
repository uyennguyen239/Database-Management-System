from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass


#create a 'Frame' as 'class'. Frame a widget that serves as a container for other widgets
#create main window of the application
class Project_IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry ("1350x700+0+0")
        self.root.title ("Inventory Management System | Developed by UN")

    #Prepare Logo1 for tittle
        #Open the image using  PIL
        image = Image.open("Images/logo1.png")

        #Resize the image to the desired width and height
        width = 75  # Specify the desired width
        height = 50  # Specify the desired height
        image = image.resize((width, height), Image.ANTIALIAS)

         # Create PhotoImage from the opened image
        self.icon_title = ImageTk.PhotoImage(image)

        #===TITLE===
        title=Label(self.root,text="Inventory Management System",image=self.icon_title, compound=LEFT, font =("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        #===btn_logout===
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2")
        btn_logout.place(x=1100, y=10, heigh=50, width=150)

        #===clock===
        self.lbl_clock = Label(self.root,text="Welcome to Inventory system\t\t Date: MM-DD-YYY\t\t Time: HH:MM:SS", font =("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        #===LEFT MEUNU===
            #frame line
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0, y=102, width=200, height=565)

            #prepare NILogo for MenuLogo
        self.MenuLogo = Image.open("Images/NILogo.png")
        self.MenuLogo = self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

            #Menu Logo
        lbl_MenuLogo = Label (LeftMenu, image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP, fill=X)

            #Menu button on LeftMenu
        lbl_menu = Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688")
        lbl_menu.pack(side= TOP, fill= X)

            # Create sidearrow image
        self.icon_side = Image.open("Images/sidearrow.png")
        self.icon_side = self.icon_side.resize((15,15), Image.ANTIALIAS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)

            # Create employee button on Left Menu and bring to new window when click
        btn_employee = Button(LeftMenu,text="Employee", command = self.employee,image = self.icon_side, compound = LEFT, padx = 5, anchor = W,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand1")
        btn_employee.pack(side = TOP, fill= X)
        
            # Create Supplier button on Left Menu
        btn_supplier = Button(LeftMenu,text="Supplier",image = self.icon_side, compound = LEFT, padx = 5, anchor = W,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand1")
        btn_supplier.pack(side = TOP, fill= X)

            # Create Category button on Left Menu
        btn_category = Button(LeftMenu,text="Category",image = self.icon_side, compound = LEFT, padx = 5, anchor = W,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand1")
        btn_category.pack(side = TOP, fill= X)

            # Create Product button on Left Menu
        btn_product = Button(LeftMenu,text="Product",image = self.icon_side, compound = LEFT, padx = 5, anchor = W,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand1")
        btn_product.pack(side = TOP, fill= X)

            # Create Sales button on Left Menu
        btn_sales = Button(LeftMenu,text="Sales",image = self.icon_side, compound = LEFT, padx = 5, anchor = W,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand1")
        btn_sales.pack(side = TOP, fill= X)

            # Create Exit button on Left Menu
        btn_exit = Button(LeftMenu,text="Exit",image = self.icon_side, compound = LEFT, padx = 5, anchor = W,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand1")
        btn_exit.pack(side = TOP, fill= X)

        #===CONTENT===
            # Create Total Employee 
        self.lbl_employee = Label(self.root, text = "Total Employee\n[0]",bd = 5, relief = RIDGE, bg = "#33bbf9", fg="white", font = ("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150,width=300)

            # Create Total Suplier
        self.lbl_supplier = Label(self.root, text = "Total Supplier\n[0]",bd = 5, relief = RIDGE, bg = "#33bbf9", fg="white", font = ("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150,width=300)

            # Create Total Category
        self.lbl_category = Label(self.root, text = "Total Category\n[0]",bd = 5, relief = RIDGE, bg = "#33bbf9", fg="white", font = ("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150,width=300)

            # Create Total Product
        self.lbl_product = Label(self.root, text = "Total Product\n[0]",bd = 5, relief = RIDGE, bg = "#33bbf9", fg="white", font = ("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150,width=300)

            # Create Total Sales
        self.lbl_sales = Label(self.root, text = "Total Sales\n[0]",bd = 5, relief = RIDGE, bg = "#33bbf9", fg="white", font = ("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=6500, y=300, height=150,width=300)

        #===FOOTER===
        lbl_footer = Label(self.root,text= "Nippon Industries Inventory Management System \n Technical Support 1-800-123-4567 | Develop by UN", font =("times new roman",15),bg="#4d636d",fg="white")
        lbl_footer.pack(side = BOTTOM, fill= X)

#==================================================================================

    def employee(self):
            self.new_win = Toplevel(self.root)
            self.new_obj = employeeClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = Project_IMS(root)
    root.mainloop()

