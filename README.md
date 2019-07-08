# 知识图谱实例
参考：[stock-knowledge-graph](https://github.com/lemonhu/stock-knowledge-graph) 

源代码在构建过程中存在不少的问题，调整后在自己环境下重新跑通一遍.

## 环境依赖
> window10 + python3.6:
> - lxml
> - pandas
> - beautifulsoup4
> - tushare

## 源码结构
执行过程如下标注步骤：
```
knowledge-graph-example
├── build_csv.py # 4. 构建neo4j导入格式
├── data
│   ├── executive_prep.csv
│   ├── import
│   │   ├── concept.csv
│   │   ├── executive.csv
│   │   ├── executive_stock.csv
│   │   ├── import.report
│   │   ├── industry.csv
│   │   ├── stock.csv
│   │   ├── stock_concept.csv
│   │   └── stock_industry.csv
│   ├── stockpage.zip # 1. 解压到当前文件夹
│   ├── stock_concept_prep.csv
│   └── stock_industry_prep.csv
├── design.png
├── extract.py # 2. 提取数据
├── import.sh # 5. 导入数据库脚本
├── README.md
├── requirements.txt
├── result.txt
├── stock.py # 3. 获取数据
└── test.py

```
## 设计模式
![](./design.png)

