"""
LeetCode 配置文件管理
"""
import os
import json
from pathlib import Path
from typing import Optional, Dict

# 项目根目录
ROOT_DIR = Path(__file__).parent.parent

# 配置文件路径
CONFIG_FILE = ROOT_DIR / ".leetcode_config.json"


def get_default_config() -> Dict:
    """获取默认配置"""
    return {
        "leetcode.com": {
            "base_url": "https://leetcode.com",
            "graphql_url": "https://leetcode.com/graphql",
            "api_url": "https://leetcode.com/api/problems/all/",
            "submit_url": "https://leetcode.com/problems/{slug}/submit/",
            "check_url": "https://leetcode.com/submissions/detail/{submission_id}/check/",
            "cookies": {
                "csrftoken": "",
                "LEETCODE_SESSION": ""
            }
        },
        "leetcode.cn": {
            "base_url": "https://leetcode.cn",
            "graphql_url": "https://leetcode.cn/graphql",
            "api_url": "https://leetcode.cn/api/problems/all/",
            "submit_url": "https://leetcode.cn/problems/{slug}/submit/",
            "check_url": "https://leetcode.cn/submissions/detail/{submission_id}/check/",
            "cookies": {
                "csrftoken": "",
                "LEETCODE_SESSION": ""
            }
        },
        "default_site": "leetcode.com"
    }


def load_config() -> Dict:
    """加载配置文件"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            # 合并默认配置，确保新字段存在
            default = get_default_config()
            for site in default:
                if site not in config:
                    config[site] = default[site]
                else:
                    for key in default[site]:
                        if key not in config[site]:
                            config[site][key] = default[site][key]
            return config
    return get_default_config()


def save_config(config: Dict) -> None:
    """保存配置文件"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


def get_site_config(site: str = None) -> Dict:
    """获取指定站点的配置"""
    config = load_config()
    site = site or config.get("default_site", "leetcode.com")
    return config.get(site, config.get("leetcode.com"))


def set_cookies(site: str, csrftoken: str, session: str) -> None:
    """设置站点 Cookie"""
    config = load_config()
    site_config = config.get(site, get_default_config()[site])
    site_config["cookies"]["csrftoken"] = csrftoken
    site_config["cookies"]["LEETCODE_SESSION"] = session
    config[site] = site_config
    save_config(config)
    print(f"已更新 {site} 的 Cookie 配置")


def set_default_site(site: str) -> None:
    """设置默认站点"""
    config = load_config()
    config["default_site"] = site
    save_config(config)
    print(f"已将默认站点设置为 {site}")


def get_cookies(site: str = None) -> Dict:
    """获取 Cookie"""
    site_config = get_site_config(site)
    return site_config.get("cookies", {})


def is_configured(site: str = None) -> bool:
    """检查是否已配置"""
    cookies = get_cookies(site)
    return bool(cookies.get("csrftoken") and cookies.get("LEETCODE_SESSION"))
