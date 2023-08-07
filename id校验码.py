# 作者: wangshijiang   GitHub: https://github.com/iwqculrbud/wangshijiang-python.git
while True:
    def id_jisuan(id):
        s = []
        number_list2 = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
        number_list1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        a = 0

        for numbers in number_list1:
            c = id[a]
            b = int(c) * int(numbers)
            s.append(b)
            a += 1

        sm = sum(s)
        z = sm % 11
        zv = str(id) + str(number_list2[z])
        print("over")
        return zv



    command = input("请输入指令,使用help查看帮助: ")
    message1 = 'command\n\n\thelp\t\t查看帮助\n\ts\t\t\t计算身份证校验码\n\tc\t\t\t检查身份证是否合法\n'
    message2 = '\tquit\t\t退出\n作者: wangshijiang\t\t\tGitHub: https://github.com/iwqculrbud/wangshijiang-python.git'


    if command.lower() == 'help':
        print(message1 + message2)

    if command.lower() == 's':
        id = input("输入前17位身份证号: ")
        if len(id) != 17:
            id = input("不合法请再次输入(17): ")
        zv = id_jisuan(id)
        z = zv[17]
        print(f"您的身份证为 {zv} , 校验码为{z}")

    if command.lower() == 'c':
        id_18 = input("请输入18位身份证号: ")
        if len(id_18) == 18:
            zv = id_jisuan(id=id_18)
        else:
            id_18 = input("输入不是18位，请再次输入: ")
        zvs = zv[0:18]
        if zvs == id_18:
            print(f"就校验码看ID {zvs} 是合法的!!")
        else:
            print(f"就校验码看ID {zvs}不合法!!!")

    if command.lower() == 'quit':
        break

















