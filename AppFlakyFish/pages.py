from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SellPage_ReadOnly(Page):
    form_model = 'player'
    def is_displayed(player):
        return player.round_number in [1,2,3,4]

    def vars_for_template(self):
        self.player.update_money()
        self.subsession.update_stock()
        self.round_number
        return {
            'round_number' : self.round_number,
            'money': self.player.money,
            'stock_1': round(self.subsession.stock_1, 2),
            'stock_2': round(self.subsession.stock_2, 2),
            'stock_3': round(self.subsession.stock_3, 2),
            'stock_4': round(self.subsession.stock_4, 2),
            'stock_5': round(self.subsession.stock_5, 2),
            'stock_6': round(self.subsession.stock_6, 2)
        }


class BuyPage_ReadOnly(Page):
    form_model = 'player'
    def is_displayed(player):
        return player.round_number in [1,2,3,4]

    def vars_for_template(self):
        return {
            'round_number': self.round_number,
            'money': self.player.money,
            'stock_1': round(self.subsession.stock_1, 2),
            'stock_2': round(self.subsession.stock_2, 2),
            'stock_3': round(self.subsession.stock_3, 2),
            'stock_4': round(self.subsession.stock_4, 2),
            'stock_5': round(self.subsession.stock_5, 2),
            'stock_6': round(self.subsession.stock_6, 2)
        }

    # def before_next_page(self):
    #
    #     # print(f'当前轮数：{self.round_number}')
    #     # print(f'未更新股价{self.subsession.stock_1}')
    #     # import random
    #     # self.subsession.stock_1 = self.subsession.stock_1 + c(random.randint(1, 3))
    #     # print(f'新的股价：{self.subsession.stock_1}')
    #         print(f'当前资金：{self.player.money}')
    #         self.player.money = self.player.money + c(10)
    #         print(f'更新后资金：{self.player.money}')


class SellPage_sellable(Page):
    form_model = 'player'
    def is_displayed(player):
        return player.round_number > 4

    def vars_for_template(self):
        self.player.update_money()
        self.subsession.update_stock()
        self.round_number
        return {
            'round_number' : self.round_number,
            'money': self.player.money,
            'stock_1': round(self.subsession.stock_1, 2),
            'stock_2': round(self.subsession.stock_2, 2),
            'stock_3': round(self.subsession.stock_3, 2),
            'stock_4': round(self.subsession.stock_4, 2),
            'stock_5': round(self.subsession.stock_5, 2),
            'stock_6': round(self.subsession.stock_6, 2)
        }


class BuyPage_buyable(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number > 4

    def vars_for_template(self):
        return {
            'round_number': self.round_number,
            'money': self.player.money,
            'stock_1': round(self.subsession.stock_1, 2),
            'stock_2': round(self.subsession.stock_2, 2),
            'stock_3': round(self.subsession.stock_3, 2),
            'stock_4': round(self.subsession.stock_4, 2),
            'stock_5': round(self.subsession.stock_5, 2),
            'stock_6': round(self.subsession.stock_6, 2)
        }

page_sequence = [SellPage_ReadOnly, BuyPage_ReadOnly, SellPage_sellable, BuyPage_buyable]
