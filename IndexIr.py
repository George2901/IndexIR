import urllib.request, urllib.parse, urllib.error, http.client, re, urllib.request, urllib.error, urllib.parse, time, sys
userAGE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', userAGE)]
sitelist = []
comp = []
 
def header():
	print("""
  ########    ####  ##        ##    ######      ##########  
  ##     ##    ##   ###       ##  ##           ##        ##
  ##     ##    ##   ####      ##  ##           ##        ##
  ########     ##   ##  ##    ##  ##   ######  ##        ##
  ##     ##    ##   ##    ##  ##  ##     ##    ##        ##
  ##     ##    ##   ##      ####  ##     ##    ##        ##
  ########    ####  ##        ##   #######      ##########   

   _______BINGO v1.0-site collector using bing dork_________
                         *********gretz to all member of ICH             
""") 

def dorker(dork,pages):
    d = urllib.parse.quote(dork)
    p = 1
    m = pages * 10
    while p <= m:
        try:
            search = "http://www.bing.com/search?q=" + d +"&first=" + str(p)
            req = opener.open(search)
            source = req.read().decode('utf-8')
            sites = re.findall('<h2><a href="http://(.*?)"', source)
            sitelist.extend(sites)
            p += 10
        except urllib.error.URLError:
            print ("url error")
            continue
        except urllib.error.HTTPError:
            print ("http error")
            continue
        except IOError:
            continue
        except http.client.HTTPException:
            continue
    uniqsites = list(set(sitelist))  
    for line in uniqsites:
        sep = '/'
        build = "http://" + line.split(sep,1)[0]
        comp.append(build)
        print(build)
    final1 = list(set(comp))
    l = "results" + str(len(final1)) + ".txt"
    foo = open(l,"w")
    for ss in final1:
        foo.write(ss + "\n")
    foo.close()
    
    print("[OK] saved as " + l)
    
    
header()

dr = input('Type Your dork :: ')
numpages = int(input(' Number of pages to look for  :: '))
print('[>] Searching ... ')
dorker(dr, numpages)
