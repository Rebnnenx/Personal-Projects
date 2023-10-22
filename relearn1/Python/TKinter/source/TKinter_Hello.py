#import statements
import tkinter as tk

try:
    #fixes window resolution blur in Windows OS
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    
    #creates root window
    root = tk.Tk()
    
    #adds title text
    root.title('Tkinter Window Demo')
    
    
    ''' this section below covers the elements which make up a  window'''
    
    #default window width and height
    window_width =300
    window_height =200
    
    #get computer screen dimensions
    screen_width= root.winfo_screenwidth()
    screen_height= root.winfo_screenheight()
    
    #get center points of the screen compared to window size
    center_x= int(screen_width/2 -window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    
    #root window with dimensions and position (WidthxHeight+-LR+-TB) + == from the Left or Top, - == from the Right or Bottom
    #sets position of window in the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    #controls whether or not window is resisable (default is true) (width, height)
    root.resizable(True, False)
    
    #controls minimum size of window (width, height)
    root.minsize(window_width-100, window_height)
    
    #controls maximum size of window (width, height)
    root.maxsize(1000, window_height)
    
    #control the opacity/transparency of the window
    root.attributes('-alpha',0.7)
    
    root.wm_iconbitmap('//boxofholding/Data/Brennen/GitHub/Personal-Projects/relearn1/Python/TKinter/assets/pythontutorial.ico')
    
    #places a label on the root window
    message = tk.Label(root, text="Hello, World!")
    message.pack()
    
    #forces window to topsmost layer
    root.attributes('-topmost', 1)
    
    '''Note could also use .lift or .lower to make '''
    #keeps the window displayed
    root.mainloop()
