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

        # label1ウィジェット
        self.label1 = tk.Label(self,text="プログラミング言語を\n一つ選択してください", padx = 50)
        self.label1.pack()

        # radio1ウィジェット
        self.select_var = tk.IntVar()
        self.select_var.set(1)

        self.languages = [("Python",1),("PHP",2),("Ruby",3),("Java",4),("C",5)]

        def showchoice(): # radio1の選択肢をクリックした時の処理
            for language, val in self.languages: # ループ開始
                if val == self.select_var.get(): # 選択されている言語とlanguagesリストの言語を照合
                    self.label2_text.set(language + " でよろしいですか？") # label2ウィジェットのテキストを変更
                    self.answer = language # answer変数に選択されている言語を保持
                    break

        for language, val in self.languages:
            self.radio1 = tk.Radiobutton(self, text=language, value=val, variable=self.select_var, command=showchoice)
            self.radio1.pack(anchor=tk.W)

        # label2ウィジェット
        self.label2_text = tk.StringVar()
        self.label2_text.set("言語を選択してください")

        self.label2 = tk.Label(self, textvariable=self.label2_text)
        self.label2.pack()

        # button1ウィジェット
        self.answer = "言語が選択されていません" # answer変数を定義
        def button1_clicked(): # button1をクリックした時の処理
            if self.answer == "言語が選択されていません": # ansewr変数の中身で条件分岐
                self.label2_text.set(self.answer) # label2ウィジェットのテキストを書き換え
            else:
                print(self.answer) # 選ばれた言語をコンソールに標準出力
                app.quit() # アプリケーションを終了

        self.button1 = tk.Button(self,text="OK！", command=button1_clicked, padx = 20) # button1ウィジェットを生成
        self.button1.pack() # button1ウィジェットを配置

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
