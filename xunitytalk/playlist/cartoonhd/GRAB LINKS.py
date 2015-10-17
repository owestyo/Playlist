import urllib2,re,os

import json


 
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

FIRST='<poster>[B][COLOR cyan].[/COLOR][COLOR red]M[/COLOR][COLOR yellow]i[/COLOR][COLOR magenta]k[/COLOR][COLOR lime]e[/COLOR][COLOR white]y[/COLOR][COLOR orange]1[/COLOR][COLOR cyan]2[/COLOR][COLOR red]3[/COLOR][COLOR yellow]4[/COLOR] [COLOR magenta]P[/COLOR][COLOR lime]l[/COLOR][COLOR white]a[/COLOR][COLOR orange]y[/COLOR][COLOR cyan]L[/COLOR][COLOR red]i[/COLOR][COLOR yellow]s[/COLOR][COLOR magenta]t[/COLOR][/B]</poster>\n<thumbnail>https://raw.githubusercontent.com/MzDiobolik/Playlist/master/xunitytalk/icon.png</thumbnail>\n<fanart>https://raw.githubusercontent.com/MzDiobolik/Playlist/master/xunitytalk/fanart.jpg</fanart>\n\n'
f = open('playlist', mode='w')
f.write(FIRST)
f.close()


a=OPEN_URL('http://gappcenter.com/app/cartoon/mapi.php?action=getcategory&os=newiosfull&version=2.1&deviceid=537BE108497E67A84974CD560691D906&token=&time=&device=iphone')
link=json.loads(a)

data=link['Data']

for field in data:
    name= field['Name'].encode("utf-8")
    iconimage= field['Image'].encode("utf-8")
    
    action=field['Action'].encode("utf-8")
    if 'Top' in name:
        name='.[COLOR cyan]%s[/COLOR]'% name
    if 'Disney' in name:
        name='.[COLOR cyan]%s[/COLOR]'% name


        
    DIR='<name>%s</name>\n<link>https://raw.githubusercontent.com/MzDiobolik/Playlist/master/xunitytalk/playlist/cartoonhd/%s.xml</link>\n<thumbnail>%s</thumbnail>\n\n' % (name,action,iconimage)
    f = open('playlist', mode='a')
    f.write(DIR)
    f.close()
    
    SECOND='<poster>[B][COLOR cyan].[/COLOR][COLOR red]M[/COLOR][COLOR yellow]i[/COLOR][COLOR magenta]k[/COLOR][COLOR lime]e[/COLOR][COLOR white]y[/COLOR][COLOR orange]1[/COLOR][COLOR cyan]2[/COLOR][COLOR red]3[/COLOR][COLOR yellow]4[/COLOR] [COLOR magenta]P[/COLOR][COLOR lime]l[/COLOR][COLOR white]a[/COLOR][COLOR orange]y[/COLOR][COLOR cyan]L[/COLOR][COLOR red]i[/COLOR][COLOR yellow]s[/COLOR][COLOR magenta]t[/COLOR][/B]</poster>\n<thumbnail>https://raw.githubusercontent.com/MzDiobolik/Playlist/master/xunitytalk/icon.png</thumbnail>\n<fanart>https://raw.githubusercontent.com/MzDiobolik/Playlist/master/xunitytalk/fanart.jpg</fanart>\n\n'
    f = open(action+'.xml', mode='w')
    f.write(SECOND)
    f.close()
    new_url='http://gappcenter.com/app/cartoon/mapi.php?action=getlistcontent&cate=%s&pageindex=0&pagesize=1000&os=newiosfull&version=2.2&deviceid=537BE108497E67A84974CD560691D906&token=63EFF51FE2236915658D502AE089350C&time=1389744589&device=iphone'%action
    response=OPEN_URL(new_url)
    
    if not 'invalid token' in response:
        DATA=json.loads(response)

        data=DATA['Data']

        for field in data:
            name= field['Name'].encode("utf-8")
            iconimage= field['Image'].encode("utf-8")
            url=field['Link'].encode("utf-8")

            
            action_='<item>\n<title>%s</title>\n<link>%s</link>\n<thumbnail>%s</thumbnail>\n</item>\n\n'%(name,url,iconimage)
            f = open(action+'.xml', mode='a')
            f.write(action_)
            f.close() 
        

print 'FINISHED'
