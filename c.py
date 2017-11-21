import sys
import psycopg2

connection = psycopg2.connect(database="coala", user = "fazley", password = "password", host = "127.0.0.1", port = "5432")
cursor = connection.cursor()

def sentInput():
    cursor.execute("select analysis from sentiment order by analysis_id desc limit 1")
    text_news = cursor.fetchall()
    connection.commit()
    return text_news

def techInput():
    cursor.execute("select output from technical order by output_id desc limit 1")
    output = cursor.fetchall()
    connection.commit()
    return output

def decisiontree(sent, tech):
    if sent == [('buy',)] and tech == [('buy',)]:
        decision = 'buy'
    if sent == [('buy',)] and tech == [('volatile',)]:
        decision = 'buy'
    else:
        decision = 'Nothing to do'
    return decision

sa = sentInput()
ta = techInput()


print('Sentiment : ', str(sa))
print('\nTechnical : ', str(ta))
decision = decisiontree(sa, ta)
print('\nFinal Decision: \n',decision)

connection.close()
cursor.close()