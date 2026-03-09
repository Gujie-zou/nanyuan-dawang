// 标的数据库
const stocksDB = [
    {
        code: "002353",
        name: "杰瑞股份",
        type: "股票",
        tags: ["燃气轮机", "油服设备", "中东冲突"],
        recommenders: ["东吴证券"],
        reports: ["2026-03-08-东吴证券-机械设备.md"],
        summary: "燃气轮机成撬环节龙头，受益北美AIDC自建电+中东油服双轮驱动",
        related_hotspots: ["AI算力电力需求", "霍尔木兹海峡", "油气价格上涨"],
        price: { current: "45.2", target: "55.0", upside: "+21%" }
    },
    {
        code: "600031",
        name: "三一重工",
        type: "股票",
        tags: ["工程机械", "出口链"],
        recommenders: ["东吴证券"],
        reports: ["2026-03-08-东吴证券-机械设备.md"],
        summary: "工程机械龙头，出口同比+38.8%，受益欧美复苏+非洲印尼需求",
        related_hotspots: ["工程机械出口", "一带一路", "制造业复苏"],
        price: { current: "18.5", target: "23.0", upside: "+24%" }
    },
    {
        code: "600547",
        name: "山东黄金",
        type: "股票",
        tags: ["黄金", "避险资产"],
        recommenders: ["东方证券", "华金证券"],
        reports: ["2026-03-01-东方证券-有色金属.md", "2026-03-01-华金证券-A股策略.md"],
        summary: "国内黄金龙头，资源储量领先，受益地缘冲突避险需求",
        related_hotspots: ["伊以冲突", "美联储降息", "央行购金"],
        price: { current: "28.3", target: "35.0", upside: "+24%" }
    },
    {
        code: "600988",
        name: "赤峰黄金",
        type: "股票",
        tags: ["黄金", "避险资产"],
        recommenders: ["东方证券"],
        reports: ["2026-03-01-东方证券-有色金属.md"],
        summary: "海外矿山布局，成本优势显著，黄金业务纯度高",
        related_hotspots: ["伊以冲突", "金价上涨"],
        price: { current: "19.8", target: "25.0", upside: "+26%" }
    },
    {
        code: "601899",
        name: "紫金矿业",
        type: "股票",
        tags: ["黄金", "铜", "有色"],
        recommenders: ["国金证券", "东方证券", "中银证券"],
        reports: ["2026-03-01-国金证券-A股策略.md", "2026-03-01-东方证券-有色金属.md"],
        summary: "金铜双轮驱动，全球化布局，HALO核心资产",
        related_hotspots: ["地缘冲突", "铜价上涨", "资源安全"],
        price: { current: "17.2", target: "22.0", upside: "+28%" }
    },
    {
        code: "603019",
        name: "中科曙光",
        type: "股票",
        tags: ["AI算力", "超节点", "国产替代"],
        recommenders: ["东兴证券"],
        reports: ["2026-03-02-东兴证券-通信-超节点.md"],
        summary: "国产算力龙头，超节点集群方案打破英伟达独大格局",
        related_hotspots: ["AI算力", "超节点", "国产替代"],
        price: { current: "68.5", target: "85.0", upside: "+24%" }
    },
    {
        code: "600309",
        name: "万华化学",
        type: "股票",
        tags: ["化工", "MDI", "中东冲突"],
        recommenders: ["中邮证券"],
        reports: ["2026-03-05-中邮证券-化工.md"],
        summary: "MDI/TDI全球龙头，运输受阻推升产品价格，受益能源安全",
        related_hotspots: ["霍尔木兹海峡", "MDI涨价", "化工"],
        price: { current: "82.3", target: "100.0", upside: "+21%" }
    },
    {
        code: "600989",
        name: "宝丰能源",
        type: "股票",
        tags: ["化工", "煤制烯烃"],
        recommenders: ["中邮证券"],
        reports: ["2026-03-05-中邮证券-化工.md"],
        summary: "煤制烯烃龙头，油价上涨凸显煤头路径成本优势",
        related_hotspots: ["油价上涨", "煤头路径", "烯烃"],
        price: { current: "32.1", target: "40.0", upside: "+25%" }
    },
    {
        code: "688433",
        name: "华曙高科",
        type: "股票",
        tags: ["3D打印", "AI硬件", "消费电子"],
        recommenders: ["国金证券"],
        reports: ["2026-02-28-国金证券-计算机-3D打印.md"],
        summary: "3D打印设备龙头，自研光束整形技术+大尺寸设备",
        related_hotspots: ["3D打印", "消费电子", "钛合金"],
        price: { current: "28.6", target: "38.0", upside: "+33%" }
    },
    {
        code: "601869",
        name: "长飞光纤",
        type: "股票",
        tags: ["通信", "光棒", "锗"],
        recommenders: ["中国银河"],
        reports: ["2026-03-04-中国银河-通信-锗与光棒.md"],
        summary: "全球光棒龙头，受益光棒价格上行+特种光纤高毛利",
        related_hotspots: ["AI算力", "6G", "光棒涨价"],
        price: { current: "35.2", target: "45.0", upside: "+28%" }
    },
    {
        code: "002624",
        name: "完美世界",
        type: "股票",
        tags: ["游戏", "内容出海"],
        recommenders: ["开源证券"],
        reports: ["2026-03-02-开源证券-传媒-内容出海.md"],
        summary: "游戏出海龙头，《异环》全球预约超2500万",
        related_hotspots: ["内容出海", "游戏", "AI赋能"],
        price: { current: "12.8", target: "18.0", upside: "+41%" }
    },
    {
        code: "1024.HK",
        name: "快手-W",
        type: "港股",
        tags: ["短剧", "内容出海", "AI"],
        recommenders: ["开源证券"],
        reports: ["2026-03-02-开源证券-传媒-内容出海.md"],
        summary: "短剧+AI双重优势，Kwai巴西6000万日活",
        related_hotspots: ["短剧出海", "AI短剧", "Kwai"],
        price: { current: "58.5", target: "75.0", upside: "+28%" }
    }
];

// 按板块分类
const sectors = {
    "AI算力/通信": ["中科曙光", "浪潮信息", "长飞光纤", "中天科技"],
    "黄金/有色": ["山东黄金", "赤峰黄金", "紫金矿业"],
    "机械设备": ["杰瑞股份", "三一重工", "伟创电气", "步科股份", "卧龙电驱"],
    "化工": ["万华化学", "宝丰能源"],
    "传媒/游戏": ["完美世界", "快手-W", "昆仑万维"],
    "高端制造": ["华曙高科", "大族激光", "铂力特"]
};
