import re
from pathlib import Path

def get_tracked_files(yaml_path):
    """步驟 1：萃取 _toc.yml 中已註冊的檔案路徑"""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'-\s*file:\s*([^\n\r]+)', content)
    tracked = set()
    for m in matches:
        clean_path = m.strip().strip('"\'')
        clean_path = re.sub(r'\.(ipynb|md)$', '', clean_path)
        tracked.add(clean_path)
    return tracked

def get_disk_files_map(base_path, folders_to_check):
    """步驟 2：掃描硬碟，建立 {乾淨路徑: 完整路徑} 的對照字典"""
    disk_files_map = {}
    for folder in folders_to_check:
        path = Path(base_path) / folder
        for file in path.rglob('*'):
            if file.suffix in ['.ipynb', '.md']:
                # 取得乾淨路徑作為 Key
                clean_path = file.with_suffix('').as_posix()
                # 取得帶副檔名的完整路徑作為 Value
                full_path = file.as_posix()
                disk_files_map[clean_path] = full_path
    return disk_files_map

def generate_title(file_path):
    """步驟 3：從檔名自動生成友善的標題"""
    # 取得檔名（不含路徑與副檔名）
    filename = Path(file_path).stem
    # 將底線替換為空白，幫助排版美觀
    title = filename.replace('_', ' ')
    return title

if __name__ == "__main__":
    yaml_file = '_toc.yml'
    target_folders = ['01_Derivations', '02_Concepts','03_Intuitions'] 
    
    print("🔍 開始盤點並比對檔案...\n")
    
    tracked_set = get_tracked_files(yaml_file)
    disk_map = get_disk_files_map('.', target_folders)
    
    # 找出在硬碟字典中，但不在 YAML 集合中的 Key
    forgotten_keys = set(disk_map.keys()) - tracked_set
    
    if not forgotten_keys:
        print("✅ 太棒了！沒有發現遺漏的檔案。")
    else:
        print(f"⚠️ 發現 {len(forgotten_keys)} 個未登記檔案，準備將其寫入 _toc.yml 底部...")
        
        # 步驟 4：使用 'a' (Append) 模式附加到 YAML 檔尾
        with open(yaml_file, 'a', encoding='utf-8') as f:
            f.write("\n\n# ====== 以下為機器人自動加入的待分類區 (Inbox) ======\n")
            f.write("# 提醒：請將以下區塊「剪下」並「貼上」到上方合適的章節 (sections) 內\n")
            
            for key in sorted(forgotten_keys):
                full_path = disk_map[key]
                title = generate_title(full_path)
                
                # 按照 jb-book 的 YAML 縮排格式寫入
                # 注意：這裡預設縮排為 2 個空白，作為最外層的 chapters 項目
                f.write(f"  - file: {full_path}\n")
                f.write(f"    title: \"[待分類] {title}\"\n")
                print(f"  -> 已寫入: {full_path}")
                
        print("\n✅ 更新完成！請打開 _toc.yml 查看最下方，並進行手動搬移。")