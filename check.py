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

        # label1ウィジェットを生成・配置
        self.label1 = tk.Label(self,text="興味のある分野を選択してください", padx = 50)
        self.label1.pack()

        # Checkbarフレームを定義
        class Checkbar(tk.Frame):
            def __init__(self, master=None, items=[], side=tk.LEFT, anchor=tk.W):
                super().__init__(master)

                self.vars = [] # 各項目のチェック状態を保持するvarsリストを定義
                for item in items:
                    select_var = tk.IntVar()
                    self.check = tk.Checkbutton(self, text=item, variable=select_var)
                    self.check.pack(anchor=tk.W, side=tk.LEFT)
                    self.vars.append(select_var) # ウィジェット変数select_varをvarsリストに追加

            # Checkbarフレームの各項目のチェック状態を返すstate関数を定義
            def state(self):
                return map((lambda select_var: select_var.get()), self.vars)

        # field_barフレームを生成・配置
        self.items1 = ["インフラ", "ネットワーク", "バックエンド", "フロントエンド", "デザイン"] # items1リストを定義
        self.field_bar = Checkbar(self, items=self.items1)
        self.field_bar.pack(side=tk.TOP)
        self.field_bar.config(relief=tk.GROOVE, bd=2)

        # product_barフレームを生成・配置
        self.items2 = ["Webアプリ", "スマホアプリ", "デスクトップアプリ"] # items2リストを定義
        self.product_bar = Checkbar(self, items=self.items2)
        self.product_bar.pack()

        # button1ウィジェット
        def button1_clicked(): # button1をクリックした時の処理
            answer1 = [] # answer1リストを定義
            for i, state in enumerate(self.field_bar.state()): # ループ開始、field_barフレームの各項目のチェック状態リストを参照
                if state == 1: # リストi番目のチェック状態がオンなら
                    answer1.append(self.items1[i]) # items1リストのi番目の項目をanswer1リストに加える

            answer2 = [] # answer2リストを定義
            for i, state in enumerate(self.product_bar.state()): # ループ開始、product_barフレームの各項目のチェック状態リストを参照
                if state == 1: # リストi番目のチェック状態がオンなら
                    answer2.append(self.items2[i]) # items2リストのi番目の項目をanswer2リストに加える

            print(answer1,answer2) # answer1リスト、answer2リストの中身をコンソールに出力

        self.button1 = tk.Button(self,text="確認", command=button1_clicked, padx=50) # button1ウィジェットを生成
        self.button1.pack() # button1ウィジェットを配置

        # button2ウィジェット
        self.button2 = tk.Button(self,text="終了", command=root.quit, padx=50) # button2ウィジェットを生成
        self.button2.pack() # button2ウィジェットを配置

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
