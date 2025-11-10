import math
import object_data as ojd

def move_monster():
    # หาค่าต่างระหว่างตำแหน่งของผู้เล่นกับมอนสเตอร์
    dx = ojd.test_rect.x - ojd.test_rect2.x
    dy = ojd.test_rect.y - ojd.test_rect2.y
    distance = math.hypot(dx, dy)

    # ถ้ามีระยะห่างมากกว่า 40 ให้มอนสเตอร์เคลื่อนเข้าใกล้
    if distance >= 40:
        dx, dy = dx / distance, dy / distance  # ทำให้เป็นทิศทางหน่วย (normalize)
        ojd.test_rect2.x += dx * ojd.monster_speed
        ojd.test_rect2.y += dy * ojd.monster_speed
