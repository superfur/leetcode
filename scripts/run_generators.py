import os
import subprocess
import sys

def main():
    """主函数"""
    # 确保scripts目录存在
    os.makedirs("scripts", exist_ok=True)
    
    # 安装必要的Python包
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
    
    # 运行问题获取脚本
    print("正在获取LeetCode问题列表...")
    subprocess.run([sys.executable, "scripts/fetch_problems.py"], check=True)
    
    # 运行解法生成脚本
    print("正在生成各种语言的解法...")
    subprocess.run([sys.executable, "scripts/generate_solutions.py"], check=True)
    
    print("生成完成！")

if __name__ == "__main__":
    main() 