import tkinter as tk
import random
import time
import threading

# 温暖的便签内容列表
warm_messages = [
    "今天也要好好爱自己 ❤️",
    "你值得所有的美好和幸福",
    "每一天都是新的开始",
    "保持微笑，世界会因你而更美",
    "小小的进步也是值得庆祝的",
    "你是独一无二的存在",
    "对自己温柔一些",
    "相信一切都会越来越好",
    "你的存在本身就是一种美好",
    "给自己一个温暖的拥抱",
    "今天也要好好照顾自己",
    "你比想象中更坚强",
    "感恩生命中的小确幸",
    "一切困难都会过去",
    "你是被爱着的",
    "保持内心的平静与喜悦",
    "每一天都充满新的希望",
    "你正在成为更好的自己",
    "对自己说声辛苦了",
    "阳光总在风雨后",
    "你是这个世界的光",
    "相信自己的直觉",
    "给自己一点休息的时间",
    "你的笑容是最美的风景",
    "一切都会如你所愿",
    "你拥有改变一切的力量",
    "今天也要开心哦",
    "你是如此珍贵",
    "保持对生活的热爱",
    "你的努力终将开花结果",
    "温柔对待自己和他人",
    "每一天都是礼物",
    "你值得被温柔以待",
    "保持内心的光芒",
    "相信美好的事情即将发生",
    "你是生命的奇迹",
    "对自己好一点",
    "一切都会是最好的安排",
    "你的心知道答案",
    "活在当下，享受此刻",
    "你是足够好的",
    "保持对世界的好奇",
    "你的存在让世界更美好",
    "相信爱的力量",
    "你是勇敢的",
    "今天也要充满感恩",
    "一切都会顺利的",
    "你是生命的艺术家",
    "保持心灵的开放",
    "你的旅程是独特的",
    "相信自己的价值",
    "你是美丽的",
    "今天也要保持希望",
    "一切都会变得简单",
    "你是自由的",
    "保持内心的平和",
    "你的梦想值得追求",
    "相信生命的过程",
    "你是完整的",
    "今天也要充满能量"
]

# 温暖色调的颜色列表
warm_colors = [
    "#FFF0F5", "#FFE4E1", "#FFEFD5", "#FFFACD", "#F0FFF0",  # 柔和的粉色、橙色、黄色、绿色
    "#F0F8FF", "#E6E6FA", "#FFF8DC", "#FFEBCD", "#FFDAB9",
    "#FFDEAD", "#FFEFDB", "#FFF5EE", "#FDF5E6", "#FAFAD2",
    "#F5F5DC", "#F0FFFF", "#F5FFFA", "#FFFAF0", "#FFFFF0",
    "#E0FFFF", "#E0FFE0", "#FFE0E0", "#FFFFE0", "#E6F3FF"
]


class WarmNotePopup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口

        self.popup_active = True
        self.used_messages = set()  # 记录已使用的消息
        self.available_messages = warm_messages.copy()  # 可用消息列表

        # 创建30秒后停止的线程
        stop_thread = threading.Thread(target=self.stop_after_30s)
        stop_thread.daemon = True
        stop_thread.start()

        # 开始创建弹窗
        self.create_popups()

        self.root.mainloop()

    def stop_after_30s(self):
        # 运行30秒后停止
        time.sleep(30)
        self.popup_active = False
        self.root.quit()
        self.root.destroy()

    def create_popups(self):
        if not self.popup_active:
            return

        # 创建弹窗
        self.create_popup()

        # 更快的间隔 - 随机间隔后创建下一个弹窗 (0.2-0.8秒)
        delay = random.uniform(0.2, 0.8)
        self.root.after(int(delay * 1000), self.create_popups)

    def create_popup(self):
        if not self.available_messages:
            # 如果所有消息都已使用，重置
            self.available_messages = warm_messages.copy()
            self.used_messages.clear()

        # 随机选择未使用的消息
        message = random.choice(self.available_messages)
        self.available_messages.remove(message)
        self.used_messages.add(message)

        popup = tk.Toplevel()

        # 移除窗口装饰
        popup.overrideredirect(True)

        # 更小的窗口尺寸
        window_width = 120
        window_height = 60

        # 随机设置窗口位置
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        x = random.randint(50, screen_width - window_width - 50)
        y = random.randint(50, screen_height - window_height - 50)
        popup.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 随机选择颜色
        bg_color = random.choice(warm_colors)

        # 创建彩色框体
        frame = tk.Frame(
            popup,
            bg=bg_color,
            width=window_width,
            height=window_height,
            relief="raised",
            borderwidth=2
        )
        frame.pack(fill="both", expand=True)
        frame.pack_propagate(False)  # 防止内容改变框架大小

        # 添加便签内容 - 使用更小的字体
        label = tk.Label(
            frame,
            text=message,
            wraplength=window_width - 20,
            bg=bg_color,
            fg="black",
            font=("微软雅黑", 9),  # 更小的字体
            pady=10
        )
        label.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        # 更短的弹窗显示时间（2-5秒）
        auto_close_time = random.randint(2000, 5000)
        popup.after(auto_close_time, popup.destroy)


if __name__ == "__main__":
    WarmNotePopup()