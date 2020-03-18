# bindメソッドで押されたボタンのテキストを参照して正解不正解を判定するパターン

import tkinter as tk

questions = [
                {"問題文":"この本のタイトルはなんでしょう？",
                    "選択肢":["Pythonの教科書", "ゼロから学ぶPython", "プログラミングはじめの一歩", "本は本でも食べられない本"],
                    "正解":"プログラミングはじめの一歩"},
                {"問題文":"次のうちPythonに当てはまるのは？",
                    "選択肢":["静的型付け言語", "動的型付け言語", "オレ的カッコつけ言語"],
                    "正解":"動的型付け言語"},
                {"問題文":"次のうちPythonに当てはまるのは？",
                    "選択肢":["シンプルで扱いやすい汎用言語", "国産のプログラミング言語", "マークアップ言語の1つ", "ブラウザ上で動作するスクリプト言語"],
                    "正解":"シンプルで扱いやすい汎用言語"}
            ]

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("クイズPythonアカデミー")

        # 変数定義
        self.question_number = 0
        self.score = 0.00
        self.allocate_points = 100 / len(questions)

        # 実行内容
        self.pack()
        self.create_widget()
        self.create_buttons()

    # create_widgetメソッドを定義
    def create_widget(self):

        # 背景画像
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.pack()
        self.bg_img = tk.PhotoImage(file="haikei.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        canvas.create_image(400, 300, image=self.bg_img)

        # 得点版
        self.scoreboard = tk.Label(self, relief=tk.RIDGE, width=17, height=3, text="得点\n" + str(round(self.score, 2)), font=("游ゴシック体", "20", "bold"), bg="white")
        self.scoreboard.place(x=500, y=10)

        # 第〇問
        self.question_number_label = tk.Label(self, relief=tk.RIDGE, width=28, height=1, anchor=tk.N, text="第" + str(self.question_number + 1) + "問", font=("游ゴシック体", "20", "bold"), bg="white")
        self.question_number_label.place(x=10, y=10)

        # 問題文
        self.sentence = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.NW, justify="left", wraplength=470, text=questions[self.question_number]["問題文"], font=("游ゴシック体", "20", "bold"), bg="white")
        self.sentence.place(x=10, y=60)

    # create_buttonsメソッドを定義
    def create_buttons(self):

        # 選択肢ボタン
        self.buttons = []
        for i,choice in enumerate(questions[self.question_number]["選択肢"]):
            button = tk.Button(self, width=28, text=choice, font=("游ゴシック体", "20", "bold"), bg="white")
            button.bind("<Button-1>", self.button_clicked)
            button.place(x=10, y=350 + (i * 60))
            self.buttons.append(button)

    # create_resultメソッドを定義
    def create_result(self):
        # 問題文
        result = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.CENTER, wraplength=470,text="問題は以上です。\nお疲れさまでした。",font=("游ゴシック体", "20", "bold"), bg="white")
        result.place(x=10, y=60)

    # ボタンを全てDISABLEDにする処理
    def button_disabled(self):
        for button in self.buttons:
            button["state"] = tk.DISABLED

    # 選択肢ボタンが押された時の処理
    def button_clicked(self, event):
        self.button_disabled()
        if event.widget["text"] == questions[self.question_number]["正解"]:
            self.sentence["text"] = "正解！"
            self.score += self.allocate_points
            self.scoreboard["text"] = "得点\n" + str(round(self.score, 2))
        else:
            self.sentence["text"] = "不正解！"

        self.after(1500, self.next)

    # 正解不正解表示後の処理
    def next(self):
        self.question_number += 1
        self.destroy_buttons() # 選択肢ボタンをすべて削除

        if self.question_number < len(questions):
            self.question_number_label["text"] = "第" + str(self.question_number + 1) + "問" # 何問目かを更新
            self.sentence["text"] = questions[self.question_number]["問題文"] # 問題文を更新
            self.create_buttons() # 次の問題を描画
        else:
            self.question_number_label.destroy()
            self.sentence.destroy()
            self.create_result() # リザルト画面を描画

    # ボタンを削除する処理
    def destroy_buttons(self):
        for button in self.buttons:
            button.destroy()

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
