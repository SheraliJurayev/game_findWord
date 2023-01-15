# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:00:01 2023

@author: Sh_Jurayeff
"""

import random
from uzwords import words

def get_words():
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word :
        if letter in user_letters.upper():
            display_letter += letter
        else: 
            display_letter+='-'
    return display_letter
def play():
    word = get_words()
    word_letters=set(word)
    
    user_letters = ''
    print(f"Men {len(word)} xonali so'z o'yladim. Harflarini toping , men sizga so'zni aytaman. ")        
            
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
        letter=input("Krill alifbosida harf kiriitng: ").upper()
        if letter in user_letters:
            print("Siz bu harfni oldin kiritgansiz. Boshqa harf kiriting.")
            continue
        elif letter in word :
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri.")
        else:
            print("Bunday harf yo'q")
        user_letters+=letter
      
    print(f"Tabriklaymiz {word} so'zini {len(user_letters)} ta urinishda topdingiz.")   
    
play()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    