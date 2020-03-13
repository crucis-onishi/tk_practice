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
        self.sentence_text = tk.StringVar()
        self.score = 0.00
        self.allocate_points = 100 / len(questions)
        self.score_text = tk.StringVar()
        self.score_text.set("得点\n0.00")

        # 実行内容
        self.pack()
        self.create_widget()
        self.create_question()

    # create_widgetメソッドを定義
    def create_widget(self):

        # 背景画像
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.pack()
        self.bg_img = tk.PhotoImage(file="haikei.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        canvas.create_image(400, 300, image=self.bg_img)

        # 得点版
        scoreboard = tk.Label(self, relief=tk.RIDGE, width=17, height=3, textvariable=self.score_text, font=("游ゴシック体", "20", "bold"), bg="white")
        scoreboard.place(x=500, y=10)

    # create_questionメソッドを定義
    def create_question(self):

        # 第〇問
        question_number_label = tk.Label(self, relief=tk.RIDGE, width=28, height=1, anchor=tk.N, text="第" + str(self.question_number + 1) + "問", font=("游ゴシック体", "20", "bold"), bg="white")
        question_number_label.place(x=10, y=10)

        # 問題文
        self.sentence_text.set(questions[self.question_number]["問題文"]) # sentence_textに文字列代入
        sentence = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.NW, justify="left", wraplength=470, textvariable=self.sentence_text,font=("游ゴシック体", "20", "bold"), bg="white")
        sentence.place(x=10, y=60)

        # 選択肢ボタン
        for i,choice in enumerate(questions[self.question_number]["選択肢"]):
            button = tk.Button(self, width=28, text=choice, font=("游ゴシック体", "20", "bold"), bg="white")
            button.bind("<Button-1>", self.button_clicked)
            button.place(x=10, y=350 + (i * 60))

    # create_resultメソッドを定義
    def create_result(self):
        # 問題文
        result = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.CENTER, wraplength=470,text="問題は以上です。\nお疲れさまでした。",font=("游ゴシック体", "20", "bold"), bg="white")
        result.place(x=10, y=60)

    # 選択肢ボタンが押された時の処理
    def button_clicked(self, event):
        if event.widget["text"] == questions[self.question_number]["正解"]:
            self.sentence_text.set("正解！")
            self.score += self.allocate_points
            self.score_text.set("得点\n" + str(round(self.score, 2)))
        else:
            self.sentence_text.set("不正解！")

        self.after(1500, self.next)

    # 正解不正解表示後の処理
    def next(self):
        self.question_number += 1
        self.destroy_widgets(self) # フレームの子要素を全て削除
        self.create_widget() # ウィジェットを再生成

        if self.question_number < len(questions):
            self.create_question() # 次の問題を描画
        else:
            self.create_result() # リザルト画面を描画

    # フレームの子要素削除メソッドを定義
    def destroy_widgets(self,parent):
        children = parent.winfo_children()
        for child in children:
            child.destroy()

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
