# save car_list to db

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Car
from config import Config

# 建立資料庫連線
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)

# 建立 Session 類別
Session = sessionmaker(bind=engine)

# 建立 Session 物件
session = Session()

# 從文件中載入 JSON 數據
with open('cars.json', 'r') as f:
    data = json.load(f)

# 將 JSON 數據轉換為 Car 物件並添加到 session
for item in data:
    car = Car(
        name=item['name'],
        seat_number=item['seat'],
        door_number=item['door'],
        body=item['body'],
        displacement=item['displacement'],
        car_length=item['car_length'],
        wheelbase=item['wheelbase'],
        power_type=item['power_type'],
        brand=item['brand'],
        model=item['model'],
    )
    session.add(car)

# 提交 session
session.commit()

# 關閉 session
session.close()
