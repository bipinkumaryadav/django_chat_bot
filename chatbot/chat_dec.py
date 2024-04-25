def check_word(word):
    word_lst = ["Wine Glass (All purpose)", 'Red Balloon (for light-bodied red wines)', 'Beer Goblet', 'Beer Mugs',
                'Beer Pilsner', 'Beer Stout', 'Beer Tulip Stems', 'Belgian Beer Glass', 'Brandy Snifter',
                'Champagne Flute',
                'Cider Glass', 'Decanter', 'Dessert Wine Glass', 'Digestif Glass', 'English Pub Glass',
                'Giant Beer Glass',
                'Highball or Collins Glass', 'Iced Tea Glass', 'Juice Glass', 'Liqueur Glass', 'Margarita Glass',
                'Martini Glass',
                'Neat Spirit Glass', 'Old Fashioned Glass', 'Red Wine Glass', 'Shot Glass', 'Tom Collins Glass',
                'Water Goblet',
                'White Wine Glass', 'White Wine (Full Body Glass)', 'Side Bowl (250 ml)', 'Coffee Cup (100 ml)',
                'Dinner Plate (10")',
                'Half Plate (8")', 'Pasta Plate (8")', 'Quarter Plate (6")', 'Relish Plate', 'Salad Bowl (300 ml)',
                'Sauce Bowl (200 ml)',
                'Sauce Tray', 'Soup Bowl (250 ml)', 'Soup Cup (250 ml)', 'Soup Plate (8")', 'Tea Cup (200 ml)',
                'Vegetable Bow',
                'Baby Spoon (5.5" - 6.0")', 'Butter Knife (5.0" - 6.0")', 'Cheese Spoon (6.5" - 7.0")',
                'Coffee Spoon (4.5" - 5.0")',
                'Cream Spoon (4.5" - 5.0")', 'Dessert Fork (7.0" - 7.5")', 'Dessert Knife (8.0" - 8.5")',
                'Dessert Spoon (8.0" - 8.5")',
                'Dinner Knife (9.0" - 10.0")', 'Fish Fork (7.0" - 8.0")', 'Fish Knife (8.0" - 9.0")',
                'Fruit Fork (5.5" - 6.0")',
                'Fruit Knife (6.0" - 7.0")', 'Fruit Spoon (5.5" - 6.0")', 'Ham Fork (7.0" - 8.0")',
                'Icecream Spoon (6.0" - 6.5")',
                'Olive Spoon (6.0" - 6.5")', 'Rice Spoon (10.0" - 11.0")', 'Roast Fork (10.0" - 11.0")',
                'Salad Spoon & Fork (8.5" - 9.0")',
                'Serving Spoon & Fork (10.0" - 11.0")', 'Snail Forks (4.5" - 5.0")', 'Soup Spoon (7.0" - 7.5")',
                'Steak Knife (8.0" - 9.0")',
                'Sugar Spoon (5.5" - 6.0")', 'Sundae Spoon / Parfait Spoon (9.0" - 10.0")', 'Table Fork (8.0" - 8.5")',
                'Table Knife (8.0" - 8.5")',
                'Table Spoon (8.0" - 8.5")', 'Tea Spoon (5.0" - 5.5")', 'Pastry Fork (5.0" - 5.5")', 'Oyster Fork',
                'Bottle Cooler', 'Bud Vase',
                'Butter Dish', 'Cheese Dish', 'Coffee Pot', 'Creamer', 'Cruet Set', 'Egg Cup', 'Finger Bowl',
                'Ice Bucket', 'Ice cream Cup', 'Milk Pot',
                'Mustard Pot', 'Oil Vinegar Set', 'Sauce Boat', 'Soup Tureen', 'Sugar Bowl', 'Tea / Sugar Bags Holder',
                'Tea Pot', 'Water Jug',
                'Wine Cooler']
    rtn_lst = []
    for x in word_lst:
        if x.lower().find(word.lower()) >= 0:
            rtn_lst.append(x)

    return rtn_lst


if __name__ == '__main__':
    print(check_word("water"))

