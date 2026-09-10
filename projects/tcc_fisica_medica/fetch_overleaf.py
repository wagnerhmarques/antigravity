import urllib.request
import urllib.parse
import json
import re
import http.cookiejar

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "https://www.overleaf.com/read/mfdyzfxvctqw"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
resp = opener.open(req)
html = resp.read().decode('utf-8')

csrf_match = re.search(r'name="ol-csrfToken"\s+content="([^"]+)"', html)
csrf = csrf_match.group(1)

grant_url = "https://www.overleaf.com/read/mfdyzfxvctqw/grant"
post_data = json.dumps({'_csrf': csrf}).encode('utf-8')
grant_req = urllib.request.Request(grant_url, data=post_data, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Referer': url,
    'X-Csrf-Token': csrf,
    'Content-Type': 'application/json'
})
grant_resp = opener.open(grant_req)
grant_json = grant_resp.read().decode('utf-8')
print("Grant JSON:", grant_json)

data = json.loads(grant_json)
if 'project_id' in data:
    proj_id = data['project_id']
elif 'redirect' in data:
    proj_id = data['redirect'].split('/')[-1]
else:
    proj_id = None

print("Proj ID:", proj_id)
if proj_id:
    zip_url = f"https://www.overleaf.com/project/{proj_id}/download/zip"
    zip_req = urllib.request.Request(zip_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    zip_resp = opener.open(zip_req)
    zip_data = zip_resp.read()
    print("Downloaded zip size:", len(zip_data))
    with open("/Users/user/.gemini/antigravity-ide/scratch/overleaf_project.zip", "wb") as f_out:
        f_out.write(zip_data)
    print("Saved!")
