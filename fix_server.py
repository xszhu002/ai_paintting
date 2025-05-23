#!/usr/bin/env python
# 创建一个脚本来修复server.py中的缩进错误

with open('server.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 修复第一处缩进问题：验证令牌函数
for i in range(len(lines)):
    if '# 如果未传入token，从请求头获取' in lines[i]:
        # 找到if token is None行
        if i+1 < len(lines) and 'if token is None:' in lines[i+1]:
            # 如果下一行auth_header不是正确缩进
            if i+2 < len(lines) and not lines[i+2].startswith('        auth_header'):
                lines[i+2] = '        auth_header' + lines[i+2].lstrip()
                print(f"修复了第{i+3}行的缩进问题(验证令牌函数)")

# 修复第二处缩进问题：敏感词检测部分
for i in range(len(lines)):
    if '# 备用的简化敏感词检测逻辑' in lines[i]:
        # 找到if not custom_words行
        if i+1 < len(lines) and 'if not custom_words:' in lines[i+1]:
            # 检查sensitive_words是否缩进正确
            if i+2 < len(lines) and not lines[i+2].startswith('            sensitive_words'):
                lines[i+2] = '            sensitive_words' + lines[i+2].lstrip()
                print(f"修复了第{i+3}行的缩进问题(敏感词检测)")

# 修复第三处缩进问题：简单分类
for i in range(len(lines)):
    if '# 简单分类：中文或英文' in lines[i]:
        # 检查下一行是否正确缩进
        if i+1 < len(lines) and not lines[i+1].startswith('                    category'):
            lines[i+1] = '                    category' + lines[i+1].lstrip()
            print(f"修复了第{i+2}行的缩进问题(简单分类)")
        
        # 检查if category行是否正确缩进
        if i+2 < len(lines) and 'if category not in categories:' in lines[i+2]:
            if not lines[i+2].startswith('                    if'):
                lines[i+2] = '                    if' + lines[i+2].lstrip()
                print(f"修复了第{i+3}行的缩进问题(分类判断)")
                
            # 检查categories.append行是否正确缩进
            if i+3 < len(lines) and 'categories.append' in lines[i+3]:
                if not lines[i+3].startswith('                        categories'):
                    lines[i+3] = '                        categories' + lines[i+3].lstrip()
                    print(f"修复了第{i+4}行的缩进问题(添加分类)")

# 修复第四处缩进问题：获取学生信息
for i in range(len(lines)):
    if 'if not student_id or not username:' in lines[i]:
        # 检查student_info行是否正确缩进
        if i+1 < len(lines) and 'student_info =' in lines[i+1]:
            if not lines[i+1].startswith('                student_info'):
                lines[i+1] = '                student_info' + lines[i+1].lstrip()
                print(f"修复了第{i+2}行的缩进问题(学生信息获取)")
                
            # 检查if student_info行是否正确缩进
            if i+2 < len(lines) and 'if student_info and' in lines[i+2]:
                if not lines[i+2].startswith('                if'):
                    lines[i+2] = '                if' + lines[i+2].lstrip()
                    print(f"修复了第{i+3}行的缩进问题(学生信息判断)")
                    
                # 检查student_id赋值行是否正确缩进
                if i+3 < len(lines) and 'student_id = student_info' in lines[i+3]:
                    if not lines[i+3].startswith('                    student_id'):
                        lines[i+3] = '                    student_id' + lines[i+3].lstrip()
                        print(f"修复了第{i+4}行的缩进问题(学生ID赋值)")
                        
                    # 检查用户名注释行是否正确缩进
                    if i+4 < len(lines) and '# 如果还是没有用户名' in lines[i+4]:
                        if not lines[i+4].startswith('                    #'):
                            lines[i+4] = '                    #' + lines[i+4].lstrip()
                            print(f"修复了第{i+5}行的缩进问题(用户名注释)")
                            
                        # 检查if not username行是否正确缩进
                        if i+5 < len(lines) and 'if not username:' in lines[i+5]:
                            if not lines[i+5].startswith('                        if'):
                                lines[i+5] = '                        if' + lines[i+5].lstrip()
                                print(f"修复了第{i+6}行的缩进问题(用户名判断)")
                                
                            # 检查username赋值行是否正确缩进
                            if i+6 < len(lines) and 'username = request.cookies' in lines[i+6]:
                                if not lines[i+6].startswith('                            username'):
                                    lines[i+6] = '                            username' + lines[i+6].lstrip()
                                    print(f"修复了第{i+7}行的缩进问题(用户名赋值)")

# 写回文件
with open('server.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("缩进问题修复完成，请重启服务器试试。") 