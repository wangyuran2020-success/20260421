import streamlit as st
import datetime

# --- 1. 页面设置 ---
st.set_page_config(page_title="深渊探测器", page_icon="🔍", layout="centered")

# --- 2. 视觉样式设计 ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e1dd; }
    .stButton>button { width: 100%; background-color: #4a4e69; color: white; border-radius: 5px; height: 3em; }
    .warning-box { background-color: #430000; padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; color: #ffcccc; }
    .report-card { background-color: #1b263b; padding: 20px; border-radius: 10px; border-left: 5px solid #e0e1dd; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 核心计算逻辑 ---
def get_profection_house(birth_date, birth_time):
    # 这里是一个简化的小限算法：以出生年为起点
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    house = (age % 12) + 1
    return age, house

# --- 4. 数据库（主公的洞察资产） ---
DATABASE = {
    1: {
        "title": "身份认同与镜像焦虑审计",
        "stress_core": "您正处于‘自我形象重塑期’。压力源于外界期待与自我认知之间的断裂。您是否在疯狂追求‘更好的自己’，却在镜子里找不到归属？",
        "biz_hedge": "停止‘形象装修’，执行一周的‘去标签化’生活，卸下所有社交头衔。",
        "soul_hedge": "完成一份《自我真实属性清单》，找回不被外界定义的初始动力。",
        "base_stress": 75
    },
    2: {
        "title": "核心价值与生存焦虑审计",
        "stress_core": "您正处于‘价值感极度敏感期’。您是否正试图用金钱和世俗成就来衡量自身的安全感？",
        "biz_hedge": "锁定生存红线数字，完成一份《非金钱资产清单》，梳理核心硬实力。",
        "soul_hedge": "接触大自然，寻找土地带给您的稳固感。进行‘价值剥离’冥想。",
        "base_stress": 85
    },
    3: {
        "title": "心智带宽与日常秩序审计",
        "stress_core": "您正处于‘生存秩序碎裂期’。琐碎的信息、无效的沟通、以及平级关系的内耗正在蚕食您的大脑。",
        "biz_hedge": "执行‘信息斋戒’，关闭非核心通知。物理隔离那些消耗您的碎裂关系。",
        "soul_hedge": "降级表达。放弃向所有人证明自己，改用书面逻辑同步，找回思考深度。",
        "base_stress": 70
    },
    4: {
        "title": "根基动荡与归属感重构审计",
        "stress_core": "您正处于‘心理地基的地震期’。关于‘家’和‘归属’的旧有概念正在崩塌。这种漂泊感本质上是灵魂在寻找新的着陆点。",
        "biz_hedge": "建立一个物理层面的‘避难所’。处理积压已久的生存底层逻辑问题。",
        "soul_hedge": "与内在的‘自卑小孩’对话。承认当下的漂泊是为下一阶段的深扎做准备。",
        "base_stress": 80
    },
    10: {
        "title": "职业声望与权力博弈审计",
        "stress_core": "您正处于‘社会存在感的极限测试期’。外界的名声和地位成了沉重的枷锁，您在怀疑脱离平台后自己还是谁。",
        "biz_hedge": "进行‘离职演习’：假设明天失去所有职权，您的核心竞争力还剩什么？",
        "soul_hedge": "关闭社交网络，享受‘不被看见’的自由。找回作为‘专业匠人’的初心。",
        "base_stress": 78
    }
}

# --- 5. APP 前端交互 ---
st.title("🔍 深渊探测器")
st.markdown("### 生命黑匣子：个人年度压力深度审计系统")
st.write("---")

# 数据输入区
with st.container():
    st.write("#### 第一步：输入生命参数")
    col_a, col_b = st.columns(2)
    with col_a:
        name = st.text_input("您的称呼", placeholder="例：Charles")
        birth_date = st.date_input("出生日期", value=datetime.date(1982, 9, 12))
    with col_b:
        birth_time = st.time_input("出生时间 (精准到分钟)", value=datetime.time(22, 45))
        is_working = st.selectbox("当前生活状态", ["在职/平稳", "失业/转型/巨大变动"])

st.write("")
if st.button("开始深层扫描并生成审计报告"):
    if name:
        age, house = get_profection_house(birth_date, birth_time)
        report = DATABASE.get(house, {
            "title": "未知领域审计",
            "stress_core": "该宫位逻辑尚在深渊中录入，但当前的行星波动依然在影响您。",
            "biz_hedge": "保持冷静，观察周围的重复性事件。",
            "soul_hedge": "静坐，等待雾气散去。",
            "base_stress": 50
        })
        
        # 压力计算
        final_stress = report["base_stress"]
        if is_working == "失业/转型/巨大变动":
            final_stress += 10
            
        # 结果呈现
        st.balloons()
        st.write("---")
        st.write(f"### 审计报告单：{name}")
        st.write(f"**当前周岁：** {age} 岁 | **激活压力中心：** 第 {house} 宫")
        
        # 压力读数
        st.metric(label="🌪️ 精神过载读数", value=f"{final_stress} / 100")
        
        # 高压警告
        if final_stress >= 85:
            st.markdown(f"""
            <div class="warning-box">
            <h4>🚨 深度预警</h4>
            <p>主审官提示：你需要好好评估一下自我价值了。别担心，来找我，我帮你做一个全面的评估，让我们一起找出答案。</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

        # 报告详情
        st.markdown(f"""
        <div class="report-card">
        <h3>主题：{report['title']}</h3>
        <p><b>核心诊断：</b>{report['stress_core']}</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.success(f"**💼 商业/行为对冲建议**\n\n{report['biz_hedge']}")
        with c2:
            st.info(f"**🌙 精神/疗愈对冲建议**\n\n{report['soul_hedge']}")
            
        st.write("---")
        st.caption("提示：本系统基于古典占星小限逻辑与深度心理学审计。所有建议仅供决策参考。")
    else:
        st.error("请输入您的称呼以开启审计。")
