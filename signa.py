#coding:utf-8
import itchat
import re
from wordcloud import WordCloud
itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]
signature_list = []
for friend in friends:
    signature = friend["Signature"].strip()
    signature = re.sub("<span.*>", "", signature)
    print signature
    signature_list.append(signature)
with open('sig.txt','w') as f:
    for s in signature_list:
        if s == '':
            pass
        else:
            f.write(s.encode('utf-8'))
            f.write('\n')
content = ""
for s in signature_list:
    content = content +" "+s
cut_text = " ".join(jieba.cut(content))
cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="simhei.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
#         mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=40
    )
word_cloud = cloud.generate(cut_text) # 产生词云
word_cloud.to_file("save.jpg") #保存图片
# male = female = other = 0
# #friends[0]是自己的信息，所以要从friends[1]开始
# for i in friends[1:]:
#     sex = i["Sex"]
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other +=1
# #计算朋友总数
# total = len(friends[1:])
# #打印出自己的好友性别比例
# print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
# "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
# "不明性别好友： %.2f%%" % (float(other) / total * 100))
