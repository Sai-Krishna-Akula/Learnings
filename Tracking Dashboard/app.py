import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from datetime import date
from calendar import monthrange


# -------------------- DB --------------------
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS progress (
    goal TEXT,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    done INTEGER
)
""")
conn.commit()


# -------------------- Utils --------------------
def green_gradient(progress: float):
    return (0.0, progress, 0.0)


def days_in_month(year, month):
    return monthrange(year, month)[1]


# -------------------- App --------------------
st.set_page_config(page_title="Consistency Dashboard", layout="wide")
st.title("📊 Consistency Dashboard")

today = date.today()
year, month = today.year, today.month
total_days = days_in_month(year, month)

# ---- Add Goal ----
with st.sidebar:
    st.header("➕ Add Goal")
    new_goal = st.text_input("Goal name")
    if st.button("Add"):
        if new_goal.strip():
            st.success("Goal added (tracked automatically)")
        else:
            st.error("Goal cannot be empty")

# ---- Load Goals ----
df = pd.read_sql("SELECT DISTINCT goal FROM progress", conn)
goals = df["goal"].tolist()

# ---- Main UI ----
for goal in goals:
    st.subheader(goal)

    cols = st.columns(total_days)
    completed = 0

    for day in range(1, total_days + 1):
        cursor.execute("""
            SELECT done FROM progress
            WHERE goal=? AND day=? AND month=? AND year=?
        """, (goal, day, month, year))
        result = cursor.fetchone()
        checked = bool(result[0]) if result else False

        with cols[day - 1]:
            if st.checkbox(str(day), value=checked, key=f"{goal}-{day}"):
                cursor.execute("""
                    INSERT OR REPLACE INTO progress
                    VALUES (?, ?, ?, ?, 1)
                """, (goal, day, month, year))
                conn.commit()
                completed += 1
            else:
                cursor.execute("""
                    DELETE FROM progress
                    WHERE goal=? AND day=? AND month=? AND year=?
                """, (goal, day, month, year))
                conn.commit()

    progress = completed / total_days
    color = green_gradient(progress)

    fig, ax = plt.subplots()
    ax.pie(
        [completed, total_days - completed],
        colors=[color, "#eeeeee"],
        startangle=90,
        counterclock=False
    )
    ax.set_title(f"{progress:.1%} Consistency")
    st.pyplot(fig)

    st.divider()
