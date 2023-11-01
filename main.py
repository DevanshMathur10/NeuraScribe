from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color,Ellipse
from kivy.clock import Clock
import time
from image_process import proc
import os
import shutil
from kivy.core.window import Window

Window.size = (400, 700)

class DrawInput(Widget):
    def on_touch_down(self, touch):
        try:
            if (85<touch.x<315) and (120<touch.y<350):
                with self.canvas:
                    Color(1,1,1)
                    d=10.0
                    #touch.ud["line"]=Line(points=(touch.x,touch.y))
                    touch.ud["Ellipse"]=Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
        except:
            pass

    def on_touch_move(self, touch):
        try:
            if (85<touch.x<315) and (120<touch.y<350):
                with self.canvas:
                    Color(1,1,1)
                    d=10.0
                    touch.ud["Ellipse"]=Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
                    #touch.ud["Ellipse"]=Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
        except:
            pass

    def on_touch_up(self, touch):
        pass


class MyApp(MDApp):

    def build(self):

        rootWindow=Widget()

        back=Image(source="NeuraScribe/back.jpg")
        self.painter=DrawInput()
        back.add_widget(self.painter)

        b1 = Button(text ="clear",size=(100,50),pos=(200,50))
        b1.bind(on_release=self.clear_canvas)
        back.add_widget(b1)
        b2 = Button(text ="Predict",size=(100,50),pos=(100,50))
        b2.bind(on_release=self.prediction)
        back.add_widget(b2)

        self.label=Label(text="DIGIT\nPREDICTION\nUSING\nNEURAL\nNETWORK",pos=(150,520),font_size='40sp',font_name='Elianto-Regular.otf',color=(0,0,0),halign="center")
        back.add_widget(self.label)

        self.lbl=Label(text="No Prediction!",pos=(150,370),font_size='20sp',font_name='MontserratAlternates-Light.otf',color=(0,0,0),halign="center")
        back.add_widget(self.lbl)

        return back

    def prediction(self,obj):
        self.doscreenshot()
        if os.path.exists("NeuraScribe/screenshot.jpg"):
            print("File exists.")
            self.num=proc()
            self.lbl.text=f"My Neural Network\npredicts\n{self.num} !"
            #print("Num in canvas",self.num)
        else:
            print("File does not exist.")
            pass
        #Clock.schedule_once(self.export)

    def clear_canvas(self,obj):
        self.painter.canvas.clear()
        if os.path.exists("NeuraScribe/screenshot.jpg"):
            os.remove("NeuraScribe/screenshot.jpg")
        else:
            pass
 
    def doscreenshot(self,*args):
        file_name=Window.screenshot(name='NeuraScribe/screenshot.jpg')
        name_parts = file_name.split('.')
        new_name = ''.join([name_parts[0][:-4], '.', name_parts[1]])
        shutil.move(file_name, new_name)


if __name__=="__main__":
    app=MyApp()
    app.run()