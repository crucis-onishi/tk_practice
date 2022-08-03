import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")
        self.master.geometry("300x200")

        # 変数定義
        self.elapse = 0 # 経過時間保存用の変数を定義
        self.after_id = 0 # after_id変数を定義

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # label1ウィジェットを作成
        self.label1 = tk.Label(self,text=str(self.elapse) + "秒経過しました", font="24")
        self.label1.pack()

    # 毎秒の処理
    def update_time(self):
        self.elapse += 1
        self.label1["text"] = str(self.elapse) + "秒経過しました"
        self.after_id = app.after(1000, self.update_time)
        # 10秒経過すると更新を停止
        if self.elapse == 10:
            app.after_cancel(self.after_id)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.update_time()
    app.mainloop()
