import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")
        self.master.geometry("800x700")

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):

        # canvasウィジェットを作成
        self.canvas = tk.Canvas(self, width=800, height=700)
        self.canvas.pack()

        self.bg_img1 = tk.PhotoImage(file="img/bg_img1.png")
        self.bg_img2 = tk.PhotoImage(file="img/bg_img2.png") # 画像2もキャンバス作成時に読み込んでおく
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img1, tag="img1") # オプション引数tagでタグを付ける

        # ボタンを作成・配置
        delete_button = tk.Button(self, text="画像を消去", font=("MSゴシック体", "20","bold"), command=self.delete_img)
        delete_button.place(x=100, y=620)

        create_button1 = tk.Button(self, text="画像1を表示", font=("MSゴシック体", "20","bold"), command=self.create_img1)
        create_button1.place(x=300, y=620)

        create_button2 = tk.Button(self, text="画像2を表示", font=("MSゴシック体", "20","bold"), command=self.create_img2)
        create_button2.place(x=510, y=620)

    # 各ボタンが押された時の処理
    def delete_img(self):
        self.canvas.delete("img1", "img2") # 指定したタグが付いている画像を消去

    def create_img1(self):
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img1, tag="img1") # 画像1にimg1タグを付けて描画

    def create_img2(self):
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img2, tag="img2") # 画像2にimg2タグを付けて描画

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
