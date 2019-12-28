import tkinter as tk
from tkinter.filedialog import askopenfilename # tkinter.filedialogモジュールのaskopenfilenameメソッドをインポート

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack() # メインフレームを配置
        self.create_menu() # 下記で定義しているcreate_menuメソッドを実行
        self.create_widget() # 下記で定義しているcreate_widgetメソッドを実行

    # create_menuメソッドを定義
    def create_menu(self):
        # メニューバー用の関数を定義
        def NewFile():
            print("New File!")
        def OpenFile():
            file_name = askopenfilename() # インポートしたtkinter.filedialogモジュールのaskopenfilenameメソッドを代入
            print(file_name)
        def About():
            print("このアプリはhogehogeなアプリです")

        self.menu_bar = tk.Menu(self)
        root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0) # 大項目「ファイル」を生成、切り取り線をオフに
        self.menu_bar.add_cascade(label="ファイル", menu=self.file_menu) # 大項目「ファイル」を配置
        self.file_menu.add_command(label="新規作成", command=NewFile) # 小項目「新規作成」に処理を割り当て
        self.file_menu.add_command(label="開く", command=OpenFile) # 小項目「開く」に処理を割り当て
        self.file_menu.add_separator() # セパレーターを追加
        self.file_menu.add_command(label="終了", command=root.quit) # 小項目「終了」に処理を割り当て

        self.help_menu = tk.Menu(self, tearoff=2) # 大項目「ヘルプ」を生成、切り取り線をオフに
        self.menu_bar.add_cascade(label="ヘルプ", menu=self.help_menu) # 大項目「ヘルプ」を配置
        self.help_menu.add_command(label="このアプリケーションの情報を表示します", command=About) # 小項目に処理を割り当て

    # create_widgetメソッドを定義
    def create_widget(self):
        # label1ウィジェット
        self.label1 = tk.Label(self,text="メニューバーを\n使ってみましょう", padx = 100, pady=75)
        self.label1.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
