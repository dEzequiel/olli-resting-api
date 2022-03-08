from repository.get_all_items import get_all_items


def get_item_by_sell_in(sell_in):
    items = list(filter(lambda item: item['sell_in'] == sell_in, get_all_items()))
    return items if len(items) != 0 else f"Items with sell_in={sell_in} not found"
