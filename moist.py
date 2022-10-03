test_cases = int(input())

for i in range(1, test_cases + 1):
    
    N = int(input())
    deck = []
    deck_sort1 = []
    deck_sort2 = []
    cost = 0
    
    for i in range(N):
        name = input()
        deck.append(name)
        
    for i in range(len(deck)):
        deck_sort1.append(deck[i])
        deck_sort2.append(deck[i])
        
        deck_sort1.sort()
        
        if deck_sort1 != deck_sort2:
            cost += 1
            deck_sort2.sort()
            
    print(f"Case #{test_cases}: {cost}")
        
