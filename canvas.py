import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")
        self.master.geometry("800x600")

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # canvasウィジェットを作成
        self.canvas = tk.Canvas(self, width=800, height=600) # canvasウィジェットを作成
        self.canvas.pack() # canvasウィジェットを配置

        self.bg_img = tk.PhotoImage(file="img/bg_img.png") # 画像ファイルのオブジェクトを作成
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img) # 画像を描画
        # この時anchorを指定しないと原点がキャンバスオブジェクトの中央になってしまう。

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
