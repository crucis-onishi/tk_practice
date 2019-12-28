import tkinter as tk

 # tk.Frameを継承したFrame1クラスを作成
class Frame1(tk.Frame):
    def __init__(self, master=None): # コンストラクタを定義
        super().__init__(master, width=400, height=300) # 継承元クラス（tk.Frame）のコンストラクタを呼び出し、幅と高さを指定

        #ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # フレームの設定
        self.config(bg="whitesmoke") # 背景色を指定
        self.propagate(False) # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)

        # 実行内容
        self.pack() # フレームを配置
        self.create_widget() # 下記で定義しているcreate_widgetメソッドを実行

    #create_widgetメソッドを定義
    def create_widget(self):

        # ラベルを作成
        self.label1 = tk.Label(self, text=u"これはラベルです")
        self.label1.pack()

        # エントリーを作成
        self.entry1 = tk.Entry(self)
        self.entry1.insert(tk.END, u"これはエントリーです")
        self.entry1.pack()

        # ボタンを作成
        button1 = tk.Button(self, text=u"これはボタンです")
        button1.pack()

if __name__ == "__main__": # このファイルが実行されている場合の処理
    root = tk.Tk() # rootインスタンスを生成
    f1 = Frame1(master=root) # Frame1クラスからf1インスタンスを生成
    f1.mainloop() # f1インスタンスのイベントハンドラを呼び出し
