import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # label1ウィジェットを作成
        msg = "うへっへへへうへへへへへ\nでへへェェうへへェェうヒィッ\nうひうひうひうはァッ\nでへっでへっどぅひひひひひ\nふっふふはっひひお\nへおへおへへェェッ"

        self.label1 = tk.Label(self,text=msg, font="24")
        self.label1.pack(side="right")

        # label2ウィジェットを作成
        self.icon = tk.PhotoImage(file="img/denchan.png") # 画像のパスをicon変数に代入

        self.label2 = tk.Label(self,image=self.icon, bg="white") # image引数に表示したい画像のパスを指定してインスタンスを生成
        self.label2.pack(side="left") # label2ウィジェットを配置

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
