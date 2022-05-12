### Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice? (Wikipedia)

I was watching *Survivor* S42E10 last night, and was intrigued by the Do or Die twist. I had heard of the Monty Hall problem before, and the setup was similar to it, but instead of goats and a car, it was fire and a skull. The Monty Hall problem is infamous for causing a debate in the mathematic and statistical world. While it's common knowledge now that switching provides better odds of winning, I wanted to make a Python simulation to prove this. 

The Python script is short and sweet. It has a predefined number of simulations to run (I ran 1,000) and the option to switch doors or not. Here are the findings:

```
n=1000
Switching Wins: 681
Switching Losses: 1000
Switching Win %: 68
```

```
n=1000
Staying Wins: 347
Staying Losses: 1000
Staying Win %: 35
```

The findings of the simulation corrobate the statistical analysis of the problem. Switching your selection when faced in a Monty Hall-esque scenario increases your odds of winning. Just a future note to myself if I ever make it to *Survivor*. :)
