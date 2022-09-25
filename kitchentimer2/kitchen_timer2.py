import tkinter as tk
import time
import math
import sys

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

        # 全体の親キャンバス
        self.canvas_bg = tk.Canvas(self.master, width=430, height=280, bg="#333")
        self.canvas_bg.pack()

        # タイマーの背景画像
        self.timer_bg_img = tk.PhotoImage(file="./img/timer_bg.png")
        self.canvas_bg.create_image(0, 0, anchor=tk.NW, image=self.timer_bg_img, tag="timer_bg")

        # タイマーのテキスト
        self.update_min_text() # 分の表示更新
        self.update_sec_text() # 秒の表示更新

        # Minボタン
        self.min_button_img = tk.PhotoImage(file="./img/min_button.png")
        self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_img, tag="min_button_img")
        self.canvas_bg.tag_bind("min_button_img", "<Button-1>", self.min_button_clicked)
        self.canvas_bg.tag_bind("min_button_img", "<ButtonRelease-1>", self.min_button_released)

        # secボタン
        self.sec_button_img = tk.PhotoImage(file="./img/sec_button.png")
        self.canvas_bg.create_image(90, 210, anchor=tk.NW, image=self.sec_button_img, tag="sec_button_img")
        self.canvas_bg.tag_bind("sec_button_img", "<Button-1>", self.sec_button_clicked)
        self.canvas_bg.tag_bind("sec_button_img", "<ButtonRelease-1>", self.sec_button_released)

        # resetボタン
        self.reset_button_img = tk.PhotoImage(file="./img/reset_button.png")
        self.canvas_bg.create_image(150, 210, anchor=tk.NW, image=self.reset_button_img, tag="reset_button_img")
        self.canvas_bg.tag_bind("reset_button_img", "<Button-1>", self.reset_button_clicked)
        self.canvas_bg.tag_bind("reset_button_img", "<ButtonRelease-1>", self.reset_button_released)

        # start/stopボタン
        self.start_button_img = tk.PhotoImage(file="./img/start_button.png")
        self.canvas_bg.create_image(270, 160, anchor=tk.NW, image=self.start_button_img, tag="start_button_img")
        self.canvas_bg.tag_bind("start_button_img", "<Button-1>", self.start_button_clicked)
        self.canvas_bg.tag_bind("start_button_img", "<ButtonRelease-1>", self.start_button_released)

# 各ボタンが押された時の処理

    # minボタンを押した時
    def min_button_clicked(self, event):

        if self.left_min < 59: # 最大59分まで
            self.set_time += 60 # セット時間をプラス
            self.left_min += 1
            self.update_min_text() # 分の表示更新
            self.layer_adjustment() # レイヤーの前後調整

        # 暗いボタンを表示
        self.min_button_shadow_img = tk.PhotoImage(file="./img/min_button_shadow.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        self.canvas_bg.create_image(30, 210, anchor=tk.NW, image=self.min_button_shadow_img, tag="min_button_shadow_img")

    # minボタンを離した時
    def min_button_released(self, event):
        self.canvas_bg.delete("min_button_shadow_img") # 暗いボタンを消去

    # secボタンを押した時
    def sec_button_clicked(self, event):
        if self.left_sec < 59: # 最大59秒まで
            self.set_time += 1 # セット時間をプラス
            self.left_sec += 1
            self.update_sec_text() # 秒の表示更新
            self.layer_adjustment() # レイヤーの前後調整

        # 暗いボタンを表示
        self.sec_button_shadow_img = tk.PhotoImage(file="./img/sec_button_shadow.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        self.canvas_bg.create_image(90, 210, anchor=tk.NW, image=self.sec_button_shadow_img, tag="sec_button_shadow_img")

    # secボタンを離した時
    def sec_button_released(self, event):
        self.canvas_bg.delete("sec_button_shadow_img") # 暗いボタンを消去

    # resetボタンを押した時
    def reset_button_clicked(self, event):
        self.set_time = 0 # セット時間をリセット
        self.left_min = 0 # 残り時間（分）をリセット
        self.left_sec = 0 # 残り時間（秒）をリセット

        self.update_min_text() # 分の表示更新
        self.update_sec_text() # 秒の表示更新

        self.layer_adjustment() # レイヤーの前後調整

        # 暗いボタンを表示
        self.reset_button_shadow_img = tk.PhotoImage(file="./img/reset_button_shadow.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        self.canvas_bg.create_image(150, 210, anchor=tk.NW, image=self.reset_button_shadow_img, tag="reset_button_shadow_img")

    # resetボタンを離した時
    def reset_button_released(self, event):
        self.canvas_bg.delete("reset_button_shadow_img") # 暗いボタンを消去

    # start/stopボタンを押した時
    def start_button_clicked(self, event):

        if self.timer_on == False:
            # 暗いボタンを表示
            self.start_button_shadow_img = tk.PhotoImage(file="./img/start_button_shadow.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
            self.canvas_bg.create_image(270, 160, anchor=tk.NW, image=self.start_button_shadow_img, tag="start_button_shadow_img")

        elif self.timer_on == True:
            # 暗いボタンを表示
            self.start_button_shadow_img = tk.PhotoImage(file="./img/stop_button_shadow.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
            self.canvas_bg.create_image(270, 160, anchor=tk.NW, image=self.start_button_shadow_img, tag="start_button_shadow_img")

    # startボタンを離した時
    def start_button_released(self, event):
        self.canvas_bg.delete("start_button_shadow_img") # 暗いボタンを消去

        if self.set_time >= 1:

            if self.timer_on == False:

                # ボタン画像を変更
                self.canvas_bg.delete("start_button_img") # 画像を消去
                self.start_button_img = tk.PhotoImage(file="./img/stop_button.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
                self.canvas_bg.create_image(270, 160, anchor=tk.NW, image=self.start_button_img, tag="start_button_img")
                self.canvas_bg.tag_bind("start_button_img", "<Button-1>", self.start_button_clicked)
                self.canvas_bg.tag_bind("start_button_img", "<ButtonRelease-1>", self.start_button_released)

                self.layer_hidden_buttons() # ストップ以外のボタンを隠す

                # タイマー開始
                self.timer_on = True

                self.start_time =time.time() # 開始時間を代入
                self.update_time() # updateTime関数を実行

            elif self.timer_on == True:

                # タイマーストップ
                self.timer_on = False

                # ボタン画像を変更
                self.canvas_bg.delete("start_button_img") # 画像を消去
                self.start_button_img = tk.PhotoImage(file="./img/start_button.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
                self.canvas_bg.create_image(270, 160, anchor=tk.NW, image=self.start_button_img, tag="start_button_img")
                self.canvas_bg.tag_bind("start_button_img", "<Button-1>", self.start_button_clicked)
                self.canvas_bg.tag_bind("start_button_img", "<ButtonRelease-1>", self.start_button_released)

                self.layer_adjustment() # レイヤーの前後調整

                self.set_time = self.left_time
                app.after_cancel(self.after_id)

    # 表示時間の更新処理
    def update_time(self):
        self.elapsed_time = time.time() - self.start_time  # 経過時間を計算
        self.left_time = self.set_time - self.elapsed_time # 残り時間を計算
        self.left_min = self.left_time // 60 # 残り時間（分）を計算
        self.left_sec = self.left_time % 60 # 残り時間（秒）を計算

        self.update_min_text() # 分の表示更新
        self.update_sec_text() # 秒の表示更新

        if self.left_time > 0.1:
            self.after_id = self.after(10, self.update_time)
        else:
            self.timer_on = False

            self.set_time = self.left_time

            # ボタン画像を変更
            self.canvas_bg.delete("start_button_img") # 画像を消去
            self.start_button_img = tk.PhotoImage(file="./img/start_button.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
            self.canvas_bg.create_image(270, 160, anchor=tk.NW, image=self.start_button_img, tag="start_button_img")
            self.canvas_bg.tag_bind("start_button_img", "<Button-1>", self.start_button_clicked)
            self.canvas_bg.tag_bind("start_button_img", "<ButtonRelease-1>", self.start_button_released)

            self.layer_adjustment() # レイヤーの前後調整

# 個別の処理

    # 分の表示更新
    def update_min_text(self):
        self.canvas_bg.delete("min_text") # 表示時間（分）を消去
        self.canvas_bg.create_text(280, 80, text=str(math.floor(self.left_min)).zfill(2) + "：", font=("MSゴシック体", "80", "bold"), fill="#ffffff", tag="min_text", anchor="e") # 分を表示
        self.layer_hidden_buttons() # ストップ以外のボタンを隠す

    # 秒の表示更新
    def update_sec_text(self):
        self.canvas_bg.delete("sec_text") # 表示時間（秒）を消去
        self.canvas_bg.create_text(280, 80, text=str(math.floor(self.left_sec)).zfill(2), font=("MSゴシック体", "80", "bold"), fill="#ffffff", tag="sec_text", anchor="w") # 秒を表示
        self.layer_hidden_buttons() # ストップ以外のボタンを隠す

    # レイヤーの前列後列調整
    def layer_adjustment(self):
        self.canvas_bg.tag_raise("timer_bg")
        self.canvas_bg.tag_raise("min_text")
        self.canvas_bg.tag_raise("sec_text")
        self.canvas_bg.tag_raise("min_button_img")
        self.canvas_bg.tag_raise("sec_button_img")
        self.canvas_bg.tag_raise("reset_button_img")
        self.canvas_bg.tag_raise("start_button_img")
        self.canvas_bg.tag_raise("start_button_shadow_img")

    # ストップ以外のボタンを隠す
    def layer_hidden_buttons(self):
        self.canvas_bg.tag_raise("timer_bg")
        self.canvas_bg.tag_raise("min_text")
        self.canvas_bg.tag_raise("sec_text")
        self.canvas_bg.tag_raise("start_button_img")
        self.canvas_bg.tag_raise("start_button_shadow_img")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
