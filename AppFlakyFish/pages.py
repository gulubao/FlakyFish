from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SellPage_ReadOnly(Page):

    form_model = 'player'

    def is_displayed(player):
        return player.round_number in [1,2,3,4]

    def vars_for_template(self):
        self.player.update_money()
        self.group.update_stock_price()
        self.player.update_stock_1_amount()
        self.player.update_stock_2_amount()
        self.player.update_stock_3_amount()
        self.player.update_stock_4_amount()
        self.player.update_stock_5_amount()
        self.player.update_stock_6_amount()

        return {
            'round_number': self.round_number,
            'money': self.player.money,
            'stock_1_price': round(self.group.stock_1_price, 2),
            'stock_2_price': round(self.group.stock_2_price, 2),
            'stock_3_price': round(self.group.stock_3_price, 2),
            'stock_4_price': round(self.group.stock_4_price, 2),
            'stock_5_price': round(self.group.stock_5_price, 2),
            'stock_6_price': round(self.group.stock_6_price, 2),

            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount,

        }

    def js_vars(self):
        return dict(
                   highcharts_series = [
                       {
                        'name' : 'stock_1_price',
                        'data' :  [round(g.stock_1_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_2_price',
                        'data' :  [round(g.stock_2_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_3_price',
                        'data' :  [round(g.stock_3_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_4_price',
                        'data' :  [round(g.stock_4_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_5_price',
                        'data' :  [round(g.stock_5_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_6_price',
                        'data' :  [round(g.stock_6_price,2) for g in self.group.in_all_rounds()]
                        }
                       ]
                    )


class BuyPage_ReadOnly(Page):

    form_model = 'player'

    def is_displayed(player):
        return player.round_number in [1,2,3,4]

    def vars_for_template(self):
        self.player.update_stock_1_amount()
        self.player.update_stock_2_amount()
        self.player.update_stock_3_amount()
        self.player.update_stock_4_amount()
        self.player.update_stock_5_amount()
        self.player.update_stock_6_amount()
        return {
            'round_number': self.round_number,
            'money': self.player.money,
            'stock_1_price': round(self.group.stock_1_price, 2),
            'stock_2_price': round(self.group.stock_2_price, 2),
            'stock_3_price': round(self.group.stock_3_price, 2),
            'stock_4_price': round(self.group.stock_4_price, 2),
            'stock_5_price': round(self.group.stock_5_price, 2),
            'stock_6_price': round(self.group.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount
        }
    
    def js_vars(self):
        return dict(
                   highcharts_series = [
                       {
                        'name' : 'stock_1_price',
                        'data' :  [round(g.stock_1_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_2_price',
                        'data' :  [round(g.stock_2_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_3_price',
                        'data' :  [round(g.stock_3_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_4_price',
                        'data' :  [round(g.stock_4_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_5_price',
                        'data' :  [round(g.stock_5_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_6_price',
                        'data' :  [round(g.stock_6_price,2) for g in self.group.in_all_rounds()]
                        }
                       ]
                    )





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
    form_fields = ['stock_1_sell_amount', 'stock_2_sell_amount', 'stock_3_sell_amount', 'stock_4_sell_amount', 'stock_5_sell_amount', 'stock_6_sell_amount']
    # form_fields = ['stock_1_sell_amount', 'stock_2_sell_amount']



    def is_displayed(player):
        return player.round_number > 4

    def vars_for_template(self):
        self.player.update_money()
        self.group.update_stock_price()
        self.player.update_stock_1_amount()
        self.player.update_stock_2_amount()
        self.player.update_stock_3_amount()
        self.player.update_stock_4_amount()
        self.player.update_stock_5_amount()
        self.player.update_stock_6_amount()
        return {
            'round_number' : self.round_number,
            'money': self.player.money,
            'stock_1_price': round(self.group.stock_1_price, 2),
            'stock_2_price': round(self.group.stock_2_price, 2),
            'stock_3_price': round(self.group.stock_3_price, 2),
            'stock_4_price': round(self.group.stock_4_price, 2),
            'stock_5_price': round(self.group.stock_5_price, 2),
            'stock_6_price': round(self.group.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount
        }


    def js_vars(self):
        return dict(
                   highcharts_series = [
                       {
                        'name' : 'stock_1_price',
                        'data' :  [round(g.stock_1_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_2_price',
                        'data' :  [round(g.stock_2_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_3_price',
                        'data' :  [round(g.stock_3_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_4_price',
                        'data' :  [round(g.stock_4_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_5_price',
                        'data' :  [round(g.stock_5_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_6_price',
                        'data' :  [round(g.stock_6_price,2) for g in self.group.in_all_rounds()]
                        }
                       ]
                    )


    # @staticmethod
    # def error_message(player, values):
    #     print('values is', values)
    #     if values['stock_1_sell_amount'] >10:
    #         return ' 不能卖太多'



    def before_next_page(self):
        print(f'self.player.stock_1_sell_amount = {self.player.stock_1_sell_amount}')
        print(f'self.player.stock_2_sell_amount = {self.player.stock_2_sell_amount}')

        self.player.stock_1_amount = self.player.stock_1_amount - self.player.stock_1_sell_amount
        self.player.stock_2_amount = self.player.stock_2_amount - self.player.stock_2_sell_amount
        self.player.stock_3_amount = self.player.stock_3_amount - self.player.stock_3_sell_amount
        self.player.stock_4_amount = self.player.stock_4_amount - self.player.stock_4_sell_amount
        self.player.stock_5_amount = self.player.stock_5_amount - self.player.stock_5_sell_amount
        self.player.stock_6_amount = self.player.stock_6_amount - self.player.stock_6_sell_amount

        print(f'self.player.stock_1_amount = {self.player.stock_1_amount}')
        print(f'self.player.stock_2_amount = {self.player.stock_2_amount}')


class BuyPage_buyable(Page):

    form_model = 'player'
    form_fields = ['stock_1_bid_amount', 'stock_2_bid_amount', 'stock_3_bid_amount', 'stock_4_bid_amount', 'stock_5_bid_amount', 'stock_6_bid_amount']

    def is_displayed(player):
        return player.round_number > 4

    def vars_for_template(self):
         return {
            'round_number': self.round_number,
            'money': self.player.money,
            'stock_1_price': round(self.group.stock_1_price, 2),
            'stock_2_price': round(self.group.stock_2_price, 2),
            'stock_3_price': round(self.group.stock_3_price, 2),
            'stock_4_price': round(self.group.stock_4_price, 2),
            'stock_5_price': round(self.group.stock_5_price, 2),
            'stock_6_price': round(self.group.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount
        }

    def js_vars(self):
        return dict(
                   highcharts_series = [
                       {
                        'name' : 'stock_1_price',
                        'data' :  [round(g.stock_1_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_2_price',
                        'data' :  [round(g.stock_2_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_3_price',
                        'data' :  [round(g.stock_3_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_4_price',
                        'data' :  [round(g.stock_4_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_5_price',
                        'data' :  [round(g.stock_5_price,2) for g in self.group.in_all_rounds()]
                        }, {
                        'name' : 'stock_6_price',
                        'data' :  [round(g.stock_6_price,2) for g in self.group.in_all_rounds()]
                        }
                       ]
                    )

    def before_next_page(self):
        self.player.stock_1_amount = self.player.stock_1_amount + self.player.stock_1_bid_amount
        self.player.stock_2_amount = self.player.stock_2_amount + self.player.stock_2_bid_amount
        self.player.stock_3_amount = self.player.stock_3_amount + self.player.stock_3_bid_amount
        self.player.stock_4_amount = self.player.stock_4_amount + self.player.stock_4_bid_amount
        self.player.stock_5_amount = self.player.stock_5_amount + self.player.stock_5_bid_amount
        self.player.stock_6_amount = self.player.stock_6_amount + self.player.stock_6_bid_amount


page_sequence = [SellPage_ReadOnly, BuyPage_ReadOnly, SellPage_sellable, BuyPage_buyable]


# http://218.89.243.9:8000/InitializeParticipant/imvcaecj

# http://10.31.166.192/InitializeParticipant/imvcaecj