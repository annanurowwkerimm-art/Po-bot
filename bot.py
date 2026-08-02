Python import time
from pocketoptionapi. stable_api import
PocketOption
api = PocketOption ("'annanurowwkerimm@gmail.com",
"kerimm0909" )
api. connect ()
ASSET = "EUR/USD"
degistirebilirsin
AMOUNT = 10
($)
DURATION = 60
dakika)
# sifti
# islem miktar1
# saniye (1
def sinyal():
status, candles =
api get_candles (ASSET, DURATION, 5)
ユf
not status:
return None
close = [c["close"] for c in
candles]
if close[-1l > close[-2]:
return "call"
# BUY
else:
return "put"
# SELL
while True: try:

yon = sinyal()

if yon:

status, deal =

api. buy (AMOUNT, ASSET, yon, DURATION)

print("ISLEM:"
, yon,
"I
ID: "
, deal, "| OK:" , status)

time. sleep (5)

except Exception
as e:

print("HATA:" , e)

time. sleep (10)

A SENIN_EMAILIN ve SENIN_SIFREN
