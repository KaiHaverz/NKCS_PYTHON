contacts = []

def add_contact():
    name = input("请输入姓名: ")
    qq = input("请输入QQ号码: ")
    phone = input("请输入电话号码: ")
    email = input("请输入电子邮件: ")

    contact_info = {
        'name': name,
        'qq': qq,
        'phone': phone,
        'email': email
    }

    contacts.append(contact_info)
    print(f"\n成功添加: {contact_info['name']} !")
    return contact_info

def delete_contact():
    if not contacts:
        print("没有联系人可以删除。")
        return

    show_contacts()
    serial_number = int(input("请输入要删除的联系人编号: "))
    if serial_number < 0 or serial_number >= len(contacts):
        print("无效的编号。")
    else:
        deleted_contact = contacts.pop(serial_number)
        print(f"成功删除: {deleted_contact['name']}")

def modify_contact():
    if not contacts:
        print("没有联系人可以修改。")
        return

    show_contacts()
    serial_number = int(input("请输入要修改的联系人编号: "))
    if serial_number < 0 or serial_number >= len(contacts):
        print("无效的编号。")
    else:
        print("可编辑的子项如下:")
        print("1. 姓名")
        print("2. QQ号码")
        print("3. 电话号码")
        print("4. 电子邮件")

        option = int(input("请输入要修改的子项编号: "))
        if option >= 1 and option <= 4:
            keys = ["name", "qq", "phone", "email"]
            new_value = input(f"请输入新的{keys[option - 1]}，若不修改输入空格: ")
            if new_value.strip() != "":
                contacts[serial_number][keys[option - 1]] = new_value
                print("修改成功!")
            else:
                print("修改取消。")
        else:
            print("输入错误。")

def find_contact():
    if not contacts:
        print("没有联系人可以查找。")
        return

    search_key = input("请输入搜索关键词 (如姓名、电话等): ")
    found_contacts = []
    for contact in contacts:
        for value in contact.values():
            if search_key in str(value):
                found_contacts.append(contact)
                break
    if found_contacts:
        print("找到的联系人信息:")
        for contact in found_contacts:
            print(contact)
    else:
        print("未找到符合条件的联系人。")

def show_contacts():
    if not contacts:
        print("当前没有联系人信息。")
    else:
        print("\n已修改，最新的列表为\n")
        print("{:<5} {:<10} {:<15} {:<15} {:<25}".format("No.", "Name", "QQ", "Phone", "E-mail"))
        for index, contact in enumerate(contacts):
            print("{:<5} {:<10} {:<15} {:<15} {:<25}".format(index + 1, contact['name'], contact['qq'], contact['phone'], contact['email']))

def main_menu():
    while True:
        print("\n======================================== 联系人管理系统 ========================================\n")
        print("a: 添加联系人")
        print("d: 删除联系人")
        print("c: 修改联系人")
        print("f: 查找联系人")
        print("s: 显示所有联系人")
        choice = input("\n请输入您的操作: ")
        if choice == "a":
            add_contact()
        elif choice == "d":
            delete_contact()
        elif choice == "c":
            modify_contact()
        elif choice == "f":
            find_contact()
        elif choice == "s":
            show_contacts()
        else:
            print("输入错误，请重新输入。")

if __name__ == "__main__":
    main_menu()