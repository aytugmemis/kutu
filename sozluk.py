None
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "TOXIC":"Bır miktar zehır bulunan organizma",
            "ONLINE":"Çevrim içi demek",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Bu sözlükte böyle bır kelime yok")
    # Kelime eşleşmiyorsa ne yapmalıyız?
    
