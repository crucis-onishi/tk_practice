import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack()
        self.create_widget1()

    # create_widget1メソッドを定義
    def create_widget1(self):

        items = ["氏名", "生年月日", "電話番号", "メールアドレス"] # itemsリストを定義

        # label1ウィジェット
        self.label1 = tk.Label(self,text="ユーザー情報を入力してください", padx = 50)
        self.label1.pack(padx=5, pady=5)

        # button1が押された時に実行されるfetchメソッドを定義
        def fetch(entries): # entriesリストの要素は(項目名, entryウィジェット)のタプルとなっている
            for entry in entries: # ループ開始
                item = entry[0] # 項目名を取得
                text = entry[1].get() # entryウィジェットの入力値を取得
                print('{}: "{}"'.format(item, text)) # 値をフォーマットして出力

        # 各項目のlabelとentry
        def makeform(self, items): # 処理を呼び出せるようmakeform関数としてまとめる
            entries = [] # entriesリストを定義
            for item in items:
                row = tk.Frame(self)
                label = tk.Label(row,text=item)
                entry = tk.Entry(row)

                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                label.pack(side=tk.LEFT)
                entry.pack(side=tk.RIGHT, fill=tk.X)
                entries.append((item, entry)) # 項目名と生成したentryウィジェットのタプルを1つの要素としてentriesリストに追加
            return entries # entriesリストを返り値として返す
        ents = makeform(self, items) # ents変数を定義してmakeform関数を代入

        self.button1 = tk.Button(self, text="確認",command=(lambda e=ents: fetch(e))) # ボタンが押されるとmakeform関数を実行してその返り値を使ってfetch関数を実行
        self.button2 = tk.Button(self, text="終了", command=root.quit)
        self.button1.pack(side=tk.LEFT, padx=5, pady=5)
        self.button2.pack(side=tk.LEFT, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
