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

for line in lines:
    if len(line['cycle']) == 2:
        exchangeCount2 += 1
    elif len(line['cycle']) == 3:
        exchangeCount3 += 1
    elif len(line['cycle']) == 4:
        exchangeCount4 += 1
    elif len(line['cycle']) >= 5:
        exchangeCount5More += 1

print(str(exchangeCount2) + "  " + str(round(exchangeCount2/totalNumber*100, 2)) + "%")
print(str(exchangeCount3) + "  " + str(round(exchangeCount3/totalNumber*100, 2)) + "%")
print(str(exchangeCount4) + "  " + str(round(exchangeCount4/totalNumber*100, 2)) + "%")
print(str(exchangeCount5More) + "  " + str(round(exchangeCount5More/totalNumber*100, 2)) + "%")

exchangeCountKinds = '2', '3', '4', '5+'
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
exchangeCountNums = [exchangeCount2, exchangeCount3, exchangeCount4, exchangeCount5More]
plt.pie(x=exchangeCountNums,
		labels=exchangeCountKinds,
		autopct="%3.1f%%",
		startangle=60,
		colors=colors)
plt.show()

tokens = {}
for line in lines:
    if not line['only_cycle']['profit_token'] in tokens.keys():
        tokens[line['only_cycle']['profit_token']] = 1
    else:
        tokens[line['only_cycle']['profit_token']] += 1

tokenKinds = tokens.keys()
tokensNums = tokens.values()
plt.pie(tokensNums,tokenKinds)
plt.show()

profitAmountList = []
for line in lines:
    profitAmountList.append(line['only_cycle']['profit_amount'])
x = list(range(len(profitAmountList)))
y = profitAmountList
plt.bar(x, y)
plt.show()



