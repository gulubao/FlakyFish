from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants





class SellPage(Page):
    form_model = 'player'


class BuyPage(Page):
    form_model = 'player'

    def vars_for_template(self):
        self.player.update_money()
        self.subsession.update_stock()
        return {
            'money': self.player.money,
            'stock_1': self.subsession.stock_1
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




#
# class MyPage(Page):
#     pass
#
#
# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass

page_sequence = [BuyPage]
#page_sequence = [SellPage, BuyPage]
