import json


path = './data.json'

# 初学者，代码中出现的问题欢迎指正
# 初学python，为了更好的掌握python基础的方法函数使用，所以目前使用尽可能少的库进行数据的相关操作
# 此处选择的是使用本地化json文件的形式进行数据的存储与读取
# 后期会再使用sql等数据库的形式重写数据存储方面的操作
# 因为使用的是json文件形式做数据本地化处理所以存在很多便利性问题，后期会替换为sql相关的方法进行调整


def initialize_data():
    # level 0-超级管理员
    #       1-图书管理员
    #       2-用户管理员
    #       3-普通用户
    # status 0-账号正常
    #        9-账号被禁用
    manager = {
        'users': [
            {
                # 初始化超级管理员账号信息
                'user_name': 'admin',
                'user_pwd': 'admin',
                'level': 0,         # 权限等级
                'info': '',         # 账号备注信息
                'status': 0         # 账号状态信息
            }
        ],
        'books': [
        ],
        'book_classify': [
        ]
    }
    # 字典转json
    # print(json.dumps(manager))
    return json.dumps(manager)


def reload_data():
    # 刷新本地的模拟数据文件
    json_data_str = open(path, 'r').read()
    data = json.loads(json_data_str)
    return data


def write_data(json_data):
    # 写入数据至本地json文件中保存
    file = open(path, 'w')
    file.write(json.dumps(json_data))
    file.close()


def return_menu():
    # 返回当前登录账号相关的菜单信息
    return {
        '0': "1、添加图书管理员\n2、添加用户管理员\n3、账号禁用\n4、查看所有用户列表\n5、查看图书列表\n6、切换账号\n7、退出系统",
        '1': "1、添加图书\n2、删除图书\n3、查看图书列表\n4、搜索图书\n5、切换账号\n6、退出系统",
        '2': "1、添加用户\n2、用户封禁\n3、用户列表\n4、切换账号\n5、退出系统",
        '3': "1、查看图书列表\n2、搜索图书\n3、切换账号\n4、退出系统"
    }


def user_login(user_name, user_pwd):
    # 账号登录
    data = reload_data()
    user_list = data['users']
    for user in user_list:
        if user_name == user['user_name'] and user_pwd == user['user_pwd']:
            # 账号存在,登录成功,并返回账号信息
            if user['status'] == 9:
                return '账号已被禁用,请联系管理员'
            else:
                return user
    return '账号不存在或账号密码错误,请重试！'


def user_add(level):
    # 添加权限账号，包括图书管理员、用户管理员、普通用户
    # 读取本地json文件内容然后进行数据格式转换
    print('功能：添加用户'.center(50, '-'))
    data = reload_data()
    user_list = data['users']
    user_name = input('请输入要添加的账号用户名:')
    user_pwd = input('请输入要添加的账号密码:')
    for user in user_list:
        if user_name == user['user_name']:
            print('该账号已存在,请重新输入!')
            input('按enter键继续')
            return
    user_list.append({
        'user_name': user_name,
        'user_pwd': user_pwd,
        'level': level,
        'info': '',
        'status': 0
    })
    data['users'] = user_list
    write_data(data)
    print('账号添加成功')
    input('按enter键继续')


def user_disable():
    # 账号禁用
    print('功能：账号禁用'.center(50, '-'))
    data = reload_data()
    user_list = data['users']
    user_name = input('请输入要禁用的账号用户名:')
    for user in user_list:
        if user_name == user['user_name']:
            info = input('请简单描述禁用的原因:')
            user_tem = user
            user_tem['status'] = 9
            user_tem['info'] = info
            item_index = user_list.index(user)
            user_list[item_index] = user_tem
            data['users'] = user_list
            write_data(data)
            print('操作成功,%s 已被禁用' % user_name)
            input('按enter键继续')
            return
    print('账号不存在,请检查后重新输入!')
    input('按enter键继续')


def user_all(user_level):
    # 查询所有用户列表
    print('功能：用户列表'.center(50, '-'))
    data = reload_data()
    user_list = data['users']
    print('用户列表'.center(48, '-'))
    print("%s%s%s%s" % ('用户名'.ljust(15), '权限等级'.ljust(10), '账号状态'.ljust(10), '备注信息',))
    for user in user_list:
        level = ''
        status = ''
        if user['level'] == 0:
            level = '超级管理员'
            if user_level == 2:
                continue
        elif user['level'] == 1:
            level = '图书管理员'
            if user_level == 2:
                continue
        elif user['level'] == 2:
            level = '用户管理员'
            if user_level == 2:
                continue
        elif user['level'] == 3:
            level = '普通用户'
        else:
            pass

        if user['status'] == 0:
            status = '正常'
        elif user['status'] == 9:
            status = '禁用'
        else:
            pass
        print("%s%s%s%s" % (user['user_name'].ljust(15), level.ljust(10), status.ljust(10), user['info']))
    print('-' * 50)
    input('按enter键继续')
