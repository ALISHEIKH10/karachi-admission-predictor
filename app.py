import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from universities_data import KARACHI_UNIVERSITIES
from predictor import get_all_predictions, get_best_recommendation

st.set_page_config(
    page_title="Karachi University Admission Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stButton > button {
    background: #1a3c6e !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.8rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Karachi University Admission Predictor")
st.caption("Enter your marks and find out which university you can get into — based on 2024 merit data.")

with st.sidebar:
    st.markdown("### How It Works")
    st.markdown("""
    1. Enter Matric marks  
    2. Enter Inter marks  
    3. Enter entry test marks for each university  
    4. Click Predict  
    5. See your results and best recommendation
    """)
    st.markdown("---")
    st.markdown("### Supported Universities")
    for key, uni in KARACHI_UNIVERSITIES.items():
        st.markdown(f"- {uni['full_name']}")
    st.markdown("---")
    st.caption("Merit data based on 2024 admissions. Results are estimates only.")

st.markdown("## Step 1 — Matric Marks")
col1, col2, col3 = st.columns(3)
with col1:
    matric_obtained = st.number_input("Matric Obtained Marks", min_value=0, max_value=1100, value=850, step=1)
with col2:
    matric_total = st.number_input("Matric Total Marks", min_value=900, max_value=1100, value=1100, step=1)
with col3:
    matric_pct_preview = (matric_obtained / matric_total * 100) if matric_total > 0 else 0
    st.metric("Matric Percentage", f"{matric_pct_preview:.1f}%")

st.selectbox("Matric Board", ["Karachi Board (BSEK)", "Federal Board (FBISE)", "Aga Khan Board", "Other"])

st.markdown("## Step 2 — Inter / FSc / FA Marks")
col1, col2, col3 = st.columns(3)
with col1:
    inter_obtained = st.number_input("Inter Obtained Marks", min_value=0, max_value=1200, value=900, step=1)
with col2:
    inter_total = st.number_input("Inter Total Marks", min_value=900, max_value=1200, value=1100, step=1)
with col3:
    inter_pct_preview = (inter_obtained / inter_total * 100) if inter_total > 0 else 0
    st.metric("Inter Percentage", f"{inter_pct_preview:.1f}%")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Inter Group", [
        "Pre-Engineering (Physics, Chemistry, Math)",
        "Pre-Medical (Physics, Chemistry, Biology)",
        "Commerce (Economics, Accounting, Business)",
        "Computer Science (Physics, Math, CS)",
        "Arts / Humanities", "General Science"
    ])
with col2:
    st.selectbox("Inter Board", ["Karachi Board (BSEK)", "Federal Board (FBISE)", "Aga Khan Board", "Other"])

st.markdown("## Step 3 — University Entry Tests")
st.caption("Add marks for each university where you gave the entry test.")

num_unis = st.slider("How many universities did you apply to?", min_value=1, max_value=8, value=3)

uni_tests = []
for i in range(num_unis):
    st.markdown(f"#### University {i+1}")
    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
    with col1:
        selected_uni = st.selectbox(
            f"Select University {i+1}",
            options=list(KARACHI_UNIVERSITIES.keys()),
            format_func=lambda x: KARACHI_UNIVERSITIES[x]["full_name"],
            key=f"uni_{i}",
            index=min(i, len(KARACHI_UNIVERSITIES) - 1)
        )
    with col2:
        programs = KARACHI_UNIVERSITIES[selected_uni]["programs"]
        selected_program = st.selectbox("Program", options=programs, key=f"prog_{i}")
    with col3:
        test_obtained = st.number_input("Test Marks Obtained", min_value=0, max_value=200, value=65, step=1, key=f"to_{i}")
    with col4:
        test_total = st.number_input("Test Total Marks", min_value=50, max_value=200, value=100, step=1, key=f"tt_{i}")

    test_pct = (test_obtained / test_total * 100) if test_total > 0 else 0
    st.caption(f"Test Score: {test_pct:.1f}%  |  Entry Test Name: {KARACHI_UNIVERSITIES[selected_uni]['entry_test']}")

    uni_merit = KARACHI_UNIVERSITIES[selected_uni]["merit_2024"]
    program_key = next(
        (k for k in uni_merit if k.lower() in selected_program.lower() or selected_program.lower() in k.lower()),
        list(uni_merit.keys())[0]
    )
    uni_tests.append({
        "uni_key": selected_uni,
        "program": program_key,
        "program_full": selected_program,
        "test_obtained": test_obtained,
        "test_total": test_total,
        "test_pct": test_pct
    })
    st.markdown("---")

if st.button("Predict My Admission Chances"):

    student_data = {
        "matric_obtained": matric_obtained,
        "matric_total": matric_total,
        "inter_obtained": inter_obtained,
        "inter_total": inter_total,
        "tests": uni_tests
    }

    results, matric_pct, inter_pct = get_all_predictions(student_data)
    best = get_best_recommendation(results)

    st.markdown("---")
    st.markdown("# Your Admission Analysis")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Matric %", f"{matric_pct:.1f}%")
    col2.metric("Inter %", f"{inter_pct:.1f}%")
    col3.metric("Universities Applied", len(results))
    col4.metric("Good Chances", sum(1 for r in results if r["prediction"]["percentage"] > 40))

    if best:
        st.markdown("---")
        st.markdown("## Best Recommendation")
        uni  = best["uni_info"]
        pred = best["prediction"]
        col1, col2, col3, col4 = st.columns(4)
        col1.success(f"**{uni['full_name']}**")
        col2.metric("Your Merit Score", f"{best['merit_score']:.1f}")
        col3.metric("Admission Chance", f"{pred['percentage']}%")
        col4.metric("Annual Fee", f"Rs. {uni['annual_fee']:,}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Rating", f"{uni['rating']}/5")
        col2.metric("Job Placement", uni["job_placement"])
        col3.metric("Type", uni["type"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Strengths**")
            for s in uni["strengths"]:
                st.success(f"+ {s}")
        with col2:
            st.markdown("**Weaknesses**")
            for w in uni["weaknesses"]:
                st.warning(f"- {w}")

        st.info(f"""
        Location: {uni['location']}  |  Established: {uni['established']}  
        Environment: {uni['environment']}  |  Campus Life: {uni['campus_life']}  
        Website: {uni['website']}  |  Phone: {uni['phone']}  
        Merit Formula: {uni['merit_formula']}
        """)

    st.markdown("---")
    st.markdown("## All Universities Result")

    for r in results:
        pred       = r["prediction"]
        uni        = r["uni_info"]
        chance_pct = pred["percentage"]

        col1, col2 = st.columns([2, 1])
        with col1:
            if chance_pct >= 70:
                st.success(f"**{uni['full_name']}**  —  {r['program']}")
            elif chance_pct >= 40:
                st.warning(f"**{uni['full_name']}**  —  {r['program']}")
            else:
                st.error(f"**{uni['full_name']}**  —  {r['program']}")

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Your Merit",       f"{r['merit_score']:.1f}")
            c2.metric("Last Merit 2024",  str(pred.get("last_merit", "N/A")))
            c3.metric("Test Score",       f"{r['test_pct']:.1f}%")
            c4.metric("Chance",           f"{chance_pct}%")
            st.progress(chance_pct / 100)
            st.caption(
                f"Status: {pred['chance']}  |  Type: {uni['type']}  |  "
                f"Fee: Rs. {uni['annual_fee']:,}/year  |  Rating: {uni['rating']}/5  |  "
                f"Placement: {uni['job_placement']}"
            )
        with col2:
            st.markdown("**Strengths**")
            for s in uni["strengths"][:3]:
                st.caption(f"+ {s}")
            st.markdown("**Weaknesses**")
            for w in uni["weaknesses"][:2]:
                st.caption(f"- {w}")

        st.markdown("---")

    # ── GRAPHS ────────────────────────────────────────────────────────────────
    st.markdown("## Results at a Glance")

    short_names = []
    for r in results:
        name = r["uni_info"]["full_name"]
        name = name.replace("University", "Uni").replace("Institute", "Inst").replace("National", "Natl")
        short_names.append(name[:28])

    your_merits = [r["merit_score"] for r in results]
    last_merits = [r["prediction"].get("last_merit", 65) for r in results]
    chances     = [r["prediction"]["percentage"] for r in results]
    fees        = [r["uni_info"]["annual_fee"] for r in results]
    ratings     = [r["uni_info"]["rating"] for r in results]
    types       = [r["uni_info"]["type"] for r in results]
    programs    = [r["program"] for r in results]

    # GRAPH 1
    st.markdown("### Graph 1 — Your Merit Score vs Minimum Required Merit")
    st.caption("Blue bar = your merit. Red bar = minimum required last year. If your blue bar is higher than red, you have a good chance.")

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        name="Your Merit Score",
        x=short_names,
        y=your_merits,
        marker_color="#1a3c6e",
        text=[str(round(m, 1)) for m in your_merits],
        textposition="auto",
        textfont=dict(size=14, color="black"),
    ))
    fig1.add_trace(go.Bar(
        name="Minimum Required Merit (2024)",
        x=short_names,
        y=last_merits,
        marker_color="#e74c3c",
        text=[str(m) for m in last_merits],
        textposition="auto",
        textfont=dict(size=14, color="black"),
    ))
    max_val = max(max(your_merits), max(last_merits)) + 15
    fig1.update_layout(
        barmode="group",
        height=480,
        font=dict(size=13, color="black"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(
            title=dict(text="University", font=dict(size=14, color="black")),
            tickfont=dict(size=12, color="black"),
            tickangle=-15,
        ),
        yaxis=dict(
            title=dict(text="Merit Score", font=dict(size=14, color="black")),
            range=[0, max_val],
            tickfont=dict(size=12, color="black"),
            gridcolor="#dddddd",
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.03,
            xanchor="center",
            x=0.5,
            font=dict(size=13, color="black"),
        ),
        margin=dict(t=80, b=80, l=60, r=40),
    )
    st.plotly_chart(fig1, use_container_width=True)

    # GRAPH 2
    st.markdown("### Graph 2 — Admission Chance for Each University")
    st.caption("Green = very likely (70%+). Orange = possible (40-70%). Red = unlikely (below 40%). Percentage shown inside each bar.")

    bar_colors = ["#27ae60" if c >= 70 else "#e67e22" if c >= 40 else "#e74c3c" for c in chances]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=chances,
        y=short_names,
        orientation="h",
        marker_color=bar_colors,
        text=[f"{c}%" for c in chances],
        textposition="auto",
        textfont=dict(size=15, color="black"),
        width=0.5,
    ))
    fig2.add_vline(x=70, line_dash="dot", line_color="#27ae60", line_width=2,
                   annotation_text="Safe Zone 70%",
                   annotation_font=dict(size=12, color="black"))
    fig2.add_vline(x=40, line_dash="dot", line_color="#e67e22", line_width=2,
                   annotation_text="Borderline 40%",
                   annotation_font=dict(size=12, color="black"))
    fig2.update_layout(
        height=max(380, len(results) * 80),
        font=dict(size=13, color="black"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(
            title=dict(text="Admission Chance (%)", font=dict(size=14, color="black")),
            range=[0, 120],
            tickfont=dict(size=12, color="black"),
            gridcolor="#dddddd",
            ticksuffix="%",
        ),
        yaxis=dict(
            title=dict(text="University", font=dict(size=14, color="black")),
            tickfont=dict(size=12, color="black"),
            automargin=True,
        ),
        margin=dict(t=60, b=60, l=220, r=60),
    )
    st.plotly_chart(fig2, use_container_width=True)

    # GRAPH 3
    st.markdown("### Graph 3 — Complete Summary Table")
    st.caption("Full comparison of all universities. Green row = good chance. Yellow = borderline. Red = low chance.")

    df = pd.DataFrame({
        "University":       [r["uni_info"]["full_name"] for r in results],
        "Program":          programs,
        "Type":             types,
        "Your Merit":       [round(r["merit_score"], 1) for r in results],
        "Min Merit 2024":   [r["prediction"].get("last_merit", "N/A") for r in results],
        "Chance %":         chances,
        "Annual Fee Rs.":   fees,
        "Rating /5":        ratings,
        "Job Placement":    [r["uni_info"]["job_placement"] for r in results],
        "Status":           [r["prediction"]["chance"] for r in results],
    })

    def highlight_row(row):
        c = row["Chance %"]
        if c >= 70:
            return ["background-color: #d5f5e3; color: black"] * len(row)
        elif c >= 40:
            return ["background-color: #fef9e7; color: black"] * len(row)
        else:
            return ["background-color: #fdecea; color: black"] * len(row)

    st.dataframe(
        df.style.apply(highlight_row, axis=1),
        use_container_width=True,
        height=min(420, (len(results) + 1) * 55),
    )
    st.caption("Green = Good chance  |  Yellow = Borderline  |  Red = Low chance")

    # GRAPH 4
    st.markdown("### Graph 4 — Annual Fee vs Admission Chance")
    st.caption("University names shown in black. Higher on Y-axis = better chance. Left on X-axis = lower fee. Best choice = top-left corner.")

    fig4 = go.Figure()
    for i, r in enumerate(results):
        color = "#27ae60" if chances[i] >= 70 else "#e67e22" if chances[i] >= 40 else "#e74c3c"
        fig4.add_trace(go.Scatter(
            x=[fees[i]],
            y=[chances[i]],
            mode="markers+text",
            name=short_names[i],
            text=[short_names[i]],
            textposition="top center",
            textfont=dict(size=12, color="black"),
            marker=dict(
                size=ratings[i] * 14,
                color=color,
                opacity=0.85,
                line=dict(width=2, color="#333333"),
            ),
            showlegend=False,
        ))
    fig4.add_hline(y=70, line_dash="dot", line_color="#27ae60", line_width=1.5,
                   annotation_text="Safe Zone 70%",
                   annotation_font=dict(size=12, color="black"))
    fig4.add_hline(y=40, line_dash="dot", line_color="#e67e22", line_width=1.5,
                   annotation_text="Borderline 40%",
                   annotation_font=dict(size=12, color="black"))
    fig4.update_layout(
        height=500,
        font=dict(size=13, color="black"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(
            title=dict(text="Annual Fee (Rs.) — Lower is cheaper", font=dict(size=14, color="black")),
            tickfont=dict(size=12, color="black"),
            gridcolor="#dddddd",
            tickformat=",",
        ),
        yaxis=dict(
            title=dict(text="Admission Chance (%) — Higher is better", font=dict(size=14, color="black")),
            range=[0, 115],
            tickfont=dict(size=12, color="black"),
            gridcolor="#dddddd",
            ticksuffix="%",
        ),
        margin=dict(t=40, b=80, l=80, r=60),
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.caption("Bubble size = university rating. Top-Left = Best Value (high chance + low fee).")
    st.markdown("## Important Tips")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("""
        **Documents to Prepare**
        - Original Matric Certificate
        - Original Inter Certificate
        - CNIC / B-Form
        - 4 Passport Size Photos
        - Domicile Certificate
        - Character Certificate
        """)
    with c2:
        st.warning("""
        **Do Not Miss Deadlines**
        - Each university has different deadlines
        - Merit lists come in August-September
        - Check fee submission deadline
        - Submit both online and physical forms
        """)
    with c3:
        st.success("""
        **Keep a Backup Plan**
        - Apply to multiple universities
        - Consider both Public and Private
        - Evening programs are also an option
        - Distance learning is also available
        """)

st.markdown("---")
st.caption("Karachi University Admission Predictor  |  Based on 2024 Merit Data  |  Results are estimates only. Always check official university websites.")
