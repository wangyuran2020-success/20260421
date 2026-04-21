import streamlit as st
import datetime

# --- 1. 页面配置与主题 ---
st.set_page_config(page_title="深渊探测器", page_icon="🔍", layout="centered")

# --- 2. 深度定制 CSS (审计报告风格) ---
st.markdown("""
    <style>
    .main { background-color: #0b0d11; color: #e0e1dd; }
    .stButton>button { width: 100%; background-color: #1b263b; color: #00ff41; border: 1px solid #00ff41; font-weight: bold; }
    .insight-box { 
        background-color: #161b22; 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid #30363d;
        border-left: 10px solid #00ff41;
        margin: 20px 0;
        font-size: 1.1em;
        line-height: 1.8;
    }
    .warning-box { 
        background-color: #3e0b0b; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #ff4b4b; 
        color: #ffcccc; 
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #1b263b 0%, #0b0d11 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 逻辑引擎 ---
def get_profection_data(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    house = (age % 12) + 1
    return age, house

# --- 4. 精彩见解数据库 (主公核心资产) ---
INSIGHTS_DB = {
    1: {
        "title": "身份认同与镜像焦虑审计",
        "deep_insight": "你正在经历一场‘自我的外壳剥落’。压力源于外界对你的期待与你自我认知之间的断裂。你是否在疯狂追求将自己打造成更好的形象，却在镜子里找不到真实的归属？你在对自我的形象、地位感到内耗，这种‘更好的自己’究竟是为谁而建？",
        "biz_advice": "停止‘形象装修’，执行一周‘去标签化’生活，卸下所有社交头衔。",
        "soul_advice": "完成一份《自我真实属性清单》，剔除所有他人眼中的评价，找回内核。",
        "base_score": 75
    },
    2: {
        "title": "核心价值与生存焦虑审计",
        "deep_insight": "目前，自我价值感是你生活中的重大议题。生活中发生的事不断引你思考自我的价值，你在社会、在他人眼中的价值。你是否感到自我的价值在被重新定义，在被反复审视？你在用金钱和世俗成就衡量自身价值，这种对安全感的渴求正让你感到前所未有的焦虑。",
        "biz_advice": "锁定生存红线数字，完成一份《非金钱资产清单》，重新梳理你的硬实力。",
        "soul_advice": "接触大自然，寻找土地带给您的稳固感。进行‘价值剥离’冥想，直视不被定义的财富。",
        "base_score": 85
    },
    4: {
        "title": "根基动荡与归属感重构审计",
        "deep_insight": "这是关于安全感、归属感以及‘家’的概念的打破与重建。你可能感到灵魂的着陆点正在松动，旧有的支撑系统已经不再适用。这种压力正在逼迫你向内扎根，去寻找那个不依赖于任何物理房产或外部关系而存在的、真正的心理地基。",
        "biz_advice": "建立一个物理层面的‘避难所’。处理积压已久的生存底层逻辑问题。",
        "soul_advice": "与内在的‘自卑小孩’对话。承认当下的漂泊感是为下一阶段更深的扎根做准备。",
        "base_score": 80
    },
    10: {
        "title": "职业声望与权力博弈审计",
        "deep_insight": "你正处于社会存在感的极限测试期。对于个人专业能力、社会认可度、事业追求及社会地位的渴望，正转化为巨大的精神压力。你是否在担心，如果脱离了当下的职位或平台，你的名声和价值是否会随之贬值？你在博弈中感到疲惫，却又不敢放手。",
        "biz_advice": "执行‘离职演习’：假设明天失去所有职权，你的核心竞争力还剩什么？",
        "soul_advice": "关闭社交网络，享受‘不被看见’的自由。找回作为‘专业匠人’而非‘职位占有者’的初心。",
        "base_score": 82
    }
}

# --- 5. 交互界面 ---
st.title("🔍 深渊探测器")
st.markdown("### 专属于你的生命黑匣子压力审计")
st.write("---")

with st.container():
    st.write("#### 📡 录入生命信号")
    c1, c2 = st.columns(2)
    with c1:
        u_name = st.text_input("如何称呼您？", placeholder="输入您的名字")
        u_birth_date = st.date_input("出生日期", value=datetime.date(1982, 9, 12))
    with c2:
        u_birth_time = st.time_input("出生时间", value=datetime.time(22, 45))
        u_status = st.selectbox("当前生活状态", ["平稳期", "失业/转型/巨大变动"])

st.write("")
if st.button("激活探测器：开启深度审计"):
    if u_name:
        u_age, u_house = get_profection_data(u_birth_date)
        
        # 匹配数据库
        data = INSIGHTS_DB.get(u_house, {
            "title": "未知领域审计",
            "deep_insight": "该宫位的深层逻辑尚在扫描中。但请记住：所有的压力都是未被对齐的能量。",
            "biz_advice": "保持观察，暂缓重大决策。",
            "soul_advice": "深呼吸，在混沌中寻找定力。",
            "base_score": 50
        })

        # 压力评分逻辑
        final_score = data["base_score"]
        if u_status == "失业/转型/巨大变动":
            final_score += 12

        st.divider()
        
        # 结果头部
        st.markdown(f"### ⚡ 审计完成：{u_name}")
        st.write(f"**当前周岁：** {u_age} 岁 | **激活压力中心：** 第 {u_house} 宫")
        
        # 压力仪表盘
        st.markdown(f"""
            <div class="metric-card">
                <p style="font-size: 0.9em; color: #888;">精神过载读数</p>
                <h1 style="color: #00ff41; margin: 0;">{final_score} / 100</h1>
            </div>
        """, unsafe_allow_html=True)
        
        # 触发高压警告
        if final_score >= 85:
            st.write("")
            st.markdown(f"""
                <div class="warning-box">
                    <h3 style="margin:0;">🚨 深度预警</h3>
                    <p style="font-size: 1.1em;"><b>你需要好好评估一下自我价值了。别担心，来找我，我帮你做一个全面的评估，让我们一起找出答案。</b></p>
                </div>
            """, unsafe_allow_html=True)

        # 精彩见解展示区 (主公要求的高亮区)
        st.write("")
        st.markdown(f"#### 🧠 主审官见解：{data['title']}")
        st.markdown(f"""
            <div class="insight-box">
                {data['deep_insight']}
            </div>
        """, unsafe_allow_html=True)

        # 对冲策略区
        st.write("#### 🛡️ 对冲方案建议")
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"**💼 商业/行为对冲**\n\n{data['biz_advice']}")
        with col2:
            st.info(f"**🌙 精神/疗愈对冲**\n\n{data['soul_advice']}")
            
        st.write("---")
        st.caption("提示：本系统基于古典占星逻辑与心理学审计。所有结果旨在帮助您从客体视角重新审视生命周期。")
    else:
        st.warning("请输入您的名字以开启深渊探测。")
