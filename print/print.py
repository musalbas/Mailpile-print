from mailpile.plugins.search import View

class SingleMessageView(View):

    @classmethod
    def view(cls, result):
        mid = result["message_ids"][0]
        return {"message": result["data"]["messages"][mid],
                "metadata": result["data"]["metadata"][mid]}
