# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:52:07 2022

@author: dudawei
"""

# import tkinter
# import tkinter.messagebox as msgbox
# import random
 
# top = tkinter.Tk()
 
# def helloCallBack():
#    random_num=random.randint(1,40)
#    msgbox.showinfo( '提示',"头等奖学号为: %d"%random_num)
#    # print('hello world')
 
# B = tkinter.Button(top, text ="点我", command = helloCallBack)
 
# B.pack()
# top.mainloop()

#%%
#pyinstaller tkinter_random.py

from tkinter import *
import tkinter.messagebox as msgbox
import random
import datetime

#import datetime

#df=pd.read_excel(r'C:\Users\davidpopo\Desktop\抽学号\初三名单.xlsx')
#student_dict1=dict(zip(df['序号'],df['班级']))
#student_dict2=dict(zip(df['序号'],df['姓名']))
#print(student_dict1)
#print(student_dict2)

class_dict={1: '初三1班', 2: '初三1班', 3: '初三1班', 4: '初三1班', 5: '初三1班', 6: '初三1班', 7: '初三1班', 8: '初三1班', 9: '初三1班', 10: '初三1班',
            11: '初三1班', 12: '初三1班', 13: '初三1班', 14: '初三1班', 15: '初三1班', 16: '初三1班', 17: '初三1班', 18: '初三1班', 19: '初三1班', 
            20: '初三1班', 21: '初三1班', 22: '初三1班', 23: '初三1班', 24: '初三1班', 25: '初三1班', 26: '初三1班', 27: '初三1班', 28: '初三1班', 29: '初三1班', 
            30: '初三1班', 31: '初三1班', 32: '初三1班', 33: '初三1班', 34: '初三1班', 35: '初三1班', 36: '初三1班', 37: '初三1班', 38: '初三1班', 39: '初三1班', 
            40: '初三1班', 41: '初三2班', 42: '初三2班', 43: '初三2班', 44: '初三2班', 45: '初三2班', 46: '初三2班', 47: '初三2班', 48: '初三2班', 49: '初三2班', 
            50: '初三2班', 51: '初三2班', 52: '初三2班', 53: '初三2班', 54: '初三2班', 55: '初三2班', 56: '初三2班', 57: '初三2班', 58: '初三2班', 59: '初三2班', 
            60: '初三2班', 61: '初三2班', 62: '初三2班', 63: '初三2班', 64: '初三2班', 65: '初三2班', 66: '初三2班', 67: '初三2班', 68: '初三2班', 69: '初三2班', 
            70: '初三2班', 71: '初三2班', 72: '初三2班', 73: '初三2班', 74: '初三2班', 75: '初三2班', 76: '初三2班', 77: '初三2班', 78: '初三2班', 79: '初三2班', 
            80: '初三3班', 81: '初三3班', 82: '初三3班', 83: '初三3班', 84: '初三3班', 85: '初三3班', 86: '初三3班', 87: '初三3班', 88: '初三3班', 89: '初三3班', 
            90: '初三3班', 91: '初三3班', 92: '初三3班', 93: '初三3班', 94: '初三3班', 95: '初三3班', 96: '初三3班', 97: '初三3班', 98: '初三3班', 99: '初三3班', 
            100: '初三3班', 101: '初三3班', 102: '初三3班', 103: '初三3班', 104: '初三3班', 105: '初三3班', 106: '初三3班', 107: '初三3班', 108: '初三3班', 109: '初三3班',
            110: '初三3班', 111: '初三3班', 112: '初三3班', 113: '初三3班', 114: '初三3班', 115: '初三3班', 116: '初三3班', 117: '初三3班', 118: '初三3班', 119: '初三4班',
            120: '初三4班', 121: '初三4班', 122: '初三4班', 123: '初三4班', 124: '初三4班', 125: '初三4班', 126: '初三4班', 127: '初三4班', 128: '初三4班', 129: '初三4班',
            130: '初三4班', 131: '初三4班', 132: '初三4班', 133: '初三4班', 134: '初三4班', 135: '初三4班', 136: '初三4班', 137: '初三4班', 138: '初三4班', 139: '初三4班',
            140: '初三4班', 141: '初三4班', 142: '初三4班', 143: '初三4班', 144: '初三4班', 145: '初三4班', 146: '初三4班', 147: '初三4班', 148: '初三4班', 149: '初三4班',
            150: '初三4班', 151: '初三4班', 152: '初三4班', 153: '初三4班', 154: '初三4班', 155: '初三4班', 156: '初三4班', 157: '初三4班', 158: '初三4班', 159: '初三5班',
            160: '初三5班', 161: '初三5班', 162: '初三5班', 163: '初三5班', 164: '初三5班', 165: '初三5班', 166: '初三5班', 167: '初三5班', 168: '初三5班', 169: '初三5班',
            170: '初三5班', 171: '初三5班', 172: '初三5班', 173: '初三5班', 174: '初三5班', 175: '初三5班', 176: '初三5班', 177: '初三5班', 178: '初三5班', 179: '初三5班',
            180: '初三5班', 181: '初三5班', 182: '初三5班', 183: '初三5班', 184: '初三5班', 185: '初三5班', 186: '初三5班', 187: '初三5班', 188: '初三5班', 189: '初三5班',
            190: '初三5班', 191: '初三5班', 192: '初三5班', 193: '初三5班', 194: '初三5班', 195: '初三5班', 196: '初三5班', 197: '初三5班', 198: '初三6班', 199: '初三6班',
            200: '初三6班', 201: '初三6班', 202: '初三6班', 203: '初三6班', 204: '初三6班', 205: '初三6班', 206: '初三6班', 207: '初三6班', 208: '初三6班', 209: '初三6班', 
            210: '初三6班', 211: '初三6班', 212: '初三6班', 213: '初三6班', 214: '初三6班', 215: '初三6班', 216: '初三6班', 217: '初三6班', 218: '初三6班', 219: '初三6班',
            220: '初三6班', 221: '初三6班', 222: '初三6班', 223: '初三6班', 224: '初三6班', 225: '初三6班', 226: '初三6班', 227: '初三6班', 228: '初三6班', 229: '初三6班',
            230: '初三6班', 231: '初三6班', 232: '初三6班', 233: '初三6班', 234: '初三6班', 235: '初三6班', 236: '初三6班', 237: '初三6班', 238: '初三6班', 239: '初三6班'}

student_name_dict={1: '方雯', 2: '顾笑宸', 3: '郭毓', 4: '胡雯菡', 5: '贾诗琪', 6: '刘婧一', 7: '刘芃阳', 8: '刘欣妍', 9: '罗悉语', 
                   10: '苗沛青', 11: '施寓晨', 12: '王潇祺', 13: '夏玉新子', 14: '张欣妍', 15: '郑羽婕', 16: '周书悦', 17: '曾霖', 18: '储宬恺', 19: '崔宇涵', 
                   20: '高嘉祺', 21: '侯沈言', 22: '黄启元', 23: '晋浩嘉', 24: '孔维亮', 25: '雷靖祁', 26: '李孚', 27: '李若拙', 28: '林子轩', 29: '马舸岭', 
                   30: '彭若轩', 31: '沈彦炜', 32: '孙沂哲', 33: '汤成东', 34: '吴宇杰', 35: '许越', 36: '许梓杰', 37: '杨启轩', 38: '张子轩', 39: '赵容谦', 
                   40: '朱子俞', 41: '白旻杨', 42: '蔡馨仪', 43: '顾馨悦', 44: '郝博雅', 45: '李弘京', 46: '李琪', 47: '李未', 48: '凌祺云', 49: '刘霈然', 
                   50: '鲁承誉', 51: '陆怡雯', 52: '田晨', 53: '王怡懿', 54: '徐丽婕', 55: '徐易辰', 56: '周楚涵', 57: '陈崔康', 58: '陈佳栋', 59: '陈子昂', 
                   60: '冯幸海', 61: '顾明睿', 62: '何威仪', 63: '李宣震', 64: '刘惠阳', 65: '陆思翰', 66: '毛一璠', 67: '牛榆钦', 68: '石桓光', 69: '宋一哲', 
                   70: '屠延堃', 71: '王语飏', 72: '吴何铭', 73: '夏仲铭', 74: '肖金韬', 75: '姚孜颢', 76: '尹豪健', 77: '张泽越', 78: '周靖衍', 79: '朱喻辰', 
                   80: '蔡昀熹', 81: '曹家仪', 82: '陈彦妃', 83: '樊海欧', 84: '李婧', 85: '李子悦', 86: '刘楚珺', 87: '刘家鋆', 88: '齐煜', 89: '宋怿文', 
                   90: '王依馨', 91: '严逸凡', 92: '殷致慧', 93: '张乐涵', 94: '赵涤玄', 95: '陈星霖', 96: '陈许乐', 97: '褚嘉祺', 98: '戴博闻', 99: '葛丰源', 
                   100: '李嘉斌', 101: '刘永乐', 102: '秦愉尧', 103: '施仁浩', 104: '陶逸远', 105: '王苏阳', 106: '韦尹寒', 107: '黄子鱼', 108: '吴云天', 109: '徐岑杰', 
                   110: '许沐安', 111: '杨轩岳', 112: '姚尚余', 113: '张熙文', 114: '张哲铭', 115: '赵子君', 116: '朱艺文', 117: '李陆瑶', 118: '沈飞扬', 119: '崔芸菲', 
                   120: '胡笑涵', 121: '李菁文', 122: '罗兰昕', 123: '任洁', 124: '孙可心', 125: '陶一诺', 126: '王诗妤', 127: '王亭絮', 128: '王依辰', 129: '吴伊朵', 
                   130: '杨昕冉', 131: '赵昱洁', 132: '赵泽群', 133: '郑芊芊', 134: '朱格嘉', 135: '陈泓奕', 136: '陈加恩', 137: '陈沛晟', 138: '陈书玮', 139: '胡放', 
                   140: '黄俊豪', 141: '梁正航', 142: '林宇哲', 143: '刘奕彤', 144: '刘昱辰', 145: '唐同舟', 146: '王宬劼', 147: '王维实', 148: '王一凡', 149: '鲜宇洋', 
                   150: '徐佳宁', 151: '徐睿阳', 152: '徐羽辰', 153: '姚陈成', 154: '叶铭玮', 155: '岳逸飞', 156: '张煜晨', 157: '周子昂', 158: '朱家懿', 159: '陈乐萱', 
                   160: '董楚越', 161: '付翊霖', 162: '郭嘉明', 163: '刘洋', 164: '倪佳悦', 165: '浦语曈', 166: '施王依', 167: '施想', 168: '苏文卿', 169: '许佳欣', 
                   170: '张竞予', 171: '张莜然', 172: '曾楷文', 173: '陈禹悦', 174: '丁旻颢', 175: '杜庆安', 176: '冯奕玮', 177: '高新语', 178: '季晨悦', 179: '李奕成', 
                   180: '刘亦宁', 181: '陆奕辰', 182: '罗志阳', 183: '马凯楷', 184: '谯致洋', 185: '万宇辰', 186: '汪思逸', 187: '魏子涵', 188: '邢家齐', 189: '徐晟垚', 
                   190: '许翔', 191: '颜圣涛', 192: '叶芃辰', 193: '俞越', 194: '庾昊晨', 195: '张思皓', 196: '张轩豪', 197: '赵仕杰', 198: '蔡欣妍', 199: '董思羽', 
                   200: '高湘宜', 201: '黄琳睿', 202: '李佩含', 203: '孙浩然', 204: '孙懿辰', 205: '吴君天', 206: '张睿妍', 207: '张熹微', 208: '钟鸣', 209: '周晨希', 
                   210: '陈思远', 211: '陈羿', 212: '陈懿迪', 213: '单徐谦', 214: '丁睿满', 215: '封景濠', 216: '冯钰阳', 217: '付啸', 218: '郭斯涵', 219: '侯雅杰', 
                   220: '姜顾旻', 221: '金浩贤', 222: '毛乐毅', 223: '孟钰轩', 224: '苗伦玮', 225: '秦米', 226: '桑翊玮', 227: '邵一航', 228: '沈思贤', 229: '束睿哲', 
                   230: '孙义潼', 231: '卫胤杰', 232: '徐一哲', 233: '杨之涵', 234: '喻潇远', 235: '袁清栩', 236: '张宸一', 237: '张峻鸣', 238: '朱加力', 239: '刘世灏'}


class_info=[(1,'初三1班'),(2,'初三2班'),(3,'初三3班'),(4,'初三4班'),(5,'初三5班'),(6,'初三6班'),(7,'所有班级')]

root = Tk()
root.title("tool for lottery")
root.geometry('300x220')

curdate=datetime.datetime.now().strftime('%Y-%m-%d')
date_text='今日日期:'+curdate
lb1 = Label(root,text=date_text,font=("黑体",10))
lb1.pack()
# lb1.place(x=0,y=360)

v = IntVar()   #1班
   
for each_id,each_class in class_info:
    choice=Radiobutton(root, text=each_class, variable=v,value=each_id,font=("微软雅黑",8))
    choice.pack(anchor="w")
    # choice.place(x=0)

v.set(7)
lb = Label(root,text='随机抽答',fg='blue',font=("黑体",19))
# lb.grid(row = 0, column=1)
# lb.pack()
lb.place(x=120,y=25)

# lb.pack()
text = Text(root,width=30,height = 3)
  

print(v.get())

def helloCallBack():
    if v.get() == 1:
        num_min=1
        num_max=40
    if v.get() == 2:
        num_min=41
        num_max=79
    if v.get() == 3:
        num_min=80
        num_max=118
    if v.get() == 4:
        num_min=119
        num_max=158
    if v.get() == 5:
        num_min=159
        num_max=197
    if v.get() == 6:
        num_min=198
        num_max=239
    if v.get() == 7:
        num_min=1
        num_max=239
    random_num=random.randint(num_min,num_max)
#    msgbox.showinfo( '抽取结果',"""    班级：%s\n    姓名：%s\n    恭喜你被抽中了！"""%(class_dict[random_num],student_name_dict[random_num]))  
    text.delete(1.0, END)
    text.insert(END,"""      班级：%s\n      姓名：%s\n     恭喜你被抽中了！"""%(
        class_dict[random_num],student_name_dict[random_num]))


B = Button(root, text ="start!", command = helloCallBack,font=("微软雅黑",16),bg='#D2E9FF',width=7)  
text = Text(root,width=18,height = 3,font=("微软雅黑",10))
# text.pack()     
text.place(x=97,y=65)
# B.pack()
B.place(x=120,y=140)         

root.mainloop()


#%%
#cd D:\lottery

