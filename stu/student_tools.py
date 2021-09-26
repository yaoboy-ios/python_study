student_list = []


def add_student():
    # 新增学生
    print('-' * 50)
    print('功能：添加学生')
    # 开始录入学生信息
    name = input('请输入学生姓名：')
    sex = input('请输入学生性别：')
    age = input('请输入学生年龄：')
    team = input('请输入学生班级：')
    student = {
        'name': name,
        'age': age,
        'sex': sex,
        'team': team
    }

    student_list.append(student)

    print('成功添加学生 %s' % student['name'])


def search_all_students():
    # 查询系统已添加的所有学生
    print('-' * 50)
    print('功能：查询所有学生列表\n')
    # 遍历列表显示全部学生信息
    for name in ["姓名", "性别", "年龄", "班级"]:
        print(name.center(8), end='')
    print('\r')
    print("=" * 50)
    if len(student_list) == 0:
        print('暂无学生列表')
    else:
        for value in student_list:
            print('%s%s%s%s' % (
                value['name'].center(8),
                value['sex'].center(8),
                value['age'].center(8),
                value['team'].center(8)
            ))
    print("=" * 50)


def del_student():
    # 删除指定学生
    # 输入学生的姓名遍历学生表如果存在即删除
    print('-' * 50)
    print('功能：删除学生')
    student = {}
    while True:
        name = input('请输入要删除学生的姓名:')
        for value in student_list:
            if name == value['name']:
                student = value
                break
        if len(student) == 0:
            print('没有查询到此学生.请检查学生姓名是否输入正确,重新输入')
        else:
            # 查询到此学生，执行删除操作
            enter_str = input('确认删除此学生(y/n)：')
            enter_str = enter_str.lower()
            if enter_str == 'y':
                student_list.remove(student)
                print('已成功删除学生：%s' % student['name'])
                break
            else:
                print('删除学生操作已取消')
                break
