from ..models import Stocks


def save_stocks(data):
    for datum in data:

        try:
            stock = Stocks.objects.get(ticker=datum['ticker'])
            if stock.name != datum['name']:
                stock.name = datum['name']
            if stock.shares_outstanding != datum['shares_outstanding']:
                stock.shares_outstanding = datum['shares_outstanding']
            stock.save()
            print(f"Updated {datum['ticker']}")
        except:
            try:
                Stocks.objects.create(ticker=datum['ticker'],
                                              name=datum['name'],
                                              shares_outstanding=datum['shares_outstanding'])
                print(f"Created {datum['ticker']}")
            except Exception as e:
                print(f"Failed saving {datum['ticker']}", e)