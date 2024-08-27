from pathlib import Path
import customtkinter
import shutil

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        # Setting default width and height of app
        self.app_width = 400
        self.app_height = 180
        
        # Getting the size of our monitor
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        
        # Find the coordinates to place app window so that it centers on screen
        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height / 2)
        
        # Set the size of our app and position it centre of monitor
        self.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')
        self.title("Jojo's Bizzare Files")
        
        # Set weight of rows and columns to place widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.select_folder_button = customtkinter.CTkButton(self, text = "Select Folder", command=self.select_folder_button_callback, width=150)
        self.select_folder_button.grid(row=0, column=0, pady=15, sticky="s")
        self.sort_button = customtkinter.CTkButton(self, text= "Sort", command=self.sort_button_callback, width=150)
        self.sort_button.grid(row=1, column=0, pady=15, sticky="n")
    
    def select_folder(self):
        foldername = customtkinter.filedialog.askdirectory(parent=app, initialdir=Path.cwd().root, title="Jojo's Bizzare Files")
        # print(foldername)
        return foldername
    
    
    # problem right now is it sorts right after selecting
    # we want to give user a choice to see the folder and a button to click to sort
    # then show folder after sorting    
    def select_folder_button_callback(self):
        self.selected_folder = self.select_folder()
        
    def sort_button_callback(self):
        self.file_sorter()
        
    def file_sorter(self):
        source = self.selected_folder
        source_dir = Path(source)
         
        files = [f for f in source_dir.iterdir() if f.is_file()]
        
        for file in files:
            target = (f'{source_dir}' + f'\{file.suffix[1:]}')
            target_dir = Path(target)
            
            if target_dir.exists() != True:
                Path.mkdir(target_dir)
            shutil.move(file, target_dir)
            
app = App()
app.mainloop()
        
    


# add a folder_check function to check if folders exist
# 1st check on startup to make sure that folder names aren't taken alrd (or we could make a special prefix name for folders so thr won't be any clashes)
# 2nd check onwards assumes that if folders exist it was created from this program itself
# then call file_sorter()

