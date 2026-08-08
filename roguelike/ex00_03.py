class QuitEvent:
    pass

class KeyEvent:
    def __init__(self, key):
        self.key = key

events = [
    KeyEvent("w"),
    KeyEvent("a"),
    QuitEvent(),
    KeyEvent("s")
]

def main():
    for event in events:
        if isinstance(event, QuitEvent):
            print("終了イベントを検知")
            break
        elif isinstance(event, KeyEvent):
            print(f"キー入力： {event.key}")

main()        