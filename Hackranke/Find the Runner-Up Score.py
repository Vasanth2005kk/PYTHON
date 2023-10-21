n = int(input("The score range:"))#normal printing statment
arr = list(map(int, input("Enter the score:").split()))
unique_scores = list(set(arr))
unique_scores.sort()
runner_up_score = unique_scores[-2]
print("The 2 maximum score:",runner_up_score)
