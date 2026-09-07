-- 코드를 작성해주세요
select sum(PRICE)
from ITEM_INFO
where RARITY in ('LEGEND')
