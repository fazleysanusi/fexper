import sys
import psycopg2
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

connection = psycopg2.connect(database="coala", user = "fazley", password = "password", host = "127.0.0.1", port = "5432")
cursor = connection.cursor()

def insertprice(EUR_rate):
    price_id = None
    cursor.execute("insert into finance values (%s) returning price_id", (EUR_rate, ))
    price_id = cursor.fetchone()[0]
    connection.commit()
    return price_id
def oldprice(price_id):
    cursor.execute("select price from finance where price_id=(%s)", (price_id, ))
    price = cursor.fetchone()[0]
    connection.commit()
    return price
    
def output(new, old):
        if new > old :
            trend = 'Uptrend'
        if new < old :
            trend = 'Downtrend'
        if new == old :
            trend = 'volatile'

        output_id = None
        cursor.execute("insert into technical values (%s) returning output_id", (trend, ))
        output_id = cursor.fetchone()[0]
        connection.commit()
        return output_id
    
    

c = CurrencyRates()
d = CurrencyCodes()
# USD rate
rate = c.get_rates('USD')
# print(rate)

# get EUR price
EUR_rate = float(c.get_rate('EUR', 'USD'))

# display the rate EUR to USD
print('EUR Rate: ', d.get_symbol('USD'), EUR_rate)

price_id = insertprice(EUR_rate)

# display old price
oldprice = oldprice(insertprice(EUR_rate))
print('Previous EUR Rate: ', d.get_symbol('USD'), oldprice)

print('output id : ', output(EUR_rate, oldprice))


connection.close()
cursor.close()