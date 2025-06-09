import random

# Proof of Work validators with random power
miners = [
    {"name": "MinerA", "power": random.randint(1, 100)},
    {"name": "MinerB", "power": random.randint(1, 100)},
    {"name": "MinerC", "power": random.randint(1, 100)},
]

# Proof of Stake validators with random stake
stakers = [
    {"name": "StakerA", "stake": random.randint(1, 1000)},
    {"name": "StakerB", "stake": random.randint(1, 1000)},
    {"name": "StakerC", "stake": random.randint(1, 1000)},
]

# Delegates for DPoS with initial zero votes
delegates = [
    {"name": "DelegateA", "votes": 0},
    {"name": "DelegateB", "votes": 0},
    {"name": "DelegateC", "votes": 0},
]

# Voters voting randomly for delegates
voters = [
    {"name": "Voter1", "vote": None},
    {"name": "Voter2", "vote": None},
    {"name": "Voter3", "vote": None},
]

# Voting logic for DPoS
for voter in voters:
    chosen_delegate = random.choice(delegates)
    voter["vote"] = chosen_delegate["name"]
    chosen_delegate["votes"] += 1

# PoW: Select miner with highest power
pow_winner = max(miners, key=lambda x: x["power"])

# PoS: Select staker with highest stake
pos_winner = max(stakers, key=lambda x: x["stake"])

# DPoS: Select delegate with highest votes
max_votes = max(delegate["votes"] for delegate in delegates)
top_delegates = [d for d in delegates if d["votes"] == max_votes]
dpos_winner = random.choice(top_delegates)

# Output
print("Proof of Work Selection:")
print(f"Validators: {miners}")
print(f"Selected Miner: {pow_winner['name']} with power {pow_winner['power']}")
print("Selection logic: Validator with highest computing power wins the mining right.\n")

print("Proof of Stake Selection:")
print(f"Validators: {stakers}")
print(f"Selected Staker: {pos_winner['name']} with stake {pos_winner['stake']}")
print("Selection logic: Validator with highest stake is chosen to create the next block.\n")

print("Delegated Proof of Stake Selection:")
print(f"Delegates: {delegates}")
print("Voters and their votes:")
for voter in voters:
    print(f"  {voter['name']} voted for {voter['vote']}")
print(f"Selected Delegate: {dpos_winner['name']} with votes {dpos_winner['votes']}")
print("Selection logic: Delegates are voted in by stakeholders; delegate with most votes produces the block.\n")
