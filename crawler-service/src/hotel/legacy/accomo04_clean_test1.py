import re
import pandas as pd
from pathlib import Path

def normalize_address(text: str) -> str:
    text = re.sub(r"\s+", "", text.replace("-", "之").replace(",", ""))
    text = re.sub(r"f", "樓", text, flags=re.IGNORECASE)
    city_pattern = r"(台北市|新北市|桃園市|台中市|台南市|高雄市|基隆市|新竹市|嘉義市|新竹縣|苗栗縣|彰化縣|南投縣|雲林縣|嘉義縣|屏東縣|台東縣|花蓮縣|宜蘭縣)"
    area_pattern = r"([\u4e00-\u9fa5]{2}(區|鄉|鎮|市))|北區|東區|南區|西區|中區|那瑪夏區|阿里山鄉|三地門鄉|太麻里鄉"
    text = re.sub(r"(台灣)?\d{3,6}$", "", text)
    text = re.sub(rf"^([0-9]{{3,6}})?台灣", "", text)
    text = re.sub(rf"({city_pattern})([0-9]{{3,5}})?", r"\1", text)
    text = re.sub(r"No\.?([0-9]+(?:之[0-9]+)?)", r"\1號", text, flags=re.IGNORECASE)
    text = re.sub(r"No", "", text, flags=re.IGNORECASE)
    if re.match(rf"^{city_pattern}", text):
        return text
    core = text
    floor_match = re.search(r"([0-9]+樓)(?:之[0-9]+)?", text)
    floor = floor_match.group(1) if floor_match else ""
    core = core.replace(floor, "")
    city = re.search(city_pattern, text)
    city_str = city.group(0) if city else ""
    core = core.replace(city_str, "")
    area = re.search(area_pattern, text)
    area_str = area.group(0) if area else ""
    core = core.replace(area_str, "")
    core = re.sub(r"(號)+", "號", core)
    no = re.search(r"[0-9]+(之[0-9]+)?號", text)
    no_str = no.group(0) if no else ""
    core = core.replace(no_str, "")
    return f"{city_str}{area_str}{core}{no_str}{floor}"

# 路徑設定與讀取
file_path = Path(__file__).resolve().parents[2] / "data" / "hotel" / "accomo03_extract_booking.csv"
data = pd.read_csv(file_path, encoding="utf-8", engine="python")

# 清理 address 欄位
data = data[~data["name"].isna()]
data["add_open"] = data["add_open"].astype(str).apply(normalize_address)
data["add"] = data["add"].astype(str).apply(normalize_address)

# 儲存清理後檔案
clean_path = Path(__file__).resolve().parents[2] / "data" / "hotel" / "accomo03_cleaned_booking.csv"
data.to_csv(clean_path, encoding="utf-8", header=True, index=False)
print("清理完成並儲存：", clean_path)