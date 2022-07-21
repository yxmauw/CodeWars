def duplicate_count(text):
    text = text.lower()
    if text == '':
        return 0
    else:
        dict = {char:0 for char in text}
        for letter in text:
            for key, value in dict.items():
                if key == letter:
                    dict[key] += 1    
        
        count = 0
        for i in dict:
            if dict[i] > 1:
                count += 1
        return count  
