import math
import matplotlib.pyplot as plt

# 第一次
# data_xy = [
#     [0.391573592834236,-0.555567842530134],
#     [0.305246947530525,-0.184248157518425],
#     [0.513556258472662,-0.400022593764121],
#     [0.420740063956144,-0.196779351301964],
#     [0.442690758680745,-0.218787417002286],
#     [0.461121940654104,-0.51819363222872],
#     [0.438470995864536,-0.187101821839723],
#     [0.218101822752986,-0.157919547454431],
#     [0.206497046796911,-0.130508859609269],
#     [0.317191011235955,-0.204269662921348],
#     [0.413107678328033,-0.255452067242163],
#     [0.437867148666968,-0.189222774514234],
#     [0.467401181281236,-0.298955020445252]
# ]


#第二次
data_xy = [
    [0.43793742280774,-0.649650061753808],
    [0.363028720626632,-0.192584856396867],
    [0.576677645121449,-0.445244956772334],
    [0.522361359570662,-0.216457960644007],
    [0.510962429233145,-0.197014925373134],
    [0.543522680833674,-0.623212096444626],
    [0.507305609481966,-0.181158679881475],
    [0.199900464499005,-0.129396151293962],
    [0.21806424255274,-0.120322272871833],
    [0.338274932614555,-0.191167323242795],
    [0.455883877656817,-0.257335406946604],
    [0.514724180837827,-0.20582745748652],
    [0.529393468118196,-0.338206324520477],
]

labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]

# 第三步：绘制散点图
# 3.1绘制样本为true的散点图
# 创建散点图
fig, ax = plt.subplots(figsize=(10, 10))
for i in range(len(data_xy)):
    ax.scatter(data_xy[i][0],data_xy[i][1],marker="o", label=labels[i])
ax.legend(["A-卫生情况","B-品牌知名度","C-公布用料信息","D-品类多样性","E-装修风格","F-服务","G-包装","H-过量糖分","I-营销活动","J-新品推出","K-价格","L-优惠活动","M-线上体验"],loc="lower right")

# 把x轴移到上方
ax.xaxis.tick_top()
# 设置x轴标签并将其置顶
ax.set_xlabel('满意影响程度(SI)', rotation=0, horizontalalignment='center',fontweight='bold',fontsize=16)
# 获取x轴的刻度位置
xticks = ax.get_xticks()
# 获取x轴的标签的位置
xlabel_position = (xticks[-1] - xticks[0]) / 2 + min(xticks)
# 设置x轴标签的位置
ax.xaxis.set_label_coords(xlabel_position+0.15, 1.1)
# 比例相等，正方形
ax.set_aspect('equal')

# 为每个点添加标签
for i in range(len(data_xy)):
    ax.annotate(labels[i], (data_xy[i][0],data_xy[i][1]),xytext=(data_xy[i][0]-0.006, data_xy[i][1]+0.01),fontsize=12, color='black', fontweight='bold')

# 设置标题，并移到下方
plt.title('KANO模型分析结果', fontweight='bold',y=-0.1,fontsize=26)
# 正常设置Y轴标题
plt.ylabel('不满意影响程度(DSI)',fontweight='bold',fontsize=16)

# 设置半圆
# 参数设置
x = 0  # 圆心的x轴坐标
y = 0  # 圆心的y轴坐标
r = math.sqrt(0.5*0.5*2)  # 圆的半径


circle = plt.Circle((x, y), r, color='lightgray', fill=False)
plt.gcf().gca().add_artist(circle)

# 添加水平1/2参考线
plt.axhline(y=-0.5, color='black', linestyle='-')
# 添加垂直1/2参考线
plt.axvline(x=0.5, color='black', linestyle='-')

from pylab import mpl
# 设置中文显示字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False


# 横纵轴最大值
plt.xlim(0,1)
plt.xticks([0, 0.5,1], ['0', '0.5', '1'])
plt.ylim(-1,0)
plt.yticks([0, -0.5,-1], ['0', '-0.5', '-1'])

# 展示图形
plt.show()
# 保存整个图形布局到PNG文件
# fig.savefig('second.png', bbox_inches='tight', dpi=300)

# 关闭图形，释放资源
plt.close(fig)
