import streamlit as st
import datetime

# --- 页面配置 ---
st.set_page_config(page_title="深渊探测器", page_icon="🔍", layout="centered")

# --- 样式设计（黑科技深海风格） ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e1dd; }
    .stButton>button { width: 100%; background-color: #4a4e69; color: white; }
    .warning-box { background-color: #780000; padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 核心逻辑函数 ---
def calculate_context(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    house = (age % 12) + 1
    return age, house

# --- 数据库（主公的洞察资产） ---
DATABASE = {
    2: {
        "title": "核心价值与生存焦虑审计",
        "stress_core": "您正处于‘价值感极度敏感期’。您是否在用金钱和世俗成就衡量自身价值？",
        "biz_hedge": "锁定生存红线数字，完成非金钱资产清单。",
        "soul_hedge": "接触大自然，寻找土地带给您的稳固感，进行呼吸冥想。",
        "base_stress": 85
    },
    10: {
        "title": "职业声望与权力博弈审计",
        "stress_core": "您正处于‘社会存在感极限测试期’。外界名声成了您的枷锁。",
        "biz_hedge": "执行‘离职演习’，评估脱离平台后的核心竞争力。",
        "soul_hedge": "关闭社交软件24小时，享受‘不被看见’的自由感。",
        "base_stress": 75
    }
}

# --- 前端界面 ---
st.title("🔍 深渊探测器：生命黑匣子审计")
st.write("---")
st.subheader("请输入您的生命参数以开启审计")

with st.form("audit_form"):
    name = st.text_input("您的称呼")
    birth_date = st.date_input("出生日期", min_value=datetime.date(1950, 1, 1))
    is_working = st.radio("当前就业状态", ["在职", "失业/转型期"])
    submit = st.form_submit_button("开始深层扫描")

if submit:
    age, house = calculate_context(birth_date)
    report = DATABASE.get(house, {"title": "系统开发中", "stress_core": "该宫位逻辑尚在录入..."})
    
    # 计算动态压力读数
    current_stress = report.get("base_stress", 50)
    if is_working == "失业/转型期":
        current_stress += 10 # 失业加权
        
    st.write(f"### 审计对象：{name} | 当前周岁：{age}")
    st.write(f"### 激活小限宫位：第 {house} 宫")
    st.write("---")
    
    # 压力读数展示
    st.metric(label="精神过载读数", value=f"{current_stress} / 100")
    
    # 高压警告语
    if current_stress >= 85:
        st.markdown(f"""
        <div class="warning-box">
        <h4>🚨 深度预警</h4>
        <p>你需要好好评估一下自我价值了。别担心，来找我，我帮你做一个全面的评估，让我们一起找出答案。</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(f"**审计结论：** {report['stress_core']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**💼 商业对冲建议**\n\n{report.get('biz_hedge')}")
    with col2:
        st.help(f"**🌙 疗愈对冲建议**\n\n{report.get('soul_hedge')}")

    st.write("---")
    st.write("想要更深度的 1 对 1 审计？点击下方联系您的专属审计师。")
