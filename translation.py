import tkinter as tk
import sys
import uuid
import requests
import base64
import hashlib

from imp import reload


class Translate():
    reload(sys)
    YOUDAO_URL = "https://openapi.youdao.com/ocrtransapi"
    APP_KEY = '7e782f78aec29bd2'
    APP_SECRET = 'Qrp2mhpcsmYpG0KWHGAgI8rIWuzuA2FV'

    def truncate(q):
        if q is None:
            return None
        size = len(q)
        if size <= 20:
            return q
        else:
            # 取前10个，总长度，后10个
            return q[0:10] + str(size) + q[size - 10:size]

    # 摘要算法
    def encrypt(signStr):
        hash_algorithm = hashlib.md5()
        # encode将signStr处理为二进制格式
        hash_algorithm.update(signStr.encode("utf-8"))
        # 获取哈希加密后的16进制字符串
        return hash_algorithm.hexdigest()

    def do_request(data):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        return requests.post(Translate.YOUDAO_URL, data=data, headers=headers)

    def connect(self):
        # 以二进制方式打开图片
        f = open(r"C:\Users\unicom_huangsl107\Desktop\1.png", "rb")
        # 读取文件内容并转换为base64编码
        q = base64.b64encode(f.read()).decode("utf-8")
        f.close()

        data = {}
        data["from"] = "auto"
        data["to"] = "auto"
        data["type"] = "1"
        data["q"] = q
        salt = str(uuid.uuid1())
        signStr = Translate.APP_KEY + q + salt + Translate.APP_SECRET
        sign = Translate.encrypt(signStr)
        data["appKey"] = Translate.APP_KEY
        data["salt"] = salt
        data["sign"] = sign

        response = Translate.do_request(data)
        print(response.content)

s1 = s.encode("unicode_escape")
s2 = s1.decode("utf-8")
s3 = s2.replace("\\x",'')
s4 = binascii.a2b_hex(s3)
s4.decode("utf-8")
trans = Translate()
trans.connect()


def get_pictures():
    return


def set_result_path():
    return


def translate_files():
    return


root = tk.Tk()
root.title("hsl youdao translation test")
frm = tk.Frame(root)
frm.grid(padx="50", pady="50")
btn_get_file = tk.Button(frm, text="choose raw material", command=get_pictures)
btn_get_file.grid(row=0, column=0, ipadx="3", ipady="3", padx="10", pady="20")
text1 = tk.Text(frm, width="40", height="10")
text1.grid(row=0, column=1)
btn_get_result_path = tk.Button(frm,
                                text="choose address for translation result",
                                command=set_result_path)
btn_get_result_path.grid(row=1, column=0)
text2 = tk.Text(frm, width="40", height="2")
text2.grid(row=1, column=1)
btn_sure = tk.Button(frm, text="Translate", command=translate_files)
btn_sure.grid(row=2, column=1)
root.mainloop()
