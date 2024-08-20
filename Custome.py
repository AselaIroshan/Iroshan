from tkinter import *
import tkinter as tk
import tkinter.font as font

class RoundedButton(tk.Canvas):
    def __init__(self, parent, border_radius, padding, color, text='', command=None, pressed_color=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="flat", highlightthickness=0, bg=parent["bg"])
        self.command = command
        self.default_color = color
        self.pressed_color = pressed_color or color
        font_size = 16
        self.font = font.Font(size=font_size, family='Helvetica', weight="bold")
        height = 100
        width = 98
        
        self.color = color

        if border_radius > 0.5 * width:
            print("Error: border_radius is greater than width.")
            

        if border_radius > 0.5 * height:
            print("Error: border_radius is greater than height.")
            

        rad = 2 * border_radius

        def shape():
            self.create_arc((0, rad, rad, 0),
                            start=90, extent=90, fill=self.color, outline=self.color)
            self.create_arc((width - rad, 0, width,
                             rad), start=0, extent=90, fill=self.color, outline=self.color)
            self.create_arc((width, height - rad, width - rad,
                             height), start=270, extent=90, fill=self.color, outline=self.color)
            self.create_arc((0, height - rad, rad, height),
                            start=180, extent=90, fill=self.color, outline=self.color)
            return self.create_polygon((0, height - border_radius, 0, border_radius, border_radius, 0, width - border_radius, 0, width,
                                        border_radius, width, height - border_radius, width - border_radius, height, border_radius, height), fill=self.color, outline=self.color)

        self.id = shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0)
        height = (y1 - y0)
        self.configure(width=width, height=height)
        self.text_id = self.create_text(width / 2, height / 2, text=text, fill='white', font=self.font)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.itemconfig(self.id, fill=self.pressed_color, outline=self.pressed_color)
        self.itemconfig(self.text_id, fill='white')

    def _on_release(self, event):
        self.itemconfig(self.id, fill=self.default_color, outline=self.default_color)
        self.itemconfig(self.text_id, fill='white')
        if self.command is not None:
            self.command()

