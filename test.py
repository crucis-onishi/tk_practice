import tkinter as tk
import time
import math

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        master.title("キッチンタイマー")
        master.geometry("430x280") # タイマーの幅は430x280

        # 変数定義
        self.left_min = 0 # 残り時間（分）
        self.left_sec = 0 # 残り時間（秒）

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # 全体の親キャンバス
        self.canvas_bg = tk.Canvas(self.master, width=430, height=280)
        self.canvas_bg.pack()

        # タイマー用のキャンバス
        self.canvas_time = tk.Canvas(self.canvas_bg, width=410, height=80, bg="lightgreen")
        self.canvas_time.place(x=10, y=10)

        # タイマーに数字を表示
        self.canvas_time.create_text(250,40,text=str(self.left_min).zfill(2) + "：", font=("MSゴシック体", "36", "bold"), tag="min_text", anchor="e") # 分を表示
        self.canvas_time.create_text(250,40,text=str(self.left_sec).zfill(2), font=("MSゴシック体", "36", "bold"), tag="sec_text", anchor="w") # 秒を表示

        # 分ボタン
        self.min_button = tk.Button(self.canvas_bg, width=8, height=2, text="分", font=("MSゴシック体", "18","bold"))
        self.min_button.place(x=10, y=100)

        # 秒ボタン
        self.sec_button = tk.Button(self.canvas_bg, width=8, height=2, text="秒", font=("MSゴシック体", "18","bold"))
        self.sec_button.place(x=150, y=100)

        # リセットボタン
        self.reset_button = tk.Button(self.canvas_bg, width=8, height=2, text="リセット", font=("MSゴシック体", "18","bold"))
        self.reset_button.place(x=290, y=100)

        # スタート/ストップボタン
        start_button = tk.Button(self.canvas_bg, width=27, height=2, text="スタート/ストップ", font=("MSゴシック体", "18","bold"))
        start_button.place(x=10, y=190)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
