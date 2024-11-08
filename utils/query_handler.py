import re

YEAR_PATTERN = '[0-9]{3,4}年'
SEASON_PATTERN = '[0-9一二三]{1,2}季'
MONTH_PATTERN = '[0-9]{1,2}月'

def extract_time(query: str) -> tuple:
    """
        回傳 月,季,分 (按照順序)，如果該項沒有則回傳空該項的 空list
    """
    
    years = re.findall(YEAR_PATTERN, query)
    seasons = re.findall(SEASON_PATTERN, query)
    months = re.findall(MONTH_PATTERN, query)
    
    
    years = [int(year.replace('年', '')) for year in years] if years else []
    seasons = [int(season.replace('季', '')  
                         .replace('一', '1')      
                         .replace('二', '2')
                         .replace('三', '3')) for season in seasons] if seasons else []
    months = [int(month.replace('月', '')) for month in months] if months else []
    
    return (years, seasons, months) 