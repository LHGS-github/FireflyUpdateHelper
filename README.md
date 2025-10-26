![ww](firefly_well.png)
# Firefly Update Helper

适用于Python项目的更新解决方案

## 特性
1. [x] 从GitHub拉取元数据

2. [x] 从GitHub下载更新包

3. [ ] 安装更新包

4. [ ] 从Firefly Update Server拉取元数据

## 食用指南

### GitHub模式 前置指南

1. 在目标仓库主分支的根目录下，新建`fuh_metadata.yaml`文件

2. 按照如下格式填写该文件
```yaml
# 不会YAML语法的话请自行百度
latest: # 最新版版本号，所有版本号必须能对应到GitHub上的一个Release
  release: v0.1 # release频道最新版
  # 或者添加更多频道，例如
  wow: v33550336.1.1
  beta: v2.0.0-delta91

latest_no: # 各个频道的最新内部版本号，只能是整数，Firefly Update Helper通过这个检查最新版
  release: 1
  # 必须和上文latest的频道一一对应
  wow: 999
  beta: 2

subchannels: #子频道，标记架构一类的信息
  arch:
    # 下面这些是子频道可用的值
    - x86
    - x64
    - armv7a
  struct:
    - onefile
    - folder

# Release中的文件必须按照此结构命名，包括后缀
# [version]指上文latest中提到的版本号
# [subchannel_name]指上文定义的子频道
# 带[]的内容会被替换成具体内容
name_format: test-[version]-[arch]-[struct].zip
# 例如v0.1版本，子频道arch为x86，子频道struct为onefile时文件名会被解析为
# test-v0.1-x86-onefile.zip
```

### 服务器模式 接入指南

Work in progress......

### 接入指南
1. 在您的项目中安装
```
pip install firefly_update_helper
```

2. 导入包并初始化更新器

GitHub模式：
```python
import firefly_update_helper as fuh
uh = fuh.UpdateHelper("github","user/repo",current_channel="release",current_subchannel={"arch":"x64","struct":"onefile"},current_version="0.1",current_ver_no=1)
```

具体使用方法已在文档字符串中说明，使用例子：
```python
a = uh.compare_latest() # 获取当前频道最新版版本号
uh.download_latest("1.zip") # 下载最新版到1.zip
```