import tkinter as tk

class app:    
    
    ansr = [0,0]
    
    wd = tk.Tk()

    wd.title('test')

    quest_num = tk.Label(wd, text='Question 1')
    quest_num.grid(row=0, column=1, padx=10, pady=5, sticky='wnse')
    
    quest = tk.Label(wd, text='How are you?')
    quest.grid(row=1, column=1, padx=10, pady=5, sticky='wnse')

    def __init__(self):
       
        btn_Y = tk.Button(self.wd, text='Yes', command=self.next_Y)
        btn_Y.grid(row=2, column=0, padx=20, pady=10, ipadx=20, sticky='e')

        btn_N = tk.Button(self.wd, text='No', command=self.next_N)
        btn_N.grid(row=2, column=2, padx=20, pady=10, ipadx=20, sticky='w')
        
        self.wd.mainloop()
        
    def next(self):
        self.quest['text'] = 'Y: ' + str(self.ansr[0]) + ' | N: ' + str(self.ansr[1]) 
        
    def next_Y(self):
        self.ansr[0]+=1
        self.next()
    
    def next_N(self):
        self.ansr[1]+=1
        self.next()
        
app()