"""
CCR network reachability test.
Tests which external endpoints are accessible from Anthropic's CCR cloud.
Run: python3 ccr_nettest.py
Results print to stdout (visible in CCR session output).
"""
import json, urllib.request

RAILWAY = 'https://web-production-eb831.up.railway.app'
DISCORD = 'https://discord.com/api/webhooks/1509646681979883670/VsGkMicnx-cj2Sr8CUJefuTGK-rx-f8Bsp1pVikRsRDTEAhutxknoWaQaHprvBvb7vku'
JSONBLOB = 'https://jsonblob.com/api/jsonBlob/019e80a6-3de9-7fcc-8495-fb3e48093bee'

results = []

def test(label, fn):
    try:
        result = fn()
        results.append(f'OK  {label}: {result}')
    except Exception as e:
        results.append(f'FAIL {label}: {e}')

# Railway GET
test('Railway GET /', lambda: urllib.request.urlopen(RAILWAY + '/', timeout=10).status)

# Railway POST log
def railway_post():
    payload = json.dumps({'user_id': 'baxter_test', 'content': 'CCR network test', 'date': '2026-06-01'}).encode()
    req = urllib.request.Request(RAILWAY + '/actions/log', data=payload, headers={'Content-Type': 'application/json'}, method='POST')
    return urllib.request.urlopen(req, timeout=10).status
test('Railway POST /actions/log', railway_post)

# jsonblob GET
test('jsonblob GET', lambda: json.loads(urllib.request.urlopen(JSONBLOB, timeout=10).read()).get('session'))

# Discord POST
def discord_post():
    payload = json.dumps({'content': 'CCR reachability test: ' + str([r[:30] for r in results])}).encode()
    req = urllib.request.Request(DISCORD, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'BaxterBot/1.0'}, method='POST')
    return urllib.request.urlopen(req, timeout=10).status
test('Discord POST webhook', discord_post)

print('=== CCR NETWORK REACHABILITY TEST ===')
for r in results:
    print(r)
print('=====================================')
