# ## HelloWorld
# print("Hello World")

# ## Định dạng chuỗi
# name = "Đình Hưng"
# age = "45"

# print(f"Hi there, my name is {name}, aged {age}")
# print("Hi there, my name is {}, aged {}",format(name,age))

s = """
    “My mom, my mom”, I know you're probably tired
Of hearin' 'bout my mom, oh-ho, whoa-ho
But this is just a story of when I was just a shorty
And how I became hooked on Va-aliu-um
Valium was in everything, food that I ate
The water that I drank, fuckin' peas in my plate
She sprinkled just enough of it to season my steak
So every day I'd have at least three stomachaches
Now tell me, what kind of mother would want to see her
Son grow up to be an undera-fuckin'-chiever?
My teacher didn't think I was gonna be nothin' either
"What the fuck you stickin' gum up under the fuckin' seat for?"
"Mrs. Mathers, your son has been huffin' ether
Either that or the motherfucker's been puffin' reefer"
But all this huffin' and puffin' wasn't what it was either
It was neither, I was buzzin' but it wasn't what she thought
Pee in a teacup? Bitch, you ain't my keeper, I'm sleepin'
What the fuck you keep on fuckin' with me for?
Slut, you need to leave me the fuck alone, I ain't playin'
Go find you a white crayon and color a fuckin' zebra!
"""
# Chuyển đoạn thơ thành danh sách các từ
words = s.split()

# Tạo một từ điển để đếm số lần xuất hiện của mỗi từ
word_count = {}
for word in words:
    # Làm sạch từ (loại bỏ dấu câu, chấm, dấu phẩy, ...)
    cleaned_word = word.strip(",.!?;:")
    # Đếm từ
    word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

# In số lần xuất hiện của mỗi từ
for word, count in word_count.items():
    print(f"{word}: {count} lần")