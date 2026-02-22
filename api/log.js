export default async function handler(req, res) {
    // 你的凭证
    const SUPABASE_URL = 'https://qxgwhtxwogstsjnuoacq.supabase.co';
    const SUPABASE_KEY = 'sb_publishable_VZixI6Z49NvH3O-zU-zcOw_LVgWhQgA';

    // 获取访问者的 IP 和 浏览器信息
    const ip = req.headers['x-forwarded-for'] || 'Unknown';
    const ua = req.headers['user-agent'] || 'Unknown';

    try {
        // 使用标准的 fetch 发送到 Supabase
        await fetch(`${SUPABASE_URL}/rest/v1/view_logs`, {
            method: 'POST',
            headers: {
                'apikey': SUPABASE_KEY,
                'Authorization': `Bearer ${SUPABASE_KEY}`,
                'Content-Type': 'application/json',
                'Prefer': 'return=minimal'
            },
            body: JSON.stringify({
                ip_address: ip.split(',')[0], // 只要第一个真实IP
                user_agent: ua
            })
        });

        // 成功返回
        res.status(200).json({ status: 'ok' });
    } catch (error) {
        // 即使报错也返回 200，保证前端能跳转
        res.status(200).json({ status: 'error' });
    }
}
