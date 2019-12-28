import tkinter as tk

 # tk.Frameを継承したApplicationクラスを作成
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("ウィンドウのタイトル")
        self.master.geometry("300x200")

        # ウィジェット変数を生成
        self.name_var = tk.StringVar(value="山田 太郎")
        self.age_var = tk.IntVar(value=20)
        self.agreement_var = tk.BooleanVar(value=False)

        # 実行内容
        self.pack()
        self.create_widget()

    # create_widgetメソッドを定義
    def create_widget(self):
        # 氏名
        self.name = tk.Entry(self,textvariable = self.name_var)
        self.name.pack()
        # 年齢
        self.age = tk.Spinbox(self,textvariable=self.age_var, from_=0, to=120)
        self.age.pack()
        # 同意
        self.agreement = tk.Checkbutton(self,text="同意します",variable=self.agreement_var)
        self.agreement.pack()
        # ボタンフレーム
        self.buttonframe = tk.Frame(self)
        self.buttonframe.pack()
        # sampleボタン
        self.sample = tk.Button(self.buttonframe,text="入力例を表示",command=self.inputSampleValue)
        self.sample.pack(side="left")
        # 確認ボタン
        self.verify = tk.Button(self.buttonframe,text="確認",command=self.outputValue)
        self.verify.pack(side="left")

    # inputSampleValueメソッドを定義
    def inputSampleValue(self):
        self.name_var.set(value="鈴木 一郎")
        self.age_var.set(value=31)
        self.agreement_var.set(value=False)

    # outputValueメソッドを定義
    def outputValue(self):
        print(self.name_var.get())
        print(self.age_var.get())
        print(self.agreement_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
