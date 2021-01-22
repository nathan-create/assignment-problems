recommendClothing :: (RealFloat a) => a -> String
recommendClothing tempCelsius
    |tempFarenheit >= 80 = "I recommend a shortsleeve shirt"
    |tempFarenheit > 65 = "I recommend a longsleeve shirt"
    |tempFarenheit > 50 = "I recommend a sweater"
    |tempFarenheit <= 50 = "I recommend a jacket"
    where tempFarenheit = (tempCelsius * 9/5) + 32

main = print(recommendClothing 62)