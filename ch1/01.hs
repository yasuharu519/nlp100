main :: IO ()
-- main = putStrLn $ ["パタトクカシーー" !! x | x <- [1, 3, 5, 7]]
main = putStrLn $ map (\x -> "パタトクカシーー" !! x) [1, 3, 5, 7]
