def positions_to_dict_of_positions_by_symbol(positions):
    positions_by_symbol = {}
    for position in positions:
        if not positions_by_symbol.get(position.symbol):
            positions_by_symbol[position.symbol] = []
        positions_by_symbol[position.symbol].append(position)

    return positions_by_symbol


def sort_positions_by_date(positions):
    positions.sort(key=lambda position: position.date)
