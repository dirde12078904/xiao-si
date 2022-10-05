info_list = []
admin_id='123'
password='123'
while True:

    print("*********************** 职员信息管理系统 ***********************")
    print("-------------------------- 1.添加信息 --------------------------")
    print("-------------------------- 2.查询信息 --------------------------")
    print("-------------------------- 3.删除信息 --------------------------")
    print("-------------------------- 4.修改信息 --------------------------")
    print("-------------------------- 5.查询所有 --------------------------")
    print("-------------------------- 6.退出系统 --------------------------")
    print("*********************** 职员信息管理系统 ***********************")
    command = int(input("请输入对应数字进行操作："))
    print("-" * 30)  # 分隔线


    def add_info(a):  # 添加函数，参数为后续操作时调用
        name = str(input("请输入员工姓名："))
        while True:  # 后续修改完善可以考虑，将此类循环单独定义为函数
            id_staff = str(input("请输入员工ID："))
            if id_staff.isdigit() is True and len(id_staff) == 5:  # 判断员工ID是否为5位纯数字
                break  # 输入正确时结束循环
            else:
                print("-" * 50)  # 分隔线
                print("【ERROR_1】：员工ID必须为5位纯数字，请重新输入！")
                print("-" * 50)  # 分隔线
        while True:  # 后续修改完善可以考虑，将此类循环单独定义为函数
            id_card = str(input("请输入身份证号："))
            #  判断身份证号是否十八位，要求除了第18位可以为x
            if len(id_card) == 18 and id_card[-1] in "0123456789xX":
                num1 = id_card[0:17]
                if num1.isdigit() is True:  # 判断前17位是否为数字
                    break
                else:
                    print("-" * 35)  # 分隔线
                    print("【ERROR_2】：身份证号前17位必须为数字,请重新输入！")
                    print("-" * 50)  # 分隔线
            else:
                print("-" * 60)  # 分隔线
                print("【ERROR_3】：身份证号输入有误，请重新输入！")
                print("身份证号必须为18位,且前17位为数字,最后一位为数字或X！")
                print("-" * 60)  # 分隔线
        print("-" * 30)  # 分隔线
        info_dic = {}
        info_dic["姓名"] = name
        info_dic["员工ID"] = id_staff
        info_dic["身份证号"] = id_card
        info_list.append(info_dic)
        if a == 1:
            print("【INFO_1】:员工信息添加成功！")
        else:
            print("【INFO_2】:修改成功！")  # 修改员工信息时调用的选项
        print("-" * 30)  # 分隔线


    def find_info(b):  # 后续加上通过员工名查找、身份证号查找
        """查找函数，参数为后续操作时调用"""
        if verify():  # 相当于 if verify() is True:
            while True:  # 后续修改完善时，可以考虑将此类循环单独定义为函数
                id_staff = str(input("请输入员工ID："))
                if id_staff.isdigit() is True and len(id_staff) == 5:  # 判断员工ID是否为5位纯数字
                    break
                else:
                    print("【ERROR_4】：员工ID必须为5位纯数字，请重新输入！")
            print("-" * 30)  # 分隔线
            if len(info_list) == 0:
                print("【ERROR_5】：查无此人，请重新输入！")
            else:
                i = 0
                while i < len(info_list):
                    info_dic = info_list[i]
                    if id_staff == info_dic.get('员工ID'):
                        if b == 2:  # 查找时调用
                            print(info_dic)  # 检查是否找到
                        else:
                            return info_dic  # 删除和修改时调用
                        break
                    else:
                        if i + 1 == len(info_list):
                            print("【ERROR_6】：查无此人，请重新输入！")
                            break
                        else:
                            i += 1
        else:
            print("【ERROR_7】：管理员账号或密码错误，请重新输入！")


    def del_info(c):  # 删除函数，参数为后续操作时调用
        info_dic = find_info(3)
        if info_dic in info_list:
            info_list.remove(info_dic)
            if c == 2:
                print("【INFO_4】：删除成功！")
            else:
                pass
        else:
            return False


    def alter_info():  # 修改函数
        if del_info(4) is False:
            pass
        else:
            print("【INFO_5】：请输入修改后的员工信息！")
            print("-" * 30)  # 分隔线
            add_info(4)


    def verify():  # 管理员验证身份函数
        id_input = str(input("请输入管理员账号："))
        pd_input = str(input("请输入管理员密码："))
        print("-" * 30)  # 分隔线
        if id_input == admin_id and pd_input == password:
            return True
        else:
            return False


    if command == 1:
        add_info(1)
    elif command == 2:
        find_info(2)
    elif command == 3:
        del_info(2)
    elif command == 4:
        alter_info()
    elif command == 5:
        if verify():  # 相当于temp = verify()  # if temp is True:
            print(info_list)
        else:
            print("【ERROR_8】：管理员账号或密码错误，请重新输入！")
    elif command == 6:
        print("【INFO_6】：谢谢使用，您已成功退出系统！")
        exit()