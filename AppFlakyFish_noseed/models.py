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
    name_in_url = 'AppFlakyFish_noseed'
    players_per_group = None
    num_rounds = 17
    endowment = 100.0


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
    # stock_1_price = models.FloatField(min=0)
    # stock_2_price = models.FloatField(min=0)
    # stock_3_price = models.FloatField(min=0)
    # stock_4_price = models.FloatField(min=0)
    # stock_5_price = models.FloatField(min=0)
    # stock_6_price = models.FloatField(min=0)
    #
    #
    # def update_stock_price(self):
    #     import random
    #
    #     def generate_random(stock_name):
    #         # 根据规则生成每轮的随机变化量
    #         # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
    #         # output:{ generated_amount:c变量，股票变更的值}
    #         def is_up_or_down(stock_name):
    #             # 根据规则判定涨或跌
    #             # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
    #             # output:{ up_or_down:string变量，股票变更的方向，如'up'}
    #             if   stock_name == 'stock_1_price':
    #                 random_number = random.random()
    #                 if random_number <= 0.65:
    #                     return 'up'
    #                 else:
    #                     return 'down'
    #
    #             elif stock_name == 'stock_2_price':
    #                 random_number = random.random()
    #                 if random_number <= 0.55:
    #                     return 'up'
    #                 else:
    #                     return 'down'
    #
    #             elif stock_name == 'stock_3_price':
    #                 random_number = random.random()
    #                 if random_number <= 0.50:
    #                     return 'up'
    #                 else:
    #                     return 'down'
    #
    #             elif stock_name == 'stock_4_price':
    #                 random_number = random.random()
    #                 if random_number <= 0.50:
    #                     return 'up'
    #                 else:
    #                     return 'down'
    #
    #             elif stock_name == 'stock_5_price':
    #                 random_number = random.random()
    #                 if random_number <= 0.45:
    #                     return 'up'
    #                 else:
    #                     return 'down'
    #
    #             elif stock_name == 'stock_6_price':
    #                 random_number = random.random()
    #                 if random_number <= 0.35:
    #                     return 'up'
    #                 else:
    #                     return 'down'
    #
    #             else:
    #                 import os
    #                 print('无此股票')
    #                 os.exit(0)
    #
    #         def change_amount(regular='regular_1'):
    #             # 根据规则判定涨跌数量
    #             def regular_1():
    #                 # 生成0-5的随机浮点数
    #                 amount = random.random()*5.0
    #                 amount = round(amount, 2)
    #                 return amount
    #
    #             def regular_2():
    #                 # 生成1,3,5的随机整数
    #                 values = [1.0, 3.0, 5.0]
    #                 amount = random.choice(values)
    #                 return amount
    #
    #             if regular == 'regular_1':
    #                 return regular_1()
    #             else:
    #                 return regular_2()
    #
    #         direction = is_up_or_down(stock_name)
    #         amount = change_amount()
    #         if direction == 'up':
    #             return amount
    #         else:
    #             return -amount
    #
    #     print(f'当前第{self.round_number}轮')
    #     if self.round_number == 1:
    #         ## 设置股票初始价格
    #         stock_1_price = round(random.random()*30+20, 2) #随机在20-50间
    #         stock_2_price = round(random.random()*30+20, 2)
    #         stock_3_price = round(random.random()*30+20, 2)
    #         stock_4_price = round(random.random()*30+20, 2)
    #         stock_5_price = round(random.random()*30+20, 2)
    #         stock_6_price = round(random.random()*30+20, 2)
    #     else:
    #         stock_1_price = self.in_round(self.round_number - 1).stock_1_price
    #         stock_1_price = stock_1_price + generate_random(stock_name='stock_1_price')
    #
    #         stock_2_price = self.in_round(self.round_number - 1).stock_2_price
    #         stock_2_price = stock_2_price + generate_random(stock_name='stock_2_price')
    #
    #         stock_3_price = self.in_round(self.round_number - 1).stock_3_price
    #         stock_3_price = stock_3_price + generate_random(stock_name='stock_3_price')
    #
    #         stock_4_price = self.in_round(self.round_number - 1).stock_4_price
    #         stock_4_price = stock_4_price + generate_random(stock_name='stock_4_price')
    #
    #         stock_5_price = self.in_round(self.round_number - 1).stock_5_price
    #         stock_5_price = stock_5_price + generate_random(stock_name='stock_5_price')
    #
    #         stock_6_price = self.in_round(self.round_number - 1).stock_6_price
    #         stock_6_price = stock_6_price + generate_random(stock_name='stock_6_price')
    #
    #     self.stock_1_price = stock_1_price
    #     self.stock_2_price = stock_2_price
    #     self.stock_3_price = stock_3_price
    #     self.stock_4_price = stock_4_price
    #     self.stock_5_price = stock_5_price
    #     self.stock_6_price = stock_6_price
    #
    # def stock_1_price_history(self):
    #     return [round(g.stock_1_price, 2) for g in self.in_previous_rounds()]
    #
    # def stock_2_price_history(self):
    #     return [round(g.stock_2_price, 2) for g in self.in_previous_rounds()]
    #
    # def stock_3_price_history(self):
    #     return [round(g.stock_3_price, 2) for g in self.in_previous_rounds()]
    #
    # def stock_4_price_history(self):
    #     return [round(g.stock_4_price, 2) for g in self.in_previous_rounds()]
    #
    # def stock_5_price_history(self):
    #     return [round(g.stock_5_price, 2) for g in self.in_previous_rounds()]
    #
    # def stock_6_price_history(self):
    #     return [round(g.stock_6_price, 2) for g in self.in_previous_rounds()]


class Player(BasePlayer):

#股票价格定义起始
    stock_1_price = models.FloatField(min=0)
    stock_2_price = models.FloatField(min=0)
    stock_3_price = models.FloatField(min=0)
    stock_4_price = models.FloatField(min=0)
    stock_5_price = models.FloatField(min=0)
    stock_6_price = models.FloatField(min=0)


    def update_stock_price(self):
        import random

        def generate_random(stock_name):
            # 根据规则生成每轮的随机变化量
            # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
            # output:{ generated_amount:c变量，股票变更的值}
            def is_up_or_down(stock_name):
                # 根据规则判定涨或跌
                # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
                # output:{ up_or_down:string变量，股票变更的方向，如'up'}
                if   stock_name == 'stock_1_price':
                    random_number = random.random()
                    if random_number <= 0.65:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_2_price':
                    random_number = random.random()
                    if random_number <= 0.55:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_3_price':
                    random_number = random.random()
                    if random_number <= 0.50:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_4_price':
                    random_number = random.random()
                    if random_number <= 0.50:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_5_price':
                    random_number = random.random()
                    if random_number <= 0.45:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_6_price':
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
            stock_1_price = round(random.random()*30+20, 2) #随机在20-50间
            stock_2_price = round(random.random()*30+20, 2)
            stock_3_price = round(random.random()*30+20, 2)
            stock_4_price = round(random.random()*30+20, 2)
            stock_5_price = round(random.random()*30+20, 2)
            stock_6_price = round(random.random()*30+20, 2)
        else:
            stock_1_price = self.in_round(self.round_number - 1).stock_1_price
            stock_1_price = stock_1_price + generate_random(stock_name='stock_1_price')

            stock_2_price = self.in_round(self.round_number - 1).stock_2_price
            stock_2_price = stock_2_price + generate_random(stock_name='stock_2_price')

            stock_3_price = self.in_round(self.round_number - 1).stock_3_price
            stock_3_price = stock_3_price + generate_random(stock_name='stock_3_price')

            stock_4_price = self.in_round(self.round_number - 1).stock_4_price
            stock_4_price = stock_4_price + generate_random(stock_name='stock_4_price')

            stock_5_price = self.in_round(self.round_number - 1).stock_5_price
            stock_5_price = stock_5_price + generate_random(stock_name='stock_5_price')

            stock_6_price = self.in_round(self.round_number - 1).stock_6_price
            stock_6_price = stock_6_price + generate_random(stock_name='stock_6_price')

        self.stock_1_price = stock_1_price
        self.stock_2_price = stock_2_price
        self.stock_3_price = stock_3_price
        self.stock_4_price = stock_4_price
        self.stock_5_price = stock_5_price
        self.stock_6_price = stock_6_price

    def stock_1_price_history(self):
        return [round(g.stock_1_price, 2) for g in self.in_previous_rounds()]

    def stock_2_price_history(self):
        return [round(g.stock_2_price, 2) for g in self.in_previous_rounds()]

    def stock_3_price_history(self):
        return [round(g.stock_3_price, 2) for g in self.in_previous_rounds()]

    def stock_4_price_history(self):
        return [round(g.stock_4_price, 2) for g in self.in_previous_rounds()]

    def stock_5_price_history(self):
        return [round(g.stock_5_price, 2) for g in self.in_previous_rounds()]

    def stock_6_price_history(self):
        return [round(g.stock_6_price, 2) for g in self.in_previous_rounds()]
#股票定义完


    money = models.FloatField(min=0)


    stock_1_bid_amount = models.IntegerField(label='你要buy多少股票1', min=0, initial=0)
    stock_2_bid_amount = models.IntegerField(label='你要buy多少股票2', min=0, initial=0)
    stock_3_bid_amount = models.IntegerField(label='你要buy多少股票3', min=0, initial=0)
    stock_4_bid_amount = models.IntegerField(label='你要buy多少股票4', min=0, initial=0)
    stock_5_bid_amount = models.IntegerField(label='你要buy多少股票5', min=0, initial=0)
    stock_6_bid_amount = models.IntegerField(label='你要buy多少股票6', min=0, initial=0)

    stock_1_sell_amount = models.IntegerField(label='你要sell多少股票1', min=0, initial=0)
    stock_2_sell_amount = models.IntegerField(label='你要sell多少股票2', min=0, initial=0)
    stock_3_sell_amount = models.IntegerField(label='你要sell多少股票3', min=0, initial=0)
    stock_4_sell_amount = models.IntegerField(label='你要sell多少股票4', min=0, initial=0)
    stock_5_sell_amount = models.IntegerField(label='你要sell多少股票5', min=0, initial=0)
    stock_6_sell_amount = models.IntegerField(label='你要sell多少股票6', min=0, initial=0)

    stock_1_amount = models.IntegerField(min=0)
    stock_2_amount = models.IntegerField(min=0)
    stock_3_amount = models.IntegerField(min=0)
    stock_4_amount = models.IntegerField(min=0)
    stock_5_amount = models.IntegerField(min=0)
    stock_6_amount = models.IntegerField(min=0)


    def update_stock_1_amount(self):
        if self.round_number == 1:
            stock_1_amount = 0
        else:
            stock_1_amount = self.in_round(self.round_number - 1).stock_1_amount
            stock_1_amount = stock_1_amount + self.stock_1_bid_amount - self.stock_1_sell_amount
        self.stock_1_amount = stock_1_amount

    def update_stock_2_amount(self):
        if self.round_number == 1:
            stock_2_amount = 0
        else:
            stock_2_amount = self.in_round(self.round_number - 1).stock_2_amount
            stock_2_amount = stock_2_amount + self.stock_2_bid_amount - self.stock_2_sell_amount
        self.stock_2_amount = stock_2_amount

    def update_stock_3_amount(self):
        if self.round_number == 1:
            stock_3_amount = 0
        else:
            stock_3_amount = self.in_round(self.round_number - 1).stock_3_amount
            stock_3_amount = stock_3_amount + self.stock_3_bid_amount - self.stock_3_sell_amount
        self.stock_3_amount = stock_3_amount

    def update_stock_4_amount(self):
        if self.round_number == 1:
            stock_4_amount = 0
        else:
            stock_4_amount = self.in_round(self.round_number - 1).stock_4_amount
            stock_4_amount = stock_4_amount + self.stock_4_bid_amount - self.stock_4_sell_amount
        self.stock_4_amount = stock_4_amount

    def update_stock_5_amount(self):
        if self.round_number == 1:
            stock_5_amount = 0
        else:
            stock_5_amount = self.in_round(self.round_number - 1).stock_5_amount
            stock_5_amount = stock_5_amount + self.stock_5_bid_amount - self.stock_5_sell_amount
        self.stock_5_amount = stock_5_amount

    def update_stock_6_amount(self):
        if self.round_number == 1:
            stock_6_amount = 0
        else:
            stock_6_amount = self.in_round(self.round_number - 1).stock_6_amount
            stock_6_amount = stock_6_amount + self.stock_6_bid_amount - self.stock_6_sell_amount
        self.stock_6_amount = stock_6_amount

    def update_money(self):
        if self.round_number == 1:
            money = 1000.0
        else:
            money = self.in_round(self.round_number - 1).money
            money = money + 10.0
        self.money = money
