import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minerals_project.settings')
django.setup()

from minerals.models import Mineral

minerals_data = [
    {"name": "Нефть", "extraction_url": "https://datawrapper.dwcdn.net/7MpOL/3/",  "reserves_url": "https://datawrapper.dwcdn.net/sTFXf/1/"},
    {"name": "Природный газ", "extraction_url": "https://datawrapper.dwcdn.net/Ruakl/1/",  "reserves_url": "https://datawrapper.dwcdn.net/GtVXT/2/"},
    {"name": "Уголь", "extraction_url": "https://datawrapper.dwcdn.net/0ejBn/1/",  "reserves_url": "https://datawrapper.dwcdn.net/Qvp52/2/"},
    {"name": "Железная руда", "extraction_url": "https://datawrapper.dwcdn.net/qwsUF/1/",  "reserves_url": "https://datawrapper.dwcdn.net/Lh5Y8/1/"},
    {"name": "Уран", "extraction_url": "https://datawrapper.dwcdn.net/yAsaP/1/",  "reserves_url": "https://datawrapper.dwcdn.net/6kw4r/1/"},
    {"name": "Марганцевые руды", "extraction_url": "https://datawrapper.dwcdn.net/SwKQK/1/",  "reserves_url": "https://datawrapper.dwcdn.net/FUv2Z/1/"},
    {"name": "Хромовые руды", "extraction_url": "https://datawrapper.dwcdn.net/dVReA/1/",  "reserves_url": "https://datawrapper.dwcdn.net/8CgZ9/2/"},
    {"name": "Бокситы", "extraction_url": "https://datawrapper.dwcdn.net/wxHvl/1/",  "reserves_url": "https://datawrapper.dwcdn.net/LcqL5/1/"},
    {"name": "Нефелиновые руды", "extraction_url": "https://datawrapper.dwcdn.net/ye2Tu/1/",  "reserves_url": "https://datawrapper.dwcdn.net/oHytr/1/"},
    {"name": "Медь", "extraction_url": "https://datawrapper.dwcdn.net/V7W7l/1/",  "reserves_url": "https://datawrapper.dwcdn.net/Gc465/1/"},
    {"name": "Никель", "extraction_url": "https://datawrapper.dwcdn.net/9txGM/2/",  "reserves_url": "https://datawrapper.dwcdn.net/MTuyn/1/"},
    {"name": "Кобальт", "extraction_url": "https://datawrapper.dwcdn.net/O7X8g/1/",  "reserves_url": "https://datawrapper.dwcdn.net/UhhkY/1/"},
    {"name": "Свинец", "extraction_url": "https://datawrapper.dwcdn.net/Rl0In/1/",  "reserves_url": "https://datawrapper.dwcdn.net/dqwwk/1/"},
    {"name": "Цинк", "extraction_url": "https://datawrapper.dwcdn.net/1ZEg4/1/",  "reserves_url": "https://datawrapper.dwcdn.net/gnace/1/"},
    {"name": "Олово", "extraction_url": "https://datawrapper.dwcdn.net/V30UE/1/",  "reserves_url": "https://datawrapper.dwcdn.net/EkRJk/1/"},
    {"name": "Вольфрам", "extraction_url": "https://datawrapper.dwcdn.net/VMBOP/1/",  "reserves_url": "https://datawrapper.dwcdn.net/g618s/1/"},
    {"name": "Молибден", "extraction_url": "https://datawrapper.dwcdn.net/dYcPB/1/",  "reserves_url": "https://datawrapper.dwcdn.net/UxCyB/1/"},
    {"name": "Титан", "extraction_url": "https://datawrapper.dwcdn.net/kL7Ge/1/",  "reserves_url": "https://datawrapper.dwcdn.net/zTbQb/1/"},
    {"name": "Цирконий", "extraction_url": "https://datawrapper.dwcdn.net/gcC3P/1/",  "reserves_url": "https://datawrapper.dwcdn.net/ia1mb/1/"},
    {"name": "Литий", "extraction_url": "https://datawrapper.dwcdn.net/auJP1/1/",  "reserves_url": "https://datawrapper.dwcdn.net/Pph19/1/"},
    {"name": "Редкоземельные металлы", "extraction_url": "https://datawrapper.dwcdn.net/ChGW2/1/",  "reserves_url": "https://datawrapper.dwcdn.net/UYnKi/1/"},
    {"name": "Скандий", "extraction_url": "https://datawrapper.dwcdn.net/eVvPU/1/",  "reserves_url": "https://datawrapper.dwcdn.net/eVvPU/1/"},
    {"name": "Золото", "extraction_url": "https://datawrapper.dwcdn.net/HgIvs/1/",  "reserves_url": "https://datawrapper.dwcdn.net/HgIvs/1/"},
    {"name": "Серебро", "extraction_url": "https://datawrapper.dwcdn.net/w6iKR/1/",  "reserves_url": "https://datawrapper.dwcdn.net/PNVH6/1/"},
    {"name": "Платиноиды", "extraction_url": "https://datawrapper.dwcdn.net/5KRHv/1/",  "reserves_url": "https://datawrapper.dwcdn.net/saY8t/1/"},
    {"name": "Алмазы", "extraction_url": "https://datawrapper.dwcdn.net/l9Hkx/1/",  "reserves_url": "https://datawrapper.dwcdn.net/lJr3M/1/"},
    {"name": "Графит", "extraction_url": "https://datawrapper.dwcdn.net/2hTzR/1/",  "reserves_url": "https://datawrapper.dwcdn.net/ZZThZ/1/"},
    {"name": "Апатитовые руды", "extraction_url": "https://datawrapper.dwcdn.net/5vkFD/1/",  "reserves_url": "https://datawrapper.dwcdn.net/Pjm4R/1/"},
    {"name": "Фосфоритовые руды", "extraction_url": "https://datawrapper.dwcdn.net/QHXv0/1/",  "reserves_url": "https://datawrapper.dwcdn.net/dwjms/1/"},
    {"name": "Калийные соли", "extraction_url": "https://datawrapper.dwcdn.net/0MU9j/1/",  "reserves_url": "https://datawrapper.dwcdn.net/jae2A/1/"},
    {"name": "Плавиковый шпат", "extraction_url": "https://datawrapper.dwcdn.net/2WVlT/1/",  "reserves_url": "https://datawrapper.dwcdn.net/lSkmx/1/"},
    {"name": "Цементное сырьё", "extraction_url": "https://datawrapper.dwcdn.net/PN0dq/1/"},
]

for data in minerals_data:
    Mineral.objects.get_or_create(**data)

print("Данные успешно добавлены в базу!")