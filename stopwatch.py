import tkinter as tk
import time

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        master.title("ストップウォッチ")
        master.geometry("400x160")

        # 変数定義
        self.startTime = 0.0 # 開始時間
        self.elapsedTime = 0.0 # 経過時間
        self.after_id = 0 # after_id変数を定義

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # canvasウィジェットを作成
        self.canvas = tk.Canvas(self.master, width=380, height=80, bg="lightgreen")
        self.canvas.place(x=10, y=10)
        self.canvas.create_text(380,40,text=round(self.elapsedTime,1), font=("MSゴシック体", "24", "bold"), tag="Time", anchor="e") # 時間0.0を表示

        # ボタンを作成・配置
        startButton = tk.Button(self.master, text="スタート", font=("MSゴシック体", "18","bold"), command=self.startButtonClicked)
        startButton.place(x=10, y=100)

        stopButton = tk.Button(self.master, text="ストップ", font=("MSゴシック体", "18","bold"), command=self.stopButtonClicked)
        stopButton.place(x=140, y=100)

        resetButton = tk.Button(self.master, text="リセット", font=("MSゴシック体", "18","bold"), command=self.resetButtonClicked)
        resetButton.place(x=270, y=100)

    # 各ボタンが押された時の処理
    def startButtonClicked(self):
        self.startTime = time.time() - self.elapsedTime # startTime変数に開始時間を代入
        self.updateTime() # updateTime関数を実行

    def stopButtonClicked(self):
        self.after_cancel(self.after_id) # updateTime関数の再帰処理を終了

    def resetButtonClicked(self):
        self.startTime = time.time() # startTime変数に現在時刻を代入
        self.elapsedTime = 0.0 # elapsedTime変数を初期化
        self.canvas.delete("Time") # 表示時間を消去
        self.canvas.create_text(380,40,text=round(self.elapsedTime,1),font=("MSゴシック体","24","bold"),tag="Time",anchor="e") # 時間0.0を表示

    # 表示時間の更新処理
    def updateTime(self):
        self.canvas.delete("Time") # 表示時間を消去
        self.elapsedTime = time.time() - self.startTime # 経過時間を代入
        self.canvas.create_text(380,40,text=round(self.elapsedTime,1),font=("MSゴシック体","24","bold"),tag="Time",anchor="e") # 経過時間を表示
        self.after_id = self.after(10, self.updateTime)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
