from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SellPage_ReadOnly(Page):

    form_model = 'player'

    def is_displayed(player):
        return player.round_number in [1,2,3,4]

    def vars_for_template(self):
        self.player.update_money()
        self.player.update_stock_price()
        self.player.update_stock_1_amount()
        self.player.update_stock_2_amount()
        self.player.update_stock_3_amount()
        self.player.update_stock_4_amount()
        self.player.update_stock_5_amount()
        self.player.update_stock_6_amount()
        return {
            'round_number': self.round_number,
            'money': self.player.money,
            'stock_1_price': round(self.player.stock_1_price, 2),
            'stock_2_price': round(self.player.stock_2_price, 2),
            'stock_3_price': round(self.player.stock_3_price, 2),
            'stock_4_price': round(self.player.stock_4_price, 2),
            'stock_5_price': round(self.player.stock_5_price, 2),
            'stock_6_price': round(self.player.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount,
        }


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
            'stock_1_price': round(self.player.stock_1_price, 2),
            'stock_2_price': round(self.player.stock_2_price, 2),
            'stock_3_price': round(self.player.stock_3_price, 2),
            'stock_4_price': round(self.player.stock_4_price, 2),
            'stock_5_price': round(self.player.stock_5_price, 2),
            'stock_6_price': round(self.player.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount
        }

    # def before_next_page(self):
    #
    #     # print(f'???????????????{self.round_number}')
    #     # print(f'???????????????{self.subsession.stock_1}')
    #     # import random
    #     # self.subsession.stock_1 = self.subsession.stock_1 + c(random.randint(1, 3))
    #     # print(f'???????????????{self.subsession.stock_1}')
    #         print(f'???????????????{self.player.money}')
    #         self.player.money = self.player.money + c(10)
    #         print(f'??????????????????{self.player.money}')


class SellPage_sellable(Page):

    form_model = 'player'
    form_fields = ['stock_1_sell_amount', 'stock_2_sell_amount', 'stock_3_sell_amount', 'stock_4_sell_amount', 'stock_5_sell_amount', 'stock_6_sell_amount']

    def is_displayed(player):
        return player.round_number > 4

    def vars_for_template(self):
        self.player.update_money()
        self.player.update_stock_price()
        self.player.update_stock_1_amount()
        self.player.update_stock_2_amount()
        self.player.update_stock_3_amount()
        self.player.update_stock_4_amount()
        self.player.update_stock_5_amount()
        self.player.update_stock_6_amount()
        return {
            'round_number' : self.round_number,
            'money': self.player.money,
            'stock_1_price': round(self.player.stock_1_price, 2),
            'stock_2_price': round(self.player.stock_2_price, 2),
            'stock_3_price': round(self.player.stock_3_price, 2),
            'stock_4_price': round(self.player.stock_4_price, 2),
            'stock_5_price': round(self.player.stock_5_price, 2),
            'stock_6_price': round(self.player.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount
        }

    def before_next_page(self):
        self.player.stock_1_amount = self.player.stock_1_amount - self.player.stock_1_sell_amount
        self.player.stock_2_amount = self.player.stock_2_amount - self.player.stock_2_sell_amount
        self.player.stock_3_amount = self.player.stock_3_amount - self.player.stock_3_sell_amount
        self.player.stock_4_amount = self.player.stock_4_amount - self.player.stock_4_sell_amount
        self.player.stock_5_amount = self.player.stock_5_amount - self.player.stock_5_sell_amount
        self.player.stock_6_amount = self.player.stock_6_amount - self.player.stock_6_sell_amount



class BuyPage_buyable(Page):

    form_model = 'player'
    form_fields = ['stock_1_bid_amount', 'stock_2_bid_amount', 'stock_3_bid_amount', 'stock_4_bid_amount', 'stock_5_bid_amount', 'stock_6_bid_amount']

    def is_displayed(player):
        return player.round_number > 4

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
            'stock_1_price': round(self.player.stock_1_price, 2),
            'stock_2_price': round(self.player.stock_2_price, 2),
            'stock_3_price': round(self.player.stock_3_price, 2),
            'stock_4_price': round(self.player.stock_4_price, 2),
            'stock_5_price': round(self.player.stock_5_price, 2),
            'stock_6_price': round(self.player.stock_6_price, 2),
            'stock_1_amount': self.player.stock_1_amount,
            'stock_2_amount': self.player.stock_2_amount,
            'stock_3_amount': self.player.stock_3_amount,
            'stock_4_amount': self.player.stock_4_amount,
            'stock_5_amount': self.player.stock_5_amount,
            'stock_6_amount': self.player.stock_6_amount
        }
    def before_next_page(self):
        self.player.stock_1_amount = self.player.stock_1_amount + self.player.stock_1_bid_amount
        self.player.stock_2_amount = self.player.stock_2_amount + self.player.stock_2_bid_amount
        self.player.stock_3_amount = self.player.stock_3_amount + self.player.stock_3_bid_amount
        self.player.stock_4_amount = self.player.stock_4_amount + self.player.stock_4_bid_amount
        self.player.stock_5_amount = self.player.stock_5_amount + self.player.stock_5_bid_amount
        self.player.stock_6_amount = self.player.stock_6_amount + self.player.stock_6_bid_amount


page_sequence = [SellPage_ReadOnly, BuyPage_ReadOnly, SellPage_sellable, BuyPage_buyable]
