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
    num_rounds = 3
    endowment = c(100)


class Subsession(BaseSubsession):
    stock_1 = models.CurrencyField(min=0)

    def update_stock(self):
        import random
        print(f'当前第{self.round_number}轮')
        if self.round_number == 1:
            stock_1 = 100
        else:
            stock_1 = self.in_round(self.round_number - 1).stock_1
            stock_1 = stock_1 + c(random.randint(1, 3))

        self.stock_1 = stock_1





class Group(BaseGroup):
    pass


class Player(BasePlayer):
    money = models.CurrencyField(min=0)
    Stock_1_amount = models.FloatField(min=0, initial=0)

    def update_money(self):
        if self.round_number == 1:
            money = 5
        else:
            money = self.in_round(self.round_number - 1).money
            money = money + c(10)
        self.money = money
