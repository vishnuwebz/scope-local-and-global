# 5 score tracker

# track scores with global and local scopes

high_score =  0
def update_score(new_score):
    global high_score
    if new_score > high_score:
        high_score =  new_score
    local_score = new_score # local
    return local_score, high_score

print(update_score(90))  # (90, 90)
print(update_score(70))  # (70, 90)

# Tracks high score globally, current score locally

