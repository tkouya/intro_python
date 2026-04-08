# address_class.py: 住所録クラス
class MyAddress:
    # no, name, yomigana, postal_address, memo
    # クラス初期化関数
    def __init__(
            self,
            no: int, # ID番号
            name: str, # 名前
            yomigana: str, # 名前の読み型
            postal_address: str # 住所 
        ):
        self.no = no
        self.name = name
        self.yomigana = yomigana
        self.postal_address = postal_address
        return
    
    # 表示
    def print_all(self):
        print(f'{self.no:5d}: {self.name}, {self.yomigana}, {self.postal_address}')
        return

    # 文字列化
    def __str__(self):
        return str([self.no, self.name, self.yomigana, self.postal_address])
