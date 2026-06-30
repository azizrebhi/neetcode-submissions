class TextProcessor:
    # Implement method overloading for format_text method
    def format_text (self,*args:str):
        if len(args)>1 :
          result = "".join(args)
          return result
        else : 
            return args[0].upper()
 



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
