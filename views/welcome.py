import flet as ft

from .logo import Logo

color = "#67dfe2"


class Welcome(ft.UserControl):
    welcome_header = "Kapsül GPT'ye Hoşgeldiniz!"
    welcome_text = "Kapsül GPT ile sohbet edebilir, sorular sorabilirsiniz. \nKapsül GPT'yi kullanmak için lütfen aşağıdaki butona tıklayın." 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(ft.Row([self.text],
                                   alignment=ft.MainAxisAlignment.CENTER,
                                   vertical_alignment=ft.CrossAxisAlignment.END))

    @property
    def text(self):
        if not hasattr(self, '_text'):
            self._text = ft.Column([
                ft.Text(self.welcome_header,
                        color=color,
                        size=25,
                        weight=ft.FontWeight.W_900,
                        selectable=True,
                        text_align=ft.alignment.center_right),
                ft.Text(self.welcome_text, selectable=True, text_align=ft.alignment.center_right),
                self.logo
            ])

        return self._text

    @property
    def logo(self):
        if not hasattr(self, '_logo'):
            self._logo = Logo()

        return self._logo
