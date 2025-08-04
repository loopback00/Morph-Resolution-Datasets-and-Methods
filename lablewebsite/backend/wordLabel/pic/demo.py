import matplotlib.pyplot as plt

# 数据与标签

labels = [
'baby products','cosmetics','clothing','medical devices',
'alcoholic beverages','food', 'health supplements'

]




percentages = [1224,1849,2275,2791,2834,5879,11189]
#percentages = [3535,8326,16169]
# 自定义颜色：淡灰 → 冷灰 → 深灰 → 蓝灰（模拟图中渐变）
colors = [
    '#dce3ec',  # weapon（浅蓝灰）
    '#cfd6df',  # physical
    '#bcc6d3',  # substances
    '#aeb9c9',  # politics
    '#9eacbf',  # employment
    '#8d9eb3',  # death
    '#7c91a7',  # sexual activity
    '#6a839b'   # body functions
]
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

# Heatmap of F1-Scores for Inter-Annotator Consistency