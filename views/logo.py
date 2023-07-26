import flet as ft

from config import IMG_PATH

class Logo(ft.UserControl):
    def __init__(self, img_name: str = "logo.png", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_path = f'{IMG_PATH}/{img_name}'

    def build(self):
        return ft.Row(
            [
                ft.Image(src=self.img_path,
                         width=180,
                         height=80,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
