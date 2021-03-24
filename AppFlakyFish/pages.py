from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ReadOnly(Page):

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
            'money': format(round(self.player.money, 2), ','),
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

#
# class BuyPage_ReadOnly(Page):
#
#     form_model = 'player'
#
#     def is_displayed(player):
#         return player.round_number in [1,2,3,4]
#
#     def vars_for_template(self):
#         self.player.update_stock_1_amount()
#         self.player.update_stock_2_amount()
#         self.player.update_stock_3_amount()
#         self.player.update_stock_4_amount()
#         self.player.update_stock_5_amount()
#         self.player.update_stock_6_amount()
#         return {
#             'round_number': self.round_number,
#             'money': round(self.player.money, 2),
#             'stock_1_price': round(self.group.stock_1_price, 2),
#             'stock_2_price': round(self.group.stock_2_price, 2),
#             'stock_3_price': round(self.group.stock_3_price, 2),
#             'stock_4_price': round(self.group.stock_4_price, 2),
#             'stock_5_price': round(self.group.stock_5_price, 2),
#             'stock_6_price': round(self.group.stock_6_price, 2),
#             'stock_1_amount': self.player.stock_1_amount,
#             'stock_2_amount': self.player.stock_2_amount,
#             'stock_3_amount': self.player.stock_3_amount,
#             'stock_4_amount': self.player.stock_4_amount,
#             'stock_5_amount': self.player.stock_5_amount,
#             'stock_6_amount': self.player.stock_6_amount
#         }
#
#     def js_vars(self):
#         return dict(
#                    highcharts_series = [
#                        {
#                         'name' : 'stock_1_price',
#                         'data' :  [round(g.stock_1_price,2) for g in self.group.in_all_rounds()]
#                         }, {
#                         'name' : 'stock_2_price',
#                         'data' :  [round(g.stock_2_price,2) for g in self.group.in_all_rounds()]
#                         }, {
#                         'name' : 'stock_3_price',
#                         'data' :  [round(g.stock_3_price,2) for g in self.group.in_all_rounds()]
#                         }, {
#                         'name' : 'stock_4_price',
#                         'data' :  [round(g.stock_4_price,2) for g in self.group.in_all_rounds()]
#                         }, {
#                         'name' : 'stock_5_price',
#                         'data' :  [round(g.stock_5_price,2) for g in self.group.in_all_rounds()]
#                         }, {
#                         'name' : 'stock_6_price',
#                         'data' :  [round(g.stock_6_price,2) for g in self.group.in_all_rounds()]
#                         }
#                        ]
#                     )

class SellPage_sellable(Page):
    form_model = 'player'
    form_fields = ['stock_1_sell_amount', 'stock_2_sell_amount', 'stock_3_sell_amount', 'stock_4_sell_amount', 'stock_5_sell_amount', 'stock_6_sell_amount']

#%%   动态验证
    def stock_1_sell_amount_error_message(self, value):
        print('value is', value)
        if value > self.player.stock_1_amount:
            return 'Sell is over ownd.'

    def stock_2_sell_amount_error_message(self, value):
        print('value is', value)
        if value > self.player.stock_2_amount:
            return 'Sell is over ownd.'

    def stock_3_sell_amount_error_message(self, value):
        print('value is', value)
        if value > self.player.stock_3_amount:
            return 'Sell is over ownd.'

    def stock_4_sell_amount_error_message(self, value):
        print('value is', value)
        if value > self.player.stock_4_amount:
            return 'Sell is over ownd.'

    def stock_5_sell_amount_error_message(self, value):
        print('value is', value)
        if value > self.player.stock_5_amount:
            return 'Sell is over ownd.'

    def stock_6_sell_amount_error_message(self, value):
        print('value is', value)
        if value > self.player.stock_6_amount:
            return 'Sell is over ownd.'

###  动态验证END

#%%
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
            'money': format(round(self.player.money, 2), ','),
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
        self.player.stock_1_amount = self.player.stock_1_amount - self.player.stock_1_sell_amount
        self.player.stock_2_amount = self.player.stock_2_amount - self.player.stock_2_sell_amount
        self.player.stock_3_amount = self.player.stock_3_amount - self.player.stock_3_sell_amount
        self.player.stock_4_amount = self.player.stock_4_amount - self.player.stock_4_sell_amount
        self.player.stock_5_amount = self.player.stock_5_amount - self.player.stock_5_sell_amount
        self.player.stock_6_amount = self.player.stock_6_amount - self.player.stock_6_sell_amount

        self.player.money = self.player.money + \
                            self.player.stock_1_sell_amount * self.group.stock_1_price + \
                            self.player.stock_2_sell_amount * self.group.stock_2_price + \
                            self.player.stock_3_sell_amount * self.group.stock_3_price + \
                            self.player.stock_4_sell_amount * self.group.stock_4_price + \
                            self.player.stock_5_sell_amount * self.group.stock_5_price + \
                            self.player.stock_6_sell_amount * self.group.stock_6_price 


class BuyPage_buyable(Page):

    form_model = 'player'
    form_fields = ['stock_1_bid_amount', 'stock_2_bid_amount', 'stock_3_bid_amount', 'stock_4_bid_amount', 'stock_5_bid_amount', 'stock_6_bid_amount']

#%% 动态验证
    def error_message(self, values):
        print('values is', values)
        if  values['stock_1_bid_amount'] * self.group.stock_1_price + \
            values['stock_2_bid_amount'] * self.group.stock_2_price + \
            values['stock_3_bid_amount'] * self.group.stock_3_price + \
            values['stock_4_bid_amount'] * self.group.stock_4_price + \
            values['stock_5_bid_amount'] * self.group.stock_5_price + \
            values['stock_6_bid_amount'] * self.group.stock_6_price \
            > self.player.money:
            return 'Your Money is not enough'
### 动态验证END

    def is_displayed(player):
        return player.round_number > 4

    def vars_for_template(self):
         return {
            'round_number': self.round_number,
            'money': format(round(self.player.money, 2), ','),
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

        self.player.money = self.player.money - \
                    self.player.stock_1_bid_amount * self.group.stock_1_price - \
                    self.player.stock_2_bid_amount * self.group.stock_2_price - \
                    self.player.stock_3_bid_amount * self.group.stock_3_price - \
                    self.player.stock_4_bid_amount * self.group.stock_4_price - \
                    self.player.stock_5_bid_amount * self.group.stock_5_price - \
                    self.player.stock_6_bid_amount * self.group.stock_6_price 


class Clear(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.money = self.player.money + \
                            self.player.stock_1_amount * self.group.stock_1_price + \
                            self.player.stock_2_amount * self.group.stock_2_price + \
                            self.player.stock_3_amount * self.group.stock_3_price + \
                            self.player.stock_4_amount * self.group.stock_4_price + \
                            self.player.stock_5_amount * self.group.stock_5_price + \
                            self.player.stock_6_amount * self.group.stock_6_price
        return {
            'round_number': self.round_number,
            'money': format(round(self.player.money, 2), ',')
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


page_sequence = [ReadOnly, SellPage_sellable, BuyPage_buyable, Clear]