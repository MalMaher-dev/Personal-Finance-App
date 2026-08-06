import DB.connection as connection
import numpy as np
import matplotlib.pyplot as plt
import textwrap


def chart_Transactions(num):
    transactions = connection.getTransactions(num)
    retailers = []
    for h in transactions:
        if h[1] not in retailers:
            retailers.append(h[1])
    costPerRetailer = []

    for index in retailers:
        cost = 0
        for i in transactions:
            if i[1] == index:
                cost += float(i[2].split('$')[1])
        costPerRetailer.append([index.strip(" "), round(float(cost), 2)])

    x = []
    y = []

    for i in costPerRetailer:
        wrappedX = textwrap.fill(i[0], width=10)
        x = np.append(x, wrappedX)
        y = np.append(y, i[1])

    plt.figure(figsize=(7.5, 6))
    plt.ylabel("Money Spent ($)")
    plt.xlabel("Retailer")
    plt.title("Money Spent per Retailer")
    bars = plt.bar(x, y)
    plt.bar_label(bars)
    plt.show()

    plt.pie(y, labels=x, autopct=lambda p: '${:.2f}'.format(p * sum(y) / 100))
    plt.title("Money Spent as a whole")
    plt.show()

chart_Transactions(9521)