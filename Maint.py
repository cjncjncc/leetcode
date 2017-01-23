# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://210.75.213.188/shh/portal/bjjs/index.aspx'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'

MonthPattern = re.compile('<!--月统计begin-->.*?<div class="tContent".*?</div>\s*?</div>',re.S)
StaLiPattern = re.compile('<li style.*?</div>\s*?</li>',re.S)
AgentPattern = re.compile('<tr>\s*?<td>\d</td>.*?</td>\s*?</tr>',re.S)
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    monthStats = re.findall(MonthPattern,content)
    if len(monthStats)== 0:
        print 'no month Stats'
    monthStr = monthStats[0]
    monthLi = re.findall(StaLiPattern,monthStr)
    agentResult = re.findall(AgentPattern,monthLi[0])
    print monthLi[0]
    print len(agentResult)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
except Exception, e:
        print e
