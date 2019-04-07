# bitcoinmningw-gas
It measures the profit that a miner can reach per day with natural gas given lots of external data that gets updated daily.

In the first computer where I run my node:

- It uses data from a gas sample to know how much power you can get from that gas sample
- With that information and the specs of a 400kw gas engine, it knows how much power it can produce for 165 miners with the highest Th/s in the market at each moment (44Th/s at the moment of writing this)
- It gets daily information about bitcoin prices and network hash-rate, as well as information from my node about blocks produced and bitcoins issued.
- This information is published by an API and available in a domain name.

The second computer:

- consumes the information from the 1st computer via API.
- Fills in an excel sheet where all the calculations are made.
- With this information a couple of macros are ran and we get from there the latest break-even $/mmBtu data, which is precisely the amount of USD/mmBtu that the gas producer can earn for his gas.
- This data gets published via twitter and eventually in a website.

