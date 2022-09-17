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
        self.timer_on = False # タイマーの状態
        self.start_time = 0 # 開始時間
        self.set_time = 0 # セット時間
        self.elapsed_time = 0 # 経過時間
        self.left_time = 0 # 残り時間
        self.left_min = 0
        self.left_sec = 0
        self.after_id = 0 # after_id変数を定義

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # 全体の親キャンバス（リトライを簡単にする用）
        self.canvas_bg = tk.Canvas(self.master, width=430, height=280)
        self.canvas_bg.pack()

        # canvasウィジェットを作成
        self.canvas_time = tk.Canvas(self.canvas_bg, width=410, height=80, bg="lightgreen")
        self.canvas_time.place(x=10, y=10)
        self.canvas_time.create_text(230,40,text=str(round(self.left_min)) + "分", font=("MSゴシック体", "36", "bold"), tag="min_text", anchor="e") # 分を表示
        self.canvas_time.create_text(340,40,text=str(round(self.left_sec)) + "秒", font=("MSゴシック体", "36", "bold"), tag="sec_text", anchor="e") # 秒を表示

        # ボタンを作成・配置
        self.minButton = tk.Button(self.canvas_bg, width=8, height=2, text="分", font=("MSゴシック体", "18","bold"), command=self.minButton_clicked)
        self.minButton.place(x=10, y=100)

        self.secButton = tk.Button(self.canvas_bg, width=8, height=2, text="秒", font=("MSゴシック体", "18","bold"), command=self.secButton_clicked)
        self.secButton.place(x=150, y=100)

        self.resetButton = tk.Button(self.canvas_bg, width=8, height=2, text="リセット", font=("MSゴシック体", "18","bold"), command=self.resetButtonClicked)
        self.resetButton.place(x=290, y=100)

        startButton = tk.Button(self.canvas_bg, width=27, height=2, text="スタート/ストップ", font=("MSゴシック体", "18","bold"), command=self.startbutton_clicked)
        startButton.place(x=10, y=190)

    # 各ボタンが押された時の処理
    def minButton_clicked(self):
        if self.left_min < 59: # 最大59分まで
            self.set_time += 60 # セット時間をプラス
            self.left_min += 1
            self.canvas_time.delete("min_text") # 表示時間（分）を消去
            self.canvas_time.create_text(230,40,text=str(round(self.left_min)) + "分", font=("MSゴシック体", "36", "bold"), tag="min_text", anchor="e") # 分を表示

    def secButton_clicked(self):
        if self.left_sec < 59: # 最大59秒まで
            self.set_time += 1 # セット時間をプラス
            self.left_sec += 1
            self.canvas_time.delete("sec_text") # 表示時間（秒）を消去
            self.canvas_time.create_text(340,40,text=str(round(self.left_sec)) + "秒", font=("MSゴシック体", "36", "bold"), tag="sec_text", anchor="e") # 秒を表示

    def resetButtonClicked(self):
        self.set_time = 0 # セット時間をリセット
        self.left_min = 0 # 残り時間（分）をリセット
        self.left_sec = 0 # 残り時間（秒）をリセット

        self.canvas_time.delete("min_text") # 表示時間（分）を消去
        self.canvas_time.create_text(230,40,text=str(round(self.left_min)) + "分", font=("MSゴシック体", "36", "bold"), tag="min_text", anchor="e") # 分を表示

        self.canvas_time.delete("sec_text") # 表示時間（秒）を消去
        self.canvas_time.create_text(340,40,text=str(round(self.left_sec)) + "秒", font=("MSゴシック体", "36", "bold"), tag="sec_text", anchor="e") # 秒を表示

    def startbutton_clicked(self):
        if self.timer_on == False:
            self.timer_on = True

            # 各種ボタンをDISABLED
            self.minButton["state"] = tk.DISABLED
            self.secButton["state"] = tk.DISABLED
            self.resetButton["state"] = tk.DISABLED

            self.start_time =time.time() # 開始時間を代入
            self.update_time() # updateTime関数を実行
        elif self.timer_on == True:
            self.timer_on = False

            # 各種ボタンをABLED
            self.minButton["state"] = tk.NORMAL
            self.secButton["state"] = tk.NORMAL
            self.resetButton["state"] = tk.NORMAL

            self.set_time = self.left_time
            app.after_cancel(self.after_id)

    # 表示時間の更新処理
    def update_time(self):
        self.elapsed_time = time.time() - self.start_time  # 経過時間を計算
        self.left_time = self.set_time - self.elapsed_time # 残り時間を計算
        self.left_min = self.left_time // 60 # 残り時間（分）を計算
        self.left_sec = self.left_time % 60 # 残り時間（秒）を計算

        self.canvas_time.delete("min_text") # 表示時間（分）を消去
        self.canvas_time.create_text(230,40,text=str(round(self.left_min)) + "分", font=("MSゴシック体", "36", "bold"), tag="min_text", anchor="e") # 分を表示

        self.canvas_time.delete("sec_text") # 表示時間（秒）を消去
        self.canvas_time.create_text(340,40,text=str(round(self.left_sec)) + "秒", font=("MSゴシック体", "36", "bold"), tag="sec_text", anchor="e") # 秒を表示

        if self.left_time > 0.1:
            self.after_id = self.after(10, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
