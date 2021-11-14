# # Creating a CalculatorApp 

# ___by Akash

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (310,480)

Builder.load_string("""
<CalLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        TextInput:
            id:input
            text:"0"
            halign:"right"
            font_size:60
            size_hint:(1, .20)
        GridLayout:
            cols:4
            rows:5
            # first row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"<-"
                on_press:root.back()
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"C"
                on_press:root.clear()
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"%"
                on_press:root.pressed('%')                
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"/"
                on_press:root.pressed('/')
            # second row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"7"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(7)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"8"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(8)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"9"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(9)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"X"
                on_press:root.pressed('*')
            # third row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"4"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(4)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"5"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(5)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"6"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(6)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"-"
                on_press:root.pressed('-')
            # fourth row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"1"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(1)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"2"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(2)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"3"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(3)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"+"
                on_press:root.pressed('+')
            # fifth row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"x[sup]n[/sup]"
                background_color:(157/255,157/255, 157/255, 1)
                markup:True
                on_press:root.pressed('**')
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"0"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(0)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"."
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed('.')
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"="
                on_press:root.answer()
""")

class CalLayout(Widget):
    
    def clear(self):
        self.ids.input.text=""
 
    def back(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        self.ids.input.text = expression
   
    def pressed(self, button):

        expression = self.ids.input.text
       
        if "Error" in expression:
            expression = ""
       
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"
        
    def answer(self):
        expression = self.ids.input.text
        try:
            
            self.ids.input.text = str(eval(expression))
            
        except:
           
            self.ids.input.text = "Error"            
    
class CalculatorApp(App):

    def build(self):
        return CalLayout()

cal = CalculatorApp()

cal.run()
