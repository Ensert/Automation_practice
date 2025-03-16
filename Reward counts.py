from decimal import Decimal
min_reward = 1340.398449697542664582
min_reward = Decimal(min_reward)
print(min_reward)
Epoch_reward = Decimal(min_reward  * 60 * 24)
print(Epoch_reward)
Year_reward = Decimal(Epoch_reward * 52)
print(Year_reward)


# 1340,398449697542664582