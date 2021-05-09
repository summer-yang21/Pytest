import configparser
import os
# 实例化
conf = configparser.ConfigParser()
filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)))+'/pytest.ini'

def write_ini(section, option, value):

    # 拼接文件路径
    conf.read(filepath)
    # 添加section，option，value
    conf.set(section, option, value)
    # 打开文件
    file = open(filepath, 'w', encoding='utf-8')
    conf.write(file)

def read_ini(section, option):
    conf.read(filepath)
    value = conf.get(section, option)
    return value




if __name__ == '__main__':
    # write_ini()
    print(read_ini('url', 'JUMP_URL'))