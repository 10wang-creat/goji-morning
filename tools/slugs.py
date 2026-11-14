# -*- coding: utf-8 -*-
"""主題編號 -> 英文代號。新增一週時只要在這裡加一行。"""
import re
SLUG = {
 "01":"goji","02":"chrysanthemum","03":"jujube","04":"hawthorn","05":"gathering",
 "06":"winter-tonic","07":"ginger","08":"longan","09":"astragalus",
 "10":"angelica","11":"tangerine","12":"lotusseed","13":"newyear","14":"spring-festival",
 "15":"rose","16":"coix","17":"mint","18":"cassia","19":"honeysuckle","20":"spring-liver",
 "21":"poria","22":"lotusleaf","23":"lily","24":"guyu","25":"loquat","26":"mugwort",
 "27":"mungbean","28":"mume","29":"ophiopogon","30":"apricot","31":"dragonboat","32":"sanfu",
 "33":"coptis","34":"yam","35":"paozhi","36":"dashu","37":"euryale","38":"fritillaria",
 "39":"blacksesame","40":"honey","41":"chushu","42":"mulberryleaf","43":"schisandra","44":"walnut",
 "45":"midautumn","46":"ejiao","47":"malt","48":"eucommia","49":"shuangjiang","50":"cinnamon",
 "51":"heshouwu","52":"pumpkinseed","53":"lidong","54":"gastrodia",
}
CN = {"一":1,"二":2,"三":3,"四":4,"五":5}
def order(name):
    s = re.sub(r"^(星期|週|周)", "", name.strip())
    m = re.match(r"(\d+)", s)
    if m: return int(m.group(1))
    return CN.get(s[0], 99) if s else 99
def fkey(x):
    m = re.match(r"\d+", x)
    return (int(m.group()) if m else 99, x)
