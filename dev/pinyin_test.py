from pypinyin import pinyin
from pypinyin import Style
from pypinyin.constants import PINYIN_DICT

print(pinyin('吗', style=Style.TONE3, heteronym=True))

PINYIN_DICT