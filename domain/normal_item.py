from domain.stock_item import Stock_Item

class Normal_Item(Stock_Item):

    def update_quality(self):

        if self.get_sell_in() <= 0:
            self.set_quality()
        else:
            self.reduce_quality(1)

        self.decrease_sell_in()