import random
print('**************************')
print('*       中国工商银行       *')
print('*       账户管理系统       *')
print('*         V1.0           *')
print('**************************')
print('*1.开户                   *')
print('*2.存钱                   *')
print('*3.取钱                   *')
print('*4.转账                   *')
print('*5.查询                   *')
print('*6.Bye                   *')
print('**************************')
bank={}
def bank_adduser(account,username,password,country,province,street,door):
    if len(bank) > 100:
        # 超出了银行上限
        return 3
    if username in bank :
        #如果名字  在    bank  执行下面的代码
        return 2
    bank[username]={
        "account":"account",
        #键一个名字       ：值来自传入的参数:account
        "password":"password",
        "country":"country",
        "province":"province",
        "street":"street",
        "door":"door",
        "money":0,
        "brnk_name":bank_name # 直接调用全局参数
    }
    return 1


def cunqian(): #存钱
    wasd = 1000
    abcd=input('请输入账号')
    efgr=input('请输入密码')
    ghil=int(input('请输入存钱金额'))
    if abcd in abcd:
        wasd += ghil
        print('存钱金额是',wasd)
    else:
        return False


def quqian():  #取钱
    cunkuan = 1000
    qwer = input('请输入账号')
    asdf = input('请输入密码')
    zxcv = int(input('请输入取钱金额'))
    if zxcv > cunkuan:
        print('您的存款不够')
    elif zxcv < cunkuan:
        cunkuan -= zxcv
        print('您的存款还剩',cunkuan)
    else:
        print('您的存款为零')


def zhuanzhang():   #转账
    weikuan = 1000
    vcd = input('请输入转账账号')
    dvd = input('请输入密码')
    asd = input('输入R转入，输入C转出')
    if asd == 'R':
        bsd = int(input('请输入转入金额'))
        print(bsd+weikuan)
    elif asd == 'C':
        csd = int(input('请输入转出金额'))
        if csd > weikuan:
            print('余额不足')
        elif csd < weikuan:
            print('转出金额为',weikuan-csd)
    else:
        print('输入有误')


def chaxun():   #查询
    username = input('请输入您的账号')
    password = input('请输入您的密码')
    yue = 1000
    if username in username:
        print('当前账号',username)
        print('当前密码','******')
        print('当前卡号余额',yue)
        print('持卡人现居住地址','xxxxxx')
        print('开户行为中国工商银行七马路支行')


bank_name= "中国工商银行七马路支行"#写死的银行地址
def useradd():
    username=input("请输入您的用户名")
    password=input("请输入您的密码")
    print("请输入您的详细信息")
    country=input("请输入您国家")
    province = input("请输入您省份")
    street = input("请输入您街道")
    door=input("请输入您的门牌号")
    account=random.randint(00000000,99999999) #随机生成8位账号
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 3:
        print("对不起，该银行的用户已满，请到其他银行办理")
    if status == 2:
        print("对不起，该用户已经开户，不要重复")
    if status == 1:
        print("恭喜你正常开户，以下是您的信息")
        info ='''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


while True:
    num=input("请输入您要办的业务：")
    if num  == "1":
        useradd()
    elif num == "2":
        cunqian()
    elif num == "3":
        quqian()
    elif num == "4":
        zhuanzhang()
    elif num == "5":
        chaxun()
    elif num == "6":
        print("再见")
        break
    else:
        print("输入有误")
        break
