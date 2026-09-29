def start(start="", goal=""):
    # start と goal が空なら無限ループ
    if start == "" or goal == "":
        i = 0
        while True:
            i += 1
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        return

    # 数字以外が入力された場合のエラーハンドリング
    try:
        start = int(start)
        goal = int(goal)
    except ValueError:
        return # 処理を中断して関数を抜ける

    # エラーなく数値に変換できた場合のみ、以下のループ処理が実行される
    for i in range(start, goal + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
def check(ch):
        if ch % 15 == 0:
            return("FizzBuzz")
        elif ch % 3 == 0:
            return("Fizz")
        elif ch % 5 == 0:
            return("Buzz")
        else:
            return ch