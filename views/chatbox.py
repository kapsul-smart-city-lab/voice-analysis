from json import load
import flet as ft
import random
import string

from controllers.chat import new_chat, open_ai, send_message, get_chat

from prompt_catcher import Listener

color = "#67dfe2"


def random_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))


def is_definied(obj: object, attr: str) -> bool:
    try:
        getattr(obj, attr)
    except:
        return False
    else:
        return True


class Message(ft.UserControl):
    def __init__(self, content: str, role, text_align, msg_align, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.role = role
        self.msg_align = msg_align
        self.text_aling = text_align

    def build(self):
        return ft.Row([
            ft.Container(
                content=ft.Text(self.content, selectable=True,
                                text_align=self.text_aling,),

                border_radius=10,
                margin=10,
                padding=10,
                width=400 if len(self.content) > 40 else None,
                border=ft.border.all(1, color=color),
                expand=False,
            )
        ],
            expand=False,
            alignment=self.msg_align)


class DefaultMessage(ft.UserControl):

    def __init__(self, question=None, response=None, page=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question
        self.response = response
        self.page = page

    def build(self):
        return ft.ElevatedButton(self.question, on_click=self.on_click, color=color)

    def on_click(self, e):
        self.page.dialog = self.popup
        self.popup.open = True
        self.page.update()

    @property
    def popup(self):
        if not is_definied(self, '_popup'):
            self._popup = ft.AlertDialog(
                modal=True,
                content=ft.Text(
                    self.response, selectable=True),
                actions=[
                    ft.TextButton("OK", on_click=self.close),
                ],
                actions_alignment=ft.MainAxisAlignment.CENTER,
            )

        return self._popup

    def close(self, e):
        self.popup.open = False
        self.page.update()


class ChatBox(ft.UserControl):
    def __init__(self, page, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.open = False
        self.id = random_id()
        self.page = page
        self.listener = Listener(callback=self.message)
        print(self.id)

    def build(self):
        return self.columns

    # ai
    def message(self, message):
        if not self.open:
            self.open = True
            res = new_chat(self.id)

        result = send_message(self.id, message).json()

        if "result" in result and  result["result"] == True:

            self.messages = get_chat(self.id).json()["history"]
            controls = []
            for message in self.messages:
                if message['role'] == "user":
                    message = Message(
                        **message, msg_align=ft.MainAxisAlignment.END,
                        text_align=ft.TextAlign.RIGHT)
                elif message['role'] == "assistant":
                    message = Message(
                        **message, msg_align=ft.MainAxisAlignment.START,
                        text_align=ft.TextAlign.LEFT)

                controls.append(message)
            self.message_column.controls = controls
            self.message_column.update()

            print("GPT'den mesaj bekleniyor...")
            result = open_ai(self.id).json()
            self.messages = get_chat(self.id).json()["history"]

        else:
            self.messages.append({"content": "Hata Oluştu", "role": "assistant"})


        # self.message_column.clean()

        controls = []
        for message in self.messages:
            if message['role'] == "user":
                message = Message(
                    **message, msg_align=ft.MainAxisAlignment.END,
                    text_align=ft.TextAlign.RIGHT)
            elif message['role'] == "assistant":
                message = Message(
                    **message, msg_align=ft.MainAxisAlignment.START,
                    text_align=ft.TextAlign.LEFT)

            controls.append(message)
        self.message_column.controls = controls
        self.message_column.update()

    @property
    def button(self):
        if not is_definied(self, '_button'):
            self._button = ft.ElevatedButton(
                "Dinle", on_click=self.listener.prompt_catcher, color=color, height=81, width=81)

        return self._button

    # @property
    # def textbox(self):
    #     if not is_definied(self, '_textbox'):
    #         self._textbox = ft.TextField(
    #             multiline=True,
    #             min_lines=3,
    #             max_lines=3,
    #             filled=True,
    #             expand=True,
    #             autofocus=True,
    #             shift_enter=True,
    #             color=color
    #         )

    #     return self._textbox

    @property
    def columns(self):
        if not is_definied(self, '_columns'):
            self._columns = ft.Column([
                self.chat_container,
                ft.Row([self.button],
                       alignment=ft.MainAxisAlignment.CENTER),
            ])

        return self._columns

    @property
    def message_column(self):
        if not is_definied(self, '_message_column'):
            self._message_column = ft.Column(
                expand=False, auto_scroll=True, spacing=10)

        return self._message_column

    @property
    def chat_container(self):
        if not is_definied(self, '_chat_container'):
            self._chat_container = ft.ResponsiveRow(
                [self.message_column],
                # border=ft.border.all(0, color=ft.colors.OUTLINE),
                # border_radius=5,
                # padding=10,
                # expand=True,
            )

        return self._chat_container
