#!/usr/bin/env python3
"""
🎮 Cocos2dx Game Reverse Engineer - Easter Egg Fun Script 🎮

Một trò chơi nhỏ để chào mừng bạn đến với repo!
"""

import math
import time

SECRET = 602660

BANNER = r"""
  ____                                ____                     
 / ___| __ _ _ __ ___   ___          | __ ) _   _ ___| |_ ___ _ __ 
| |  _ / _` | '_ ` _ \ / _ \  _____ |  _ \| | | / __| __/ _ \ '__|
| |_| | (_| | | | | | |  __/ |_____|| |_) | |_| \__ \ ||  __/ |   
 \____|\__,_|_| |_| |_|\___|        |____/ \__,_|___/\__\___|_|   
                                                                    
   🕵️  Cocos2dx Game Reverse Engineer  🕵️
"""


def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def guessing_game():
    print("\n🎯 MINI GAME: Đoán số bí mật!")
    print("=" * 40)
    print(f"Con số nằm trong khoảng 1 đến {SECRET}")
    print(f"Bạn có 7 lần đoán. Chúc may mắn! 🍀\n")

    secret = random.randint(1, SECRET)
    attempts = 7

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Lần {attempt}/{attempts} - Nhập số của bạn: "))
        except (ValueError, EOFError):
            print("❌ Vui lòng nhập một số hợp lệ!")
            continue

        if guess == secret:
            print(f"\n🎉🎉🎉 CHÍNH XÁC! Bạn đã đoán đúng sau {attempt} lần!")
            print(f"Con số bí mật là: {secret}")
            print("Bạn xứng đáng được ghi tên vào Hall of Fame! 🏆")
            return
        elif guess < secret:
            print(f"📈 Quá nhỏ! Thử số lớn hơn.")
        else:
            print(f"📉 Quá lớn! Thử số nhỏ hơn.")

        remaining = attempts - attempt
        if remaining > 0:
            print(f"   Còn {remaining} lần đoán...\n")

    print(f"\n😢 Hết lượt rồi! Con số bí mật là: {secret}")
    print("Đừng nản lòng, hãy thử lại! 💪")


def decode_mystery():
    print("\n🔍 GIẢI MÃ BÍ ẨN: File '602660'")
    print("=" * 40)
    content = "602660602660602660602660602660"
    print(f"Nội dung file: {content}")
    print_slow("\nĐang phân tích...", delay=0.05)
    time.sleep(0.5)

    chunk = "602660"
    count = content.count(chunk)
    print(f"\n✅ Phát hiện: '{chunk}' lặp lại {count} lần!")
    print(f"✅ Tổng số chữ số: {len(content)}")
    print(f"✅ Tổng giá trị số: {int(content):,}")
    print(f"✅ Căn bậc hai: {math.sqrt(int(content)):,.2f}")
    print("\n🤔 Ý nghĩa thực sự? Chỉ có tác giả mới biết... hoặc là bạn! 😏")


def ascii_art_game():
    frames = [
        r"""
    🎮
   /||\
  / || \
    ||
   /  \
  """,
        r"""
     🎮
    /||\
   / || \
     ||
    /  \
  """,
    ]
    print("\n🕹️ LOADING GAME...")
    for _ in range(3):
        for frame in frames:
            print(frame)
            time.sleep(0.3)
            print("\033[8A", end="")
    print("\n\n\n\n\n\n\n\n")
    print("✅ Game loaded! (Giả vờ thôi 😄)")


def main():
    print(BANNER)
    time.sleep(0.5)

    print_slow("Chào mừng đến với Cocos2dx Game Reverse Engineer! 🎮", delay=0.04)
    print_slow("Nơi mọi bí mật của game đều bị phơi bày... 😈\n", delay=0.04)

    while True:
        print("\n📋 MENU:")
        print("  1. 🎯 Chơi mini game đoán số")
        print("  2. 🔍 Giải mã file bí ẩn '602660'")
        print("  3. 🕹️  Xem loading animation")
        print("  4. 👋 Thoát")

        try:
            choice = input("\nChọn (1-4): ").strip()
        except EOFError:
            choice = "4"

        if choice == "1":
            guessing_game()
        elif choice == "2":
            decode_mystery()
        elif choice == "3":
            ascii_art_game()
        elif choice == "4":
            print_slow("\nTạm biệt! Hẹn gặp lại ở Hall of Fame! 🏅\n", delay=0.04)
            break
        else:
            print("❓ Lựa chọn không hợp lệ, thử lại nhé!")


if __name__ == "__main__":
    main()
