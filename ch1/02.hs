main :: IO ()
main = putStrLn $ concat $ map (\x -> (fst x):(snd x):[]) $ zip "パトカー" "タクシー"
