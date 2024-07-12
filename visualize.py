import numpy as np
import matplotlib.pyplot as plt

f = open('block_arbitrage_info.txt', 'r')
lines = f.readlines()
f.close()

totalNumber = len(lines)


exchangeCount2 = 0
exchangeCount3 = 0
exchangeCount4 = 0
exchangeCount5More = 0
nCycleCount1 = 0
nCycleCount2 = 0
nCycleCount3More = 0

"""for line in lines:
    substring = 'n_cycles='
    position = line.find(substring)
    n_cycle = int(line[position+len(substring)])
    if n_cycle == 1:
        nCycleCount1 += 1
    if n_cycle == 2:
        nCycleCount2 += 1
    if n_cycle >= 3:
        nCycleCount3More += 1

print(str(nCycleCount1) + " " + str(round(nCycleCount1/totalNumber*100, 2)) + "%")
print(str(nCycleCount2) + " " + str(round(nCycleCount2/totalNumber*100, 2)) + "%")
print(str(nCycleCount3More) + " " + str(round(nCycleCount3More/totalNumber*100, 2)) + "%")"""


"""for line in lines:
    substring = 'ArbitrageCycleExchangeItem'
    count = line.count(substring)
    print(count)
    if count == 2:
        exchangeCount2 += 1
    if count == 3:
        exchangeCount3 += 1
    if count == 4:
        exchangeCount4 += 1
    if count >= 5:
        exchangeCount5More += 1

print(str(exchangeCount2) + "  " + str(round(exchangeCount2/73*100, 2)) + "%")
print(str(exchangeCount3) + "  " + str(round(exchangeCount3/73*100, 2)) + "%")
print(str(exchangeCount4) + "  " + str(round(exchangeCount4/73*100, 2)) + "%")
print(str(exchangeCount5More) + "  " + str(round(exchangeCount5More/73*100, 2)) + "%")


exchangeCountKinds = '2', '3', '4', '5+'
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
exchangeCountNums = [exchangeCount2, exchangeCount3, exchangeCount4, exchangeCount5More]
plt.pie(x=exchangeCountNums,
		labels=exchangeCountKinds,
		autopct="%3.1f%%",
		startangle=60,
		colors=colors)
plt.title('Exchange Count in Arbitrages')
plt.show()"""

"""tokens = {}

for line in lines:
    substring = 'profit_token='
    position = line.find(substring)
    if position != -1:
        token = line[position+len(substring):position+len(substring)+44]
        if token not in tokens:
            tokens[token] = 1
        else:
            tokens[token] += 1

for key in tokens.keys():
    print(key, tokens[key], str(round(tokens[key]/72*100, 2)) + "%")


tokenKinds = ['WETH', 'USDT', 'USDC', 'LINK', 'FRAX', 'Akita Inu', 'ONDO', 'DAI', 'Others']
tokensNums = [41, 15, 5, 1, 1, 1, 1, 2, 5]
plt.pie(labels=tokenKinds, x=tokensNums, autopct="%3.1f%%",)
plt.title('Tokens in Arbitrages')
plt.show()"""

"""
profitAmountList = []
for line in lines:
    profitAmountList.append(line['only_cycle']['profit_amount'])
x = list(range(len(profitAmountList)))
y = profitAmountList
plt.bar(x, y)
plt.show()

"""
amounts = []
for line in lines:
    substring1 = 'profit_amount='
    substring2 = 'profit_taker'
    position1 = line.find(substring1)
    position2 = line.find(substring2)
    if (position1 != -1) and (position2 != -1):
        amount = int(line[position1+len(substring1):position2-2])
        amounts.append(amount)
print(amounts)
x = list(range(len(amounts)))
plt.yscale('log')
plt.scatter(x, amounts)
plt.title('Profit Amount in Arbitrages')
plt.show()
"""
for key in tokens.keys():
    print(key, tokens[key], str(round(tokens[key]/72*100, 2)) + "%")


tokenKinds = ['WETH', 'USDT', 'USDC', 'LINK', 'FRAX', 'Akita Inu', 'ONDO', 'DAI', 'Others']
tokensNums = [41, 15, 5, 1, 1, 1, 1, 2, 5]
plt.pie(labels=tokenKinds, x=tokensNums, autopct="%3.1f%%",)
plt.title('Tokens in Arbitrages')
plt.show()
"""