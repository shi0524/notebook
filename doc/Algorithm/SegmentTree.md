
# 线段树

## AOE刷怪

```
给定两个非负数组x和hp，长度都是N，再给定一个正数range
x有序，x[i]表示i号怪兽在x轴上的位置；hp[i]表示i号怪兽的血量
range表示法师如果站在x位置，用AOE技能打到的范围是：
[x-range,x+range]，被打到的每只怪兽损失1点血量
返回要把所有怪兽血量清空，至少需要释放多少次AOE技能？


思路:
    小贪心：
        每次AOE边缘刚好盖到最左侧
        最左侧为零,向右移动
    范围内加减：
        线段树
讲解:
    大厂刷题班: 第1节 第6题 02:10:00
```