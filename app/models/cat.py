from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]



# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             color=self.color,
#             personality=self.personality
#             )

# cats = [
#     Cat(1, "Luna", "black/white", "lazy"),
#     Cat(2, "Simon", "black", "might be a human stuck in a cats body"),
#     Cat(3, "Midnight", "black", "git skittish"),
#     Cat(4, "Leo", "grey tabby", "friendly"),
#     Cat(5, "Ash", "grey", "tabby"),
#     Cat(6, "alder", "auburn", "jumpy"),
#     Cat(7, "Morty", "orange", "orange"),
#     Cat(8, "fluffy", "white", "evil with a hint of benevolent"),
#     Cat(9, "Reginold", "orange", "only has one brain cell, but is descendent of Reginold the Great Tabby"),
#     Cat(10, "Katosa", "gray tabby", "Crazy Hunter"),
#     Cat(11, "Milly", "Tortoiseshell", "Loves you a lot but will probably sneeze all over you"),
#     Cat(12, "Meryl", "Tortoiseshell", "Bossy but tries to pass as the sweet one"),
#     Cat(13, "Zelda", "white, gray", "a mystery"),
#     Cat(14, "Jupiter", "orange", "socially selective"),
# ]
