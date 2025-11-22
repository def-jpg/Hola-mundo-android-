from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

class HolaApp(App):
    def build(self):
        # Configurar ventana
        Window.clearcolor = (0.2, 0.6, 0.8, 1)  # Fondo azul
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        # Etiqueta principal
        self.label = Label(
            text='¡HOLA!',
            font_size='60sp',
            color=(1, 1, 1, 1),
            bold=True
        )
        
        # Etiqueta secundaria
        self.sub_label = Label(
            text='Presiona el botón',
            font_size='30sp',
            color=(1, 1, 1, 1)
        )
        
        # Botón
        self.button = Button(
            text='¡TOCA AQUÍ!',
            font_size='35sp',
            background_color=(0.9, 0.3, 0.2, 1),
            size_hint=(1, 0.4),
            bold=True
        )
        self.button.bind(on_press=self.mostrar_mensaje)
        
        # Agregar widgets al layout
        layout.add_widget(self.label)
        layout.add_widget(self.sub_label)
        layout.add_widget(self.button)
        
        return layout
    
    def mostrar_mensaje(self, instance):
        self.label.text = '¡LO LOGASTE!'
        self.sub_label.text = '🎉 ¡Felicidades! 🎉'
        self.button.text = '¡ÉXITO!'
        self.button.background_color = (0.2, 0.8, 0.3, 1)  # Verde

# Ejecutar la app
if __name__ == '__main__':
    HolaApp().run()
