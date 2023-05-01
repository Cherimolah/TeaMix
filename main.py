from loader import app
import routing  # Импорт всех ссылок
import uvicorn
from PIL import Image


class A(list):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(A)


A()

for i in range(1, 7):
    image = Image.open(f"data/tiles/{i}.jpg")
    new_imga = image.resize((50, 50))
    new_imga.save(f"data/tiles/{i}.jpg")


if __name__ == '__main__':
    uvicorn.run(app)
