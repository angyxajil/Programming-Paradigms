factorial a = case a > 0  of
    True -> product [1..a]
    False -> 1

main = print(factorial 0)