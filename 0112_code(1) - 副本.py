lis_goods_num = [10, 10, 10, 10, 10, 10]
lis_goods_name = ['cola', 'beer', 'MineralWater', 'Hot coffee', 'Milk Tea', 'Hot Milk']
lis_goods_price = [160, 190, 150, 100, 130, 190]

lis_money_val = [500, 100, 50, 10, 5]
lis_money_num = [100, 100, 100, 100, 100]

def get_goods_code():
    valid_code = [0, 1, 2, 3, 4, 5, 6]
    temp_code = eval(input())
    while temp_code not in valid_code:
        temp_code = eval(input("入力エラー、再入力してください"))
    return temp_code - 1


def get_goods_num(goods_num):
    temp_num = eval(input())

    while temp_num > goods_num and temp_num != -1:
        temp_num = eval(input("入力した数量が足りません。再入力してください。購入を終了するには-1を入力してください."))
    return temp_num


def cashier(cost):
    print(f"今回の総消費量{cost}円.\n")

    cash_in = eval(input("紙幣を紙幣入力ポートに入れてください:"))
    cash_out = cash_in - cost

    while cash_out != 0:
        if cash_out > 0:
            lis_money_num[0] -= cash_out // 500
            lis_money_num[1] -= cash_out % 500 // 100
            lis_money_num[2] -= cash_out % 500 % 100 // 50
            lis_money_num[3] -= cash_out % 500 % 100 % 50 // 10
            lis_money_num[4] -= cash_out % 500 % 100 % 50 % 10 // 5

            print(f"成功した購入、あなたを探して{cash_out}円")
            cash_out = 0
        else:
            cash_in = eval(input("紙幣が不足しています。引き続き紙幣をスロットに入れてください:"))
            cash_out = cash_in + cash_out
    print("次回おかえりなさい")

def check():
    str_temp = ('お探しの情報を入力してください：\n'
                '1).製品在庫；\n'
                '2).貯金箱情報\n'
                '3).前のメニューに戻る\n')
    print(str_temp)

    valid_code = [1, 2, 3]

    num = eval(input("必要な情報を入力してください:"))
    while num not in valid_code:
        num = eval(input("再入力してください"))

    if num == 1:
        print('cola%dボトル ,beer%dボトル ，Mineral Water%dボトル ，Hot Coffee%dボトル ，Hot Milk%dボトル ，Milk Tea%dボトル ' % (
            lis_goods_num[0], lis_goods_num[1], lis_goods_num[2],
            lis_goods_num[3], lis_goods_num[4], lis_goods_num[5]))
    elif num == 2:
        print("500円%d 100円%d 50円%d  10円%d张 5円%d" % (
            lis_money_num[0], lis_money_num[1],
            lis_money_num[2], lis_money_num[3], lis_money_num[4],))
    elif num == 3:
        return 0
    return 1


def main_func():
    choice = eval(input(('必要なビジネスを入力してください：\n'
                         '1).商品を購入する；\n'
                         '2).管理者クエリ\n'
                         "3).プログラムを終了する"
                         '入る：')))
    flag = 1
    while flag:
        if choice == 1:
            flag = sold()
        elif choice == 2:
            flag = check()
        else:
            flag = 0

    return choice


if __name__ == '__main__':
    flag = 1

    while flag != 3:
        flag = main_func()
