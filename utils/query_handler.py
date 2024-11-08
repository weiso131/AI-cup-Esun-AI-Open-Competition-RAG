import re

YEAR_PATTERN = r"[0-9一二三四五六七八九零]{3,4}年"
SEASON_PATTERN = r"[0-9一二三四]{1,2}季"
MONTH_PATTERN = r"[0-9]{1,2}月"

CHINESE_NUM = ['○', '一', '二', '三', '四', '五', '六', '七', '八', '九']

def extract_time(query: str) -> tuple:
    """
        回傳 年,季,月 (按照順序)，如果該項沒有則回傳空該項的 空list
    """
    for i in range(10):
        query = query.replace(CHINESE_NUM[i], str(i + 1))
    years_reg = re.findall(YEAR_PATTERN, query)
    seasons = re.findall(SEASON_PATTERN, query)
    months = re.findall(MONTH_PATTERN, query)
    
    years = []
    for year in years_reg:
        year_num = int(year.replace('年', ''))
        years.append(year)
        if year_num > 1911:
            years.append(str(year_num - 1911) + '年')
        else:
            years.append(str(year_num + 1911) + '年')


    
    seasons = [int(season.replace('季', '')  
                         .replace('一', '1')      
                         .replace('二', '2')
                         .replace('三', '3')
                         .replace('四', '4')) for season in seasons] if seasons else []
    months = [int(month.replace('月', '')) for month in months] if months else []
    
    return (years, seasons, months) 