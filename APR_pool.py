# Початкові значення
initial_reward = 2106454.922187443855136000  # Початкова кількість токенів для першої епохи
DURATION = 86400  # Тривалість епохи в секундах (7 днів)
totalSuppl = (1095778714626074990914 / 1000000000000000000) * 9957  # Загальний обсяг
epochs_per_year = 52  # Кількість епох у році (тижнів)

# Список для зберігання винагород і rewardRate для кожної епохи
epoch_rewards = []
reward_rates = []

# Поточна кількість токенів для розподілу
current_reward = initial_reward

# Розрахунок для кожної епохи
for epoch in range(epochs_per_year):
    # Обчислюємо rewardRate для поточної епохи
    reward_rate = current_reward / DURATION
    reward_rates.append(reward_rate)

    # Винагорода за епоху (токени, розподілені за 7 днів)
    epoch_reward = current_reward
    epoch_rewards.append(epoch_reward)

    # Виводимо інформацію про епоху
    print(f"Epoch {epoch + 1}: Reward = {epoch_reward}, RewardRate = {reward_rate:.8f} tokens/sec")

    # Зменшуємо кількість токенів на 1% для наступної епохи
    current_reward = int(current_reward * 0.99)

# Обчислюємо загальну річну винагороду
yearly_reward = sum(epoch_rewards)
print(f"Yearly Reward: {yearly_reward}")

# Обчислюємо APR
apr = (yearly_reward / totalSuppl) * 100
print(f"APR: {apr:.10f}%")