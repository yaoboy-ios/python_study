from user_manager import reload_data, write_data


def book_add():
    # 添加图书
    # 查询现有图书列表
    print('功能：添加图书'.center(50, '-'))
    data = reload_data()
    book_list = data['books']
    book_classify_list = data['book_classify']
    print('1、在现有图书分类中添加\n2、添加新的图书分类')
    print('-' * 50)
    while True:
        options = input('请选择要进行的操作(1 or 2):')
        if options in ['1', '2']:
            if options == '1':
                for classify in book_classify_list:
                    print('%d、%s' % (book_classify_list.index(classify) + 1, classify))
                classify_num = input('请选择要添加的图书分类:')
                if classify_num in map(str, list(range(1, 1 + len(book_classify_list)))):
                    book_name = input('请输入图书名称:')
                    is_exist = False
                    for book in book_list:
                        if book['book_name'] == book_name:
                            is_exist = True
                            print('该图书已存在')
                            input('按enter键继续')
                            break
                    if is_exist:
                        break
                    price = input('请输入图书价格:')
                    publisher = input('请输入出版方：')
                    book = {
                        'id': len(book_list) + 1,
                        'book_name': book_name,
                        'price': price,
                        'publisher': publisher,
                        'classify': book_classify_list[int(classify_num) - 1]
                    }
                    book_list.append(book)
                    data['books'] = book_list
                    write_data(data)
                    print('图书添加成功')
                    input('按enter键继续')
                    break
                else:
                    print('选择的分类不存在,请重新输入')
            elif options == '2':
                classify = input('请输入分类名称:')
                book_classify_list.append(classify)
                data['book_classify'] = book_classify_list
                write_data(data)
                print('分类添加成功')
                input('按enter键继续')
            else:
                pass
        else:
            print('输入有误,请重新输入')


def book_del():
    # 删除图书
    print('功能：删除图书'.center(50, '-'))
    data = reload_data()
    book_list = data['books']
    del_book = input('请输入需要删除的图书名：')
    for book in book_list:
        if del_book == book['book_name']:
            print("%s%s%s" % ('图书名称'.ljust(15), '图书价格'.ljust(10), '出版社'.ljust(10)))
            print("%s%s%s" % (book['book_name'].ljust(15), '￥:' + book['price'].ljust(10), book['publisher'].ljust(10)))
            del_enter = input('是否真的要删除该书籍? y/n：')
            if del_enter.lower() in ['y', 'n']:
                if del_enter.lower() == 'y':
                    book_list.remove(book)
                    data['books'] = book_list
                    write_data(data)
                    print('删除成功')
                    print('-' * 50)
                    input('按enter键继续')
                    return
                else:
                    print('操作已取消')
                    print('-' * 50)
                    input('按enter键继续')
                    return
    print('没有查到相关的书籍')
    print('-' * 50)
    input('按enter键继续')


def book_all():
    # 查看图书列表
    print('功能：图书列表'.center(50, '-'))
    data = reload_data()
    book_list = data['books']
    book_classify_list = data['book_classify']
    for classify in book_classify_list:
        print('%d、%s' % (book_classify_list.index(classify) + 1, classify))
    while True:
        classify = input('请选择要查看的图书分类：')
        if classify in map(str, list(range(1, 1 + len(book_classify_list)))):
            classify_book = []
            for book in book_list:
                if book['classify'] == book_classify_list[int(classify) - 1]:
                    classify_book.append(book)
            print('%s-图书列表'.center(50, '-') % book_classify_list[int(classify) - 1])
            print("%s%s%s" % ('图书名称'.ljust(15), '图书价格'.ljust(10), '出版社'.ljust(10)))
            for book in classify_book:
                print("%s%s%s" % (book['book_name'].ljust(15), '￥:' + book['price'].ljust(10), book['publisher'].ljust(10)))
            print('-' * 50)
            input('按enter键继续')
            break
        else:
            print('选择的分类不存在,请重新输入')
            input('按enter键继续')


def book_search():
    # 在已存储的所有图书中搜索图书
    print('功能：图书搜索'.center(50, '-'))
    data = reload_data()
    book_list = data['books']
    search_list = []
    search_str = input('请输入需要搜索的图书名称：')
    for book in book_list:
        if search_str in book['book_name']:
            search_list.append(book)
    if len(search_list) == 0:
        print('没有查到相关的书籍')
    else:
        print("%s%s%s" % ('图书名称'.ljust(15), '图书价格'.ljust(10), '出版社'.ljust(10)))
        for book in search_list:
            print("%s%s%s" % (book['book_name'].ljust(15), '￥:' + book['price'].ljust(10), book['publisher'].ljust(10)))
    print('-' * 50)
    input('按enter键继续')
