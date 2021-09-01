

# midplatform-v2

基于FastApi,开发模块化的运维中台

## 背景

旧版的中台是依托django模式开发，比较笨重。更新某一部分的话，整个服务会无法访问。基于此状况，基于FastAPi 进行重构，模块化、可拆卸的方式。

## 项目结构

```shell
.
|-- CHANGELOG.md
|-- LICENSE
|-- README.md					-- README文件
|-- commonModule                -- 公共模块，集成通用功能
|   |-- dao
|   |-- main.py
|   |-- module
|   |-- routers
|   |-- utils
|-- userModule					-- 用户模块，包含权限角色等
    |-- conf
    |-- libs
    |-- main.py
    |-- utils

```




## 核心依赖

| 依赖    | 版本   | 官网                          |
| ------- | ------ | ----------------------------- |
| fastapi | 0.66.0 | https://fastapi.tiangolo.com/ |
| Uvicorn | 0.14.0 | https://github.com/encode/uvicorn/releases |
| tortoise-orm | 0.17.5 | https://tortoise-orm.readthedocs.io/en/latest/ |

