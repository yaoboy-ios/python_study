from student_tools import add_student,search_all_students,del_student

while True:
    print('*' * 20)
    print('欢迎使用【小妖学生管理系统】1.0 \n\n1.新增学生\n2.查看所有学生\n3.删除学生\n0.退出系统\n')
    print('*' * 20)

    # 检测用户输入选项
    options = input('请选择需要使用的功能选项：')
    # 对用户输入发选项进行输出
    print('您选择的功能选项是：%s' % options)
    if options in ['1', '2', '3']:
        if options == '1':
            add_student()
        elif options == '2':
            search_all_students()
        else:
            del_student()
    elif options == '0':
        print('欢迎再次使用【小妖学生管理系统】')
        break
    else:
        print('输入错误，请重新输入')
