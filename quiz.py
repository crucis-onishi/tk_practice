import tkinter as tk
import threading
import time

questions = [
                {"問題文":"この本のタイトルはなんでしょう？", "選択肢":["Pythonの教科書", "ゼロから学ぶPython", "プログラミングはじめの一歩", "本は本でも食べられない本"], "正解":3},
                {"問題文":"次のうちPythonに当てはまるのは？", "選択肢":["静的型付け言語", "動的型付け言語", "オレ的カッコつけ言語"], "正解":2},
                {"問題文":"次のうちPythonに当てはまるのは？", "選択肢":["シンプルで扱いやすい汎用言語", "国産のプログラミング言語", "マークアップ言語の1つ", "ブラウザ上で動作するスクリプト言語"], "正解":1}
            ]

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 変数定義
        self.question_number = 0
        self.sentence_text = tk.StringVar()
        self.score = 0.00
        self.score_text = tk.StringVar()
        self.score_text.set("得点\n0.00")

        # 実行内容
        self.pack()
        self.create_widget()
        self.create_question()

    # create_widgetメソッドを定義
    def create_widget(self):

        # 背景画像
        bg_img = tk.Canvas(self, width=800, height=600)
        bg_img.pack()
        self.haikei = tk.PhotoImage(file="haikei.png") # イメージは、必ずインスタンス変数に代入する必要があります。そうしないと、関数を抜けたとたん変数のメモリーが 回収され、イメージが消えてしまうからです。
        bg_img.create_image(400, 300, image=self.haikei)

        # 得点版
        label = tk.Label(self, relief=tk.RIDGE, width=17, height=3, textvariable=self.score_text, font=("MSゴシック", "20", "bold"), bg="white")
        label.place(x=500, y=10)

    # create_questionメソッドを定義
    def create_question(self):

        # 第〇問
        question_number_label = tk.Label(self, relief=tk.RIDGE, width=28, height=1, anchor=tk.N, text="第" + str(self.question_number + 1) + "問", font=("MSゴシック", "20", "bold"), bg="white")
        question_number_label.place(x=10, y=10)

        # 問題文
        self.sentence_text.set(questions[self.question_number]["問題文"]) # sentence_textに文字列代入
        sentence = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.NW, justify="left", wraplength=470, textvariable=self.sentence_text,font=("MSゴシック", "20", "bold"), bg="white")
        sentence.place(x=10, y=60)

        # 選択肢
        for i,choices in enumerate(questions[self.question_number]["選択肢"]):
            if i + 1 == questions[self.question_number]["正解"]:
                correct_button = tk.Button(self, width=28, text=choices, font=("MSゴシック", "20", "bold"), bg="white", command=self.correct)
                correct_button.place(x=10, y=350 + (i * 60))
            else:
                incorrect_button = tk.Button(self, width=28, text=choices, font=("MSゴシック", "20", "bold"), bg="white", command=self.incorrect)
                incorrect_button.place(x=10, y=350 + (i * 60))

    # create_resultメソッドを定義
    def create_result(self):
        # 問題文
        result = tk.Label(self, relief=tk.RIDGE, width=28, height=8,anchor=tk.CENTER, wraplength=470,text="問題は以上です。\nお疲れさまでした。",font=("MSゴシック", "20", "bold"), bg="white")
        result.place(x=10, y=60)


    # 選択肢削除メソッドを定義
    def destroy_choices(self,parent):
        children = parent.winfo_children()
        for child in children:
            child.destroy()

    # 選択肢ボタンが押された時の処理
    def correct(self):
        self.sentence_text.set("正解！")
        self.score += 100 / len(questions)
        self.score_text.set("得点\n" + str(round(self.score, 2)))
        self.after(1500, self.next)

    def incorrect(self):
        self.sentence_text.set("不正解！")
        self.after(1500, self.next)

    # 正解不正解表示後の処理
    def next(self):
        self.question_number += 1
        self.destroy_choices(self) # フレームを削除
        self.create_widget() # フレームを再生成

        if self.question_number < len(questions):
            self.create_question() # 次の問題を描画
        else:
            self.create_result() # リザルト画面を描画

# メインの処理
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
