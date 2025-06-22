import random
import matplotlib.pyplot as plt

# Аналітичні ймовірності (у відсотках)
theoretical_probs = {
  2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
  7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}


def simulate_dice_rolls(num_rolls=100_000):
  results = {total: 0 for total in range(2, 13)}

  for _ in range(num_rolls):
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    results[roll_sum] += 1

  # Переводимо в ймовірності
  probabilities = {
    total: (count / num_rolls) * 100 for total, count in results.items()
  }
  return probabilities


# Симуляція
simulated_probs = simulate_dice_rolls()

# Вивід таблиці
print(f"{'Сума':^6} | {'Імовірність (симуляція)':^27} | {'Аналітична':^15}")
print("-" * 54)
for total in range(2, 13):
  sim = simulated_probs[total]
  theo = theoretical_probs[total]
  print(f"{total:^6} | {sim:>10.2f}% {'':<15} | {theo:>8.2f}%")

# Побудова графіку
x = list(range(2, 13))
sim_y = [simulated_probs[val] for val in x]
theo_y = [theoretical_probs[val] for val in x]

plt.figure(figsize=(10, 5))
plt.bar(x, sim_y, width=0.4, label="Симуляція", align="center", color="#69b3a2")
plt.plot(x, theo_y, marker='o', color='red', linestyle='--', label="Аналітична")
plt.xticks(x)
plt.xlabel("Сума")
plt.ylabel("Імовірність (%)")
plt.title("Імовірності сум при киданні двох кубиків")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()