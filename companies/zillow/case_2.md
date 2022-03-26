Zillow Offers takes requests from Sellers N a day
Each day we evaluate these requests and try to come with a fee and a fair market value estimate for for each home
Use cases like: Marketing/etc
We wanted to come up with a metric that helped us prioritize which homes we would target
maximize total global fee -> considerations:
    (1) if "offer" is too low, we'll be told no and get 0 revenue therefore 0 fee -> we can't observe the counter factual
    (2) Golilocks -- offer got a yes and we were able to realize a "good" fee. We can observe this
    (3) if "offer" is too high, we take a loss. We can observe that.
    
    
    subject to a consideration around "fee risk" which is variance around fee.
    
    
Tools:
1) Conversion model (takes fee as input) outputs a probability of acceptance
3) Fee model (predicts the correct fee takes features about the home) outputs an expected fee, and an uncertainty on the fee
p(conversion) * fee +- the uncertainy from the fee model
