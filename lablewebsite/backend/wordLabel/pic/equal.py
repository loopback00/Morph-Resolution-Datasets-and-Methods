import matplotlib.pyplot as plt

labels = ['Jingdong', 'Kuashou', 'Douyin']
percentages = [3535, 8326, 16169]

# 颜色数应和数据长度一致
colors = ['#dce3ec', '#aeb9c9', '#6a839b']

fig, ax = plt.subplots(figsize=(6, 6), dpi=100)

# ✅ 控制饼图固定位置和大小（left, bottom, width, height）
ax.set_position([0.05, 0.1, 0.65, 0.8])  # 可调整这组参数试效果

# 饼图绘制
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    autopct='%d%%',
    wedgeprops={'edgecolor': 'lightsteelblue'},
    textprops={'fontsize': 18, 'color': 'black'}
)

# 图例始终右侧对齐
ax.legend(
    labels,
    loc='center left',
    bbox_to_anchor=(1.0, 0.5),
    frameon=False,
    fontsize=10
)

ax.axis('equal')
ax.axis('off')

# ✅ 你可以添加一个统一的底部标签（如果需要）
fig.text(0.5, 0.03, '', ha='center', va='center', fontsize=16)

# ❌ 不再使用 tight_layout（会破坏你设定的尺寸）
# plt.tight_layout()  # ← 删掉它！

plt.show()
