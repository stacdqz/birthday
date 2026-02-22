from http.server import BaseHTTPRequestHandler
import json
import requests
import os

# 这里的凭证建议在 Vercel 后台设置环境变量，或者直接写在这里（注意安全）
SUPABASE_URL = 'https://qxgwhtxwogstsjnuoacq.supabase.co'
SUPABASE_KEY = 'sb_publishable_VZixI6Z49NvH3O-zU-zcOw_LVgWhQgA'

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. 获取访问者的 IP (Vercel 会在 Header 里提供)
        ip = self.headers.get('x-forwarded-for', 'Unknown').split(',')[0]
        ua = self.headers.get('user-agent', 'Unknown')

        # 2. 调用 Supabase 的 REST API 写入数据
        # 后端直接连 Supabase，不需要 VPN，且速度极快
        url = f"{SUPABASE_URL}/rest/v1/view_logs"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }
        payload = {"ip_address": ip, "user_agent": ua}
        
        try:
            requests.post(url, json=payload, headers=headers, timeout=5)
        except Exception as e:
            print(f"Error: {e}")

        # 3. 返回成功响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())

