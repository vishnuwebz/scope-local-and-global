# 1 counter application

def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = create_counter()
print(counter())
print(counter())
"""
1
2
"""

# uses a closure with nonlocal to maintain count across calls, simulating a stateful counter for a web app.