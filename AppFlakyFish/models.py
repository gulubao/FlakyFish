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
    name_in_url = 'AppFlakyFish_copy'
    players_per_group = None
    num_rounds = 17
    endowment = 100.0
    randomSeed = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    randomBottom = 10  # 股票随机波动不能小于此值 ，如果为 None 不设置下限 

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):

    stock_1_price = models.FloatField(min=0)
    stock_2_price = models.FloatField(min=0)
    stock_3_price = models.FloatField(min=0)
    stock_4_price = models.FloatField(min=0)
    stock_5_price = models.FloatField(min=0)
    stock_6_price = models.FloatField(min=0)


    def update_stock_price(self):
        import random

        roundNow = self.round_number
        rng = random.Random(Constants.randomSeed[roundNow-1])

        def generate_random(stock_name):
            # 根据规则生成每轮的随机变化量
            # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
            # output:{ generated_amount:c变量，股票变更的值}
            def is_up_or_down(stock_name):
                # 根据规则判定涨或跌
                # input :{ stock_name:string变量，指定股票的名称如'stock_1'}
                # output:{ up_or_down:string变量，股票变更的方向，如'up'}
                if   stock_name == 'stock_1_price':
                    random_number = rng.random()
                    if random_number <= 0.65:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_2_price':
                    random_number = rng.random()
                    if random_number <= 0.55:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_3_price':
                    random_number = rng.random()
                    if random_number <= 0.50:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_4_price':
                    random_number = rng.random()
                    if random_number <= 0.50:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_5_price':
                    random_number = rng.random()
                    if random_number <= 0.45:
                        return 'up'
                    else:
                        return 'down'

                elif stock_name == 'stock_6_price':
                    random_number = rng.random()
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
                    amount = rng.random()*5.0
                    amount = round(amount, 2)
                    return amount

                def regular_2():
                    # 生成1,3,5的随机整数
                    values = [1.0, 3.0, 5.0]
                    amount = rng.choice(values)
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
            stock_1_price = round(rng.random()*30+20, 2) #随机在20-50间
            stock_2_price = round(rng.random()*30+20, 2)
            stock_3_price = round(rng.random()*30+20, 2)
            stock_4_price = round(rng.random()*30+20, 2)
            stock_5_price = round(rng.random()*30+20, 2)
            stock_6_price = round(rng.random()*30+20, 2)
        else:
            stock_1_price = self.in_round(self.round_number - 1).stock_1_price
            newPrice = stock_1_price + generate_random(stock_name='stock_1_price')
            if Constants.randomBottom is not None:
                if newPrice<Constants.randomBottom:
                    newPrice = Constants.randomBottom
            stock_1_price = newPrice

            stock_2_price = self.in_round(self.round_number - 1).stock_2_price
            newPrice =  stock_2_price + generate_random(stock_name='stock_2_price')
            if Constants.randomBottom is not None:
                if newPrice<Constants.randomBottom:
                    newPrice = Constants.randomBottom
            stock_2_price = newPrice

            stock_3_price = self.in_round(self.round_number - 1).stock_3_price
            newPrice = stock_3_price + generate_random(stock_name='stock_3_price')
            if Constants.randomBottom is not None:
                if newPrice<Constants.randomBottom:
                    newPrice = Constants.randomBottom
            stock_3_price = newPrice

            stock_4_price = self.in_round(self.round_number - 1).stock_4_price
            newPrice = stock_4_price + generate_random(stock_name='stock_4_price')
            if Constants.randomBottom is not None:
                if newPrice<Constants.randomBottom:
                    newPrice = Constants.randomBottom
            stock_4_price = newPrice

            stock_5_price = self.in_round(self.round_number - 1).stock_5_price
            newPrice = stock_5_price + generate_random(stock_name='stock_5_price')
            if Constants.randomBottom is not None:
                if newPrice<Constants.randomBottom:
                    newPrice = Constants.randomBottom
            stock_5_price = newPrice


            stock_6_price = self.in_round(self.round_number - 1).stock_6_price
            newPrice = stock_6_price + generate_random(stock_name='stock_6_price')
            if Constants.randomBottom is not None:
                if newPrice<Constants.randomBottom:
                    newPrice = Constants.randomBottom
            stock_6_price = newPrice

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


class Player(BasePlayer):

    money = models.FloatField(min=0)

    stock_1_amount = models.IntegerField(min=0, initial=0)
    stock_2_amount = models.IntegerField(min=0, initial=0)
    stock_3_amount = models.IntegerField(min=0, initial=0)
    stock_4_amount = models.IntegerField(min=0, initial=0)
    stock_5_amount = models.IntegerField(min=0, initial=0)
    stock_6_amount = models.IntegerField(min=0, initial=0)

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



    def update_stock_1_amount(self):
        if self.round_number == 5 and self.stock_1_amount is None:
            self.stock_1_amount = 0
        elif self.round_number > 5:
            self.stock_1_amount = self.in_round(self.round_number - 1).stock_1_amount

    def update_stock_2_amount(self):
        if self.round_number == 5 and self.stock_2_amount is None:
            self.stock_2_amount = 0
        elif self.round_number > 5:
            self.stock_2_amount = self.in_round(self.round_number - 1).stock_2_amount

    def update_stock_3_amount(self):
        if self.round_number == 5 and self.stock_3_amount is None:
            self.stock_3_amount = 0
        elif self.round_number > 5:
            self.stock_3_amount = self.in_round(self.round_number - 1).stock_3_amount

    def update_stock_4_amount(self):
        if self.round_number == 5 and self.stock_4_amount is None:
            self.stock_4_amount = 0
        elif self.round_number > 5:
            self.stock_4_amount = self.in_round(self.round_number - 1).stock_4_amount

    def update_stock_5_amount(self):
        if self.round_number == 5 and self.stock_5_amount is None:
            self.stock_5_amount = 0
        elif self.round_number > 5:
            self.stock_5_amount = self.in_round(self.round_number - 1).stock_5_amount

    def update_stock_6_amount(self):
        if self.round_number == 5 and self.stock_6_amount is None:
            self.stock_6_amount = 0
        elif self.round_number > 5:
            self.stock_6_amount = self.in_round(self.round_number - 1).stock_6_amount
            
    def update_money(self):
        if self.round_number == 1:
            money = 1000.0
        else:
            money = self.in_round(self.round_number - 1).money
            money = money + 10.0
        self.money = money


# {field_name}_error_message()
# 这是验证一个字段的最灵活的方法。

# class Player(BasePlayer):
#     offer = models.CurrencyField()
#     budget = models.CurrencyField()

# def offer_error_message(player, value):
#     print('value is', value)
#     if value > player.budget:
#         return 'Cannot offer more than your remaining budget'


# def stock_1_sell_amount_error_message(player, value):
#     print('value is', value)
#     if value > player.stock_1_amount:
#         return 'Cannot sell more than your remaining stock.'

# {field_name}_max()
# 此函数为在模型字段中动态地设置 max= 的方法。例如：

# class Player(BasePlayer):
#     offer = models.CurrencyField()
#     budget = models.CurrencyField()


# def offer_max(player):
#     return player.budget

# def stock_1_sell_amount_max(player):
#     return player.stock_1_amount

# def stock_2_sell_amount_max(player):
#     return player.stock_2_amount

# def stock_3_sell_amount_max(player):
#     return player.stock_3_amount

# def stock_4_sell_amount_max(player):
#     return player.stock_4_amount

# def stock_5_sell_amount_max(player):
#     return player.stock_5_amount

# def stock_6_sell_amount_max(player):
#     return player.stock_6_amount