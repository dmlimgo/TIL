# ex 2-7
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)

# for country, _ in traveler_ids:
#     print(country)


# ex 2-8
# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]

# print('{:17} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:17} | {:^9.4f} | {:^9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     print(fmt.format(name, latitude, longitude))


# ex expression
# name = 'Jack'
# age = 10
# print(f'{name:10}{age}')
# print(f'{name!r:10}{age}')


# ex 2-10
# from collections import namedtuple

# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])
# print(City._fields)
# LatLong = namedtuple('LatLong', 'lat long')
# delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# delhi = City._make(delhi_data)
# print(delhi._asdict())


# 표 2-1
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# c = (7, 8, 9)
# d = ('x', 'y', 'z')
# a[1] = 5
# print(a)

# ex 2-11
# invoice = """
# 0.....6.............................36........46...52....
# 1909  Pimoroni PiBrella             $17.50    3    $52.50
# 1489  6mm Tactile Switch x20         $4.95    2     $9.90
# 1510  Panavise Jr. - PV-201         $28.00    1    $28.00
# 1601  PiFTF Mini Kit 320x240        $34.95    1    $34.95
# """

# SKU = slice(0, 6)
# DESCRIPTION = slice(6, 36)
# UNIT_PRICE = slice(36, 46)
# QUANTITY = slice(46, 51)
# ITEM_TOTAL = slice(51, None)
# line_items = invoice.split('\n')[2:-1]
# for item in line_items:
#     print(item[UNIT_PRICE], item[DESCRIPTION])

# ex
# l = list(range(10))
# l[3:6] = [100]
# print(l)
# del l[::4]
# print(l)

# ex 2-12, 2-13
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
board[1][0] = '*'
print(board)