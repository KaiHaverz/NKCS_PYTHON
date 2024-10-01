def welcome():

    welcome_msg='''
    ==================== Welcome to InfoSystem! ====================
    
    1:增加联系人
    2:删除联系人
    3:修改联系人
    4:查找联系人
    5:展示所有联系人
    
    =================================================================
    '''

    print(welcome_msg)

    input("请输入相应功能对应的数字：")

class Contact:
    def __init__(self,name,qq,phone,email):
        self.name=name
        self.qq=qq
        self.phone=phone
        self.email=email




if __name__ == '__main__':
    welcome()