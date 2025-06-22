items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
  # Обчислюємо співвідношення калорій до вартості
  sorted_items = sorted(
    items.items(),
    key=lambda x: x[1]['calories'] / x[1]['cost'],
    reverse=True
  )

  selected = []
  total_cost = 0
  total_calories = 0

  for name, info in sorted_items:
    if total_cost + info['cost'] <= budget:
      selected.append(name)
      total_cost += info['cost']
      total_calories += info['calories']

  return selected, total_cost, total_calories


def dynamic_programming(items, budget):
  item_list = list(items.items())
  n = len(item_list)

  # dp[i][w] — максимальні калорії для перших i предметів з бюджетом w
  dp = [[0] * (budget + 1) for _ in range(n + 1)]

  # Побудова таблиці DP
  for i in range(1, n + 1):
    name, data = item_list[i - 1]
    cost = data['cost']
    calories = data['calories']
    for w in range(budget + 1):
      if cost <= w:
        dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
      else:
        dp[i][w] = dp[i - 1][w]

  # Відновлення вибраних страв
  w = budget
  selected = []
  for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
      name, data = item_list[i - 1]
      selected.append(name)
      w -= data['cost']

  total_calories = dp[n][budget]
  total_cost = sum(items[name]['cost'] for name in selected)

  return selected[::-1], total_cost, total_calories  # порядок прямий


if __name__ == '__main__':
  budget = 100

  greedy_result = greedy_algorithm(items, budget)
  print("Greedy algorithm result:")
  print(f"Selected: {greedy_result[0]}")
  print(f"Total cost: {greedy_result[1]}")
  print(f"Total calories: {greedy_result[2]}")

  dp_result = dynamic_programming(items, budget)
  print("\nDynamic Programming result:")
  print(f"Selected: {dp_result[0]}")
  print(f"Total cost: {dp_result[1]}")
  print(f"Total calories: {dp_result[2]}")