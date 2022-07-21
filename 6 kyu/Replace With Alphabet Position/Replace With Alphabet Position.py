def alphabet_position(text):
    if len(text) == 0:
        return ''
    else:
        text = text.lower()
        low_text = [s for s in text if s.isalpha()]
        num_text = ' '.join([str(ord(s)-96) for s in low_text]) 
        return num_text
