from controllers.helpers.api import interface


def send_message(chatName: str, text: str,):
    return interface.request(
        ["chat", "message"],
        **{
            "method": "post",
            "json": {
                "name": chatName,
                "message": {
                    "content": text,
                    "role": "user"
                }
            }
        }
    )


def open_ai(chatName: str):
    return interface.request(
        ["chat", "send-history"],

        **{
            "method": "post",
            "json": {
                "name": chatName
            }
        }
    )


def new_chat(chatName: str):
    return interface.request(
        ["chat"],
        **{
            "method": "post",
            "json": {
                "name": chatName
            }
        }
    )


def get_chat(chatName: str):
    return interface.request(
        ["chat"],
        **{
            "method": "get",
            "json": {
                "name": chatName
            }
        }
    )


