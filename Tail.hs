take' :: (Num i, Ord i) => i -> [a] -> [a]  
take' n _  
    | n <= 0   = []  
take' _ []     = []  
take' n (x:xs) = x : take' (n-1) xs

reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x:xs) = (reverseList xs) ++ [x]

tail' :: (Num i, Ord i) => i -> [a] -> [a]  
tail' n _
    | n <= 0 = []
tail' _ [] = []
tail' n l = reverse ( take' n (reverseList l))
main = print(tail' 4 [8,3,-1,2,-5,7])