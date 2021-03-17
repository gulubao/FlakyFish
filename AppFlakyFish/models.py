from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'AppFlakyFish'
    players_per_group = None
    num_rounds = 17
    endowment = 100.0


class Subsession(BaseSubsession):
    stock_1 = models.FloatField(min=0)
    stock_2 = models.FloatField(min=0)
    stock_3 = models.FloatField(min=0)
    stock_4 = models.FloatField(min=0)
    stock_5 = models.FloatField(min=0)
    stock_6 = models.FloatField(min=0)

    def update_stock(self):
        import random

        def generate_random(stock_name):
            # 根据规则生成每轮的随机变化量
            # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
            # output:{ generated_amount:c变量，股票变更的值}
            def is_up_or_down(stock_name):
                # 根据规则判定涨或跌
                # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
                # output:{ up_or_down:string变量，股票变更的方向，如'up'}
                if   stock_name == 'stock_1':
                    random_number = random.random()
                    if random_number <= 0.65:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_2':
                    random_number = random.random()
                    if random_number <= 0.55:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_3':
                    random_number = random.random()
                    if random_number <= 0.50:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_4':
                    random_number = random.random()
                    if random_number <= 0.50:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_5':
                    random_number = random.random()
                    if random_number <= 0.45:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_6':
                    random_number = random.random()
                    if random_number <= 0.35:
                        return 'up'
                    else:
                        return 'down'

                else:
                    import os
                    print('无此股票')
                    os.exit(0)

            def change_amount(regular='regular_1'):
                # 根据规则判定涨跌数量
                def regular_1():
                    # 生成0-5的随机浮点数
                    amount = random.random()*5.0
                    amount = round(amount, 2)
                    return amount

                def regular_2():
                    # 生成1,3,5的随机整数
                    values = [1.0, 3.0, 5.0]
                    amount = random.choice(values)
                    return amount

                if regular == 'regular_1':
                    return regular_1()
                else:
                    return regular_2()

            direction = is_up_or_down(stock_name)
            amount = change_amount()
            if direction == 'up':
                return amount
            else:
                return -amount

        print(f'当前第{self.round_number}轮')
        if self.round_number == 1:
            ## 设置股票初始价格
            stock_1 = round(random.random()*10+10, 2) #随机在10-20间
            stock_2 = round(random.random()*10+10, 2)
            stock_3 = round(random.random()*10+10, 2)
            stock_4 = round(random.random()*10+10, 2)
            stock_5 = round(random.random()*10+10, 2)
            stock_6 = round(random.random()*10+10, 2)
        else:
            stock_1 = self.in_round(self.round_number - 1).stock_1
            stock_1 = stock_1 + generate_random(stock_name='stock_1')

            stock_2 = self.in_round(self.round_number - 1).stock_2
            stock_2 = stock_2 + generate_random(stock_name='stock_2')

            stock_3 = self.in_round(self.round_number - 1).stock_3
            stock_3 = stock_3 + generate_random(stock_name='stock_3')

            stock_4 = self.in_round(self.round_number - 1).stock_4
            stock_4 = stock_4 + generate_random(stock_name='stock_4')

            stock_5 = self.in_round(self.round_number - 1).stock_5
            stock_5 = stock_5 + generate_random(stock_name='stock_5')

            stock_6 = self.in_round(self.round_number - 1).stock_6
            stock_6 = stock_6 + generate_random(stock_name='stock_6')

        self.stock_1 = stock_1
        self.stock_2 = stock_2
        self.stock_3 = stock_3
        self.stock_4 = stock_4
        self.stock_5 = stock_5
        self.stock_6 = stock_6

    def stock_1_history(self):
        return [round(g.stock_1,2) for g in self.in_previous_rounds()]

    def stock_2_history(self):
        return [round(g.stock_2,2) for g in self.in_previous_rounds()]

    def stock_3_history(self):
        return [round(g.stock_3,2) for g in self.in_previous_rounds()]

    def stock_4_history(self):
        return [round(g.stock_4,2) for g in self.in_previous_rounds()]

    def stock_5_history(self):
        return [round(g.stock_5,2) for g in self.in_previous_rounds()]

    def stock_6_history(self):
        return [round(g.stock_6,2) for g in self.in_previous_rounds()]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    money = models.FloatField(min=0)
    Stock_1_amount = models.FloatField(min=0, initial=0)

    stock_1 = models.FloatField(min=0)
    stock_2 = models.FloatField(min=0)
    stock_3 = models.FloatField(min=0)
    stock_4 = models.FloatField(min=0)
    stock_5 = models.FloatField(min=0)
    stock_6 = models.FloatField(min=0)

    def update_money(self):
        if self.round_number == 1:
            money = 5.0
        else:
            money = self.in_round(self.round_number - 1).money
            money = money + 10.0
        self.money = money
