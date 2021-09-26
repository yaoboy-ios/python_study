import os

from user_manager import initialize_data, return_menu, user_login, user_add, user_disable, user_all
from book_manager import book_add, book_all, book_search, book_del

path = './data.json'
if os.access(path, os.F_OK):
    # 文件存在则读取文件内容
    pass
else:
    # 文件不存在则创建
    file = open(path, 'w')
    file.write(initialize_data())
    file.close()


print('*' * 50)
print('欢迎使用小妖图书管理系统'.center(50))
print('*' * 50)


def _quit():
    print('再见,欢迎再次使用本系统')
    exit()


while True:
    user_name = input('请输入账号：')
    user_pwd = input('请输入密码：')
    result = user_login(user_name, user_pwd)
    if type(result) == str:
        print(result)
    else:
        # 登录成功,并返回登录者信息
        level = str(result['level'])
        menu = return_menu().get(level)
        if result['level'] == 0:
            print('超级管理员登录成功')
        elif result['level'] == 1:
            print('图书管理员登录成功')
        elif result['level'] == 2:
            print('用户管理员登录成功')
        else:
            print('%s 登录成功' % user_name)
        while True:
            print('功能列表'.center(48, '-'))
            print(menu)
            print('-' * 50)
            options = input('请选择需要执行操作的序号码：')
            # 生成对应登录账号返回菜单项的数目列表，并将数字数组转为字符数组
            if options in map(str, list(range(1, 1+len(menu.split('\n'))))):
                if options == '1':
                    if result['level'] == 0:
                        # 添加图书管理员
                        user_add(1)
                    elif result['level'] == 1:
                        # 添加图书
                        book_add()
                    elif result['level'] == 2:
                        # 添加普通用户
                        user_add(3)
                    elif result['level'] == 3:
                        # 查看图书列表
                        book_all()
                    pass
                elif options == '2':
                    if result['level'] == 0:
                        # 添加用户管理员
                        user_add(2)
                    elif result['level'] == 1:
                        # 删除图书
                        book_del()
                    elif result['level'] == 2:
                        # 用户禁用
                        user_disable()
                    elif result['level'] == 3:
                        # 搜索图书
                        book_search()
                    pass
                elif options == '3':
                    if result['level'] == 0:
                        # 账号禁用
                        user_disable()
                    elif result['level'] == 1:
                        # 查看图书列表
                        book_all()
                    elif result['level'] == 2:
                        # 用户列表
                        user_all(2)
                    elif result['level'] == 3:
                        # 切换账号
                        break
                    pass
                elif options == '4':
                    if result['level'] == 0:
                        # 用户列表
                        user_all(0)
                    elif result['level'] == 1:
                        # 搜索图书
                        book_search()
                    elif result['level'] == 2:
                        # 切换账号
                        break
                    elif result['level'] == 3:
                        # 退出系统
                        _quit()
                    pass
                elif options == '5':
                    if result['level'] == 0:
                        # 查看图书列表
                        book_all()
                    elif result['level'] == 1:
                        # 切换账号
                        break
                    elif result['level'] == 2:
                        # 退出系统
                        _quit()
                    pass
                elif options == '6':
                    if result['level'] == 1:
                        # 退出系统
                        _quit()
                    else:
                        # 切换账号
                        break
                elif options == '7':
                    # 退出系统
                    _quit()
                else:
                    pass
            else:
                print('输入错误，请重新输入')
