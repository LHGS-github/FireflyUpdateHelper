from setuptools import setup, find_packages

setup(
    name='firefly_update_helper',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        "httpx",
        "loguru",
        "pyyaml",
        "wget"
    ],
    author='灵魂歌手er',
    author_email='340994706@qq.com',
    description='适用于Python项目的更新解决方案',
    license='MIT',
    keywords='sample setuptools development',
    url='https://github.com/LHGS-github/FireflyUpdateHelper'
)