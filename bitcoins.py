investment_in_bitcoin = 1.2
bitcoin_to_usd = 70000

def bitcoinToUSD(bitcoin_amount,bitcoin_value_usd):
  usd_value = bitcoin_amount * bitcoin_value_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
print ("Value in bitcoin : ",investment_in_bitcoin)
print ("Value in : $",investment_in_usd)

if investment_in_usd <= 30000 :
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")

