import mouse, keyboard, getpass, os, tkinter.messagebox as mb, PIL.ImageGrab, ctypes, colorsys
from tkinter import Tk, Label, Button
import customtkinter
from threading import Thread

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# МОДЕРН ВЕРСИЯ \ КЛАСС ПОЧЕМУ ТО НЕ ДЕСТРОИТСЯ

# customtkinter.set_appearance_mode('System')
# customtkinter.set_default_color_theme('blue')

# class ColorPicker:
#     def __init__(self):
#         self.window = customtkinter.CTk() 
#         self.window.resizable(False, False)
#         self.window.geometry(f'200x42')
#         self.window.title('ColorPicker')
#         # window.iconbitmap('./colorpicker.ico')
#         self.window.config(bg='#0e0e0e')
#         # self.window.bind('<Escape>', lambda: close_class())
#         self.window.overrideredirect(1)

#         self.label = customtkinter.CTkLabel(master=self.window, text='', width=4, height=2)
#         self.label.grid(row=0, column=0,padx=(3,3),pady=(3,3))

#         self.text_lbl = customtkinter.CTkLabel(master=self.window, text='some text', width=15, height=2)
#         self.text_lbl.grid(row=0, column=1,padx=(3,3),pady=(3,3))

#         self.btn = customtkinter.CTkButton(master=self.window, text='Copy', width=4, height=2, command=lambda: self.copy_hex(self.text_lbl))

#         self.rgb_col = customtkinter.CTkLabel(master=self.window, text='', width=4, height=2)
#         self.rgb_lab = customtkinter.CTkLabel(master=self.window, text='some text', width=15, height=2)
#         self.rgb_cop = customtkinter.CTkButton(master=self.window, text='Copy', width=4, height=2, command=lambda: self.copy_hex(self.rgb_lab))

#         self.col50 = customtkinter.CTkButton(master=self.window, text='', width=4, height=2, command=lambda: self.copy_color(self.col50))
#         self.col100 = customtkinter.CTkButton(master=self.window, text='', width=4, height=2, command=lambda: self.copy_color(self.col100))
#         self.col150 = customtkinter.CTkButton(master=self.window, text='', width=4, height=2, command=lambda: self.copy_color(self.col150))
#         self.col200 = customtkinter.CTkButton(master=self.window, text='', width=4, height=2, command=lambda: self.copy_color(self.col200))
#         self.col10 = customtkinter.CTkButton(master=self.window, text='', width=4, height=2, command=lambda: self.copy_color(self.col10))

#         self.t = Thread(target=self.infinity_pos)
#         self.t.daemon = True           
#         self.t.start()

#         self.window.mainloop()

#     def close_class(self):
#         self.window.destroy()

#     def rgb2hex(self, colortuple):
#         return '#' + ''.join(f'{i:02X}' for i in colortuple)

#     def copy_hex(self, color):
#         copied = color.cget('text')
#         print(copied)
#         self.window.clipboard_append(copied)
#         mb.showinfo('Copied!!', 'Copied!!')
#         self.window.destroy()

#     def copy_color(self, color):
#         copied = color.configure('background')[4]
#         print(copied)
#         self.window.clipboard_append(copied)
#         mb.showinfo('Copied!!', 'Copied!!')
#         self.window.destroy()

#     def check_color(self, color):
#         for i in range(len(color)):
#             if (color[i] >= 255):
#                 color[i] -= 255
#         return color

#     def mouse_pressed(self, position):
#         self.window.geometry(f'200x140')
#         self.window.focus_set()
#         self.window.attributes('-topmost',True)
#         self.window.overrideredirect(0)
#         rgb = PIL.ImageGrab.grab().load()[position[0], position[1]]

#         self.text_lbl.configure(width=15)
#         self.btn.grid(row=0, column=2,padx=(3,3),pady=(3,3))

#         self.rgb_col.grid(row=1, column=0,padx=(3,3),pady=(3,3))
#         self.rgb_lab.grid(row=1, column=1,padx=(3,3),pady=(3,3))
#         self.rgb_cop.grid(row=1, column=2,padx=(3,3),pady=(3,3))
#         self.rgb_col.configure(bg_color=self.rgb2hex(rgb))
#         self.rgb_lab.configure(text=','.join([str(i) for i in rgb]))

#         color50 = [round(rgb[0] * 0.5), round(rgb[1] * 0.5), round(rgb[2] * 0.5)]
#         color150 = [round(rgb[0] * 1.5), round(rgb[1] * 1.5), round(rgb[2] * 1.5)]
#         color200 = [round(rgb[0] * 2), round(rgb[1] * 2), round(rgb[2] * 2)]
#         color10 = [round(rgb[0] * 0.1), round(rgb[1] * 0.1), round(rgb[2] * 0.1)]

#         self.col10.place(x=3, y=96)
#         self.col10.configure(bg_color=self.rgb2hex(self.check_color(color10)))
#         self.col50.place(x=43, y=96)
#         self.col50.configure(bg_color=self.rgb2hex(self.check_color(color50)))
#         self.col100.place(x=83, y=96)
#         self.col100.configure(bg_color=self.rgb2hex(rgb))
#         self.col150.place(x=123, y=96)
#         self.col150.configure(bg_color=self.rgb2hex(self.check_color(color150)))
#         self.col200.place(x=163, y=96)
#         self.col200.configure(bg_color=self.rgb2hex(self.check_color(color200)))

#     def infinity_pos(self):
#         while True:
#             position = mouse.get_position()
#             if mouse.is_pressed('left'):
#                 self.mouse_pressed(position)
#                 break
#             self.window.attributes('-topmost',True)
#             if (position[0] + 200 > screensize[0] or position[1] + 45 > screensize[1]):
#                 self.window.geometry(f'200x42+{position[0]-205}+{position[1]-45}')
#             else:
#                 self.window.geometry(f'200x42+{position[0]+5}+{position[1]+5}')
#             rgb = PIL.ImageGrab.grab().load()[position[0], position[1]]
#             hex_code = self.rgb2hex(rgb)
#             self.label.configure(bg_color=hex_code)
#             self.text_lbl.configure(text=hex_code)
#         print('1')

#     def __del__(self):
#         print('destroed')

# ОБЫЧНАЯ ВЕРСИЯ \ РАБОТАЕТ СТАБИЛЬНО
class ColorPicker:
    def __init__(self):
        self.window = Tk() 
        self.window.resizable(False, False)
        self.window.geometry(f'200x42')
        self.window.title('ColorPicker')
        # window.iconbitmap('./colorpicker.ico')
        self.window.config(bg='#0e0e0e')
        # self.window.bind('<Escape>', lambda: close_class())
        self.window.overrideredirect(1)

        self.label = Label(text='', width=4, height=2, bg='white')
        self.label.grid(row=0, column=0,padx=(3,3),pady=(3,3))

        self.text_lbl = Label(text='some text', fg='white', bg='#0e0e0e', width=15, height=2)
        self.text_lbl.grid(row=0, column=1,padx=(3,3),pady=(3,3))

        self.btn = Button(text='Copy', width=4, height=2, command=lambda: self.copy_hex(self.text_lbl))

        self.rgb_col = Label(text='', width=4, height=2, bg='white')
        self.rgb_lab = Label(text='some text', fg='white', bg='#0e0e0e', width=15, height=2)
        self.rgb_cop = Button(text='Copy', width=4, height=2, command=lambda: self.copy_hex(self.rgb_lab))

        self.col50 = Button(text='', width=4, height=2, borderwidth='0', command=lambda: self.copy_color(self.col50))
        self.col100 = Button(text='', width=4, height=2, borderwidth='0', command=lambda: self.copy_color(self.col100))
        self.col150 = Button(text='', width=4, height=2, borderwidth='0', command=lambda: self.copy_color(self.col150))
        self.col200 = Button(text='', width=4, height=2, borderwidth='0', command=lambda: self.copy_color(self.col200))
        self.col10 = Button(text='', width=4, height=2, borderwidth='0', command=lambda: self.copy_color(self.col10))

        self.t = Thread(target=self.infinity_pos)
        self.t.daemon = True           
        self.t.start()

        self.window.mainloop()

    def close_class(self):
        self.window.destroy()

    def rgb2hex(self, colortuple):
        return '#' + ''.join(f'{i:02X}' for i in colortuple)

    def copy_hex(self, color):
        copied = color.cget('text')
        print(copied)
        self.window.clipboard_append(copied)
        mb.showinfo('Copied!!', 'Copied!!')
        self.window.destroy()

    def copy_color(self, color):
        copied = color.config('background')[4]
        print(copied)
        self.window.clipboard_append(copied)
        mb.showinfo('Copied!!', 'Copied!!')
        self.window.destroy()

    def check_color(self, color):
        for i in range(len(color)):
            if (color[i] >= 255):
                color[i] -= 255
        return color

    def mouse_pressed(self, position):
        self.window.geometry(f'200x140')
        self.window.focus_set()
        self.window.attributes('-topmost',True)
        self.window.overrideredirect(0)
        rgb = PIL.ImageGrab.grab().load()[position[0], position[1]]

        self.text_lbl.config(width=15)
        self.btn.grid(row=0, column=2,padx=(3,3),pady=(3,3))

        self.rgb_col.grid(row=1, column=0,padx=(3,3),pady=(3,3))
        self.rgb_lab.grid(row=1, column=1,padx=(3,3),pady=(3,3))
        self.rgb_cop.grid(row=1, column=2,padx=(3,3),pady=(3,3))
        self.rgb_col.config(bg=self.rgb2hex(rgb))
        self.rgb_lab.config(text=','.join([str(i) for i in rgb]))

        color50 = [round(rgb[0] * 0.5), round(rgb[1] * 0.5), round(rgb[2] * 0.5)]
        color150 = [round(rgb[0] * 1.5), round(rgb[1] * 1.5), round(rgb[2] * 1.5)]
        color200 = [round(rgb[0] * 2), round(rgb[1] * 2), round(rgb[2] * 2)]
        color10 = [round(rgb[0] * 0.1), round(rgb[1] * 0.1), round(rgb[2] * 0.1)]

        self.col10.place(x=3, y=96)
        self.col10.config(bg=self.rgb2hex(self.check_color(color10)))
        self.col50.place(x=43, y=96)
        self.col50.config(bg=self.rgb2hex(self.check_color(color50)))
        self.col100.place(x=83, y=96)
        self.col100.config(bg=self.rgb2hex(rgb))
        self.col150.place(x=123, y=96)
        self.col150.config(bg=self.rgb2hex(self.check_color(color150)))
        self.col200.place(x=163, y=96)
        self.col200.config(bg=self.rgb2hex(self.check_color(color200)))

    def infinity_pos(self):
        while True:
            position = mouse.get_position()
            if mouse.is_pressed('left'):
                self.mouse_pressed(position)
                break
            self.window.attributes('-topmost',True)
            if (position[0] + 200 > screensize[0] or position[1] + 45 > screensize[1]):
                self.window.geometry(f'200x42+{position[0]-205}+{position[1]-45}')
            else:
                self.window.geometry(f'200x42+{position[0]+5}+{position[1]+5}')
            rgb = PIL.ImageGrab.grab().load()[position[0], position[1]]
            hex_code = self.rgb2hex(rgb)
            self.label.config(bg=hex_code)
            self.text_lbl.config(text=hex_code)
        print('1')

    def __del__(self):
        print('destroed')

# АВТОЗАГРУЗКА ПРИ ВКЛЮЧЕНИИ ВИНДЫ
# USER_NAME = getpass.getuser()
# def add_to_startup(file_path=""):
#     if file_path == "":
#         file_path = os.path.realpath(__file__)
#     bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
#     with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
#         bat_file.write(r'start "" %s' % file_path)
# add_to_startup()

keyboard.add_hotkey("ctrl+alt+j", lambda: ColorPicker())
keyboard.wait('ctrl+alt+p')