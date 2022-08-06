import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master,  width=200, height=150)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")

        # 実行内容
        self.pack() # メインフレームを配置
        self.create_widget() # create_widgetメソッドを実行

    #create_widgetメソッドを定義
    def create_widget(self):

        # 1つ目のフレーム
        frame1 = tk.Frame(self.master, relief=tk.RIDGE, bd=2) # tk.Frameクラスからframe1インスタンスを生成
        list1 = [("A", "lightskyblue"), ("B", "khaki"), ("C", "yellowgreen"), ("D", "hotpink")] # list1リストを定義
        for text, color in list1: # ループ開始
            label=tk.Label(frame1, text=text, bg=color, font=("20")) # labelウィジェットを作成
            label.pack(side=tk.LEFT) # labelウィジェットを配置
        frame1.place(relx=0.1, rely=0.1) # frame1フレームを配置

        # 2つ目のフレーム
        frame2 = tk.Frame(self.master, relief=tk.RIDGE, bd=2) # tk.Frameクラスからframe2インスタンスを生成
        list2 = [("A", "lightskyblue"), ("B", "khaki"), ("C", "yellowgreen"), ("D", "hotpink")] # list2リストを定義
        for i, (text, color) in enumerate(list2): # ループ開始
            label=tk.Label(frame2, text=text, bg=color, font=("20")) # labelウィジェットを作成
            label.grid(row=i//2, column=i%2) # labelウィジェットを配置
        frame2.place(relx=0.6, rely=0.5) # frame2フレームを配置

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
