# 这是一个转换字符的程序
# 作者：　'wangshijiang'

def shift(inputzifu):
    a = []
    a.append(inputzifu)
    changdu = len(inputzifu)
    print(f"数据长度为：　{changdu}")
    print(f"原始数据为: {a[0]}")
def allshift(inputzifu=None):
    if inputzifu == 'ac':
        print(f"转换为全大写后的数据为：　{inputzifu.upper()}")
    elif inputzifu == 'al':
        print(f"转换为全小写后的数据为：　{inputzifu.lower()}")
    elif inputzifu == 'fc':
        print(f"首字母大写后的数据为：　{inputzifu.title()}")
def helpinfo(helpinfo):
    message1 = '帮助信息\n\thelp/h\t\t显示帮助信息\n\tquit\t\t退出程序\n\tac\t\t\t全部大写'
    message2 = '\tal\t\t\t全部小写\n\tfc\t\t\t每个字段首字母大写'
    print(message1)
    print(message2)
def quit_stop(stop):
    print("感谢您的使用，再见!!!")
    exit(1)


print("欢迎来到这里！")
print("我很高兴各位的使用!!!")
print("开发者：　'wangshijiang'\t\t\t\tGitHub: https://github.com/iwqculrbud/wangshijiang-python.git\t\t\t\tQQ: ")
print("输入help查看帮助，输入quit退出本程序。")
while True:
    while True:
        inputzifu = input("请输入您需要转换的字符：　")
        if inputzifu == 'help':
            helpinfo(helpinfo)
        elif inputzifu == 'quit':
            quit_stop('stop')
        else:
            break
    while True:
        zhiwangtai = input("请输入执行方法：　")
        if zhiwangtai == 'quit':
            quit_stop('stop')
        elif zhiwangtai == 'help':
            helpinfo(helpinfo)
        elif zhiwangtai == 'ac':
            allshift('ac')
            shift(inputzifu)
            break
        elif zhiwangtai == 'al':
            allshift('al')
            shift(inputzifu)
            break
        elif zhiwangtai == 'fc':
            allshift('fc')
            shift(inputzifu)
            break
        else:
            print(f"您输入的方法{zhiwangtai}错误，请再次输入。（输入help查看帮助）")
    print("请问您还要继续吗？（y/n）")
    user_decide = input("请输入您的决定：　")
    if user_decide.lower() == 'y':
        break
    elif user_decide.lower() == 'n':
        quit_stop('stop')
    else:
        print(f"您输入的决定{user_decide.lower()}不合规，只有y/n(不分大小写)。")